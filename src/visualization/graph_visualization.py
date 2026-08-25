"""
Visualização do grafo da cidade.

Este módulo utiliza o NetworkX e o Matplotlib para representar
graficamente as localidades e as ruas da cidade utilizada
no projeto Sabor Express.

A visualização permite observar:
- os pontos da cidade;
- as conexões entre as localidades;
- as distâncias entre os pontos.
"""

import matplotlib.pyplot as plt
import networkx as nx

from src.models.city_graph import criar_grafo


def visualizar_grafo(grafo):
    """
    Gera uma visualização do grafo da cidade.

    Parâmetros:
        grafo: grafo da cidade criado com NetworkX.
    """

    # Define a posição dos pontos automaticamente.
    posicao = nx.spring_layout(grafo, seed=42)

    # Cria a área de visualização.
    plt.figure(figsize=(10, 7))

    # Desenha os pontos da cidade.
    nx.draw_networkx_nodes(
        grafo,
        posicao,
        node_size=1800
    )

    # Desenha as ruas que conectam os pontos.
    nx.draw_networkx_edges(
        grafo,
        posicao,
        width=2
    )

    # Exibe o nome de cada localidade.
    nx.draw_networkx_labels(
        grafo,
        posicao,
        font_size=10,
        font_weight="bold"
    )

    # Obtém as distâncias das ruas.
    pesos = nx.get_edge_attributes(grafo, "weight")

    # Exibe as distâncias nas conexões.
    nx.draw_networkx_edge_labels(
        grafo,
        posicao,
        edge_labels=pesos,
        font_size=10
    )

    # Título da visualização.
    plt.title("Grafo da Cidade - Sabor Express")

    # Remove os eixos para deixar o mapa mais limpo.
    plt.axis("off")

    # Ajusta automaticamente os elementos da figura.
    plt.tight_layout()

    # Exibe o gráfico.
    plt.show()


if __name__ == "__main__":
    """
    Executa a visualização do grafo quando este arquivo
    é executado diretamente pelo Python.
    """

    # Cria o grafo da cidade.
    cidade = criar_grafo()

    # Gera a visualização.
    visualizar_grafo(cidade)