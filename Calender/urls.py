from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.FullCalenderView.as_view()),
    url(r'^diary/$', views.DiaryList.as_view(), name='Diary'),
    url(r'^diary_detail/$', views.DiaryDetail.as_view(), name='Diary_detail'),
]
