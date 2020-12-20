from django.http import QueryDict

from rest_framework import views
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import DayOfWeekSerializer
from .services import get_week_schedule, get_day_schedule


class WeekAPIView(views.APIView):
    """View для отображения расписания на целую неделю"""
    def get(self, request: Request):
        days = get_week_schedule(request.GET)
        serializer = DayOfWeekSerializer(days, many=True)
        return Response(data=serializer.data, status=200)


class DayAPIView(views.APIView):
    """View для отображения расписания на 1 день"""
    def get(self, request: Request):
        day_schedule = get_day_schedule(request.GET)
        serializer = DayOfWeekSerializer(day_schedule, many=True)
        return Response(data=serializer.data, status=200)
