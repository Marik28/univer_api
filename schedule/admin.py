from django.contrib import admin
from .models import Day, LessonKind, Subject, Lesson


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('time', '__str__', 'day', 'teacher', 'parity')
    list_display_links = ('__str__',)
    list_filter = ('day', 'teacher', 'parity')

    def archive(self):
        pass


admin.site.register(Subject)
admin.site.register(Day)
admin.site.register(LessonKind)
