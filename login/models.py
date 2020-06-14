from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class userdata(models.Model):
    name=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    username= models.CharField(max_length=100)
    email=models.EmailField(max_length=70,blank=True)
    password=models.CharField(max_length=100)
    birthdate=models.DateField(null=True)
    gender=models.CharField(max_length=50)
    phone=models.BigIntegerField()
