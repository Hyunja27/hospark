from django.shortcuts import render, redirect
from ..movie_data import movie_total


movie_total.cleaning_db

def views_movies(request, dest) :
    list_url = []
    url = []
    for key, value in movie_total.cleaning_db:
         list_url.append(value["Poster"])
    i = 3
    url = {list_url[i],list_url[i + 1], list_url[i + 2]}
    render (request,dest, url)

