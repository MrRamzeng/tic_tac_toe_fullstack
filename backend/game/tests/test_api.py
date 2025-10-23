import pytest

from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_game():
    client = APIClient()
    response = client.post(reverse('create'))
    assert response.status_code == 201
    data = response.json()
    assert 'id' in data
    assert 'board' in data
    assert data['board'] == [""] * 9
    assert data['current_player'] == 'X'

    response = client.get(reverse('get_game', args=[data['id']]))
    assert response.status_code == 200
    response = client.post(
        reverse('move', args=[data['id']]), {
            'position': 0
        }, format='json'
    )
    assert response.status_code == 202
    assert response.json()['board'][0] == 'X'
    assert response.json()['current_player'] == 'O'

