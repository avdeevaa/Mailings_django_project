# from django.apps import AppConfig
#
#
# class UsersConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'users'

from django.contrib import admin

from users.models import User

admin.site.register(User)