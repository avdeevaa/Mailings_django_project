from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
import os
from django.core.mail import send_mail
from django.db import connections
from config import settings


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
        """записывает время рассылки"""
        with self.connect().cursor() as cur:
            cur.execute(
                f'UPDATE mailings_settings SET mailing_time = %s WHERE id = %s',
                (new_mailing_time, row_id)
            )
        self.disconnect()

    def update_status(self, row_id, new_status):
        """записывает новый статус"""
        with self.connect().cursor() as cur:
            cur.execute(
                f'UPDATE mailings_settings SET status = %s WHERE id = %s',
                (new_status, row_id)
            )
        self.disconnect()


def send_mailing():
    # print("Я отправил")  # Эта штука работает прекрасно

    dbmanager = DBManager()  # Создаем экземпляр класса DBManager
    all_settings = dbmanager.connect_to_settings()

    time = datetime.now()
    # current_time = time.strftime("%H:%M:%S")

    for setting in all_settings:
        row_id, mailing_time, periodicity, status, client_id, message_id = setting

        if status == 'created':
            send_mail(
                "theme",
                'HI HI HI',
                settings.EMAIL_HOST_USER,
                ['zi_daae@mail.ru']  ### to doo - client id,
            )
            new_status = 'completed'
            dbmanager.update_status(row_id, new_status)

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
    # scheduler.add_job(send_mailing, 'interval', seconds=15)  # каждых 15 сек запускает функцию send mailing
    scheduler.add_job(send_mailing, 'interval', seconds=50)
    # scheduler.add_job(send_mailing, 'cron', hour=8, minute=10)
    scheduler.start()



    #  сохраняем лог после отправки - НАДО СДЕЛАТЬ