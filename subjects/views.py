from django.shortcuts import get_object_or_404
from rest_framework import views
from rest_framework.request import Request
from rest_framework.response import Response


from schedule.models import Subject
from schedule.serializers import SubjectSerializer
from subjects.serializers import SubjectDetailSerializer
from subjects.services import filter_subjects


class SubjectListView(views.APIView):
    def get(self, request: Request):
        subjs = Subject.objects.all()
        serializer = SubjectDetailSerializer(subjs, many=True)
        return Response(serializer.data, status=200)


class SubjectAPIView(views.APIView):
    """View для отображения информации о конкретном предмете"""
    def get(self, request: Request, pk):
        subj = get_object_or_404(Subject, pk=pk)
        serializer = SubjectDetailSerializer(subj, many=False)
        return Response(serializer.data, status=200)


class SubjectFilterAPIView(views.APIView):
    """"""
    def get(self, request: Request):
        subjects = filter_subjects(request.GET)
        serializer = SubjectDetailSerializer(subjects, many=True)
        return Response(serializer.data, status=200)
