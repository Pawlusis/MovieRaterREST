from django.db import models

class Movie(models.Model):
    tittle = models.CharField(max_length=64)
    describe = models.TextField(max_length=256)
    after_premiere = models.BooleanField(default=False)
    premiere = models.DateField(null=True, blank=True)
    year = models.IntegerField()
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.tittle + "(" + str(self.year) + ")"
    #test commit


