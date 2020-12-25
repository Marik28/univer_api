from rest_framework import serializers

from .models import Lesson, Subject, Day


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ('name', 'code', 'index')


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        exclude = ['slug']


class LessonSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    day = DaySerializer()

    class Meta:
        model = Lesson
        fields = ('id', 'time', 'subject', 'kind', 'teacher', 'day', 'is_numerator')
