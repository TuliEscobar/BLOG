from django.db import models

from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    dni = models.IntegerField(null=True, blank=True)

class Meta:
    db_table="usuarios"
