from rest_framework import serializers

from schedule.models import Subject

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


class TeacherLittleInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ("id", "second_name", "first_name", "middle_name")


class TeacherSubjectListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ("id", "name",)


class TeacherDetailSerializer(serializers.ModelSerializer):
    practic_set = TeacherSubjectListSerializer(many=True, read_only=True)
    lecture_set = TeacherSubjectListSerializer(many=True, read_only=True)
    lab_set = TeacherSubjectListSerializer(many=True, read_only=True)
    department = DepartmentSerializer()

    class Meta:
        model = Teacher
        exclude = ('slug',)
