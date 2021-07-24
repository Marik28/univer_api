from django.db import models

from teachers.models import Teacher


class Group(models.Model):
    name = models.CharField(max_length=15, verbose_name='Название группы')
    curator = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return str(self.name)
