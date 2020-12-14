# Generated by Django 3.1.3 on 2020-11-13 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dayofweek',
            options={'ordering': ['day'], 'verbose_name': 'День недели', 'verbose_name_plural': 'Дни недели'},
        ),
        migrations.AlterModelOptions(
            name='lessontype',
            options={'ordering': ['name'], 'verbose_name': 'Тип занятия', 'verbose_name_plural': 'Типы занятия'},
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='type',
        ),
        migrations.AddField(
            model_name='lesson',
            name='kind',
            field=models.CharField(choices=[('LE', 'Лекция'), ('LA', 'Лабораторная работа'), ('SP', 'СРСП'), ('PR', 'Практика'), ('KC', 'Кураторский час')], default='LE', max_length=2),
        ),
    ]
