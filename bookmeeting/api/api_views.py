from rest_framework.generics import ListAPIView
from .api_serializer import MeetingRoomSerializer
from bookmeeting.models import MeetingRoom


class MeetRoomView(ListAPIView):
    serializer_class = MeetingRoomSerializer

    queryset = MeetingRoom.objects.all()
