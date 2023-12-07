from django.urls import path
from mailings.views import MessageListView, MessageDetailView, MessageUpdateView, MessageDeleteView, MessageCreateView


app_name = 'mailings'


urlpatterns = [
    path('', MessageListView.as_view(), name='main_page'),
    path('main/', MessageListView.as_view(), name='main_page'),

    path('message/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('create/', MessageCreateView.as_view(), name='create_message'),
    path('update/<int:pk>/', MessageUpdateView.as_view(), name='update_message'),
    path('delete/<int:pk>/', MessageDeleteView.as_view(), name='delete_message'),

]
