# Generated by Django 3.1.4 on 2020-12-28 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_auto_20201225_2348'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='day',
            options={'ordering': ['index'], 'verbose_name': 'День недели', 'verbose_name_plural': 'Дни недели'},
        ),
    ]
