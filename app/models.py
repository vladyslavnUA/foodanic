from django.db import models
from datetime import datetime, timedelta
from markdownx.models import MarkdownxField

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    prep = models.CharField(max_length=255)
    cook = models.CharField(max_length=255)
    servings = models.IntegerField(default=1, null=True, blank=True)
    image = models.ImageField(upload_to='media/')
    ingredients = MarkdownxField()
    directions = MarkdownxField()
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name