from django.db import models


class Movie(models.Model):
    movie_id = models.CharField(max_length=32, unique=True)
    title = models.CharField(max_length=200)
    actor1_name = models.CharField(max_length=100)
    actor2_name = models.CharField(max_length=100, blank=True)
    director_name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    release_year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} ({self.release_year})"
