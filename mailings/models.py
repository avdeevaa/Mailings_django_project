from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=150, verbose_name='имя')
    fathers_name = models.CharField(max_length=150, verbose_name='отчество', null=True, blank=True)
    surname = models.CharField(max_length=150, verbose_name='фамилия')
    email = models.CharField(max_length=150, verbose_name='email')
    comment = models.TextField(verbose_name='комментарий', null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.surname}: {self.email}'

    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = "клиенты"
        ordering = ('surname',)


class Settings(models.Model):

    FREQUENCY_CHOICES = [
        ('once_a_day', 'Once a Day'),
        ('once_a_week', 'Once a Week'),
        ('once_a_month', 'Once a Month'),
    ]

    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('created', 'Created'),
        ('started', 'Started'),
    ]

    mailing_time = models.DateField(verbose_name="время рассылки", auto_now=True)
    periodicity = models.CharField(verbose_name="периодичность", max_length=20, choices=FREQUENCY_CHOICES, default='once_a_day')
    status = models.CharField(verbose_name="статус рассылки", max_length=20, choices=STATUS_CHOICES, default='created')

    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")

    def __str__(self):
        return f'Письмо отослано в {self.mailing_time} : {self.status}'

    class Meta:
        verbose_name = "настройка"
        verbose_name_plural = "настройки"


class Message(models.Model):
    subject = models.CharField(max_length=300, verbose_name="тема письма")
    body = models.TextField(verbose_name="тело письма")

    settings = models.ForeignKey(Settings, on_delete=models.CASCADE, verbose_name="Настройки рассылки")

    def __str__(self):
        return f'{self.subject} : {self.body}'

    class Meta:
        verbose_name = "сообщение для рассылки"
        verbose_name_plural = "сообщения для рассылки"


class Logs(models.Model):
    last_attempt = models.DateTimeField(verbose_name="Дата и время последней попытки", auto_now=True)
    status = models.IntegerField(verbose_name="статус попытки", null=True, blank=True)
    response = models.IntegerField(verbose_name="ответ почтового сервера", null=True, blank=True)

    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name="Сообщение для рассылки")

    def __str__(self):
        return f'{self.last_attempt}'

    class Meta:
        verbose_name = "лог рассылки"
        verbose_name_plural = "логи рассылки"

