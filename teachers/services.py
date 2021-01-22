from django.db.models import Q
from django.http import QueryDict

from .models import Teacher


def filter_teachers(query: QueryDict):
    q = query.get("q")
    teacher_list = Teacher.objects.filter(
        Q(second_name__iexact=q) | Q(first_name__iexact=q) |
        Q(middle_name__iexact=q)
    )
    return teacher_list
