"""
Teste do algoritmo K-Means.

O teste verifica se o algoritmo realiza o agrupamento
das localidades em duas zonas de entrega.
"""

from src.algorithms.kmeans import agrupar_entregas


def test_kmeans():
    resultado = agrupar_entregas()

    # Verifica se todas as cinco localidades foram agrupadas.
    assert len(resultado) == 5

    # Verifica se foram utilizados exatamente dois grupos.
    assert len(set(resultado.values())) == 2