from django.shortcuts import get_object_or_404
from rest_framework import views
from rest_framework.request import Request
from rest_framework.response import Response


from .models import Subject
from .serializers import SubjectDetailSerializer
from .services import filter_subjects


class SubjectListView(views.APIView):
    def get(self, request: Request):
        subjects = filter_subjects(request.GET)
        serializer = SubjectDetailSerializer(subjects, many=True)
        return Response(serializer.data, status=200)


class SubjectDetailAPIView(views.APIView):
    """View для отображения информации о конкретном предмете"""
    def get(self, request: Request, pk):
        subj = get_object_or_404(Subject, pk=pk)
        serializer = SubjectDetailSerializer(subj, many=False)
        return Response(serializer.data, status=200)
