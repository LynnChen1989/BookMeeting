from django.db import models


# Create your models here.

class MeetingRoom(models.Model):
    name = models.CharField(verbose_name='会议室名称', max_length=100)
    capacity = models.CharField(verbose_name='会议室容量', max_length=40)
    screen = models.BooleanField(verbose_name='是否有电视/投影', default=True)
    picture = models.ImageField(verbose_name='会议室图片', upload_to='meetingroom/', default='meetingroom/default.png')
    comment = models.CharField(verbose_name='其他说明', max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = '会议室信息'
        verbose_name_plural = '会议室信息'

    def __str__(self):
        return "{}".format(self.name)

    def __repr__(self):
        return "{}".format(self.name)


class BookingInfo(models.Model):
    user = models.CharField(verbose_name='预订者', max_length=40)
    meeting_room = models.ForeignKey(MeetingRoom, verbose_name='会议室', on_delete=models.CASCADE)
    start_time = models.DateTimeField(verbose_name='会议开始时间')
    end_time = models.DateTimeField(verbose_name='会议开始时间')
    duration = models.FloatField(verbose_name='会议持续时长（分钟）')
    subject = models.CharField(verbose_name='会议主题', max_length=120)
    abstract = models.TextField(verbose_name='会议大纲')
    book_time = models.DateTimeField(verbose_name='发起预定时间', auto_now=True)

    class Meta:
        verbose_name = '会议室预定信息'
        verbose_name_plural = '会议室预定信息'

    def __str__(self):
        return "{}-{}-{}".format(self.user, self.start_time, self.subject)

    def __repr__(self):
        return "{}-{}-{}".format(self.user, self.start_time, self.subject)


class MeetingInvitation(models.Model):
    user = models.CharField(verbose_name='邀约人', max_length=40)
    meeting = models.ForeignKey(BookingInfo, verbose_name='会议', on_delete=models.CASCADE)
    member = models.TextField(verbose_name='会议成员')

    def meeting_info(self):
        return {'时间': self.meeting.start_time, '主题': self.meeting.subject}

    meeting_info.short_description = '会议信息'

    class Meta:
        verbose_name = '会议邀约信息'
        verbose_name_plural = '会议邀约信息'

    def __str__(self):
        return "{}-{}".format(self.user, self.member)

    def __repr__(self):
        return "{}-{}".format(self.user, self.member)
