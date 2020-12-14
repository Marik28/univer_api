from django.test import TestCase

from .models import Teacher

teachers = Teacher.objects.all()
for teacher in teachers:
    print(teacher.get_absolute_url())
