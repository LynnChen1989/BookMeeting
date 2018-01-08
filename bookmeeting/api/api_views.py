from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView
from .api_serializer import MeetingRoomSerializer, UserSerializer
from bookmeeting.models import MeetingRoom


class MeetRoomView(ListAPIView):
    serializer_class = MeetingRoomSerializer

    queryset = MeetingRoom.objects.all()


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.exclude(username__in=['admin', 'oamanager'])
