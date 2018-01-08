from django.conf.urls import url
from bookmeeting.api.api_views import MeetRoomView, UserListView

app_name = 'bootmeeting'

urlpatterns = [
    url(r"meetingroom-info/$", MeetRoomView.as_view(), name='meetingroot-info'),
    url(r"users/$", UserListView.as_view(), name='users'),
]
