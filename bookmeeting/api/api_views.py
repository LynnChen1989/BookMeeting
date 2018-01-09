from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response

from .api_serializer import MeetingRoomSerializer, UserSerializer, BookingInfoSerializer
from bookmeeting.models import MeetingRoom, BookingInfo


class MeetRoomView(ListAPIView):
    serializer_class = MeetingRoomSerializer

    queryset = MeetingRoom.objects.all()


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.exclude(username__in=['admin', 'oamanager'])


class BookView(ListCreateAPIView):
    serializer_class = BookingInfoSerializer
    queryset = BookingInfo.objects.all()

    def perform_create(self, serializer):
        # 保存外键表的方法
        serializer.save(meeting_room=MeetingRoom.objects.get(name=self.request.data.get('meeting_room')))

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.data)
        return self.create(request, *args, **kwargs)
