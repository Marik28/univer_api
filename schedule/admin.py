from django.contrib import admin
from .models import *


admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Lesson)
admin.site.register(DayOfWeek)

