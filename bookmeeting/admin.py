from django.contrib import admin
from django.contrib.auth.models import User
from django.conf import settings
from bookmeeting.models import BookingInfo, MeetingRoom


# Register your models here.


class MeetingRoomBookInline(admin.TabularInline):
    model = BookingInfo


@admin.register(MeetingRoom)
class MeetingRoomAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('name', 'screen', 'capacity', 'picture', 'comment')
    list_filter = ('name', 'screen')
    inlines = [MeetingRoomBookInline, ]


@admin.register(BookingInfo)
class BookingInfoAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('user', 'meeting_room', 'start_time', 'end_time',
                    'duration', 'subject', 'abstract', 'member', 'book_time', 'invitation')
    list_filter = ('user', 'meeting_room')


# class UserAdmin(admin.ModelAdmin):
#     list_per_page = 50
#     list_display = ('username', 'first_name', 'email', 'is_active', 'is_staff', 'is_superuser')
#     list_filter = ('is_active', 'username')
#     search_fields = ('username',)
#     actions = ['sync_user_from_oa']
#
#     def sync_user_from_oa(self, request, queryset):
#         from .logic import sync_user
#         sync_user()
#
#     sync_user_from_oa.short_description = '从OA系统同步用户'
#
#
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
