from rest_framework import serializers

from .models import Lesson, Subject, Day, LessonKind

from teachers.serializers import TeacherSerializer


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ('name', 'code', 'index')


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        exclude = ['slug']


class LessonKindSerializer(serializers.ModelSerializer):

    class Meta:
        model = LessonKind
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    day = DaySerializer()
    kind = LessonKindSerializer()
    teacher = TeacherSerializer()

    class Meta:
        model = Lesson
        fields = '__all__'
