from django.contrib import admin

from .models import TeacherPosition, Teacher, Department


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("__str__", "second_name", "first_name", "middle_name", "department",)
    list_display_links = ("__str__",)
    search_fields = ("second_name", "first_name", "middle_name",)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "abbreviation")


admin.site.register(TeacherPosition)
