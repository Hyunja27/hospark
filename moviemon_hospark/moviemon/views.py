from django.shortcuts import render
# from movie_data.movie_total import

# Create your views here.


def Titlescreen(request):
    print(request.GET)
    return render(request, 'pages/Titlescreen.html')

def Wordmap(request):
    return render(request, 'pages/wordmap.html')

def Battle(request):
    return render(request, 'pages/battle/1.html')

def Moviedex(request):
    return render(request, 'pages/moviedex.html')

def Detail(request):
    return render(request, 'pages/moviedex/1.html')

def Option(request):
    return render(request, 'pages/options.html')

def Save(request):
    return render(request, 'pages/options/save_game.html')

def Load(request):
    return render(request, 'pages/options/load_game.html')

def start(request):
    return render(request, 'pages/Titlescreen.html')

