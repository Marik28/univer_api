# Generated by Django 3.1.4 on 2020-12-28 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0008_lesson_archived'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='parity',
            field=models.CharField(choices=[('N', 'числитель'), ('D', 'знаменатель'), ('B', 'всегда')], default='B', max_length=1, verbose_name='Четность недели'),
        ),
    ]