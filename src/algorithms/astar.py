"""
Algoritmo A* (A-Star).

Este módulo implementa o algoritmo A* para encontrar
um caminho de menor custo entre dois pontos do grafo
da cidade.

O algoritmo utiliza o custo já percorrido e uma
estimativa do custo restante até o destino.
"""

import networkx as nx

from src.models.city_graph import criar_grafo


def heuristica(grafo, atual, destino):
    """
    Calcula uma estimativa do custo entre o ponto atual
    e o destino.

    A heurística utilizada considera o menor custo médio
    por unidade de distância observado nas conexões do grafo.
    """

    pos_atual = grafo.nodes[atual]["pos"]
    pos_destino = grafo.nodes[destino]["pos"]

    distancia = (
        (pos_atual[0] - pos_destino[0]) ** 2
        + (pos_atual[1] - pos_destino[1]) ** 2
    ) ** 0.5

    return distancia


def busca_a_estrela(grafo, origem, destino):
    """
    Encontra o caminho de menor custo entre dois pontos
    utilizando o algoritmo A*.

    Retorna:
        caminho: lista de pontos percorridos.
        custo_total: custo total da rota.
    """

    caminho = nx.astar_path(
        grafo,
        origem,
        destino,
        heuristic=lambda atual, destino: heuristica(
            grafo, atual, destino
        ),
        weight="weight"
    )

    custo_total = nx.path_weight(
        grafo,
        caminho,
        weight="weight"
    )

    return caminho, custo_total


if __name__ == "__main__":

    cidade = criar_grafo()

    origem = "Centro"
    destino = "Oeste"

    caminho, custo = busca_a_estrela(
        cidade,
        origem,
        destino
    )

    print("Busca A* (A-Star)")
    print("-----------------")
    print("Ponto de origem:", origem)
    print("Destino:", destino)
    print("Caminho encontrado:", caminho)
    print("Custo total:", custo)