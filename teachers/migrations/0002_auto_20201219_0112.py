# Generated by Django 3.1.4 on 2020-12-18 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['name'], 'verbose_name': 'Кафедра', 'verbose_name_plural': 'Кафедры'},
        ),
        migrations.AlterModelOptions(
            name='teacherposition',
            options={'ordering': ['name'], 'verbose_name': 'Должность преподавателя', 'verbose_name_plural': 'Должности преподавателей'},
        ),
    ]