from rest_framework import serializers

from .models import Lesson, Subject, Day, LessonKind

from teachers.serializers import TeacherSerializer


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ('name',)


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        exclude = ['slug']


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
