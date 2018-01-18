"""BookMeeting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from bookmeeting.views import BookMeetingView, BookView, MeetingLoginView
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view

admin.site.site_header = "会议室预定系统后台管理"
# admin.site.login_template = "login.html"
admin.site.site_title = "会议室预定系统后台管理"

urlpatterns = [
                  path('admin/', admin.site.urls),
                  url(r'^api-docs/$', get_swagger_view(title='会议室预定系统API'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('bookmeeting', BookMeetingView.as_view()),
    url(r'^$', login_required(BookMeetingView.as_view(), login_url='login'), name='bookmeeting'),
    url(r'^book/', login_required(BookView.as_view(), login_url='login'), name='book'),
    url(r'^login/', MeetingLoginView.as_view(), name='login'),
]

# for rest_framework
urlpatterns += [
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/bookmeeting/', include('bookmeeting.urls', namespace='bookmeeting'))
]
