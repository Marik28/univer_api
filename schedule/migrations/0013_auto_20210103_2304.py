# Generated by Django 3.1.4 on 2021-01-03 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_auto_20201228_2153'),
        ('schedule', '0012_auto_20210103_2243'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['day'], 'verbose_name': 'Пара', 'verbose_name_plural': 'Пары'},
        ),
        migrations.AlterUniqueTogether(
            name='lesson',
            unique_together={('subject', 'parity', 'day', 'time'), ('subject', 'parity', 'day', 'teacher', 'time')},
        ),
    ]