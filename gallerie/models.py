from django.db import models
from django.utils import timezone 

# Create your models here.

class MyPhotoModel(models.Model):
    titre = models.CharField(max_length=200)
    image = models.ImageField(upload_to="gallerie")
    date_creation = models.DateTimeField(default=timezone.now,verbose_name="Date de creation")

    def __str__(self):
        return self.titre