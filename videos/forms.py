from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = [
            "movie_id",
            "title",
            "actor1_name",
            "actor2_name",
            "director_name",
            "genre",
            "release_year",
        ]
