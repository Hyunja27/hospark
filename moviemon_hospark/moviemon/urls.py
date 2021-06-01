from . import views
from .view_file import battle_views, situation_obt_views, title_views, save_load_views, world_views, option_views, save_views, views_moviedex, views_moviedex_detail
from django.shortcuts import render, redirect
from django.urls import path, include

urlpatterns = [
    path('', title_views.Titlescreen, name="Titlescreen_page"),
    path('worldmap', world_views.Worldmap, name="Worldmap_page"),
    path('battle/<str:id>', battle_views.Battle, name="Battle_page"),
    path('moviedex', views_moviedex.views_movies, name="Moviedex"),
    path('moviedex/<str:imdbID>', views_moviedex_detail.views_detail, name="Detail"),
    path('options', option_views.Option, name="Option"),
    path('situation_obt', situation_obt_views.Situation_obt, name="situation_obt"),
    path('situation_cap', situation_obt_views.Situation_cap, name="situation_cap"),
    path('options/save_game', save_views.Save, name="Save"),
    path('options/load_game', save_load_views.Load, name="Load"),
]

#   context = {'mon_id': id,
#            'ballnum': g.movieballCount,
#            'ch_a': "8px",
#             'ch_b': "0px",
#             'poster': mon_info['poster'],
#             'winnig': mon_info['winnig'],
#             'strength': g.get_strength()
#             }
