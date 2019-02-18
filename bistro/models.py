from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Category(models.Model):  
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name
        
class Shop(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=200)
    explanation = models.CharField(max_length=200)

    def __str__(self):
        return self.shop_name
    
    def shop_explanation(self):
        return self.explanation

class Review(models.Model):
    name = models.ForeignKey(Shop, on_delete=models.CASCADE)
    review_date = models.DateTimeField('date published')
    score = models.IntegerField(default=0)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.comment

    def shop_score(self):
        return self.score