from django.db import models


class Goal(models.Model):
    goal = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True