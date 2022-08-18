from django.db import models


# Create your models here.
class User(models.Model):
    user_code = models.CharField(max_length=32, primary_key=True, null=False)
    name = models.CharField(max_length=128, null=False)
    surnames = models.CharField(max_length=256)
    pwd = models.CharField(max_length=8, null=False)
