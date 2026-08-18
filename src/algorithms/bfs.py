"""
Algoritmo de Busca em Largura (BFS).

Este módulo implementa o algoritmo Breadth-First Search (BFS),
utilizado para percorrer o grafo da cidade a partir de um ponto
de origem.

O BFS visita os pontos por níveis, explorando primeiro os pontos
mais próximos da origem antes de avançar para pontos mais distantes.
"""

from collections import deque

from src.models.city_graph import criar_grafo


def busca_em_largura(grafo, origem):
    """
    Realiza uma busca em largura (BFS) no grafo.

    O algoritmo percorre os vértices por níveis. Primeiro são
    visitados os pontos diretamente conectados à origem e,
    posteriormente, os pontos dos níveis seguintes.

    Parâmetros:
        grafo: grafo que será percorrido.
        origem: ponto inicial da busca.

    Retorno:
        list: lista contendo os pontos visitados na ordem
        em que foram encontrados.

    Exceções:
        ValueError: quando o ponto de origem não existe no grafo.
    """

    # Verifica se o ponto de origem existe no grafo.
    if origem not in grafo:
        raise ValueError(
            f"O ponto de origem '{origem}' não existe no grafo."
        )

    # A fila controla a ordem de processamento dos pontos.
    # O BFS utiliza a lógica FIFO:
    # First In, First Out (primeiro a entrar, primeiro a sair).
    fila = deque([origem])

    # Registra os pontos que já foram encontrados.
    # Isso evita que um mesmo ponto seja colocado várias vezes
    # na fila.
    visitados = {origem}

    # Armazena a ordem em que os pontos são visitados.
    ordem_visita = []

    # Continua enquanto existirem pontos aguardando na fila.
    while fila:

        # Remove o primeiro elemento da fila.
        atual = fila.popleft()

        # Registra o ponto na ordem de visitação.
        ordem_visita.append(atual)

        # Obtém os pontos diretamente conectados ao ponto atual.
        for vizinho in grafo.neighbors(atual):

            # Verifica se o vizinho ainda não foi visitado.
            if vizinho not in visitados:

                # Marca o vizinho como visitado.
                visitados.add(vizinho)

                # Coloca o vizinho no final da fila.
                fila.append(vizinho)

    return ordem_visita


if __name__ == "__main__":
    """
    Executa um exemplo do algoritmo BFS utilizando
    o grafo da cidade definido no módulo city_graph.
    """

    # Cria o grafo que representa a cidade.
    cidade = criar_grafo()

    # Define o ponto inicial da busca.
    origem = "Centro"

    # Executa o algoritmo de Busca em Largura.
    resultado = busca_em_largura(cidade, origem)

    # Exibe os resultados no terminal.
    print("Busca em Largura (BFS)")
    print("----------------------")
    print("Ponto de origem:", origem)
    print("Ordem de visitação:")
    print(resultado)