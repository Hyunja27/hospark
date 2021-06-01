from tkinter.constants import NO
from django.shortcuts import render, redirect
import sys
import os
import re
# Create your views here.


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
        a_regex = re.compile("slota")
        b_regex = re.compile("slotb")
        c_regex = re.compile("slotc")
        directory = os.path.dirname("./moviemon/saved_game/")
        for file in sorted(os.listdir(directory)):
            if re.match(a_regex, file) is not None:
                load["A"] = re.match(a_regex, file)
        for file in sorted(os.listdir(directory)):
            if re.match(b_regex, file) is not None:
                load["B"] = re.match(b_regex, file)
        for file in sorted(os.listdir(directory)):
            if re.match(c_regex, file) is not None:
                load["C"] = re.match(c_regex, file)
        self.load = load

index = Index(0, 0)


def views_Load(request):
    if request.GET.get('key', None) is not None:
        return get_id(request, index)
    color = [0, 0, 0]
    print(index.index)
    color[index.index] = "#ffd700"
    tmp = {
        'A': color[0],
        'B': color[1],
        'C': color[2],
        "load" : index.load
    }
    return render(request, 'pages/Load.html', tmp)

def get_id(request, index):
    id = request.GET.get('key', None)
    load = {"A": 0, "B": 0, "C": 0}
    index.input_load(load)
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
