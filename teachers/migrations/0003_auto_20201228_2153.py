# Generated by Django 3.1.4 on 2020-12-28 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_auto_20201219_0112'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='teacher',
            unique_together={('first_name', 'second_name', 'middle_name')},
        ),
    ]