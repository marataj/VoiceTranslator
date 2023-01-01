from django.db import models

# Create your models here.

class Language(models.Model):
    language = models.CharField(max_length=30)
    translate_short = models.CharField(max_length=10)
    recognition_short = models.CharField(max_length=10)
