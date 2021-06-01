from django.http import request
from django.shortcuts import render, redirect
from django.urls import path, include
from ..middlewares.loadSessionMiddleware import loadSession_middleware
from ..utils.game_data import G_Data, load_data, save_data


class Index():
    g = G_Data.load(load_data())
    def __init__(self, index):
        self.index = index
    def press_left(self):
        if (self.index == 0) :
            self.index = len(self.g.captured_list) - 1
        else :
            self.index = self.index - 1
    def press_right(self):
        if (self.index == len(self.g.captured_list) - 1):
            self.index = 0
        else :
            self.index = self.index + 1

index = Index(0)

def views_movies(request):
    g = G_Data.load(load_data())
    dict_cap_mon = {}
    if not g.captured_list :
        return redirect('Worldmap_page')
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
        if now == next and prev == now :
            movie_dec_ls.append(movie_dex(0, movie_ls[now], 0))
        elif len(g.captured_list) == 2 :
            movie_dec_ls.append(movie_dex(0, movie_ls[now], movie_ls[next]))
        else :
            movie_dec_ls.append(movie_dex(movie_ls[prev], movie_ls[now], movie_ls[next]))
    if request.GET.get('key', None) is not None:
        print(index.index)
        return get_id(request, index, movie_ls[index.index].imdbID)
    print(index.index, len(movie_ls))
    if not movie_dec_ls:
        id = {0}
    elif len(movie_dec_ls) == 1 :
        id = movie_dec_ls[0]
    elif len(movie_dec_ls) == 2:
        id = movie_dec_ls[index.index]
    else :
        id = movie_dec_ls[index.index]
    tmp = {
        'movie': id,
        "index" : index.index,
        "total" : len(movie_dec_ls)
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
    if request.GET.get('key', None) is not None:
        id = request.GET.get('key', None)
    print("id")
    if id == "left":
        print("left")
        index.press_left()
    elif id == "right":
        print("right")
        index.press_right()
    elif id == "Select":
        index.index = 0
        return redirect('Worldmap_page')
    elif id == "A":
        return redirect(request.path+"/"+imdbID)
    return redirect(request.path)

