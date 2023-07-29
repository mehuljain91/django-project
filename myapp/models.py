from django.db import models
from django.db import connections

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    role = models.CharField(max_length=100)
    class Meta:
        db_table = "users"