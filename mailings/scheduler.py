from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
import os
from django.core.mail import send_mail
from django.db import connections
from config import settings
from mailings.models import Message, Client, Settings


class DBManager:
    def __init__(self, database_name='default'):
        self.database_name = database_name

    def connect(self):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
        connection = connections[self.database_name]
        connection.connect()
        return connection

    def disconnect(self):
        connection = connections[self.database_name]
        connection.close()

    def connect_to_settings(self, table_name='mailings_settings'):
        with self.connect().cursor() as cur:
            cur.execute(
                f'SELECT * FROM {table_name}'
            )
            result = cur.fetchall()

            return result

    def update_mailing_time(self, row_id, new_mailing_time):
        """Записывает время рассылки"""
        with self.connect().cursor() as cur:
            cur.execute(
                f'UPDATE mailings_settings SET mailing_time = %s WHERE id = %s',
                (new_mailing_time, row_id)
            )
        self.disconnect()

    def update_status(self, row_id, new_status):
        """Записывает новый статус"""
        with self.connect().cursor() as cur:
            cur.execute(
                f'UPDATE mailings_settings SET status = %s WHERE id = %s',
                (new_status, row_id)
            )
        self.disconnect()

    def write_logs(self, row_id, mailing_time, new_status, response):
        """Записывает дату и время последней попытки, новый статус, ответ почтового сервера"""
        with self.connect().cursor() as cur:
            cur.execute(
                'INSERT INTO mailings_logs (last_attempt, status, response, settings_id) VALUES (%s, %s, %s, %s)',
                (mailing_time, new_status, response, row_id)
            )
        self.disconnect()


def send_mailing():
    dbmanager = DBManager()
    all_settings = dbmanager.connect_to_settings()

    time = datetime.now()
    current_time = time.strftime("%Y-%m-%d")
    # Вот так это создает проблему с часовыми поясами ("%Y-%m-%d %H:%M:%S")

    for setting in all_settings:
        row_id, mailing_time, periodicity, status, client_id, message_id = setting

        settings_object = Settings.objects.get(id=row_id)
        message_object = settings_object.message  # Здесь мы вытаскиваем по айди сообщение, которое посылаем потом

        client_object = settings_object.client  # А здесь клиента, чтобы потом послать емаил!

        if current_time == mailing_time.strftime("%Y-%m-%d") and status == 'created':
            sent_count = send_mail(
                message_object.subject,
                message_object.body,
                settings.EMAIL_HOST_USER,
                [client_object.email]
            )
            new_status = 'completed'
            dbmanager.update_status(row_id, new_status)

            if sent_count > 0:
                response = f'Письмо успешно отправлено по адресу {client_object.email}'
            else:
                response = f'Письмо не отправилось по адресу {client_object.email}'

            dbmanager.write_logs(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), new_status, response, row_id)

        else:
            if periodicity == 'once_a_day' and status == 'completed':
                next_mailing_time = now + timedelta(days=1)
                dbmanager.update_mailing_time(row_id, next_mailing_time)

            elif periodicity == 'once_a_week' and status == 'completed':
                next_mailing_time = now + timedelta(days=7)
                dbmanager.update_mailing_time(row_id, next_mailing_time)

            elif periodicity == 'once_a_month' and status == 'completed':
                next_mailing_time = now + timedelta(days=30)
                dbmanager.update_mailing_time(row_id, next_mailing_time)

    dbmanager.disconnect()


now = datetime.now()
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
# print(formatted_now)


def start():
    """запускает APScheduler"""
    scheduler = BackgroundScheduler()
    # scheduler.add_job(send_mailing, 'interval', seconds=15)
    scheduler.add_job(send_mailing, 'interval', seconds=50)
    # scheduler.add_job(send_mailing, 'cron', hour=8, minute=10)
    scheduler.start()



    #  сохраняем лог после отправки - НАДО СДЕЛАТЬ