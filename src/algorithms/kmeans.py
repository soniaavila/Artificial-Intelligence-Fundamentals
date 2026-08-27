"""
Algoritmo K-Means.

Este módulo utiliza o algoritmo K-Means para agrupar
pontos de entrega próximos em zonas.

A ideia é auxiliar a Sabor Express a organizar os pedidos
em grupos de regiões, facilitando o planejamento das entregas.
"""

from sklearn.cluster import KMeans


def agrupar_entregas():
    """
    Agrupa os pontos de entrega em zonas utilizando K-Means.

    Retorna:
        Um dicionário contendo cada localidade e o grupo
        ao qual ela pertence.
    """

    # Coordenadas fictícias das localidades da cidade.
    # Os valores representam a posição aproximada de cada ponto.
    pontos = {
    "Centro": [0, 0],
    "Norte": [0, 3],
    "Sul": [0, -3],
    "Leste": [3, 0],
    "Oeste": [-3, 0]
}

    # Converte as coordenadas para uma lista.
    locais = list(pontos.keys())
    coordenadas = list(pontos.values())

    # Define a quantidade de zonas de entrega.
    kmeans = KMeans(
        n_clusters=2,
        random_state=42,
        n_init=10
    )

    # Realiza o agrupamento.
    grupos = kmeans.fit_predict(coordenadas)

    # Organiza o resultado.
    resultado = {}

    for local, grupo in zip(locais, grupos):
        resultado[local] = grupo + 1

    return resultado


if __name__ == "__main__":
    """
    Executa um exemplo do agrupamento de entregas.
    """

    resultado = agrupar_entregas()

    print("K-Means - Agrupamento de Entregas")
    print("---------------------------------")
    print("Quantidade de zonas: 2")
    print()

    for grupo in sorted(set(resultado.values())):
        locais = [
            local
            for local, grupo_local in resultado.items()
            if grupo_local == grupo
        ]

        print(f"Zona {grupo}:")
        print(locais)
        print()