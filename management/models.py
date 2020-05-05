from django.db import models
from django.contrib.auth.models import User

class category(models.Model):
    name = models.CharField(max_length=64, null=False, blank=True)

    def __str__(self):
        return self.name

class foods(models.Model):
    food_name=       models.CharField(max_length=64, null=False, blank=True)
    price=              models.IntegerField()
    category_fk=   models.ForeignKey(category, on_delete=models.CASCADE, null=True , blank=False)

    def __str__(self):
        return self.food_name
