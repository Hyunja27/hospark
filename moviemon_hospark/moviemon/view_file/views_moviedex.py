from django.http import request
from django.shortcuts import render, redirect
from ..movie_data import movie_total

class Index():
    def __init__(self):
        self.num = 0
    def press_left(self):
        self.num = self.num - 1
    def press_right(self):
        self.num = self.num + 1
index = Index()


def views_movies(request):
    dic_movie = movie_total.cleaning_db()
    movie_ls = []
    movie_dec_ls = []
    for id, key in dic_movie.items():
        if (type(key) == dict):
            movie_ls.append(movie_inf(imdbID=id, Title=key["Title"], Poster=key["Poster"], Director=key["Director"], Year=key["Year"], imdbRating=key["imdbRating"], Plot=key["Plot"], Actors=key["Actors"]))
    for i in range(len(movie_ls)):
        prev = i - 1
        now = i
        next = i + 1
        if (i == 0):
            prev = len(movie_ls) - 1
        if (i == len(movie_ls) - 1):
            next = 0
        movie_dec_ls.append(
            movie_dex(movie_ls[prev], movie_ls[now], movie_ls[next]))
    if request.GET.get('key', None) is not None:
        return get_id(request, index, movie_ls)
    tmp = {
        'movie': movie_dec_ls[index.num]
    }
    return render(request, 'pages/Moviedex.html', tmp)


class movie_inf:
    def __init__(self, imdbID, Title, Poster, Director, Year, imdbRating, Plot, Actors):
        self.imdbTd = imdbID
        self.Title = Title
        self.Poster = Poster
        self.Director = Director
        self.Year = Year
        self.imdbRating = imdbRating
        self.Plot = Plot
        self.Actors = Actors

class movie_dex:
    def __init__(self, prev, now, next):
        self.prev = prev
        self.now = now
        self.next = next


def get_id(request, index, movie_dec_ls):
    id = request.GET.get('key', None)
    if id == "left":
        print("left")
        index.press_left()
    elif id == "right":
        print("right")
        index.press_right()
    elif id == "Select":
        return redirect('Worldmap_page')
    elif id == "A":
        temp = {
            'detail' : movie_dec_ls[index.num]
        }
        return render(request, 'pages/Moviedex_detail.html', temp)
    return redirect(request.path)
