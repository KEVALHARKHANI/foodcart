from django.db import models
from home.models import restro,food,address
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Orders(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    foodsid = models.CharField(max_length=200)
    restroid = models.ForeignKey(restro,on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    total=models.BigIntegerField()
    address=models.CharField(max_length=800)
    quantity=models.CharField(max_length=100)
    payment_method=models.CharField(max_length=100)