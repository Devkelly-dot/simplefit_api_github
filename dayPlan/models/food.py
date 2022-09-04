from django.db import models

from .abstract import BaseModel, Tracked, Name

class Food(BaseModel, Tracked, Name):
    pass

__all__ = (
    "Food",
)