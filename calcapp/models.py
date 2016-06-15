from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Calculation(models.Model):
    user = models.ForeignKey(User)
    num1 = models.FloatField()
    num2 = models.FloatField()
    mathop = models.CharField(max_length=1)
    result = models.FloatField()
    finalstring = models.TextField()
