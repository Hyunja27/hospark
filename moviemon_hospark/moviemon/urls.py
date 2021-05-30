from . import views

from django.urls import path, include

urlpatterns = [
    path('', views.Titlescreen, name="Titlescreen_page"),
    path('wordmap', views.Wordmap, name="Wordmap_page"),
    path('battle/1', views.Battle, name="Battle_page"),
    path('moviedex', views.Moviedex, name="Moviedex"),
    path('moviedex/1', views.Detail, name="Detail"),
    path('options', views.Option, name="Option"),
    path('options/save_game', views.Save, name="Save"),
    path('options/load_game', views.Load, name="Load"),
    path('start', views.start, name="Load"),
]
