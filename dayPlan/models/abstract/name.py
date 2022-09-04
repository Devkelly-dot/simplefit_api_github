from django.db import models


class Name(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True
