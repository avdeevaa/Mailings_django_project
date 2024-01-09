from random import sample

from django.shortcuts import render, reverse
from mailings.models import Message, Client, Settings, Logs, Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def main_page(request):

    total_messages_count = Message.objects.count()
    active_logs_count = Logs.objects.count()
    active_clients_count = Client.objects.count()

    all_blogs = Blog.objects.all()
    random_blogs = sample(list(all_blogs), min(3, all_blogs.count()))

    context = {
        'total_messages_count': total_messages_count,
        'active_logs_count': active_logs_count,
        'active_clients_count': active_clients_count,
        'random_blogs': random_blogs
    }

    return render(request, 'mailings/main_page.html', context)


class MessageListView(ListView):
    """ shows all messages"""
    model = Message
    template_name = 'mailings/message_list.html'


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


#  часть 2 - добавляем вьюшки для блога


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'image', 'date_of_publication')
    template_name = 'mailings/blog_form.html'

    def get_success_url(self):
        return reverse('mailings:read_blog')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'image', 'date_of_publication')
    template_name = 'mailings/blog_form.html'

    def get_success_url(self):
        return reverse('mailings:read_blog')


class BlogListView(ListView):
    model = Blog
    template_name = 'mailings/blog_list.html'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'mailings/blog_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'mailings/blog_confirm_delete.html'

    def get_success_url(self):
        return reverse('mailings:read_blog')

