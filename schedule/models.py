from django.db import models

from pytils.translit import slugify

from groups.models import Group
from schedule.choices import LessonKind, WeekDays, Parity
from schedule.model_managers import LessonManager
from teachers.models import Teacher


class Subject(models.Model):
    """Модель, отображающая предмет"""
    name = models.CharField(max_length=255, verbose_name='Название предмета',
                            help_text='Не более 100 символов')
    lecturer = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='Лектора', related_name='lecture_set')
    lab_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True,
                                    verbose_name='Преподаватель, ведущий лабораторные', related_name='lab_set')
    practic_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True,
                                        verbose_name='Преподаватель, ведущий практику',
                                        related_name='practic_set')
    official_playlist_url = models.URLField(max_length=255, null=True, blank=True,
                                            verbose_name='Ссылка на плейлист на канале КарТУ')
    my_playlist_url = models.URLField(max_length=255, null=True, blank=True,
                                      verbose_name='Ссылка на плейлист на моем канале')
    slug = models.SlugField(max_length=200, null=True, blank=True, unique=True,
                            verbose_name='Удобное представления URL', help_text='Устанавливается автоматически ')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self))
        super().save(*args, *kwargs)

    class Meta:
        ordering = ['name']
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


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
