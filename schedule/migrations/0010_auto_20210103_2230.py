# Generated by Django 3.1.4 on 2021-01-03 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0009_lesson_parity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='parity',
            field=models.CharField(choices=[('Числитель', 'числитель'), ('Знаменатель', 'знаменатель'), ('Всегда', 'всегда')], default='B', max_length=15, verbose_name='Четность недели'),
        ),
    ]