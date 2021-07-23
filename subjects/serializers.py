from rest_framework import serializers

from schedule.models import Subject
from teachers.serializers import TeacherBriefInfoSerializer


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
