from django.http import QueryDict

from studenthelp.schedule.models import DaySchedule, Day


def get_week_schedule(request_query: QueryDict) -> list[DaySchedule]:
    """Возвращает расписание на неделю числитель/знаменатель"""
    if len(request_query) == 0:
        days = DaySchedule.objects.all()
    else:
        numerator = bool(int(request_query['is_numerator'][0]))
        days = DaySchedule.objects.filter(is_numerator=numerator)
    return days


def get_day_schedule(request_query: QueryDict):
    """Возвращает расписание на 1 день"""
    week_day = Day.objects.get(code=request_query['day'][0])
    numerator = bool(int(request_query['is_numerator'][0]))
    day_schedule = DaySchedule.objects.filter(day=week_day).filter(is_numerator=numerator)
    return day_schedule
