from tkinter.constants import NO
from django.shortcuts import render, redirect
# from movie_data.movie_total import

# Create your views here.

memu = 0

def press_up(request):
    print("up")

def press_left():
    print("left")

def press_right():
    print("right")

def press_down():
    print("down")

def press_A():
    print("A")

def press_B():
    print("B")

def press_Start():
    print("Start")

def press_Select():
    print("Select")

def get_id(request):
    id = request.GET.get('key', None)
    if id == "up":
        press_up(request)
    elif id == "left":
        press_left()
    elif id == "right":
        press_right()
    elif id == "down":
        press_down()
    elif id == "A":
        press_A()
    elif id == "B":
        press_B()
    elif id == "Start":
        press_Start()
    elif id == "Select":
        press_Select()
    return redirect(request.path)

def Titlescreen(request):
    id = request.GET.get('key', None)
    if id is not None:
        return get_id(request)
    return render(request, 'pages/Titlescreen.html')

def Worldmap(request):
    id = request.GET.get('key', None)
    print("[", request.path, "]", id)
    if id is not None:
        return get_id(request)
    return render(request, 'pages/Worldmap.html')

def Battle(request):
    id = request.GET.get('key', None)
    if id is not None:
        return get_id(request)
    return render(request, 'pages/Battle.html')

def Moviedex(request):
    id = request.GET.get('key', None)
    if id is not None:
        return get_id(request)
    return render(request, 'pages/Moviedex.html')

def Detail(request):
    id = request.GET.get('key', None)
    if id is not None:
        return get_id(request)
    return render(request, 'pages/Moviedex.html')

def Option(request):
    id = request.GET.get('key', None)
    if id is not None:
        return get_id(request)
    return render(request, 'pages/Options.html')

def Save(request):
    id = request.GET.get('key', None)
    if id is not None:
        return get_id(request)
    return render(request, 'pages/options/save_game.html')

def Load(request):
    id = request.GET.get('key', None)
    if id is not None:
        return get_id(request)
    return render(request, 'pages/options/load_game.html')
