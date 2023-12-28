from django.shortcuts import render, reverse
from mailings.models import Message, Client, Settings, Logs
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class MessageListView(ListView):
    """ shows main page"""
    model = Message
    template_name = 'mailings/main_page.html'


class MessageDetailView(DetailView):
    """ shows one item (mailing message)"""
    model = Message
    template_name = 'mailings/message_detail.html'


class MessageUpdateView(UpdateView):
    """makes changes in the model Massage == UPDATE"""
    model = Message
    fields = ('subject', 'body', 'settings')
    template_name = 'mailings/message_form.html'

    def get_success_url(self):
        return reverse('mailings:main_page')


class MessageDeleteView(DeleteView):
    """deletes one model of Message"""
    model = Message
    template_name = 'mailings/message_confirm_delete.html'

    def get_success_url(self):
        return reverse('mailings:main_page')


class MessageCreateView(CreateView):
    model = Message
    fields = ('subject', 'body', 'settings')
    template_name = 'mailings/message_form.html'

    def get_success_url(self):
        return reverse('mailings:main_page')


class ClientListView(ListView):
    """ shows all clients"""
    model = Client
    template_name = 'mailings/client_list.html'


class ClientDetailView(DetailView):
    """ shows one item (one client)"""
    model = Client
    template_name = 'mailings/client_detail.html'


class ClientUpdateView(UpdateView):
    """makes changes in the model Client == UPDATE"""
    model = Client
    fields = ('name', 'fathers_name', 'surname', 'email', 'comment')
    template_name = 'mailings/client_form.html'

    def get_success_url(self):
        return reverse('mailings:all_clients')


class ClientCreateView(CreateView):
    model = Client
    fields = ('name', 'fathers_name', 'surname', 'email', 'comment')
    template_name = 'mailings/client_form.html'

    def get_success_url(self):
        return reverse('mailings:all_clients')


class ClientDeleteView(DeleteView):
    """deletes one model of Client"""
    model = Client
    template_name = 'mailings/client_confirm_delete.html'

    def get_success_url(self):
        return reverse('mailings:all_clients')


class SettingsListView(ListView):
    """ shows all settings"""
    model = Settings
    template_name = 'mailings/settings_list.html'


class SettingsCreateView(CreateView):
    model = Settings
    fields = ('periodicity', 'status', 'client', 'message')
    template_name = 'mailings/settings_form.html'

    def get_success_url(self):
        return reverse('mailings:all_settings')


class LogsListView(ListView):
    """ shows all logs"""
    model = Logs
    template_name = 'mailings/logs_list.html'

