from django.contrib import admin

from schedule.admin import LessonInline
from .models import Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    inlines = [LessonInline]
