from django.contrib import admin

from .models import TeacherPosition, Teacher, Department


admin.site.register(Teacher)
admin.site.register(Department)
admin.site.register(TeacherPosition)
