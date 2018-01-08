from django.contrib.auth.models import User

from bookmeeting.models import MeetingRoom, MeetingInvitation, BookingInfo
from rest_framework import serializers


class MeetingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingRoom
        fields = ('name', 'capacity', 'screen', 'comment')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name')