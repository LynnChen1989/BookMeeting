from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView, DestroyAPIView
from rest_framework.response import Response
from datetime import datetime
import pytz
from rest_framework.views import APIView

from .api_serializer import MeetingRoomSerializer, UserSerializer, BookingInfoSerializer
from bookmeeting.models import MeetingRoom, BookingInfo


class MeetRoomView(ListAPIView):
    serializer_class = MeetingRoomSerializer
    queryset = MeetingRoom.objects.all()


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.exclude(username__in=['admin', 'oamanager'])


class BookView(ListCreateAPIView, DestroyAPIView):
    serializer_class = BookingInfoSerializer

    def get_queryset(self):
        queryset = BookingInfo.objects.all()
        return queryset

    def perform_create(self, serializer):
        # 保存外键表的方法
        serializer.save(meeting_room=MeetingRoom.objects.get(name=self.request.data.get('meeting_room')))

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # TODO 预定的时候会出现覆盖的情况，目前没想好怎么处理
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        request_data = request.data
        id = request_data.get('id', None)
        book_user = request_data.get('bookUser', None)
        if id:
            b = BookingInfo.objects.get(id=id)
            if b.user != book_user:
                return Response({
                    'message': '您无权删除他人的预定',
                    'status': 900
                })
            else:
                b.delete()
                return Response({
                    'message': '取消预定成功',
                    'status': status.HTTP_204_NO_CONTENT
                })


class BookCollectionView(APIView):
    serializer_class = BookingInfoSerializer

    @property
    def time_deadline(self):
        today = datetime.today()
        end = {
            'start': '08:00:00',
            'forenoon': '12:00:00',
            'afternoon': '18:00:00',
            'evening': '23:59:59'
        }
        today_fmt = '{}-{}-{}'.format(today.year, today.month, today.day)
        return {
            'start': datetime.strptime('{} {}'.format(today_fmt, end.get('start')), "%Y-%m-%d %H:%M:%S").replace(
                tzinfo=pytz.timezone('Asia/Shanghai')),

            'forenoon': datetime.strptime('{} {}'.format(today_fmt, end.get('forenoon')), "%Y-%m-%d %H:%M:%S").replace(
                tzinfo=pytz.timezone('Asia/Shanghai')),

            'afternoon': datetime.strptime('{} {}'.format(today_fmt, end.get('afternoon')),
                                           "%Y-%m-%d %H:%M:%S").replace(
                tzinfo=pytz.timezone('Asia/Shanghai')),

            'evening': datetime.strptime('{} {}'.format(today_fmt, end.get('evening')), "%Y-%m-%d %H:%M:%S").replace(
                tzinfo=pytz.timezone('Asia/Shanghai')),
        }

    @staticmethod
    def fmt(minutes):
        hour = int(minutes / 60)
        minutes = int(minutes % 60)
        return '{}小时{}分'.format(hour, minutes)

    def get(self, request):
        meeting_room = request.GET.get('meetingroom', None)
        if not meeting_room:
            return Response({
                'error': 'meetingroom arguments miss.'
            })
        forenoon = BookingInfo.objects.filter(start_time__gte=self.time_deadline.get('start'),
                                              end_time__lte=self.time_deadline.get('forenoon'),
                                              meeting_room__name=meeting_room)
        afternoon = BookingInfo.objects.filter(start_time__gte=self.time_deadline.get('forenoon'),
                                               end_time__lte=self.time_deadline.get('afternoon'),
                                               meeting_room__name=meeting_room)
        evening = BookingInfo.objects.filter(start_time__gte=self.time_deadline.get('afternoon'),
                                             end_time__lte=self.time_deadline.get('evening'),
                                             meeting_room__name=meeting_room)
        forenoon_book, afternoon_book, evening_book = 0, 0, 0
        for f in forenoon: forenoon_book += f.duration
        for a in afternoon: afternoon_book += a.duration
        for e in evening: evening_book += e.duration

        response = Response({
            'forenoon_book': self.fmt(forenoon_book),
            'forenoon_rest': self.fmt(240 - forenoon_book),
            'afternoon_book': self.fmt(afternoon_book),
            'afternoon_rest': self.fmt(360 - afternoon_book),
            'evening_book': self.fmt(evening_book),
            'evening_rest': self.fmt(360 - evening_book)
        })
        return response
