from django.db import models


class Group(models.Model):

    name = models.CharField(max_length=15, verbose_name='Название группы')

    class Meta:
        ordering = ['name']
