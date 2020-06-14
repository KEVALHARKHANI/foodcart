from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=100)
    expiry_date = models.CharField(max_length=200)
    card_number = models.PositiveIntegerField(default=0)
    username=models.ForeignKey(User,on_delete=models.CASCADE)
