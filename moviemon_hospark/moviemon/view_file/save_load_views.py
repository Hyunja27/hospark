from tkinter.constants import NO
from django.shortcuts import render, redirect
# Create your views here.

saveloadmenu = {
    'a': 1,
}

def press_up(request):
    if saveloadmenu['a'] != 1:
        saveloadmenu['a'] -= 1
    if saveloadmenu['a'] == 1:
        context = {
            'ch_a': "14px",
            'ch_b': "0px",
            'ch_c': "0px"
        }
    else:
        context = {
            'ch_a': "0px",
            'ch_b': "14px",
            'ch_c': "0px"
        }
    return render(request, 'pages/Load.html', context)

def press_left(request):
    print("left")


def press_right(request):
    print("right")


def press_down(request):
    if saveloadmenu['a'] != 3:
        saveloadmenu['a'] += 1
    if saveloadmenu['a'] == 2:
        context = {
            'ch_a': "0px",
            'ch_b': "14px",
            'ch_c': "0px"
        }
    else:
        context = {
            'ch_a': "0px",
            'ch_b': "0px",
            'ch_c': "14px"
        }
    return render(request, 'pages/Load.html', context)


def press_A(request):
        context = {
            'ch_a': "14px",
            'ch_b': "0px"
        }
        print(context)
        return render(request, 'pages/Titlescreen.html', context)
    # return Titlescreen(request)


def press_B(request):
        context = {
            'ch_a': "0px",
            'ch_b': "14px"
        }
        print(context)
        return render(request, 'pages/Titlescreen.html', context)

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
    return render(request, 'pages/Save.html')


def Load(request):
    id = request.GET.get('key', None)
    if id is not None:
        return get_id(request)
    return render(request, 'pages/Load.html')
