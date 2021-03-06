from django.http import QueryDict, HttpResponseBadRequest

from .exceptions import NotCorrectQuery
from .models import Lesson, Day


def parse_num(request_query: QueryDict) -> bool:
    return bool(int(request_query['is_numerator']))


def parse_parity(request_query: QueryDict) -> bool:
    try:
        parity = request_query['parity']
    except KeyError:
        raise NotCorrectQuery('Не было передано значение четности недели')
    if parity == 'числитель':
        return True
    elif parity == 'знаменатель':
        return False
    else:
        raise NotCorrectQuery(f'Неизвестное значение четности недели ({parity}). Допустимы только числитель/знаменатель')


def get_week_schedule(request_query: QueryDict):
    """Возвращает расписание на неделю числитель/знаменатель"""
    if len(request_query) == 0:
        days = Lesson.objects.all()
    else:
        is_numerator = parse_parity(request_query)
        if is_numerator:
            days = Lesson.objects.numerator()
        else:
            days = Lesson.objects.denominator()
    return days


def get_day_schedule(request_query: QueryDict):
    """Возвращает расписание на 1 день. Если на этот день нет расписания,
    возвращает None"""
    try:
        week_day = Day.objects.get(name=request_query['day_name'].lower())
    except KeyError:
        raise NotCorrectQuery("Не передано значение дня недели")
    except Day.DoesNotExist:
        raise NotCorrectQuery("Некорректное значение дня недели")
    else:
        is_numerator = parse_parity(request_query)
        if is_numerator:
            parity_schedule = Lesson.objects.numerator()
        else:
            parity_schedule = Lesson.objects.denominator()
        day_schedule = parity_schedule.filter(day=week_day).filter(archived=False)
    return day_schedule
