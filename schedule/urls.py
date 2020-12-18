from django.urls import path

from . import views


urlpatterns = [
    path('', views.WeekAPIView.as_view()),
]