from django.db import models

# Create your models here.

class Image(models.Model):
    text = models.TextField("Text", default="Insert description here", max_length=500)
    image = models.ImageField("Path", height_field=None,\
                              width_field=None, max_length=None)