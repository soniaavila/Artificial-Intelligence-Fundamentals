"""
Teste do algoritmo DFS (Busca em Profundidade).

Verifica se a busca iniciada no ponto "Centro"
percorre as localidades na ordem esperada.
"""

from src.models.city_graph import criar_grafo
from src.algorithms.dfs import busca_em_profundidade


def test_dfs():
    cidade = criar_grafo()

    resultado = busca_em_profundidade(cidade, "Centro")

    assert resultado == [
        "Centro",
        "Norte",
        "Leste",
        "Oeste",
        "Sul",
    ]