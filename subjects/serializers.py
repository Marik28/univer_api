from rest_framework import serializers

from groups.serializers import GroupSerializer
from teachers.serializers import TeacherBriefInfoSerializer

from .models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    group = GroupSerializer()

    class Meta:
        model = Subject
        exclude = ['slug', 'lecturer', 'lab_teacher', 'practic_teacher']


class SubjectDetailSerializer(serializers.ModelSerializer):
    group = GroupSerializer()
    lecturer = TeacherBriefInfoSerializer()
    lab_teacher = TeacherBriefInfoSerializer()
    practic_teacher = TeacherBriefInfoSerializer()

    class Meta:
        model = Subject
        exclude = ['slug']
