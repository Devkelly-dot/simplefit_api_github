from django.db import models

from .abstract import BaseModel, Tracked, Name, Goal
from django.utils.translation import gettext_lazy as _

class Lift(BaseModel, Tracked, Name, Goal):
    class MeasurementChoices(models.TextChoices):
        KG  = 'KG', _('kg')
        LB  = 'LB', _('lb')

    measurement = models.CharField(max_length=2, choices=MeasurementChoices.choices,default="LB")
    weight = models.PositiveIntegerField(default=0)
    reps = models.PositiveIntegerField(default=1)


__all__ = (
    "Lift",
)