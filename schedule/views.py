import datetime as dt

from django.db.models import Q
from django.http import QueryDict
from rest_framework import views
from rest_framework.request import Request
from rest_framework.response import Response

from .models import DaySchedule, Day
from .serializers import DayOfWeekSerializer


class WeekAPIView(views.APIView):
    def get(self, request: Request):
        print(request.GET)
        days = get_schedule(request.GET)
        serializer = DayOfWeekSerializer(days, many=True)
        return Response(data=serializer.data, status=200)


class DayAPIView(views.APIView):
    def get(self, request: Request, day_code):
        week_day = Day.objects.get(code=day_code)
        day_schedule = DaySchedule.objects.filter(day=week_day)
        serializer = DayOfWeekSerializer(day_schedule, many=True)
        return Response(data=serializer.data, status=200)


def get_schedule(request_query: QueryDict):
    if len(request_query) == 0:
        days = DaySchedule.objects.all()
    else:
        if int(request_query['is_numerator'][0]):
            days = DaySchedule.objects.filter(is_numerator=True)
        else:
            days = DaySchedule.objects.filter(is_numerator=False)
    return days
