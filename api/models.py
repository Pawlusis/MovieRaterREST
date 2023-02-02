from django.db import models

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class ExtraInfo(models.Model):
    CATEGORIES = {
        (0, 'Undefined'),
        (1, 'Horror'),
        (2, 'Sci-fi'),
        (3, 'Drama'),
        (4, 'Comedy')
    }

    time = models.IntegerField()
    category = models.IntegerField(choices=CATEGORIES, default=0)

class Movie(models.Model):
    tittle = models.CharField(max_length=32)
    describe = models.TextField(max_length=256)
    after_premiere = models.BooleanField(default=False)
    premiere = models.DateField(null=True, blank=True)
    year = models.IntegerField()
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2,
                                      null=True, blank=True)
    extra_info = models.OneToOneField(ExtraInfo, on_delete=models.CASCADE,
                                      null=True, blank=True)

    def __str__(self):
        return self.our_name()

    def our_name(self):
        return self.tittle + " (" + str(self.year) + ")"

class Review(models.Model):
    describe = models.TextField(default='')
    stars = models.IntegerField(default=5)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                             related_name='reviews')

class Actor(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    movies = models.ManyToManyField(Movie)