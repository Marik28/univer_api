import csv
import datetime as dt

from django.db import IntegrityError
from django.db.models import Model

from schedule.models import Subject, Day, Lesson, LessonKind
from teachers.models import Teacher, Department


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
            subj = Subject(name=name)
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


def make_schedule_from_csv(csv_file: str) -> None:
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row['teacher'].split()[0])
            print(row['numerator'])
            print(row['kind'])
            subj = Subject.objects.get(name=row['subject'])
            kind = LessonKind.objects.get(name=row['kind'])
            teacher = Teacher.objects.get(second_name=row['teacher'].split()[0].strip())
            time = dt.time().fromisoformat(row['time'])
            day = Day.objects.get(name=row['day_of_week'])
            numerator = get_numerator(row['numerator'])

            if numerator is None:
                nums = [True, False]
            else:
                nums = [numerator]
            for num in nums:
                lesson = Lesson(subject=subj, kind=kind, teacher=teacher, time=time, day=day, is_numerator=num)
                try:
                    lesson.save()
                except IntegrityError:
                    pass
