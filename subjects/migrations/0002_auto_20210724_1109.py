# Generated by Django 3.1.4 on 2021-07-24 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='subgroup',
            field=models.IntegerField(choices=[(1, 'First Group'), (2, 'Second Group'), (3, 'Both')], default=3),
        ),
        migrations.AlterField(
            model_name='subjectname',
            name='name',
            field=models.CharField(help_text='Не более 255 символов', max_length=255, verbose_name='Название предмета'),
        ),
    ]