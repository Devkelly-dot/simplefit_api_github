from django.db import models
from django.contrib.auth.models import AbstractUser
from .abstract import Name, BaseModel

class User(BaseModel,AbstractUser,Name):
    email = models.EmailField(unique=True, null=True)

    def __str__(self):
        return self.username

__all__ = (
    "User",
)