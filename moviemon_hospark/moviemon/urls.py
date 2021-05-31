from . import views
from .view_file import title_views, save_load_views, world_views, option_views, save_views
from django.shortcuts import render, redirect
from django.urls import path, include

urlpatterns = [
    path('', title_views.Titlescreen, name="Titlescreen_page"),
    path('worldmap', world_views.Worldmap, name="Worldmap_page"),
    path('battle/1', views.Battle, name="Battle_page"),
    path('moviedex', views.Moviedex, name="Moviedex"),
    path('moviedex/1', views.Detail, name="Detail"),
    path('options', option_views.Option, name="Option"),
    path('options/save_game', save_views.Save, name="Save"),
    path('options/load_game', save_load_views.Load, name="Load"),
]

