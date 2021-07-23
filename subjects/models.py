from django.db import models
from pytils.translit import slugify

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