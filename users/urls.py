from django.contrib.auth import logout

from django.urls import path
from django.contrib.auth.views import LoginView

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, generate_new_password, logout_view

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/newpassword', generate_new_password, name='generate_new_password'),

]

