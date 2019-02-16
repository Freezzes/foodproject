from django.db import models

# Create your models here.

class Shop(models.Model):
    shop_name = models.CharField(max_length=200)
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.shop_name


class review(models.Model):
    name = models.ForeignKey(Shop, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.comment

    def shop_score(self):
        return self.score