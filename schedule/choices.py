from django.db import models


class Parity(models.Choices):
    NUMERATOR = 'Числитель'
    DENOMINATOR = 'Знаменатель'
    ALWAYS = 'Всегда'


class LessonKind(models.Choices):
    LECTURE = 'Лекция'
    LAB = 'Лабораторное занятие'
    SEMINAR = 'Семинар'
    SRSP = 'СРСП'
    SRS = 'СРС'
    CURATORIAL_HOUR = 'Кураторский час'


class WeekDays(models.Choices):
    MONDAY = "Понедельник"
    TUESDAY = "Вторник"
    WEDNESDAY = "Среда"
    THURSDAY = "Четверг"
    FRIDAY = "Пятница"
    SATURDAY = "Суббота"
    SUNDAY = "Воскресенье"
