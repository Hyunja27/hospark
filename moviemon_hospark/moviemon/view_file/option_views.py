from tkinter.constants import NO
from django.shortcuts import render, redirect
from . import title_views, load_views, world_views
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
        return render(request, 'pages/Options.html', context)
    print("A")
    return redirect('Save')


def press_B(request):
    if titlemenu['b'] == 0:
        titlemenu['a'] = 0
        titlemenu['b'] = 1
        context = {
            'ch_a': "0px",
            'ch_b': "14px"
        }
        print(context)
        return render(request, 'pages/Options.html', context)
    print("B")
    return redirect('Titlescreen_page') 

def press_Start(request):
    return redirect('Worldmap_page') 


def get_id(request):
    id = request.GET.get('key', None)
    if id == "A":
        return press_A(request)
    elif id == "B":
        return press_B(request)
    elif id == "Start":
        return press_Start(request)
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
    return render(request, 'pages/options/save_game.html')


def Load(request):
    id = request.GET.get('key', None)
    if id is not None:
        return get_id(request)
    return render(request, 'pages/options/load_game.html')
