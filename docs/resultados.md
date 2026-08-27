# 📊 Resultados e Análises

Este documento apresenta os resultados obtidos durante a execução dos
algoritmos de Inteligência Artificial implementados no projeto
**Otimização Inteligente de Rotas para a Sabor Express**.

---

## 1. Cenário Utilizado

A cidade foi representada por cinco localidades:

- Centro
- Norte
- Sul
- Leste
- Oeste

As conexões entre as localidades representam ruas e possuem pesos
correspondentes às distâncias estimadas.

| Origem | Destino | Peso |
|---|---|---:|
| Centro | Norte | 4 |
| Centro | Sul | 6 |
| Centro | Leste | 3 |
| Centro | Oeste | 5 |
| Norte | Leste | 2 |
| Sul | Oeste | 2 |
| Leste | Oeste | 4 |

---

## 2. Resultado da Busca em Largura — BFS

O algoritmo **Breadth-First Search (BFS)** realiza a busca explorando
os nós por níveis.

### Execução

**Ponto de origem:**

```text
Centro