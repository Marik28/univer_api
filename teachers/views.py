from django.shortcuts import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Teacher

from .serializers import TeacherDetailSerializer
from .services import filter_teachers


class TeacherListView(APIView):
    """View для отображения информации обо всех преподах"""
    def get(self, request: Request):
        teachers = Teacher.objects.all()
        serializer = TeacherDetailSerializer(teachers, many=True)
        return Response(data=serializer.data, status=200)


class TeacherDetailView(APIView):
    """View для обо всех преподах"""
    def get(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        serializer = TeacherDetailSerializer(teacher, many=False)
        return Response(serializer.data, status=200)


class TeacherFilterView(APIView):
    """возращает отфильтрованный список преподов на основе GET запроса"""
    def get(self, request: Request):
        teachers = filter_teachers(request.GET)
        serializer = TeacherDetailSerializer(teachers, many=True)
        return Response(serializer.data, status=200)
