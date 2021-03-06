import re

from django.core import validators
from django.db import models
from django.urls import reverse
from pytils.translit import slugify


class TeacherPosition(models.Model):
    """Модель, отображающая должность преподавателя"""
    name = models.CharField(max_length=100, verbose_name='Название должности')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Должность преподавателя'
        verbose_name_plural = 'Должности преподавателей'


class Department(models.Model):
    """Модель, отображающая кафедру"""
    name = models.CharField(max_length=255, verbose_name='Название кафедры')
    abbreviation = models.CharField(max_length=10, verbose_name='Аббревиатура')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'


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
                                    verbose_name='Номер телефона преподавателя',
                                    help_text='Пример: +7-708-999-99-99. Пробелы и тире можно не писать')
    slug = models.SlugField(max_length=200, null=True, blank=True, unique=True,
                            verbose_name='Удобное представления URL', help_text='Устанавливается автоматически ')
    kstu_link = models.URLField(max_length=255, null=True, blank=True,
                                verbose_name='Ссылка на преподавателя на сайте KSTU')
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="E-mail преподавателя")

    def display_phone_number(self):
        """Отображение телефона без пробелов"""
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
        self.slug = slugify(str(self))
        super().save(*args, *kwargs)

    class Meta:
        ordering = ['second_name', 'first_name']
        unique_together = [['first_name', 'second_name', 'middle_name']]
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
