# Generated by Django 3.1.4 on 2020-12-28 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0007_auto_20201228_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='archived',
            field=models.BooleanField(default=False, verbose_name='Заархивированный предмет'),
        ),
    ]
