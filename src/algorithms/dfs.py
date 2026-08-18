"""
Algoritmo de Busca em Profundidade (DFS).

Este módulo implementa o algoritmo Depth-First Search (DFS),
utilizado para percorrer o grafo da cidade a partir de um
ponto de origem.

O algoritmo explora um caminho o mais profundamente possível
antes de retornar e explorar outro caminho.
"""

from src.models.city_graph import criar_grafo


def busca_em_profundidade(grafo, origem):
    """
    Realiza uma busca em profundidade (DFS) no grafo.

    A busca em profundidade explora um caminho até o ponto
    mais distante possível antes de retornar para explorar
    outras possibilidades.

    Parâmetros:
        grafo: grafo da cidade que será percorrido.
        origem: ponto inicial da busca.

    Retorno:
        Uma lista contendo os pontos visitados pela ordem
        em que foram encontrados.
    """

    # Conjunto utilizado para registrar os pontos
    # que já foram visitados.
    visitados = set()

    # Lista que armazenará a ordem de visitação.
    ordem_visita = []

    def explorar(atual):
        """
        Função auxiliar responsável por explorar
        o grafo de forma recursiva.
        """

        # Marca o ponto atual como visitado.
        visitados.add(atual)

        # Registra o ponto na ordem de visitação.
        ordem_visita.append(atual)

        # Percorre os vizinhos do ponto atual.
        for vizinho in grafo.neighbors(atual):

            # Se o vizinho ainda não foi visitado,
            # continua a exploração por ele.
            if vizinho not in visitados:
                explorar(vizinho)

    # Inicia a busca pelo ponto de origem.
    explorar(origem)

    return ordem_visita


if __name__ == "__main__":
    """
    Executa um exemplo do algoritmo DFS utilizando
    o grafo da cidade criado no módulo city_graph.
    """

    # Cria o grafo que representa a cidade.
    cidade = criar_grafo()

    # Define o ponto inicial da busca.
    origem = "Centro"

    # Executa o algoritmo DFS.
    resultado = busca_em_profundidade(cidade, origem)

    # Exibe os resultados no terminal.
    print("Busca em Profundidade (DFS)")
    print("--------------------------")
    print("Ponto de origem:", origem)
    print("Ordem de visitação:")
    print(resultado)