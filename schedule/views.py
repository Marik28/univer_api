from rest_framework import views, status
from rest_framework.request import Request
from rest_framework.response import Response

from .exceptions import NotCorrectQuery
from .serializers import LessonSerializer
from .services import filter_lessons


class WeekAPIView(views.APIView):
    """View для отображения расписания на целую неделю"""
    def get(self, request: Request):
        day = request.GET.get("day")
        group = request.GET.get("group")
        subgroup = request.GET.get("subgroup")
        parity = request.GET.get("parity")
        try:
            lessons = filter_lessons(day, group, subgroup, parity)
        except NotCorrectQuery as e:
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)
        serializer = LessonSerializer(lessons, many=True)
        return Response(data=serializer.data)
