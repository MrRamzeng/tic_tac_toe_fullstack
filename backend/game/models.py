import json

from django.db import models


class Game(models.Model):
    board = models.CharField(max_length=255, default=json.dumps([''] * 9))
    current_player = models.CharField(max_length=1, default='X')
    winner = models.CharField(max_length=1, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def make_move(self, position: int) -> bool:
        board = json.loads(str(self.board))
        if board[position] or self.winner:
            return False

        if 0 <= position < 9:
            board[position] = self.current_player
            self.board = json.dumps(board)
            self._check_winner()
            if not self.winner:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
            self.save()
            return True

    def _check_winner(self):
        board = json.loads(self.board)
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # строки
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # столбцы
            [0, 4, 8], [2, 4, 6]              # диагонали
        ]

        for cell_1, cell_2, cell_3 in win_combinations:
            if (board[cell_1] == board[cell_2] == board[cell_3]
                    and board[cell_3]):
                self.winner = board[cell_3]
                return

        if all(board):
            self.winner = 'D'  # - Draw (Ничья)
        return
