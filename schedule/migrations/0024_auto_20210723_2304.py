# Generated by Django 3.1.4 on 2021-07-23 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
        ('schedule', '0023_lesson_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.group', verbose_name='Группа, у которой пара'),
        ),
    ]
