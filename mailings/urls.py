from django.urls import path
from mailings.views import MessageListView, MessageDetailView, MessageUpdateView, MessageDeleteView, MessageCreateView, \
    LogsListView, BlogDeleteView, BlogCreateView, BlogListView, BlogUpdateView, BlogDetailView
from mailings.views import ClientListView, ClientDetailView, ClientUpdateView, ClientCreateView, ClientDeleteView
from mailings.views import SettingsListView, SettingsCreateView

app_name = 'mailings'


urlpatterns = [
    path('', MessageListView.as_view(), name='main_page'),
    path('main/', MessageListView.as_view(), name='main_page'),

    path('message/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('create/', MessageCreateView.as_view(), name='create_message'),
    path('update/<int:pk>/', MessageUpdateView.as_view(), name='update_message'),
    path('delete/<int:pk>/', MessageDeleteView.as_view(), name='delete_message'),

    path('clients/', ClientListView.as_view(), name='all_clients'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('update_client/<int:pk>/', ClientUpdateView.as_view(), name='update_client'),
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('delete_client/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),

    path('settings/', SettingsListView.as_view(), name='all_settings'),
    path('create_settings', SettingsCreateView.as_view(), name='create_settings'),

    path('logs/', LogsListView.as_view(), name='all_logs'),

    path('create-blog/', BlogCreateView.as_view(), name='create_blog'),
    path('blog/', BlogListView.as_view(), name='read_blog'),
    path('update-blog/<int:pk>/', BlogUpdateView.as_view(), name='update_blog'),
    path('delete-blog/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog'),
    path('view-blog/<int:pk>/', BlogDetailView.as_view(), name='view_blog'),
]
