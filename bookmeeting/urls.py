from django.conf.urls import url
from bookmeeting.api.api_views import MeetRoomView

app_name = 'bootmeeting'

urlpatterns = [
    url(r"meetingroom-info/$", MeetRoomView.as_view(), name='meetingroot-info'),
]
