from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.FullCalenderView.as_view()),
    url(r'^Diary/$', views.DiaryView.as_view(), name='Diary_detail'),
]
