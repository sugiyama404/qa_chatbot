from django.db import models

# Create your models here.
class Ghostintheshell(models.Model):
    category = models.CharField(max_length=100)
    question = models.TextField()
    answer = models.TextField()

