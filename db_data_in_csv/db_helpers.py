import csv

from schedule.models import Subject, Day
from teachers.models import Teacher, Department


def add_teachers_to_db(csv_file: str, department) -> None:
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