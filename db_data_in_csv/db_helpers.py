import csv
import datetime as dt

from django.db import IntegrityError
from django.db.models import Model

from schedule.models import Subject, Day, Lesson, LessonKind
from teachers.models import Teacher, Department, TeacherPosition


def add_teachers_to_db(csv_file: str, department: Model) -> None:
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            second_name = row['second_name']
            first_name = row['first_name']
            middle_name = row['middle_name']
            kstu_link = row['kstu_link']
            teacher = Teacher(second_name=second_name, first_name=first_name, middle_name=middle_name,
                              kstu_link=kstu_link, department=department)
            teacher.save()


def add_departments_to_db(csv_file: str) -> None:
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name, abbr = row['name'], row['abbreviation']
            dep = Department(name=name, abbreviation=abbr)
            dep.save()


def add_subjects_to_db(csv_file: str) -> None:
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['name']
            my_link = row['my_link']
            subj = Subject(name=name, my_playlist_url=my_link)
            subj.save()


def add_days_to_db(csv_file: str) -> None:
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            code = row['code']
            name = row['day']
            index = row['index']
            day = Day(name=name, code=code, index=index)
            day.save()


def get_numerator(txt: str):
    if txt == '-':
        return None
    else:
        return bool(txt == 'числитель')


def get_parity(txt: str):
    if txt == '-':
        return 'Всегда'
    return txt.capitalize()


def make_schedule_from_csv(csv_file: str) -> None:
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            subj = Subject.objects.get(name=row['subject'])
            kind = LessonKind.objects.get(name=row['kind'])
            teacher = row['teacher']
            if teacher == '':
                teacher = None
            else:
                teacher = Teacher.objects.get(second_name=teacher.split()[0].strip())
            time = dt.time().fromisoformat(row['time'])
            day = Day.objects.get(name=row['day_of_week'])
            parity = get_parity(row['numerator'])
            print(f'{teacher=}')
            print(f'{subj=}')
            print(f'{kind.name=}')
            if kind.name == 'Лекция':
                subj.lecturer = teacher
            elif kind.name == 'Лабораторное занятие':
                subj.lab_teacher = teacher
            elif kind.name == 'Семинар':
                subj.lab_teacher = teacher
            lesson = Lesson(subject=subj, kind=kind, teacher=teacher, time=time, day=day, parity=parity)
            subj.save()
            try:
                lesson.save()
            except IntegrityError:
                pass


def add_teacher_positions_to_db(filename: str) -> None:
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=",")
        for row in reader:
            print(row)
            name = row['position']
            pos = TeacherPosition(name=name)
            pos.save()


def add_lesson_kinds_to_db(filename: str) -> None:
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=",")
        for row in reader:
            print(row)
            name = row['kind']
            pos = LessonKind(name=name)
            pos.save()
