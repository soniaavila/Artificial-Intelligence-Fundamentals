"""
Algoritmo K-Means.

Este módulo utiliza o algoritmo K-Means para agrupar
pontos de entrega próximos em zonas.

A ideia é auxiliar a Sabor Express a organizar os pedidos
em grupos de regiões, facilitando o planejamento das entregas.
"""

import csv
from pathlib import Path

from sklearn.cluster import KMeans


def carregar_pontos():
    """
    Carrega os pontos de entrega a partir do arquivo CSV.

    Retorna:
        Uma tupla contendo:
        - locais: nomes das localidades;
        - coordenadas: posições numéricas dos pontos.
    """

    caminho_arquivo = (
        Path(__file__).resolve().parents[2]
        / "data"
        / "pontos_entrega.csv"
    )

    locais = []
    coordenadas = []

    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            locais.append(linha["local"])
            coordenadas.append([
                float(linha["x"]),
                float(linha["y"])
            ])

    return locais, coordenadas


def agrupar_entregas():
    """
    Agrupa os pontos de entrega em zonas utilizando K-Means.

    Retorna:
        Um dicionário contendo cada localidade e o grupo
        ao qual ela pertence.
    """

    # Carrega os dados do arquivo CSV.
    locais, coordenadas = carregar_pontos()

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