from django.db import models

class ExtraInfo(models.Model): # OneToOne
    CATEGORY = {
        (0, 'Undefined'),
        (1, 'Horror'),
        (2, 'Sci-fi'),
        (3, 'Drama'),
        (4, 'Comedy')
    }


    time = models.IntegerField()
    category = models.IntegerField(choices=CATEGORY, default=0)
class Movie(models.Model): #OneToOne
    tittle = models.CharField(max_length=64)
    describe = models.TextField(max_length=256)
    after_premiere = models.BooleanField(default=False)
    premiere = models.DateField(null=True, blank=True)
    year = models.IntegerField()
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2)

    extra_info = models.OneToOneField(ExtraInfo, on_delete=models.CASCADE, null= True, blank=True)
    def __str__(self):
        return self.tittle + "(" + str(self.year) + ")"


class Review(models.Model): #OneToMany
    describe = models.TextField(default='', max_length=500)
    stars = models.IntegerField(default=5)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')

