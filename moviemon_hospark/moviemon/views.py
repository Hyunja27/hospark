from tkinter.constants import NO
from django.shortcuts import render
# from movie_data.movie_total import

# Create your views here.


def press_up():
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
    if id is not None:
        if id == "up":
            press_up
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


def Titlescreen(request):
    get_id(request)
    return render(request, 'pages/Titlescreen.html')


def Wordmap(request):
    get_id(request)
    return render(request, 'pages/wordmap.html')


def Battle(request):
    get_id(request)
    return render(request, 'pages/battle/1.html')


def Moviedex(request):
    get_id(request)
    return render(request, 'pages/moviedex.html')


def Detail(request):
    get_id(request)
    return render(request, 'pages/moviedex/1.html')


def Option(request):
    get_id(request)
    return render(request, 'pages/options.html')


def Save(request):
    get_id(request)
    return render(request, 'pages/options/save_game.html')


def Load(request):
    get_id(request)
    return render(request, 'pages/options/load_game.html')

<<<<<<< HEAD
def start(request):
    return render(request, 'pages/Titlescreen.html')

=======
# def up(request) :
    # get_id(request)
    # print(request.Get())
>>>>>>> 7faa8416bc2f6f6ecf70d39e0f9389e31d2193fa
