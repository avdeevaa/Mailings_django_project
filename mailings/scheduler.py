from apscheduler.schedulers.background import BackgroundScheduler

from apscheduler.triggers.cron import CronTrigger


def send_mailing():
    print("Я отправил")
    #  получить текущее время и дату
    #  получить все настройки -- из бд результат модели
    #  цикл по настройкам + 1) if условие, которое проверяет что текущее время равно времени из рассылки (часы и минуты)
        #  if 2) если периодичность == ежедневное, то отправляем рассылку
        #  elif 3) если периодичность == еженедельное и остаток от деления на 7 равен 0 (разница между текущей датой и датой в бд), то отправляем рассылку
     #  elif 4) если периодичность == еженемес и остаток от деления на 30 равен 0 (разница между текущей датой и датой в бд), то отправляем рассылку
        #  домашка 22.2 -- будет отправка на почту

    #  сохраняем лог после отправки


def start():
    """запускает APScheduler"""
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_mailing, 'interval', seconds=15) #  каждых 15 сек запускает функцию send mailing
    scheduler.start()



# @register_job
# def configure_scheduler():
#     scheduler = BackgroundScheduler()
#
#     pass

