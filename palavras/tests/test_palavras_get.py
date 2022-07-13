import pytest
from django.urls import reverse



@pytest.fixture
def resposta(client):
    resp = client.get(reverse('palavras:home'))
    return resp


def test_status_code(resposta):
    assert resposta.status_code == 200