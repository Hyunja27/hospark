from django.http import request
from django.shortcuts import render, redirect
from ..movie_data import movie_total
from django.urls import path, include
from ..settings import basic_data
from .views_moviedex import movie_inf

def views_detail(request, imdbID):

    dict_cap_mon = {}
    for i in basic_data.CAPTURE_MON_LIST:
        for key, values in i.items() :
            dict_cap_mon[key] = values
    
    data = dict_cap_mon[imdbID]
    choice = movie_inf(imdbID=imdbID, Title=data["title"], Poster=data["poster"], Director=data["director"], Year=data["year"], imdbRating=data["rating"], Plot=data["plot"], Actors=data["actors"])
    temp = {
        'detail' : choice
    }
    if request.GET.get('key', None) is not None:
        return get_id(request)
    return render(request, 'pages/Moviedex_detail.html', temp)

def get_id(request):
    id = request.GET.get('key', None)
    print(id)
    if id == "B":
        print("B")
        return redirect("Moviedex")
    return redirect(request.path)