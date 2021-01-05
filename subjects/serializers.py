from rest_framework import serializers

from schedule.models import Subject
from teachers.serializers import TeacherLittleInfoSerializer


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        exclude = ['slug']


class SubjectDetailSerializer(serializers.ModelSerializer):
    lecturer = TeacherLittleInfoSerializer()
    lab_teacher = TeacherLittleInfoSerializer()
    practic_teacher = TeacherLittleInfoSerializer()

    class Meta:
        model = Subject
        exclude = ['slug']
