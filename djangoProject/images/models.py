from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Image(models.Model):
    text = models.TextField("Text", default="Insert description here", max_length=500)
    image = models.ImageField("Path", height_field=None,\
                              width_field=None, max_length=None)
    liked_by = models.ManyToManyField(User, related_name="liked_images", blank=True)