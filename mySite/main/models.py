from django.db import models

class ImageModel(models.Model):
    image_nobg = models.ImageField(upload_to='images/%Y/%m/%d')
