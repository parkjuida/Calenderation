from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^registration/', views.Registration.as_view()),
    url(r'^login/', views.Login.as_view()),
    url(r'^logout/', views.Logout.as_view())
]
