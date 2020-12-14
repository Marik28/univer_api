# Generated by Django 3.1.3 on 2020-11-13 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LessonType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Максимальная длина 50 символов', max_length=50, verbose_name='Тип занятия')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название должности')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Максимальная длина 50 символов', max_length=50, verbose_name='Имя преподавателя')),
                ('second_name', models.CharField(help_text='Максимальная длина 50 символов', max_length=50, verbose_name='Фамилия преподавателя')),
                ('middle_name', models.CharField(help_text='Максимальная длина 50 символов', max_length=50, verbose_name='Отчество преподавателя')),
                ('position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='schedule.position', verbose_name='Должность преподавателя')),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': 'Преподаватели',
                'ordering': ['second_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Не более 50 симвлов', max_length=50, verbose_name='Название предмета')),
                ('lab_teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='lab_teacher', to='schedule.teacher', verbose_name='Имя преподавателя, ведущего лабораторные')),
                ('lecturer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='lecturer', to='schedule.teacher', verbose_name='Имя лектора')),
                ('practic_teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='practic_teacher', to='schedule.teacher', verbose_name='Имя преподавателя, ведущего практику')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Время начала занятия')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='schedule.subject', verbose_name='Название предмета')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='schedule.teacher', verbose_name='Преподаватель')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='schedule.lessontype', verbose_name='Типа занятия')),
            ],
            options={
                'verbose_name': 'Пара',
                'verbose_name_plural': 'Пары',
                'ordering': ['time'],
            },
        ),
        migrations.CreateModel(
            name='DayOfWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(verbose_name='День недели')),
                ('is_numerator', models.BooleanField(verbose_name='Является ли числетелем')),
                ('lessons', models.ManyToManyField(to='schedule.Lesson')),
            ],
            options={
                'ordering': ['day'],
            },
        ),
    ]
