from django.contrib.auth.models import User

from bookmeeting.models import MeetingRoom, BookingInfo
from rest_framework import serializers


class MeetingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingRoom
        fields = ('name', 'capacity', 'screen', 'comment', 'picture')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name')


class BookingInfoSerializer(serializers.ModelSerializer):
    meeting_room = serializers.CharField(source='meeting_room.name')

    class Meta:
        model = BookingInfo
        fields = ('user', 'meeting_room', 'start_time', 'end_time',
                  'duration', 'subject', 'abstract', 'book_time', 'invitation', 'member')
