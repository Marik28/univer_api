import re

from django.core import validators
from django.db import models

from .choices import TeacherPosition


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
    position = models.CharField(max_length=30, choices=TeacherPosition.choices, default=TeacherPosition.SENIOR_LECTURER,
                                verbose_name='Должность', )
    department = models.ForeignKey(Department, on_delete=models.SET_NULL,
                                   verbose_name='Кафедра', null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True,
                                    validators=[
                                        validators.RegexValidator(
                                            regex=r'\+7[ -]?7[0-9]{2}[ -]?[0-9]{3}[ -]?[0-9]{2}[ -]?[0-9]{2}'
                                        )],
                                    verbose_name='Номер телефона преподавателя',
                                    help_text='Пример: +7-708-999-99-99. Пробелы и тире можно не писать')
    kstu_link = models.URLField(max_length=255, null=True, blank=True,
                                verbose_name='Ссылка на преподавателя на сайте KSTU')
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="E-mail преподавателя")

    def display_phone_number(self):
        """Отображение телефона без пробелов"""
        if self.phone_number:
            delimiters = r'[ -]{1}'
            splitted = re.split(delimiters, str(self.phone_number))
            return ''.join(splitted)
        else:
            return None

    def __str__(self):
        return f'{self.second_name}, {self.first_name} {self.middle_name}'

    class Meta:
        ordering = ['second_name', 'first_name']
        unique_together = [['first_name', 'second_name', 'middle_name']]
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
