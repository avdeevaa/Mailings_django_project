import random

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, reverse, redirect
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/registration.html'

    def get_success_url(self):
        return reverse('users:login')

    def form_valid(self, form):
        user = form.save()
        send_mail(
            "Confirmation of email",
            "Welcome to our website!",
            settings.EMAIL_HOST_USER,
            [user.email]

        )
        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/user_form.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('catalog:main_page')


def generate_new_password(request):
    new_password = ''.join([str(int(random.random() * 10)) for _ in range(12)])
    send_mail(
                "Change of password",
                f"Your new password is {new_password}",
                settings.EMAIL_HOST_USER,
                [request.user.email]

            )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('catalog:main_page'))





