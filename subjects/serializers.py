from rest_framework import serializers

from teachers.serializers import TeacherBriefInfoSerializer

from .models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        exclude = ['slug']


class SubjectDetailSerializer(serializers.ModelSerializer):
    lecturer = TeacherBriefInfoSerializer()
    lab_teacher = TeacherBriefInfoSerializer()
    practic_teacher = TeacherBriefInfoSerializer()

    class Meta:
        model = Subject
        exclude = ['slug']
