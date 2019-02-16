from django.db import models

# Create your models here.

class Shop(models.Model):
    shop_name = models.CharField(maxlength=200)
    category = models.CharField(maxlength=20)

class review(models.Model):
    name = models.ForeignKey(Shop)
    comment = models.CharField(max_length=200)
    score = models.IntegerField(default=0)