from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Teacher, TeacherPosition, Department

from schedule.serializers import SubjectSerializer
from .serializers import TeacherSerializer, TeacherPositionSerializer, DepartmentSerializer, TeacherDetailSerializer


class TeacherListView(APIView):
    """View для отображения информации о преподе"""
    def get(self, request: Request):
        teachers = Teacher.objects.all()
        serializer = TeacherDetailSerializer(teachers, many=True)
        return Response(data=serializer.data, status=200)
