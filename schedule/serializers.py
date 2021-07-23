from rest_framework import serializers

from groups.serializers import GroupSerializer
from subjects.serializers import SubjectSerializer
from .models import Lesson

from teachers.serializers import TeacherSerializer


class LessonSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    teacher = TeacherSerializer()
    group = GroupSerializer()

    class Meta:
        model = Lesson
        exclude = ('archived',)
