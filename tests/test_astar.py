"""
Teste do algoritmo A* (A-Star).

Verifica se o algoritmo encontra o caminho de menor
custo entre "Centro" e "Oeste".
"""

from src.models.city_graph import criar_grafo
from src.algorithms.astar import busca_a_estrela


def test_astar():
    cidade = criar_grafo()

    caminho, custo = busca_a_estrela(
        cidade,
        "Centro",
        "Oeste"
    )

    assert caminho == ["Centro", "Oeste"]
    assert custo == 5