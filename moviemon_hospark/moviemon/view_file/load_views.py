import pickle
from tkinter.constants import NO, NONE
from django.shortcuts import render, redirect
from ..utils.game_data import G_Data, load_data, save_data
import sys
import os
import re


class Index():
    g = G_Data.load(load_data())
    def __init__(self, index, loadA={}, loadB={}, loadC={}):
        self.index = index
        self.loadA = loadA
        self.loadB = loadB
        self.loadC = loadC

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
        if self.index == 0:
            type = "slota"
        elif self.index == 1:
            type = "slotb"
        elif self.index == 2:
            type = "slotc"
        regex = re.compile(type)
        path = "./moviemon/saved_game/"
        for file in sorted(os.listdir(path)):
            if re.match(regex, file) is not None:
                try:
                    data = load_data(path+file)
                    save_data(data)
                    return('load_game')
                except Exception as e:
                    return ('Load')
        return ('Load')

    def input_load(self, loadA={}, loadB={}, loadC={}):
        a_regex = re.compile("slota")
        b_regex = re.compile("slotb")
        c_regex = re.compile("slotc")
        path = "./moviemon/saved_game/"
        for file in sorted(os.listdir(path)):
            if re.match(a_regex, file) is not None:
                self.loadA = load_data(path+file)
                break
            else:
                self.loadA = {}
        for file in sorted(os.listdir(path)):
            if re.match(b_regex, file) is not None:
                self.loadB = load_data(path+file)
                break
            else:
                self.loadB = {}
        for file in sorted(os.listdir(path)):
            if re.match(c_regex, file) is not None:
                self.loadC = load_data(path+file)
                break
            else:
                self.loadC = {}


index = Index(0, 0)


def views_Load(request, load):
    color = [0, 0, 0]
    color[index.index] = "#ffd700"
    index.input_load()
    a = "x"
    b = "x"
    c = "x"
    if not index.loadA:
        pass
    else:
        a = str(len(index.loadA["captured_list"]))
    if not index.loadB:
        pass
    else:
        b = str(len(index.loadB["captured_list"]))
    if not index.loadC:
        pass
    else:
        c = str(len(index.loadC["captured_list"]))
    tmp = {
        'A': color[0],
        'B': color[1],
        'C': color[2],
        "load_A": a,
        "load_B": b,
        "load_C": c,
    }
    if  load == "load" :
        tmp["load"] = "start"
    else :
        tmob["load"] = "load"
    if request.GET.get('key', None) is not None:
        return get_id(request, index)
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
        t = index.press_A()
        return (redirect(t))
    elif id == "B":
        return redirect('Worldmap_page')
    return redirect(request.path)
