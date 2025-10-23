import json
import pytest

from game.models import Game


@pytest.mark.django_db
def test_make_move_and_winner():
    game = Game.objects.create()
    assert json.loads(game.board) == [""]*9
    assert game.current_player == "X"
    assert game.make_move(0) is True
    assert json.loads(game.board)[0] == "X"
    for cell in range(1, 7):
        assert game.make_move(cell) is True
    assert json.loads(game.board) == [
        'X', 'O', 'X', 'O', 'X', 'O', 'X', '', ''
    ]
    assert game.winner == 'X'
