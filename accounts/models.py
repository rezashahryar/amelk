from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_integer

# Create your models here.


class User(AbstractUser):
    mobile = models.CharField(max_length=11, validators=[validate_integer])

    def __str__(self):
        return self.mobile
