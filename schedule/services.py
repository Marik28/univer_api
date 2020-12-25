from django.http import QueryDict

from .models import Lesson, Day


def get_week_schedule(request_query: QueryDict) -> list[Lesson]:
    """Возвращает расписание на неделю числитель/знаменатель"""
    if len(request_query) == 0:
        days = Lesson.objects.all()
    else:
        numerator = bool(int(request_query['is_numerator'][0]))
        days = Lesson.objects.filter(is_numerator=numerator)
    return days


def get_day_schedule(request_query: QueryDict):
    """Возвращает расписание на 1 день. Если на этот день нет расписания,
    возвращает None"""
    try:
        week_day = Day.objects.get(code=request_query['day'][0])
    except Day.DoesNotExist:
        day_schedule = None
    else:
        numerator = bool(int(request_query['is_numerator'][0]))
        day_schedule = Lesson.objects.filter(day=week_day).filter(is_numerator=numerator)
    return day_schedule
