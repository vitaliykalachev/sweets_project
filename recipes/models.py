from django.db import models

# Create your models here.

class Recipes(models.Model):
    recipe_name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)