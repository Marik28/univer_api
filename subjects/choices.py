from django.db import models


class SubGroup(models.Choices):
    FIRST_GROUP = 1
    SECOND_GROUP = 2
    BOTH = 3
