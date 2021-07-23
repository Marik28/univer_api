from .models import Group


def get_group_list():
    return Group.objects.all()
