from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.WeekAPIView.as_view()),
    url(r'^day/(?P<day_code>\w+)/$', views.DayAPIView.as_view()),
]