from django.http import request
from django.shortcuts import render, redirect
from ..movie_data import movie_total
from django.urls import path, include
from ..settings import basic_data

class Index():
    def __init__(self, num):
        self.num = num
    def press_left(self):
        if (self.num < 0) :
            self.num = len(basic_data.CAPTURE_MON_LIST)
        else :
            self.num = self.num - 1
    def press_right(self):
        if (self.num == len(basic_data.CAPTURE_MON_LIST)) :
            self.num = 0
        else :
            self.num = self.num + 1

index = Index(0)

def views_movies(request):

    dict_cap_mon = {}
    for i in basic_data.CAPTURE_MON_LIST:
        for key, values in i.items() :
            dict_cap_mon[key] = values
    dic_movie = movie_total.cleaning_db()
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
        return get_id(request, index, movie_ls[index.num].imdbID)
    tmp = {
        'movie': movie_dec_ls[index.num]
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

