from django.db.models import Q
from django.http import QueryDict

from schedule.models import Subject


def filter_subjects(query: QueryDict):
    subjects = Subject.objects.filter(
        Q(name__icontains=query.get("q"))
    )
    return subjects
