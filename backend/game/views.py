from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Game
from .serializers import GameSerializer


@api_view(['POST'])
def create_game(request):
    serializer = GameSerializer(data=request.data)
    if serializer.is_valid():
        game = serializer.save()
        return Response(GameSerializer(game).data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_game(request, id):
    game = get_object_or_404(Game, pk=id)
    return Response(GameSerializer(game).data, status.HTTP_200_OK)


@api_view(['POST'])
def make_move(request, id):
    game = get_object_or_404(Game, pk=id)
    try:
        position = int(request.data.get('position'))
        if game.make_move(position):
            return Response(GameSerializer(game).data, status.HTTP_202_ACCEPTED)
        else:
            return Response(
                {'error': 'Invalid move'},
                status.HTTP_400_BAD_REQUEST
            )
    except Game.DoesNotExist:
        return Response({'error': 'Game not found'}, status.HTTP_404_NOT_FOUND)

