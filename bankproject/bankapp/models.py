from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=250,unique=True)
    password=models.CharField(max_length=250)

    def __str__(self):
        return self.usename

