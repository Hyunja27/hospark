import pickle
from tkinter.constants import NO, NONE
from django.shortcuts import render, redirect
from ..utils.game_data import G_Data, load_data, save_data
import sys, os, re

class Index():
    def __init__(self, index, load):
        self.index = index
        self.load = load

    def press_left(self):
        if (self.index == 0):
            self.index = 2
        else:
            self.index = self.index - 1

    def press_right(self):
        if (self.index == 2):
            self.index = 0
        else:
            self.index = self.index + 1

    def press_A(self):
        print("a")

    def input_load(self, load):
        path ="./moviemon/saved_game/"
        a_regex = re.compile("slota")
        b_regex = re.compile("slotb")
        c_regex = re.compile("slotc")
        directory = os.path.dirname(path)
        for file in sorted(os.listdir(directory)):
            if re.match(a_regex, file) is not None:
                load.A = load_data(path + file)
            else :
                load.A = {}
        for file in sorted(os.listdir(directory)):
            if re.match(b_regex, file) is not None:
                load.B = load_data(path + file)
            else :
                load.B = {}
        for file in sorted(os.listdir(directory)):
            if re.match(c_regex, file) is not None:
                load.C = re.match(b_regex, file)
            else :
                load.C = {}
        self.load = load

index = Index(0, 0)


def views_Load(request):
    if request.GET.get('key', None) is not None:
        return get_id(request, index)
    color = [0, 0, 0]
    color[index.index] = "#ffd700"
    class load():
        def __init__(self, A, B, C):
            self.A = A 
            self.B = B
            self.C = C 
    index.input_load(load)
    a = "x";
    b = "x";
    c = "x";
    print(index.load.A)
    if (index.load.A is not {}) :
        a = str(len(index.load.A["captured_list"]))
    if (index.load.B is not NONE)  :
        b = str(len(index.load.B["captured_list"]))
    if (index.load.C is not NONE) :
        c = str(len(index.load.C["captured_list"]))
    tmp = {
        'A': color[0],
        'B': color[1],
        'C': color[2],
        "load_A" : a,
        "load_B" : b,
        "load_C" : c,
    }
    return render(request, 'pages/Load.html', tmp)

def get_id(request, index):
    id = request.GET.get('key', None)

   
    if id == "left":
        print("left")
        index.press_left()
    elif id == "right":
        print("right")
        index.press_right()
    elif id == "A":
        print("A")
        index.press_A()
    elif id == "B":
        print("B")
        return redirect('Titlescreen_page')
    return redirect(request.path)
