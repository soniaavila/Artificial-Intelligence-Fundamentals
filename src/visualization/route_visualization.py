"""
Visualização de uma rota encontrada pelo algoritmo A*.

Este módulo utiliza NetworkX e Matplotlib para representar
graficamente o grafo da cidade e destacar o caminho encontrado
entre uma origem e um destino.

A visualização facilita a interpretação dos resultados
obtidos pelo algoritmo A*.
"""

import matplotlib.pyplot as plt
import networkx as nx

from src.models.city_graph import criar_grafo
from src.algorithms.astar import busca_a_estrela


def visualizar_rota(grafo, caminho, origem, destino):
    """
    Exibe o grafo da cidade destacando a rota encontrada.

    Parâmetros:
        grafo: grafo que representa a cidade.
        caminho: lista de pontos que formam a rota encontrada.
        origem: ponto inicial da rota.
        destino: ponto final da rota.
    """

    # ---------------------------------------------------------------
    # POSIÇÃO DOS PONTOS
    # ---------------------------------------------------------------

    # Define uma disposição fixa dos pontos.
    # O seed garante que o desenho permaneça consistente
    # entre diferentes execuções.
    posicoes = nx.spring_layout(
        grafo,
        seed=42
    )

    # ---------------------------------------------------------------
    # CRIAÇÃO DA FIGURA
    # ---------------------------------------------------------------

    plt.figure(
        figsize=(12, 8)
    )

    # ---------------------------------------------------------------
    # DESENHO DAS RUAS
    # ---------------------------------------------------------------

    # Desenha todas as ruas do grafo.
    # As ruas que não fazem parte da rota ficam em cinza.
    nx.draw_networkx_edges(
        grafo,
        pos=posicoes,
        edge_color="lightgray",
        width=2
    )

    # ---------------------------------------------------------------
    # DESENHO DOS PONTOS
    # ---------------------------------------------------------------

    # Desenha todos os pontos inicialmente em cinza.
    nx.draw_networkx_nodes(
        grafo,
        pos=posicoes,
        node_color="lightgray",
        node_size=1800
    )

    # ---------------------------------------------------------------
    # NOMES DOS PONTOS
    # ---------------------------------------------------------------

    nx.draw_networkx_labels(
        grafo,
        pos=posicoes,
        font_size=11,
        font_weight="bold"
    )

    # ---------------------------------------------------------------
    # DESTAQUE DA ROTA
    # ---------------------------------------------------------------

    if caminho:

        # Cria as conexões que fazem parte da rota.
        arestas_rota = list(
            zip(caminho, caminho[1:])
        )

        # Destaca as ruas utilizadas pela rota.
        nx.draw_networkx_edges(
            grafo,
            pos=posicoes,
            edgelist=arestas_rota,
            edge_color="red",
            width=5
        )

        # Destaca todos os pontos que fazem parte da rota.
        nx.draw_networkx_nodes(
            grafo,
            pos=posicoes,
            nodelist=caminho,
            node_color="orange",
            node_size=2000
        )

        # Destaca a origem em verde.
        nx.draw_networkx_nodes(
            grafo,
            pos=posicoes,
            nodelist=[origem],
            node_color="green",
            node_size=2200
        )

        # Destaca o destino em azul.
        nx.draw_networkx_nodes(
            grafo,
            pos=posicoes,
            nodelist=[destino],
            node_color="blue",
            node_size=2200
        )

        # Desenha novamente os nomes para garantir
        # que permaneçam visíveis sobre os nós.
        nx.draw_networkx_labels(
            grafo,
            pos=posicoes,
            font_size=11,
            font_weight="bold"
        )

    # ---------------------------------------------------------------
    # PESOS DAS RUAS
    # ---------------------------------------------------------------

    # Recupera os pesos associados às ruas.
    pesos = nx.get_edge_attributes(
        grafo,
        "weight"
    )

    # Exibe os pesos das ruas no gráfico.
    nx.draw_networkx_edge_labels(
        grafo,
        pos=posicoes,
        edge_labels=pesos,
        font_size=10
    )

    # ---------------------------------------------------------------
    # TÍTULO
    # ---------------------------------------------------------------

    plt.title(
        f"Rota A* - {origem} → {destino}",
        fontsize=16
    )

    # Remove os eixos para deixar o gráfico mais limpo.
    plt.axis("off")

    # Ajusta automaticamente os elementos da figura.
    plt.tight_layout()

    # ---------------------------------------------------------------
    # SALVAMENTO DA IMAGEM
    # ---------------------------------------------------------------

    # Salva a visualização na pasta images.
    #
    # Esta imagem poderá ser utilizada posteriormente:
    # - no README;
    # - na documentação;
    # - na apresentação;
    # - no vídeo da entrega.
    plt.savefig(
        "images/rota_astar_centro_oeste.png",
        dpi=300,
        bbox_inches="tight"
    )

    # ---------------------------------------------------------------
    # EXIBIÇÃO
    # ---------------------------------------------------------------

    # Abre a janela com o gráfico.
    plt.show()


# ===================================================================
# EXECUÇÃO PARA TESTE
# ===================================================================

if __name__ == "__main__":
    """
    Executa um exemplo de visualização da rota A*.

    Neste exemplo:
        Origem: Centro
        Destino: Oeste
    """

    # ---------------------------------------------------------------
    # CRIA O GRAFO
    # ---------------------------------------------------------------

    cidade = criar_grafo()

    # ---------------------------------------------------------------
    # DEFINE ORIGEM E DESTINO
    # ---------------------------------------------------------------

    origem = "Centro"
    destino = "Oeste"

    # ---------------------------------------------------------------
    # EXECUTA O ALGORITMO A*
    # ---------------------------------------------------------------

    caminho, custo = busca_a_estrela(
        cidade,
        origem,
        destino
    )

    # ---------------------------------------------------------------
    # RESULTADO NO TERMINAL
    # ---------------------------------------------------------------

    print("Visualização da rota A*")
    print("-----------------------")
    print("Ponto de origem:", origem)
    print("Destino:", destino)
    print("Caminho encontrado:", caminho)
    print("Custo total:", custo)

    # ---------------------------------------------------------------
    # GERA A VISUALIZAÇÃO
    # ---------------------------------------------------------------

    visualizar_rota(
        cidade,
        caminho,
        origem,
        destino
    )