import networkx as nx


def criar_grafo():
    """
    Cria e retorna o grafo que representa a cidade
    utilizada na simulação do projeto Sabor Express.

    Cada ponto representa uma localidade da cidade
    e cada ligação representa uma rua.
    """

    cidade = nx.Graph()

    # Pontos da cidade e suas coordenadas.
    cidade.add_nodes_from([
        ("Centro", {"pos": (0, 0)}),
        ("Norte", {"pos": (0, 3)}),
        ("Sul", {"pos": (0, -3)}),
        ("Leste", {"pos": (3, 0)}),
        ("Oeste", {"pos": (-3, 0)})
    ])

    # Ruas e distâncias.
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


if __name__ == "__main__":
    cidade = criar_grafo()

    print("Grafo da cidade criado com sucesso!")
    print("Pontos:")
    print(list(cidade.nodes))

    print("\nRuas e distâncias:")
    print(list(cidade.edges(data=True)))