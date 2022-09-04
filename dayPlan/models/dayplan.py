from django.db import models

from .abstract import BaseModel, Goal
from django.utils.translation import gettext_lazy as _

class Dayplan(BaseModel, Goal):

    class DayChoices(models.TextChoices):
        SUNDAY  = 'SU', _('Sunday')
        MONDAY = 'MO', _('Monday')
        TUESDAY = 'TU', _('Tuesday')
        WEDNESDAY = 'WE', _('Wednesday')
        THURSDAY = 'TH', _('Thursday')
        FRIDAY = 'FR', _('Friday')
        SATURDAY = 'SA', _('Saturday')

    day = models.CharField(max_length=2, choices=DayChoices.choices)
    user = models.ForeignKey("User",on_delete=models.CASCADE)

    def __str__(self):
        string = str(self.id)+": "+"user "+str(self.user.id) + " - " + str(self.day)
        return string
__all__ = (
    "Dayplan",
)