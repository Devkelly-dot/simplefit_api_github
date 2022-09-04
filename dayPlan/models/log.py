from django.db import models

from .abstract import BaseModel

class Log(BaseModel):
    user = models.ForeignKey("User",on_delete=models.CASCADE)
    date = models.DateField()
    calories = models.TextField(default="None")
    lift = models.TextField(default="None")
    cardio = models.TextField(default="None")

    def __str__(self):
        string = str(self.id)+": "+"user "+str(self.user.id) + " - " + str(self.date)
        return string

__all__ = (
    "Log",
)