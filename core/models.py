from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)


class UserProductMapping(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name="mapping", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="mapping", on_delete=models.CASCADE)


class Rating(models.Model):
    id = models.AutoField(primary_key=True)
    productMap = models.ForeignKey(UserProductMapping, related_name="rating", on_delete=models.CASCADE)
    rating = models.FloatField()


