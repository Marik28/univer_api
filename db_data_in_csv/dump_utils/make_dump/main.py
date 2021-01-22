import csv

from teachers.models import Teacher, TeacherPosition, Department


def make_departments_dump():
    deps = Department.objects.all()
    with open("departments.csv") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "abbreviation"])
        for dep in deps:
            writer.writerow([dep.name, dep.abbreviation])