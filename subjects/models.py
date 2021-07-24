from django.db import models

from groups.models import Group
from teachers.models import Teacher

from .choices import SubGroup


class SubjectName(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название предмета',
                            help_text='Не более 255 символов')

    class Meta:
        ordering = ['name']
        verbose_name = 'Название предмета'
        verbose_name_plural = 'Названия предметов'

    def __str__(self):
        return str(self.name)


class Subject(models.Model):
    """Модель, отображающая предмет"""
    name = models.ForeignKey(SubjectName, on_delete=models.CASCADE, verbose_name="Название предмета")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Группа, у которой ведется предмет")
    subgroup = models.IntegerField(choices=SubGroup.choices, default=SubGroup.BOTH,
                                   verbose_name="Подгруппа, у которой ведется предмет")
    lecturer = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='Лектор', related_name='lecture_set')
    lab_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True,
                                    verbose_name='Преподаватель, ведущий лабораторные', related_name='lab_set')
    practic_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True,
                                        verbose_name='Преподаватель, ведущий практику',
                                        related_name='practic_set')
    official_playlist_url = models.URLField(max_length=255, null=True, blank=True,
                                            verbose_name='Ссылка на плейлист на канале КарТУ')
    my_playlist_url = models.URLField(max_length=255, null=True, blank=True,
                                      verbose_name='Ссылка на плейлист на моем канале')

    def __str__(self):
        return f"{self.name} ({self.group})"

    class Meta:
        ordering = ['name']
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
