from tkinter.constants import NO
from django.http import request
from django.shortcuts import render, redirect
from ..middlewares.loadSessionMiddleware import loadSession_middleware
from ..utils.game_data import G_Data, load_data, save_data
from ..settings import basic_data
import random
# Create your views here.

situation = {
    'battle': 0,
    'getball': 0,
}

situationmanu = {
    'a' : 0,
    'b' : 0
}

X_MAX = 9
Y_MAX = 9

def toss_coin():
    return random.randint(0,1)

def encounter_something(request):
    situation['getball'] = 1
    g = G_Data.load(load_data())
    if toss_coin():
        if toss_coin():
            if toss_coin() and g.movieballCount < 42:
                if toss_coin(): ball_amount = 2
                else: ball_amount = 1
                g.movieballCount += ball_amount
                save_data(g.dump())
                return request('situation')
    return redirect(request.path)


def press_up(request):
    g = G_Data.load(load_data())
    save_data(g.dump())
    return redirect(request.path)


def press_left(request):
    g = G_Data.load(load_data())
    save_data(g.dump())
    return redirect(request.path)


def press_right(request):
    g = G_Data.load(load_data())
    save_data(g.dump())
    return redirect(request.path)


def press_down(request):
    g = G_Data.load(load_data())
    save_data(g.dump())
    return redirect(request.path)


def press_A(request):
    g = G_Data.load(load_data())
    if situationmanu['a'] == 0:
        situationmanu['a'] = 1
        context = {
            'ch_a': "17px",
            'ball_total': g.movieballCount
        }
        return render(request, 'pages/Obtain.html', context)
    print("A")
    return redirect('Worldmap_page')


def press_B(request):
    print("B")
    return redirect(request.path)


def press_Start(request):
    print("Start")
    return redirect('Option')


def press_Select(request):
    print("Select")
    return redirect('Moviedex')


def get_id(request):
    id = request.GET.get('key', None)
    if id == "up":
        return press_up(request)
    elif id == "left":
        return press_left(request)
    elif id == "right":
        return press_right(request)
    elif id == "down":
        return press_down(request)
    elif id == "A":
        return press_A(request)
    elif id == "B":
        return press_B(request)
    elif id == "Start":
        return press_Start(request)
    elif id == "Select":
        return press_Select(request)
    return redirect(request.path)


def Titlescreen(request):
    id = request.GET.get('key', None)
    if id is not None:
        return get_id(request)
    return render(request, 'pages/Titlescreen.html')

@loadSession_middleware
def Worldmap(request):
    g = G_Data.load(load_data())
    id = request.GET.get('key', None)
    if id is not None:
        return get_id(request)
    context = {'cur_x': g.px,
               'cur_y': g.py,  "ten": [i for i in range(10)], 'ballnum': g.movieballCount}
    return render(request, 'pages/Worldmap.html', context)


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

def Situation_obt(request):
    g = G_Data.load(load_data())
    id = request.GET.get('key', None)
    if id is not None:
        return get_id(request)
    context = {
            'ball_total': g.movieballCount
        }
    return render(request, 'pages/Obtain.html', context)

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