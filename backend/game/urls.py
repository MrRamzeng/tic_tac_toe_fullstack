from django.urls import path

from .views import create_game, get_game, make_move

urlpatterns = [
    path('create/', create_game),
    path('game/<int:id>/', get_game),
    path('game/<int:id>/', make_move),
]
