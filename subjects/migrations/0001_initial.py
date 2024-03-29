# Generated by Django 3.1.4 on 2021-07-23 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '0001_initial'),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Не более 100 символов', max_length=255, verbose_name='Название предмета')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('official_playlist_url', models.URLField(blank=True, max_length=255, null=True, verbose_name='Ссылка на плейлист на канале КарТУ')),
                ('my_playlist_url', models.URLField(blank=True, max_length=255, null=True, verbose_name='Ссылка на плейлист на моем канале')),
                ('slug', models.SlugField(blank=True, help_text='Устанавливается автоматически ', max_length=200, null=True, unique=True, verbose_name='Удобное представления URL')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.group')),
                ('lab_teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lab_set', to='teachers.teacher', verbose_name='Преподаватель, ведущий лабораторные')),
                ('lecturer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lecture_set', to='teachers.teacher', verbose_name='Лектора')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.subjectname')),
                ('practic_teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='practic_set', to='teachers.teacher', verbose_name='Преподаватель, ведущий практику')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
                'ordering': ['name'],
            },
        ),
    ]
