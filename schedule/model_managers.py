from django.db.models import Manager, Q


class LessonManager(Manager):

    def unarchived(self):
        """Пары, находящиеся в архиве"""
        return self.filter(archived=False)

    def archived(self):
        """Пары, не находящиеся в архиве"""
        return self.filter(archive=True)

    def numerator(self):
        """Пары, которые стоят по расписанию на числитель"""
        return self.exclude(parity='D')

    def denominator(self):
        """Пары, которые стоят по расписанию на числитель"""
        return self.exclude(parity='N')
