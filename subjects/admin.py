from django.contrib import admin

from schedule.admin import LessonInline
from .models import Subject, SubjectName


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "group", "subgroup")
    search_fields = ("name", "group")
    inlines = [LessonInline]


@admin.register(SubjectName)
class SubjectNameAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
