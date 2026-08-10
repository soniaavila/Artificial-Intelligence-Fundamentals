"""
Algoritmo de Busca em Largura (BFS).

Este módulo implementa o algoritmo Breadth-First Search (BFS),
utilizado para percorrer o grafo da cidade a partir de um ponto
de origem.

O algoritmo visita primeiro os pontos mais próximos da origem
antes de avançar para pontos mais distantes.
"""

from collections import deque

from src.models.city_graph import criar_grafo


def busca_em_largura(grafo, origem):
    """
    Realiza uma busca em largura (BFS) no grafo.

    A busca em largura percorre os vértices do grafo por níveis,
    visitando primeiro os pontos diretamente conectados à origem
    e, depois, os pontos dos níveis seguintes.

    Parâmetros:
        grafo: grafo da cidade que será percorrido.
        origem: ponto inicial da busca.

    Retorno:
        Uma lista contendo os pontos visitados pela ordem
        em que foram encontrados.
    """

    # Fila utilizada para controlar a ordem de visitação.
    fila = deque([origem])

    # Conjunto utilizado para registrar os pontos que já foram visitados.
    visitados = {origem}

    # Lista que armazenará a ordem de visitação dos pontos.
    ordem_visita = []

    # Enquanto existirem pontos aguardando na fila.
    while fila:

        # Remove o primeiro ponto da fila.
        atual = fila.popleft()

        # Registra o ponto na ordem de visitação.
        ordem_visita.append(atual)

        # Percorre os vizinhos do ponto atual.
        for vizinho in grafo.neighbors(atual):

            # Verifica se o vizinho ainda não foi visitado.
            if vizinho not in visitados:

                # Marca o vizinho como visitado.
                visitados.add(vizinho)

                # Adiciona o vizinho ao final da fila.
                fila.append(vizinho)

    return ordem_visita


if __name__ == "__main__":
    """
    Executa um exemplo do algoritmo BFS utilizando
    o grafo da cidade criado no módulo city_graph.
    """

    # Cria o grafo que representa a cidade.
    cidade = criar_grafo()

    # Define o ponto inicial da busca.
    origem = "Centro"

    # Executa o algoritmo BFS.
    resultado = busca_em_largura(cidade, origem)

    # Exibe os resultados no terminal.
    print("Busca em Largura (BFS)")
    print("----------------------")
    print("Ponto de origem:", origem)
    print("Ordem de visitação:")
    print(resultado)