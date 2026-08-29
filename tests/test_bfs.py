"""
Teste do algoritmo BFS (Busca em Largura).

Verifica se a busca iniciada no ponto "Centro"
percorre as localidades na ordem esperada.
"""

from src.models.city_graph import criar_grafo
from src.algorithms.bfs import busca_em_largura


def test_bfs():
    cidade = criar_grafo()

    resultado = busca_em_largura(cidade, "Centro")

    assert resultado == [
        "Centro",
        "Norte",
        "Sul",
        "Leste",
        "Oeste",
    ]