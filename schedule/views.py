from rest_framework import views
from rest_framework.request import Request
from rest_framework.response import Response

from .models import DaySchedule
from .serializers import DayOfWeekSerializer


class WeekAPIView(views.APIView):
    def get(self, request: Request):
        days = DaySchedule.objects.all()
        serializer = DayOfWeekSerializer(days, many=True)
        return Response(data=serializer.data, status=200)
