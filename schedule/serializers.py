from rest_framework import serializers

from subjects.serializers import SubjectSerializer
from .models import Lesson, Day

from teachers.serializers import TeacherSerializer


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ('name',)


class LessonSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    day = DaySerializer()
    teacher = TeacherSerializer()

    class Meta:
        model = Lesson
        exclude = ('archived',)
