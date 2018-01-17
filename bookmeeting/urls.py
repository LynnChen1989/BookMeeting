from django.conf.urls import url
from bookmeeting.api.api_views import MeetRoomView, UserListView, BookView, BookCollectionView

app_name = 'bootmeeting'

urlpatterns = [
    url(r"meetingroom-info/$", MeetRoomView.as_view(), name='meetingroot-info'),
    url(r"users/$", UserListView.as_view(), name='users'),
    url(r"booking/$", BookView.as_view(), name='booking'),
    url(r"today-book/$", BookCollectionView.as_view(), name='today-book'),

]
