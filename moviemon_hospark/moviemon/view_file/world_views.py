from tkinter.constants import NO
from django.shortcuts import render, redirect
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
    if (player_pos['y'] > 0):
        player_pos['y'] -= 1
    print("up ", player_pos)
    return redirect(request.path)


def press_left(request):
    if (player_pos['x'] > 0):
        player_pos['x'] -= 1
    print("left ", player_pos)
    cur_x = {'cur_x': player_pos['x']}
    cur_y = {'cur_y': player_pos['y']}
    return redirect(request.path)


def press_right(request):
    if (player_pos['x'] < X_MAX):
        player_pos['x'] += 1
    print("right ", player_pos)
    cur_x = {'cur_x': player_pos['x']}
    cur_y = {'cur_y': player_pos['y']}
    return redirect(request.path)


def press_down(request):
    if (player_pos['y'] < Y_MAX):
        player_pos['y'] += 1
    print("down ", player_pos)
    cur_x = {'cur_x': player_pos['x']}
    cur_y = {'cur_y': player_pos['y']}
    return redirect(request.path)


def press_A(request):

    print("A")
    # return Titlescreen(request)


def press_B(request):

    print("B")
    # return Titlescreen(request)


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


def Worldmap(request):
    id = request.GET.get('key', None)
    if id is not None:
        return get_id(request)
    context = {'cur_x': player_pos['x'],
               'cur_y': player_pos['y'],  "ten": [i for i in range(10)]}
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
