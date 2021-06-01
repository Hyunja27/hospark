from django.http import request
from django.shortcuts import render, redirect
from ..movie_data import movie_total
from django.urls import path, include
from ..middlewares.loadSessionMiddleware import loadSession_middleware
from ..utils.game_data import G_Data, load_data, save_data
from ..settings import basic_data
import random

g = G_Data.load(load_data())
class Index():
    def __init__(self, index):
        self.index = index
    def press_left(self):
        if (self.index < 0) :
            self.index = len(g.captured_list) - 1
        else :
            self.index = self.index - 1
    def press_right(self):
        if (self.index == len(g.captured_list) - 1):
            self.index = 0
        else :
            self.index = self.index + 1

index = Index(0)

def views_movies(request):
    dict_cap_mon = {}
    print("[",g.captured_list,"]")
    for i in g.captured_list:
        for key, values in i.items() :
            dict_cap_mon[key] = values
    movie_ls = []
    movie_dec_ls = []
    for id, data in dict_cap_mon.items():
        movie_ls.append(movie_inf(imdbID=id, Title=data["title"], Poster=data["poster"], Director=data["director"], Year=data["year"], imdbRating=data["rating"], Plot=data["plot"], Actors=data["actors"]))
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
        return get_id(request, index, movie_ls[index.index].imdbID)
    tmp = {
        'movie': movie_dec_ls[index.index]
    }
    return render(request, 'pages/Moviedex.html', tmp)


class movie_inf:
    def __init__(self, imdbID, Title, Poster, Director, Year, imdbRating, Plot, Actors):
        self.imdbID = imdbID
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


def get_id(request, index, imdbID):
    id = request.GET.get('key', None)
    print(id)
    if id == "left":
        print("left")
        index.press_left()
    elif id == "right":
        print("right")
        index.press_right()
    elif id == "Select":
        return redirect('Worldmap_page')
    elif id == "A":
        return redirect(request.path+"/"+imdbID)
    return redirect(request.path)

