from rest_framework import serializers

from .models import Game

class GameSerializer(serializers.ModelSerializer):
    board = serializers.SerializerMethodField()

    class Meta:
        model = Game
        fields = '__all__'

    def get_board(self, game):
        return game.board
