from django.contrib import admin

from schedule.admin import LessonInline
from .models import Subject, SubjectName


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    inlines = [LessonInline]


@admin.register(SubjectName)
class SubjectNameAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
