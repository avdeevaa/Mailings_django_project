from django.contrib import admin
from mailings.models import Message, Client, Settings, Logs, Blog


# from django.contrib.auth.models import User, Group, Permission

# user = User.objects.create_user(username='host40', password='54321host1')
# group = Group.objects.create(name='Host_group')
# user.groups.add(group)
#
#
# permission = Permission.objects.get(name='Can add message')
# group.permissions.add(permission)
# #  так я создала пользователя, который сможет вроде все просматривать. В админке работает весь список разрешений.
# #  если не закоментить, не работает почему-то.


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


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'content',)
    search_fields = ('content',)

