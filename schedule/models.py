from django.db import models

from groups.models import Group
from subjects.models import Subject
from teachers.models import Teacher

from .choices import LessonKind, WeekDays, Parity
from .model_managers import LessonManager


class Lesson(models.Model):
    """Модель, отображающая конкретную пару"""

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=False,
                                verbose_name='Название предмета')
    kind = models.CharField(max_length=50, choices=LessonKind.choices, default=LessonKind.LECTURE,
                            verbose_name='Тип занятия')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=False,
                                verbose_name='Преподаватель')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=False, verbose_name='Группа, у которой пара')
    time = models.TimeField(verbose_name='Время начала занятия')
    day = models.CharField(max_length=20, choices=WeekDays.choices, default=WeekDays.MONDAY, verbose_name='День недели')
    parity = models.CharField(verbose_name='Четность недели', max_length=15,
                              choices=Parity.choices, default=Parity.NUMERATOR)
    archived = models.BooleanField(verbose_name='Заархивированный предмет', default=False)
    next_assignment = models.TextField(verbose_name='Следующая домашка', null=True, blank=True)

    objects = LessonManager()

    def __str__(self):
        return f'{self.subject.name}'

    class Meta:
        ordering = ['day']
        unique_together = [['subject', 'parity', 'day', 'teacher', 'time'], ['subject', 'parity', 'day', 'time']]
        verbose_name = 'Пара'
        verbose_name_plural = 'Пары'
