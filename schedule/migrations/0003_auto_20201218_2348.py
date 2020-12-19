# Generated by Django 3.1.4 on 2020-12-18 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
        ('schedule', '0002_auto_20201216_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='department',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='position',
        ),
        migrations.AlterModelOptions(
            name='dayschedule',
            options={'ordering': ['day'], 'verbose_name': 'Расписание на 1 день', 'verbose_name_plural': 'Расписание на 1 день'},
        ),
        migrations.AlterField(
            model_name='lesson',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='teachers.teacher', verbose_name='Преподаватель'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='lab_teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lab_set', to='teachers.teacher', verbose_name='Имя преподавателя, ведущего лабораторные'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='lecturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lecture_set', to='teachers.teacher', verbose_name='Имя лектора'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='practic_teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='practic_set', to='teachers.teacher', verbose_name='Имя преподавателя, ведущего практику'),
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
        migrations.DeleteModel(
            name='TeacherPosition',
        ),
    ]
