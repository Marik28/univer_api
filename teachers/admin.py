from django.contrib import admin

from schedule.models import Lesson
from .models import Teacher, Department


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 0


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("__str__", "second_name", "first_name", "middle_name", "department",)
    list_display_links = ("__str__",)
    search_fields = ("second_name", "first_name", "middle_name",)
    inlines = [LessonInline]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "abbreviation")
