from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User
from .signal import object_viewed_signal
from home.models import restro
class Histroy(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    click=models.PositiveIntegerField()
    object_id=models.ForeignKey(restro,on_delete=models.CASCADE)
    preferred=models.PositiveIntegerField()



