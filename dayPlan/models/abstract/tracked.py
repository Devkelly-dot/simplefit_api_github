from django.db import models

class Tracked(models.Model):
    complete = models.PositiveIntegerField(default=0)
    my_dayplan = models.ForeignKey("Dayplan",on_delete=models.CASCADE)

    class Meta:
        abstract = True
