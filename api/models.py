from django.db import models

class Movie(models.Model):
    tittle = models.CharField(max_length=64)
    describe = models.TextField(max_length=256)
    after_premiere = models.BooleanField(default=False)
