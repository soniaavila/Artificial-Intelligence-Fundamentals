"""
Algoritmo A* (A-Star).

Este módulo implementa o algoritmo A* para encontrar
um caminho de menor custo entre dois pontos do grafo
da cidade.

O algoritmo utiliza:
- o custo já percorrido até o ponto atual;
- uma estimativa do custo restante até o destino.

Dessa forma, o A* consegue direcionar a busca para
o destino de maneira mais eficiente.
"""

import networkx as nx

from src.models.city_graph import criar_grafo


def busca_a_estrela(grafo, origem, destino):
    """
    Encontra o caminho de menor custo entre dois pontos
    utilizando o algoritmo A*.

    Parâmetros:
        grafo: grafo da cidade que será percorrido.
        origem: ponto inicial da rota.
        destino: ponto final da rota.

    Retorno:
        Uma tupla contendo:
        - o caminho encontrado;
        - o custo total do caminho.
    """

    # Executa o algoritmo A* utilizando o peso das ruas.
    caminho = nx.astar_path(
        grafo,
        origem,
        destino,
        weight="weight"
    )

    # Calcula o custo total percorrendo as conexões
    # existentes entre os pontos do caminho.
    custo_total = nx.path_weight(
        grafo,
        caminho,
        weight="weight"
    )

    return caminho, custo_total


if __name__ == "__main__":
    """
    Executa um exemplo do algoritmo A* utilizando
    o grafo da cidade criado no módulo city_graph.
    """

    # Cria o grafo que representa a cidade.
    cidade = criar_grafo()

    # Define o ponto inicial da rota.
    origem = "Centro"

    # Define o destino da rota.
    destino = "Oeste"

    # Executa o algoritmo A*.
    caminho, custo = busca_a_estrela(
        cidade,
        origem,
        destino
    )

    # Exibe os resultados no terminal.
    print("Busca A* (A-Star)")
    print("-----------------")
    print("Ponto de origem:", origem)
    print("Destino:", destino)
    print("Caminho encontrado:", caminho)
    print("Custo total:", custo)