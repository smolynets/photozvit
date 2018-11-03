from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=False, null=False)
