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


class Message(models.Model):
    subject = models.CharField(max_length=300, verbose_name="тема письма")
    body = models.TextField(verbose_name="тело письма")

    # settings = models.ForeignKey(Settings, on_delete=models.CASCADE, verbose_name="Настройки рассылки")

    def __str__(self):
        return f'{self.subject} : {self.body}'

    class Meta:
        verbose_name = "сообщение для рассылки"
        verbose_name_plural = "сообщения для рассылки"


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

    mailing_time = models.DateTimeField(verbose_name="время рассылки", auto_now=True)
    periodicity = models.CharField(verbose_name="периодичность", max_length=20, choices=FREQUENCY_CHOICES, default='once_a_day')
    status = models.CharField(verbose_name="статус рассылки", max_length=20, choices=STATUS_CHOICES, default='created')

    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение')

    def __str__(self):
        return f'Письмо отослано в {self.mailing_time} : {self.status}'

    class Meta:
        verbose_name = "настройка"
        verbose_name_plural = "настройки"


class Logs(models.Model):
    last_attempt = models.DateTimeField(verbose_name="Дата и время последней попытки")  # При типе данных DateTimeField возникает ошибка с записью в БД
    status = models.CharField(max_length=200, verbose_name="статус попытки", default='completed')
    response = models.CharField(max_length=200, verbose_name="ответ почтового сервера", null=True, blank=True)

    settings = models.ForeignKey(Settings, on_delete=models.CASCADE, verbose_name="Настройки рассылки")

    def __str__(self):
        return f'{self.last_attempt}'

    class Meta:
        verbose_name = "лог рассылки"
        verbose_name_plural = "логи рассылки"


class Blog(models.Model):
    title = models.CharField(max_length=300, verbose_name="заголовок")
    content = models.TextField(verbose_name='содержимое статьи')
    image = models.ImageField(upload_to='mailings/images/', verbose_name='изображение', null=True, blank=True)
    number_of_views = models.PositiveIntegerField(default=0, verbose_name="количество просмотров")
    date_of_publication = models.DateField(verbose_name='дата публикации')

    def __str__(self):
        return f'{self.title} -- {self.content}'

    class Meta:
        verbose_name = "блог"
        verbose_name_plural = "блоги"

