from ..utils.game_data import G_Data, load_data, save_data
from tkinter.constants import NO
from django.shortcuts import render, redirect
from ..middlewares.loadSessionMiddleware import loadSession_middleware
# Create your views here.

player_pos = {
    'x': 5,
    'y': 5
}

situation = {
    'battle': 0,
    'getball': 0,
}

# ten = {}

X_MAX = 9
Y_MAX = 9


def press_up(request):
    g = G_Data.load(load_data())
    if (g.py > 0):
        g.py -= 1
    print("up ", g.py)

    print(g.moviemon)
    save_data(g.dump())
    return redirect(request.path)


def press_left(request):
    g = G_Data.load(load_data())
    if (g.px > 0):
        g.px -= 1
    print("left ", g.px)
    save_data(g.dump())
    return redirect(request.path)


def press_right(request):
    g = G_Data.load(load_data())
    if (g.px < X_MAX):
        g.px += 1
    print("right ", g.px)
    save_data(g.dump())
    return redirect(request.path)


def press_down(request):
    g = G_Data.load(load_data())
    if (g.py < Y_MAX):
        g.py += 1
    print("down ", g.py)
    save_data(g.dump())
    return redirect(request.path)


def press_A(request):
    if (situation['battle'] == 1 or situation['battle'] == 1):
        player_pos['y'] += 1
    print("A")
    return redirect(request.path)


def press_B(request):
    if (situation['battle'] == 1 or situation['battle'] == 1):
        player_pos['y'] += 1
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
               'cur_y': g.py,  "ten": [i for i in range(10)]}
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
