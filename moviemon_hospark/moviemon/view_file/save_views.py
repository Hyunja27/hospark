from tkinter.constants import NO
from django.shortcuts import render, redirect
from ..middlewares.loadSessionMiddleware import loadSession_middleware
from ..utils.game_data import G_Data, load_data, save_data

# Create your views here.

saveloadmenu = {
    'a': 1,
}

saveslot = {
    'slot1': 0,
    'slot2': 2,
    'slot3': 0,
}

choose = {
            'ch_a': "0px",
            'ch_b': "14px",
            'ch_c': "0px"
        }

def press_up(request):
    if saveloadmenu['a'] != 1:
        saveloadmenu['a'] -= 1
    if saveloadmenu['a'] == 1:
        choose['ch_a'] = "14px"
        choose['ch_b'] = "0px"
        choose['ch_c'] = "0px"
    else:
        choose['ch_a'] = "0px"
        choose['ch_b'] = "14px"
        choose['ch_c'] = "0px"
    return redirect(request.path)

def press_left(request):
    print("left")


def press_right(request):
    print("right")


def press_down(request):
    if saveloadmenu['a'] != 3:
        saveloadmenu['a'] += 1
    if saveloadmenu['a'] == 2:
        choose['ch_a'] = "0px"
        choose['ch_b'] = "14px"
        choose['ch_c'] = "0px"
    else:
        choose['ch_a'] = "0px"
        choose['ch_b'] = "0px"
        choose['ch_c'] = "14px"
    return redirect(request.path)


def press_A(request):
    g = G_Data.load(load_data())
    save_data(g.dump())
    return redirect('Option')


def press_B(request):
        # return render(request.path)
    return redirect('Option')

def press_Start(request):
    print("Start")


def press_Select(request):
    print("Select")


def get_id(request):
    id = request.GET.get('key', None)
    if id == "up":
        return press_up(request)
    elif id == "down":
        return press_down(request)
    elif id == "A":
        return press_A(request)
    elif id == "B":
        return press_B(request)
    return redirect(request.path)


def Titlescreen(request):
    id = request.GET.get('key', None)
    if id is not None:
        return get_id(request)
    return render(request, 'pages/Titlescreen.html')


def Worldmap(request):
    id = request.GET.get('key', None)
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
    context = {
        'ch_a': choose['ch_a'],
        'ch_b': choose['ch_b'],
        'ch_c': choose['ch_c'],
        'slot1' : saveslot['slot1'],
        'slot2' : saveslot['slot2'],
        'slot3' : saveslot['slot3'],
        }
    return render(request, 'pages/Save.html', context)


def Load(request):
    id = request.GET.get('key', None)
    if id is not None:
        return get_id(request)
    return render(request, 'pages/Load.html')
