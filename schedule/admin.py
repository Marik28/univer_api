from django.contrib import admin

from .models import Lesson


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 0


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('time', '__str__', 'day', 'teacher', 'parity', 'kind')
    list_display_links = ('__str__',)
    list_filter = ('day', 'parity', 'teacher',)
    actions = ['archive', 'unarchive']

    def archive(self, request, queryset):
        """Заархивировать пары"""
        row_update = queryset.update(archived=False)
        if row_update == '1':
            msg = 'Была заархивирована 1 пара'
        else:
            msg = f'Были заархивированы {row_update} пар(/ы)'
        self.message_user(request, msg)

    def unarchive(self, request, queryset):
        """Разархивировать пары"""
        row_update = queryset.update(archived=True)
        if row_update == '1':
            msg = 'Была разархивирована 1 пара'
        else:
            msg = f'Были разархивированы {row_update} пар(/ы)'
        self.message_user(request, msg)

    archive.short_description = 'Заархивировать выбранные пары'
    archive.allowed_permission = ('change',)
    unarchive.short_description = 'Разархивировать выбранные пары'
    unarchive.allowed_permission = ('change',)


