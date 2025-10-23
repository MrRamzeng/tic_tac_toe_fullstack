from django.urls import path

from .views import create_game, get_game, make_move

urlpatterns = [
    path('create/', create_game, name='create'),
    path('<int:id>/', get_game, name='get_game'),
    path('<int:id>/move/', make_move, name='move'),
]
