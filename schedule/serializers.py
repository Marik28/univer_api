from rest_framework import serializers

from .models import DaySchedule, Lesson, Subject, Day


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ('name', 'code')


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        exclude = ['slug']


class LessonSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()

    class Meta:
        model = Lesson
        fields = ('id', 'time', 'subject', 'kind', 'teacher')


class DayOfWeekSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)
    day = DaySerializer()

    class Meta:
        model = DaySchedule
        fields = ('lessons', 'day', 'is_numerator')
