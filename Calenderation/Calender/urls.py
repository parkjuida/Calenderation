from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.FullCalenderView.as_view(), name='Calender'),
    url(r'^diary/$', views.DiaryList.as_view(), name='Diary'),
    url(r'^diary/diary_detail/$', views.DiaryDetail.as_view(), name='Diary_detail'),
]
