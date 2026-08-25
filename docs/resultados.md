# Resultados dos Algoritmos

Neste arquivo estão os resultados dos testes realizados com os algoritmos de busca no grafo da cidade fictícia Sabor Express.

Os pontos utilizados foram:

- Centro
- Norte
- Sul
- Leste
- Oeste

---

## 1. Busca em Largura (BFS)

### Teste

**Origem:** Centro

### Resultado

A ordem de visitação encontrada foi:

```text
Centro → Norte → Sul → Leste → Oeste
```

---

## 2. Busca em Profundidade (DFS)

### Teste

**Origem:** Centro

### Resultado

A ordem de visitação encontrada foi:

```text
Centro → Norte → Leste → Oeste → Sul
```

---

## 3. Busca A* (A-Star)

### Teste

**Origem:** Centro

**Destino:** Oeste

### Resultado

O caminho encontrado foi:

```text
Centro → Oeste
```

**Custo total:** 5

### Imagem da rota

![Rota A* - Centro → Oeste](../images/rota_astar_centro_oeste.png)