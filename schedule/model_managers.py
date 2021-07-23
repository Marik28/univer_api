from django.db.models import Manager

from .choices import Parity


class LessonManager(Manager):

    def unarchived(self):
        """Пары, находящиеся в архиве"""
        return self.filter(archived=False)

    def archived(self):
        """Пары, не находящиеся в архиве"""
        return self.filter(archived=True)

    def numerator(self):
        """Пары, которые стоят по расписанию на числитель"""
        return self.unarchived().exclude(parity=Parity.DENOMINATOR)

    def denominator(self):
        """Пары, которые стоят по расписанию на числитель"""
        return self.unarchived().exclude(parity=Parity.NUMERATOR)
