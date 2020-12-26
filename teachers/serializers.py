from rest_framework import serializers

from .models import Teacher, TeacherPosition, Department


class TeacherPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeacherPosition
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    position = TeacherPositionSerializer()

    class Meta:
        model = Teacher
        exclude = ('slug',)
