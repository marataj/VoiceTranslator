from django.db import models

# Create your models here.

class Language(models.Model):
    language = models.CharField(max_length=30)
    translate_short = models.CharField(max_length=10)
    recognition_short = models.CharField(max_length=10)

class Translates(models.Model):
    user = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)
    source_language = models.CharField(max_length=50)
    source_text = models.TextField()
    target_language = models.CharField(max_length=50)
    target_text = models.TextField()

