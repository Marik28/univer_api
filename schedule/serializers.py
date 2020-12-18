from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from .models import DaySchedule, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class DayOfWeekSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)

    class Meta:
        model = DaySchedule
        fields = ('lessons', 'day', 'is_numerator')
