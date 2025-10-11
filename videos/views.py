from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm


def movie_list(request):
    q = request.GET.get("q", "").strip()
    if q:
        movies = Movie.objects.filter(title__icontains=q)
    else:
        movies = Movie.objects.all().order_by("title")
    return render(request, "videos/movie_list.html", {"movies": movies, "q": q})


def movie_detail(request, pk):
    m = get_object_or_404(Movie, pk=pk)
    return render(request, "videos/movie_detail.html", {"movie": m})


def movie_create(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            m = form.save()
            return redirect("movie_detail", pk=m.pk)
    else:
        form = MovieForm()
    return render(request, "videos/movie_form.html", {"form": form, "mode": "Create"})


def movie_update(request, pk):
    m = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=m)
        if form.is_valid():
            m = form.save()
            return redirect("movie_detail", pk=m.pk)
    else:
        form = MovieForm(instance=m)
    return render(request, "videos/movie_form.html", {"form": form, "mode": "Update"})


def movie_delete(request, pk):
    m = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        m.delete()
        return redirect("movie_list")
    return render(request, "videos/movie_confirm_delete.html", {"movie": m})
