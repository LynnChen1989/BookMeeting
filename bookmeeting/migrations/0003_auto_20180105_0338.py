# Generated by Django 2.0 on 2018-01-05 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmeeting', '0002_bookinginfo_meeting_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingroom',
            name='comment',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='其他说明'),
        ),
    ]
