from typing import Optional

from django.db.models import QuerySet

from subjects.choices import SubGroup
from .choices import WeekDays, Parity
from .exceptions import NotCorrectQuery
from .models import Lesson


def filter_lessons(day: Optional[str],
                   group: Optional[str],
                   subgroup: Optional[int],
                   parity: Optional[str]) -> QuerySet[Lesson]:
    lessons: QuerySet = Lesson.objects.all()

    if day is not None:
        if day not in WeekDays:
            raise NotCorrectQuery("'day' query parameter must be a member of WeekDays enumerator")
        else:
            lessons = lessons.filter(day=day)

    if parity is not None:
        if parity not in Parity:
            raise NotCorrectQuery("'parity' query parameter must be a member of Parity enumerator")
        else:
            lessons = lessons.filter(parity=parity)

    if group is not None:
        lessons = lessons.filter(subject__group__name=group)
    else:
        subgroup = None

    if subgroup is not None:
        exception = NotCorrectQuery("'subgroup' query parameter must be a member of SubGroup enumerator")
        try:
            subgroup = int(subgroup)
        except ValueError:
            raise exception from None
        if subgroup not in SubGroup:
            raise exception from None
        else:
            lessons = lessons.filter(subject__subgroup=subgroup)
    return lessons
