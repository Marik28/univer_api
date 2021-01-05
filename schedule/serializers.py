from rest_framework import serializers

from subjects.serializers import SubjectSerializer
from .models import Lesson, Day, LessonKind

from teachers.serializers import TeacherSerializer


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ('name',)


class LessonKindSerializer(serializers.ModelSerializer):

    class Meta:
        model = LessonKind
        fields = ['name']


class LessonSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    day = DaySerializer()
    kind = LessonKindSerializer()
    teacher = TeacherSerializer()

    class Meta:
        model = Lesson
        exclude = ('archived',)
