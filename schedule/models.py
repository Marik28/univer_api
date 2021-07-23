from django.db import models

from pytils.translit import slugify

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


class Day(models.Model):
    """Модель дня недели"""
    code = models.CharField(max_length=10, null=True, verbose_name='Сокращенное название')
    name = models.CharField(max_length=20, verbose_name='Название дня недели')
    index = models.PositiveSmallIntegerField('Порядковый номер', null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['index']
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни недели'


class Lesson(models.Model):
    """Модель, отображающая конкретную пару"""
    PARITY_CHOICES = (
        ('Числитель', 'числитель'),
        ('Знаменатель', 'знаменатель'),
        ('Всегда', 'всегда')
    )
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='Название предмета')
    LESSON_KIND_CHOICES = (
        ('LEC', 'Лекция'),
        ('LAB', 'Лабораторное занятие'),
        ('PRC', 'Семинар'),
        ('SRSP', 'СРСП'),
        ('SRS', 'СРС'),
        ('CUR', 'Кураторский час'),
    )
    kind = models.CharField(max_length=50, choices=LESSON_KIND_CHOICES, default='LEC',
                            verbose_name='Тип занятия')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='Преподаватель')
    time = models.TimeField(verbose_name='Время начала занятия')
    day = models.ForeignKey('Day', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='День недели')
    parity = models.CharField(verbose_name='Четность недели', max_length=15, choices=PARITY_CHOICES, default='Всегда')
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
