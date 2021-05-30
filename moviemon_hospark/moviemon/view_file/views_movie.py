from django.shortcuts import render, redirect
from ..movie_data import movie_total


def views_movies(request, dest) :
    list_url = []
    url = []
    c =  movie_total.cleaning_db()
    for value in c.values():
        print(value)
        if (value is not null):
            print(value["Poster"])
        # print(list_url.append(value["Poster"]))
        # print("\n")
    # i = 3
    # url = {list_url[i],list_url[i + 1], list_url[i + 2]}
    return render(request,dest, url)

