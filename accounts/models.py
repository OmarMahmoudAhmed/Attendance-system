from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import OneToOneField
from django.contrib.auth.models import User


# Create your models here.
class UserRegister(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)


