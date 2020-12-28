from django.contrib import admin
from .models import Day, LessonKind, Subject, Lesson


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['__str__']

    def archive(self):
        pass


admin.site.register(Subject)
admin.site.register(Day)
admin.site.register(LessonKind)
