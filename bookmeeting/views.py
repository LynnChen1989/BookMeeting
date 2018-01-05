from django.shortcuts import render
from django.views.generic import TemplateView
from bookmeeting.models import MeetingRoom, MeetingInvitation, BookingInfo
import random


# Create your views here.


class BookMeetingView(TemplateView):
    template_name = 'bookmeeting.html'

    def get_context_data(self, **kwargs):
        color_list = ['default', 'primary', 'info', 'success', 'warning', 'danger']

        context = super(BookMeetingView, self).get_context_data()
        meeting_room = MeetingRoom.objects.all()
        for m in meeting_room:
            ran = random.randint(0, len(color_list) - 1)
            m.color = color_list[ran]
        context.update({'meeting_room': meeting_room})
        return context
