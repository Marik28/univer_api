# Generated by Django 3.1.4 on 2021-07-23 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0017_auto_20210723_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='day',
            field=models.CharField(choices=[('mon', 'понедельник'), ('tue', 'вторник'), ('wed', 'среда'), ('thu', 'четверг'), ('fri', 'пятница'), ('sat', 'суббота'), ('sun', 'воскресенье')], default='mon', max_length=20, verbose_name='День недели'),
        ),
    ]