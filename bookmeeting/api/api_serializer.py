from bookmeeting.models import MeetingRoom, MeetingInvitation, BookingInfo
from rest_framework import serializers


class MeetingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingRoom
        fields = ('name', 'capacity', 'screen', 'comment')
