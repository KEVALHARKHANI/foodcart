from django.db import models
from login.models import userdata
from django.contrib.auth.models import User
from django.contrib.auth.models import User

# Create your models here.
class restro(models.Model):
    catagery=models.CharField(max_length=100)
    restroname=models.CharField(max_length=200)
    address=models.CharField(max_length=300)
    specialoffer=models.BooleanField()
    offer=models.CharField(max_length=100)
    detail=models.CharField(max_length=500)
    opentime=models.TimeField()
    closetime=models.TimeField()
    image=models.ImageField(upload_to='pics',default='/static/images/restaurant.jpg')
    click=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.restroname


class food(models.Model):
    restroname=models.ForeignKey(restro,related_name='restro',on_delete=models.CASCADE)
    foodname=models.CharField(max_length=100)
    price=models.BigIntegerField()
    image = models.ImageField(upload_to='fpics',default='/static/images/restaurant.jpg')
    contain=models.CharField(max_length=500,default="none")
    catagery=models.CharField(max_length=200,default='none')
    def __str__(self):
        return self.foodname

class cart(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    foodname=models.ForeignKey(food,on_delete=models.CASCADE)
    quantity=models.BigIntegerField()
    restroname=models.ForeignKey(restro,default=3,on_delete=models.CASCADE)
class address(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    pincode=models.BigIntegerField()
    house=models.CharField(max_length=500)
    city=models.CharField(max_length=100)
    location=models.CharField(max_length=100)