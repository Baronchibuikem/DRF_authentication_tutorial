from django.db import models
from django.contrib.auth.models import AbstractUser, Group


class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    role = models.ManyToManyField(Role)
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email
