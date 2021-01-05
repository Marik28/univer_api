from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.WeekAPIView.as_view()),
    url(r'^day/$', views.DayAPIView.as_view()),
]
