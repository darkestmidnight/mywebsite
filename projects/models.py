from django.db import models
from django.utils import timezone
from django.forms import ModelForm
from django.utils.text import slugify
from django.utils.crypto import get_random_string
from django.conf import settings

from PIL import Image

import os

DEFAULT_PROJECT = 1

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=150)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    slug = models.SlugField(unique=True)
    files = models.FileField(upload_to='files/', blank=True)
    images = models.ImageField(upload_to='images/', height_field = 'img_height', width_field = 'img_width',blank=True)
    img_height = models.PositiveIntegerField(default=600)
    img_width = models.PositiveIntegerField(default=300)
    #feature_images = models.ForeignKey(P_Images, on_delete=models.CASCADE, default=DEFAULT_IMAGE_ID)
    feature_images = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Generates a random string 
        unique_string = get_random_string(length=32)

        # Combines title and unique string to slugify
        slugtext = self.title + "-" + "unique_id=-" + unique_string
        self.slug = slugify(slugtext)

        return super(Projects, self).save(*args, **kwargs)

class P_Images(models.Model):
    p_file = models.ImageField(upload_to='images/', blank=None)
    p_uploaded_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    #fk_post = models
    fk_post = models.ForeignKey(Projects, on_delete=models.CASCADE, default=DEFAULT_PROJECT)

def get_p_image_filename(instance, filename):
    title = instance.p_post.title
    slug_title = slugify(title)
    return "post_images/%s-%s" % (slug_slug, filename)