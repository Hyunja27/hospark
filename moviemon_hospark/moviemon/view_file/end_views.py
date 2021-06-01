from django.http import request
from django.shortcuts import render, redirect
from django.urls import path, include
from ..settings import basic_data

def views_End(request) :
    if request.GET.get('key', None) is not None:
        return get_id(request)
    return render(request, 'pages/end.html')

def get_id(request):
    id = request.GET.get('key', None)
    print(id)
    if id == "B":
        print("B")
        return redirect("Moviedex")
    return redirect(request.path)