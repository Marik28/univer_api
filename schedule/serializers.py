from rest_framework import serializers

from groups.serializers import GroupSerializer
from subjects.serializers import SubjectSerializer
from teachers.serializers import TeacherSerializer

from .models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    teacher = TeacherSerializer()
    group = GroupSerializer()

    class Meta:
        model = Lesson
        exclude = ('archived',)
