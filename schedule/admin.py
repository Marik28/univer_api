from django.contrib import admin
from .models import DaySchedule, Day, LessonKind, Subject, Lesson


admin.site.register(Subject)
admin.site.register(Lesson)
admin.site.register(DaySchedule)
admin.site.register(Day)
admin.site.register(LessonKind)
