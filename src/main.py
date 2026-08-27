from src.models.city_graph import criar_grafo
from src.algorithms.bfs import busca_em_largura
from src.algorithms.dfs import busca_em_profundidade
from src.algorithms.astar import busca_a_estrela
from src.algorithms.kmeans import agrupar_entregas


def main():
    print("=" * 50)
    print("SABOR EXPRESS")
    print("Otimização Inteligente de Rotas")
    print("=" * 50)

    # Cria o grafo da cidade
    cidade = criar_grafo()

    # -------------------------------------------------
    # BFS - Busca em Largura
    # -------------------------------------------------

    print("\nBFS - Busca em Largura")
    print("----------------------")

    resultado_bfs = busca_em_largura(cidade, "Centro")

    print("Ponto de origem: Centro")
    print("Ordem de visitação:")
    print(resultado_bfs)

    # -------------------------------------------------
    # DFS - Busca em Profundidade
    # -------------------------------------------------

    print("\nDFS - Busca em Profundidade")
    print("---------------------------")

    resultado_dfs = busca_em_profundidade(cidade, "Centro")

    print("Ponto de origem: Centro")
    print("Ordem de visitação:")
    print(resultado_dfs)

    # -------------------------------------------------
    # A* - Busca pelo menor caminho
    # -------------------------------------------------

    print("\nA* - Menor Caminho")
    print("------------------")

    caminho, custo = busca_a_estrela(
        cidade,
        "Centro",
        "Oeste"
    )

    print("Ponto de origem: Centro")
    print("Destino: Oeste")
    print("Caminho encontrado:", caminho)
    print("Custo total:", custo)

    # -------------------------------------------------
    # K-Means - Agrupamento de Entregas
    # -------------------------------------------------

    print("\nK-Means - Agrupamento de Entregas")
    print("---------------------------------")

    resultado_kmeans = agrupar_entregas()

    quantidade_zonas = len(
        set(resultado_kmeans.values())
    )

    print("Quantidade de zonas:", quantidade_zonas)
    print()

    for grupo in sorted(
        set(resultado_kmeans.values())
    ):

        locais = [
            local
            for local, grupo_local in resultado_kmeans.items()
            if grupo_local == grupo
        ]

        print(f"Zona {grupo}:")
        print(locais)
        print()

    # -------------------------------------------------
    # Finalização
    # -------------------------------------------------

    print("=" * 50)
    print("Execução finalizada com sucesso!")
    print("=" * 50)


if __name__ == "__main__":
    main()