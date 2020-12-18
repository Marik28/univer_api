import re

from django.core import validators
from django.db import models
from django.urls import reverse

from pytils.translit import slugify


class TeacherPosition(models.Model):
    """Модель, отображающая должность преподавателя"""
    name = models.CharField(max_length=100, verbose_name='Название должности')


class Department(models.Model):
    """Модель, отображающая кафедру"""
    name = models.CharField(max_length=255, verbose_name='Название кафедры')


class Teacher(models.Model):
    """Модель, отображающая преподавателя"""
    second_name = models.CharField(max_length=50, verbose_name='Фамилия преподавателя',
                                   help_text='Максимальная длина 50 символов')
    first_name = models.CharField(max_length=50, verbose_name='Имя преподавателя',
                                  help_text='Максимальная длина 50 символов')
    middle_name = models.CharField(max_length=50, verbose_name='Отчество преподавателя',
                                   help_text='Максимальная длина 50 символов')
    position = models.ForeignKey(TeacherPosition, on_delete=models.SET_NULL,
                                 verbose_name='Должность', null=True, blank=True, related_name='teachers')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL,
                                   verbose_name='Кафедра', null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True,
                                    validators=[
                                        validators.RegexValidator(
                                            regex=r'\+7[ -]?7[0-9]{2}[ -]?[0-9]{3}[ -]?[0-9]{2}[ -]?[0-9]{2}'
                                        )],
                                    verbose_name='Номер телефона преподавателя', help_text='Пример: +7708-999-99-99')
    slug = models.SlugField(max_length=200, null=True, blank=True, unique=True,
                            verbose_name='Удобное представления URL', help_text='Устанавливается автоматически ')
    kstu_link = models.URLField(max_length=255, null=True, blank=True,
                                verbose_name='Ссылка на преподавателя на сайте KSTU')

    def display_phone_number(self):
        if self.phone_number:
            delimiters = r'[ -]{1}'
            splitted = re.split(delimiters, self.phone_number)
            return ''.join(splitted)
        else:
            return None

    def get_absolute_url(self):
        return reverse('teacher_detail', args=[self.slug])

    def __str__(self):
        return f'{self.second_name}, {self.first_name} {self.middle_name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self) + str(self.id))
        super().save(*args, *kwargs)

    class Meta:
        ordering = ['second_name', 'first_name']
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Subject(models.Model):
    """Модель, отображающая предмет"""
    name = models.CharField(max_length=255, verbose_name='Название предмета',
                            help_text='Не более 100 символов')
    lecturer = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='Имя лектора', related_name='lecture_set')
    lab_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True,
                                    verbose_name='Имя преподавателя, ведущего лабораторные', related_name='lab_set')
    practic_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True,
                                        verbose_name='Имя преподавателя, ведущего практику',
                                        related_name='practic_set')
    official_playlist_url = models.URLField(max_length=255, null=True, blank=True,
                                            verbose_name='Ссылка на плейлист на канале КарТУ')
    my_playlist_url = models.URLField(max_length=255, null=True, blank=True,
                                      verbose_name='Ссылка на плейлист на моем канале')
    slug = models.SlugField(max_length=200, null=True, blank=True, unique=True,
                            verbose_name='Удобное представления URL', help_text='Устанавливается автоматически ')

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self) + str(self.id))
        super().save(*args, *kwargs)

    class Meta:
        ordering = ['name']
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.name


class LessonKind(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название типа пары')

    def __str__(self):
        return self.name


class Lesson(models.Model):
    """Модель, отображающая конкретную пару"""
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='Название предмета')
    kind = models.ForeignKey(LessonKind, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name='Тип занятия')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='Преподаватель')
    time = models.TimeField(verbose_name='Время начала занятия')

    def __str__(self):
        return f'{self.time} {self.subject.name}'

    class Meta:
        ordering = ['time']
        verbose_name = 'Пара'
        verbose_name_plural = 'Пары'


class Day(models.Model):
    """Модель дня недели"""
    name = models.CharField(max_length=20, verbose_name='Название дня недели')

    def __str__(self):
        return self.name


class DaySchedule(models.Model):
    """Модель, отображающая день недели с определенным расписанием"""
    lessons = models.ManyToManyField(Lesson)
    day = models.ForeignKey('Day', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='_День недели')
    is_numerator = models.BooleanField(verbose_name='Является ли числителем')

    class Meta:
        ordering = ['day']
        verbose_name = 'Расписание на 1 день'
        verbose_name_plural = 'Расписание на 1 день'
