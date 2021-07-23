from django.db.models import Q
from django.http import QueryDict

from .models import Subject


def filter_subjects(query: QueryDict):
    if len(query) > 0:
        subjects = Subject.objects.filter(
            Q(name__icontains=query.get("q"))
        )
    else:
        subjects = Subject.objects.all()
    return subjects
