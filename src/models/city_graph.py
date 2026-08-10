import networkx as nx


def criar_grafo():
    """
    Cria e retorna o grafo que representa a cidade
    utilizada na simulação do projeto Sabor Express.

    Cada ponto do grafo representa uma localidade da cidade,
    enquanto cada ligação representa uma rua entre duas localidades.

    O peso de cada ligação representa a distância estimada
    entre os pontos.
    """

    # Criação do grafo.
    # Utilizamos Graph porque as ruas serão consideradas
    # como conexões nos dois sentidos.
    cidade = nx.Graph()

    # -----------------------------------------------------------------
    # PONTOS DA CIDADE
    # -----------------------------------------------------------------
    # Cada elemento representa uma localidade que poderá ser
    # utilizada como origem, destino ou ponto de entrega.
    cidade.add_nodes_from([
        "Centro",
        "Norte",
        "Sul",
        "Leste",
        "Oeste"
    ])

    # -----------------------------------------------------------------
    # RUAS E DISTÂNCIAS
    # -----------------------------------------------------------------
    # Cada tupla possui:
    #
    # (origem, destino, distância)
    #
    # O terceiro valor será armazenado como "weight" e poderá
    # ser utilizado posteriormente pelos algoritmos de busca.
    cidade.add_weighted_edges_from([
        ("Centro", "Norte", 4),
        ("Centro", "Sul", 6),
        ("Centro", "Leste", 3),
        ("Centro", "Oeste", 5),
        ("Norte", "Leste", 2),
        ("Sul", "Oeste", 2),
        ("Leste", "Oeste", 4)
    ])

    return cidade


# ---------------------------------------------------------------------
# EXECUÇÃO PARA TESTE
# ---------------------------------------------------------------------
# Este bloco será executado somente quando este arquivo for
# executado diretamente pelo Python.
#
# Isso permite testar a construção do grafo antes de integrá-lo
# aos demais módulos do projeto.
if __name__ == "__main__":

    cidade = criar_grafo()

    print("Grafo da cidade criado com sucesso!")

    # Exibe todos os pontos cadastrados no grafo.
    print("Pontos:", list(cidade.nodes))

    # Exibe as ruas e seus respectivos pesos (distâncias).
    print("Ruas:", list(cidade.edges(data=True)))