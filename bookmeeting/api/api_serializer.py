from django.contrib.auth.models import User

from bookmeeting.models import MeetingRoom, BookingInfo
from rest_framework import serializers


class BookingInfoSerializer(serializers.ModelSerializer):
    meeting_room = serializers.CharField(source='meeting_room.name')

    class Meta:
        model = BookingInfo
        fields = ('id', 'user', 'meeting_room', 'start_time', 'end_time',
                  'duration', 'subject', 'abstract', 'book_time', 'invitation', 'member')


class MeetingRoomSerializer(serializers.ModelSerializer):
    booking_info = BookingInfoSerializer(source='bookinginfo_set', many=True)

    # 反向关联查询
    class Meta:
        model = MeetingRoom
        fields = ('name', 'capacity', 'screen', 'comment', 'picture', 'booking_info')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name')
