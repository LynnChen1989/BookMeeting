from django.contrib import admin
from bookmeeting.models import BookingInfo, MeetingInvitation, MeetingRoom


# Register your models here.


class MeetingRoomBookInline(admin.TabularInline):
    model = BookingInfo


@admin.register(MeetingRoom)
class MeetingRoomAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_filter = ('name', 'screen')
    inlines = [MeetingRoomBookInline, ]


@admin.register(MeetingInvitation)
class MeetingInvitationAdmin(admin.ModelAdmin):
    list_per_page = 20


@admin.register(BookingInfo)
class BookingInfoAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_filter = ('user', 'duration')
