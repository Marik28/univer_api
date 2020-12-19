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
        days = get_week_schedule(request.GET)
        serializer = DayOfWeekSerializer(days, many=True)
        return Response(data=serializer.data, status=200)


class DayAPIView(views.APIView):
    def get(self, request: Request):
        query: QueryDict = request.GET
        print(query)
        print()
        week_day = Day.objects.get(code=query['day'][0])
        numerator = bool(int(query['is_numerator'][0]))
        print(numerator)
        day_schedule = DaySchedule.objects.filter(day=week_day).filter(is_numerator=numerator)
        serializer = DayOfWeekSerializer(day_schedule, many=True)
        return Response(data=serializer.data, status=200)


def get_week_schedule(request_query: QueryDict):
    if len(request_query) == 0:
        days = DaySchedule.objects.all()
    else:
        if int(request_query['is_numerator'][0]):
            days = DaySchedule.objects.filter(is_numerator=True)
        else:
            days = DaySchedule.objects.filter(is_numerator=False)
    return days
