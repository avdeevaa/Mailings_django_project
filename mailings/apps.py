import time

from django.apps import AppConfig


class MailingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mailings'


    def ready(self):
        from mailings.scheduler import start #лучше делать так для нашего способа
        time.sleep(5) # искусственная задержка
        start()
