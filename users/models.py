from django.db import models
from django.contrib.auth.models import AbstractUser, Permission

from django.utils.translation import gettext as _


class User(AbstractUser):

    COUNTRIES = [
        ('ussr', 'USSR'),
        ('czechoslovakia', 'Czechoslovakia'),
    ]
    groups = models.ManyToManyField('auth.Group', blank=True, related_name='user_groups', verbose_name='Groups')

    username = None
    email = models.EmailField(unique=True, verbose_name="почта")
    avatar = models.ImageField(upload_to='users/', verbose_name="Аватар", null=True, blank=True)
    phone = models.CharField(max_length=35, verbose_name="Номер телефона")
    country = models.CharField(max_length=20, verbose_name="Страна", choices=COUNTRIES)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # так мы настраиваем, чтобы емаил стал главным полем для авторизации

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        related_name='user_set_users',
        blank=True,
        help_text=_('Specific permissions for this user.')
    )

