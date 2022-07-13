import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains



@pytest.fixture
def resposta(client):
    resp = client.get(reverse('palavras:home'))
    return resp


def test_status_code(resposta):
    assert resposta.status_code == 200


def test_se_o_formulario_esta_na_pagina(resposta):
    assertContains(resposta, '<form')


def test_se_o_botao_salvar_eh_do_tipo_submit(resposta):
    assertContains(resposta, '<button type="submit"')