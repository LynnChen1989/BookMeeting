from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.views import LoginView, LogoutView
from django import forms
from django.shortcuts import render
from django.views.generic import TemplateView
from bookmeeting.models import MeetingRoom, BookingInfo
from django.utils.translation import ugettext_lazy as _
import random


# Create your views here.


def meeting_info(context):
    color_list = ['default', 'primary', 'info', 'success', 'warning', 'danger']
    meeting_room = MeetingRoom.objects.all()
    for m in meeting_room:
        ran = random.randint(0, len(color_list) - 1)
        m.color = color_list[ran]
    context.update({'meeting_room': meeting_room})
    return context


class BookMeetingView(TemplateView):
    template_name = 'bookmeeting.html'

    def get_context_data(self, **kwargs):
        context = super(BookMeetingView, self).get_context_data()
        context = meeting_info(context)
        return context


class BookView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(BookView, self).get_context_data()
        context = meeting_info(context)
        return context

    template_name = 'book.html'


class LoginForm(AuthenticationForm):
    username = UsernameField(
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}),
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )


class MeetingLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm


class MeetingLogoutView(LogoutView):
    template_name = 'login.html'
    # pass
