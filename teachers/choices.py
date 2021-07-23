from django.db import models


class TeacherPosition(models.Choices):
    SENIOR_LECTURER = 'Старший преподаватель'
    JUNIOR_LECTURER = 'Преподаватель'
    DOCENT = 'Доцент'
    PHD = 'PhD'
