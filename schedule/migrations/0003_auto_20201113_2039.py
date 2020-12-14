# Generated by Django 3.1.3 on 2020-11-13 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_auto_20201113_2028'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LessonType',
        ),
        migrations.AlterField(
            model_name='lesson',
            name='kind',
            field=models.CharField(choices=[('LE', 'Лекция'), ('LA', 'Лабораторная работа'), ('SP', 'СРСП'), ('PR', 'Практика'), ('KC', 'Кураторский час')], default='LE', max_length=2, verbose_name='Тип занятия'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='position',
            field=models.CharField(choices=[('SL', 'Старший преподаватель'), ('JL', 'Преподаватель'), ('DO', 'Доцент'), ('CS', 'Кандидат технических наук'), ('DS', 'Доктор Технических наук')], default='JL', max_length=2),
        ),
        migrations.DeleteModel(
            name='Position',
        ),
    ]
