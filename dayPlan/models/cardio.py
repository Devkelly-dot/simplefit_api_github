from django.db import models

from .abstract import BaseModel, Tracked, Name, Goal
from django.utils.translation import gettext_lazy as _

class Cardio(BaseModel, Tracked, Name, Goal):
    class MeasurementChoices(models.TextChoices):
        MILES  = 'ML', _('Miles')
        MINUTES  = 'MN', _('Minutes')

    measurement = models.CharField(max_length=2, choices=MeasurementChoices.choices,default="MN")
    pass

__all__ = (
    "Cardio",
)