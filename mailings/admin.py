from django.contrib import admin
from mailings.models import Message, Client, Settings, Logs


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'body')
    list_filter = ('subject',)
    search_fields = ('subject',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email',)
    search_fields = ('name', 'surname', 'email',)


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('mailing_time', 'periodicity', 'status',)
    search_fields = ('mailing_time', 'periodicity', 'status',)


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('last_attempt', 'status',)
    search_fields = ('last_attempt', 'status',)

