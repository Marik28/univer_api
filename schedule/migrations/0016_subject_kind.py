# Generated by Django 3.1.4 on 2021-07-23 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0015_auto_20210106_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='kind',
            field=models.CharField(choices=[('LEC', 'Лекция'), ('LAB', 'Лабораторное занятие'), ('PRC', 'Семинар'), ('SRSP', 'СРСП'), ('SRS', 'СРС'), ('CUR', 'Кураторский час')], default='LEC', max_length=50, verbose_name='Название типа пары'),
        ),
    ]
