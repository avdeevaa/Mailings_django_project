from django.urls import path
from mailings.views import MessageListView, MessageDetailView, MessageUpdateView, MessageDeleteView, MessageCreateView
from mailings.views import ClientListView, ClientDetailView, ClientUpdateView, ClientCreateView, ClientDeleteView

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
]
