from django.shortcuts import render
from django.views.generic import TemplateView
from bookmeeting.models import MeetingRoom, BookingInfo
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
