from django.contrib.auth.models import User
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='img/')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
