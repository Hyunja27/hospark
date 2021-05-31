import random 
from tkinter.constants import NO
from django.shortcuts import render, redirect
from ..middlewares.loadSessionMiddleware import loadSession_middleware
from ..utils.game_data import G_Data, load_data, save_data
from ..settings import basic_data
# Create your views here.

titlemenu = {
    'a': 0,
    'b': 0
}

def press_A(request):
    if titlemenu['a'] == 0:
        titlemenu['b'] = 0
        titlemenu['a'] = 1
        context = {
            'ch_a': "14px",
            'ch_b': "0px"
        }
        print(context)
        return render(request, 'pages/Titlescreen.html', context)
    print("\n\n\n\n\n\n  == gettering Many Movies...... Wait Some Seconds..  ==\n\n\n\n\n\n")
    print("A")
    save_data(G_Data.load_default_settings().dump())
    g = G_Data.load(load_data())
    for index, (key, elem) in enumerate(g.moviemon.items()):
        print("[",index,"]", key, elem)
        basic_data.TOTAL_MON_LIST.append({key : elem})
    tmp = []
    while len(basic_data.IN_GAME_MON_LIST) < 15:
        pick = random.randint(0, len(basic_data.TOTAL_MON_LIST))
        if pick not in tmp:
            tmp.append(pick)
            basic_data.IN_GAME_MON_LIST.append(basic_data.TOTAL_MON_LIST[pick])
    return redirect('Worldmap_page')

def press_B(request):
    if titlemenu['b'] == 0:
        titlemenu['a'] = 0
        titlemenu['b'] = 1
        context = {
            'ch_a': "0px",
            'ch_b': "14px"
        }
        print(context)
        return render(request, 'pages/Titlescreen.html', context)

    return redirect('Load') 


def get_id(request):
    id = request.GET.get('key', None)
    if id == "A":
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
