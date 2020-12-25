from django.db import models

from pytils.translit import slugify

from teachers.models import Teacher


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

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self))
        super().save(*args, *kwargs)

    class Meta:
        ordering = ['name']
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class LessonKind(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название типа пары')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Тип пары'
        verbose_name_plural = 'Типы пары'


class Day(models.Model):
    """Модель дня недели"""
    code = models.CharField(max_length=10, null=True, verbose_name='Сокращенное название')
    name = models.CharField(max_length=20, verbose_name='Название дня недели')
    index = models.PositiveSmallIntegerField('Порядковый номер', null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни недели'


class Lesson(models.Model):
    """Модель, отображающая конкретную пару"""
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='Название предмета')
    kind = models.ForeignKey(LessonKind, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name='Тип занятия')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='Преподаватель')
    time = models.TimeField(verbose_name='Время начала занятия')
    day = models.ForeignKey('Day', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='_День недели')
    is_numerator = models.BooleanField(verbose_name='Числитель/знаменатель', null=True)

    def __str__(self):
        if self.is_numerator:
            num = 'Числитель'
        else:
            num = 'Знаменатель'
        return f'{self.time} {self.subject.name} ({self.day}|{num})'

    class Meta:
        ordering = ['time']
        verbose_name = 'Пара'
        verbose_name_plural = 'Пары'
