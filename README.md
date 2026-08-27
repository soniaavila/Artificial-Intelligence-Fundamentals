# 🚚 Otimização Inteligente de Rotas para a Sabor Express

![Status](https://img.shields.io/badge/status-em%20finalização-yellow)
![Python](https://img.shields.io/badge/python-3.13-blue)
![GitHub](https://img.shields.io/badge/github-repositório-black)

Projeto acadêmico desenvolvido para a disciplina **Artificial Intelligence Fundamentals**.

🎓 **Curso:** Gestão da Tecnologia da Informação – UniFECAF  
👩 **Autora:** Sonia Ávila de Oliveira

---

## 📌 Descrição do Projeto

A **Sabor Express** é uma empresa fictícia de delivery de alimentos localizada na região central da cidade.

Durante os horários de maior demanda, como almoço e jantar, a empresa enfrenta dificuldades para definir rotas eficientes para seus entregadores. A definição manual dos percursos pode resultar em:

- atrasos nas entregas;
- percursos maiores que o necessário;
- aumento do consumo de combustível;
- utilização ineficiente dos entregadores;
- redução da satisfação dos clientes.

Diante desse cenário, este projeto propõe uma solução baseada em **algoritmos clássicos de Inteligência Artificial**, utilizando grafos e técnicas de aprendizado não supervisionado.

A cidade é representada como um **grafo ponderado**, no qual os pontos representam localidades e as conexões representam ruas. Os pesos das conexões representam a distância estimada entre os pontos.

A solução utiliza algoritmos de busca para analisar os caminhos disponíveis e o algoritmo **K-Means** para agrupar localidades próximas em zonas de entrega.

---

# 🎯 Objetivos

## Objetivo Geral

Desenvolver uma solução computacional utilizando algoritmos clássicos de Inteligência Artificial para auxiliar na otimização das rotas de entrega da empresa Sabor Express.

## Objetivos Específicos

- Representar a cidade por meio de um grafo ponderado;
- Modelar localidades e conexões entre os pontos;
- Utilizar algoritmos de busca para percorrer o grafo;
- Encontrar caminhos de menor custo entre localidades;
- Comparar o comportamento dos algoritmos BFS, DFS e A*;
- Agrupar localidades próximas utilizando K-Means;
- Organizar as entregas em zonas;
- Avaliar os resultados obtidos;
- Demonstrar como técnicas de Inteligência Artificial podem apoiar decisões logísticas.

---

# 🧠 Abordagem da Solução

A solução foi dividida em duas etapas principais:

### 1. Busca de rotas

A cidade foi modelada como um grafo utilizando a biblioteca **NetworkX**.

Foram implementados três algoritmos de busca:

- BFS (Breadth-First Search);
- DFS (Depth-First Search);
- A* (A-Star).

Os algoritmos permitem analisar diferentes formas de percorrer o grafo e encontrar caminhos entre os pontos da cidade.

### 2. Agrupamento das entregas

Para situações com vários pedidos, foi utilizado o algoritmo **K-Means**, pertencente à área de aprendizado não supervisionado.

As localidades possuem coordenadas fictícias e são agrupadas em duas zonas.

Essa estratégia permite imaginar uma divisão das entregas por regiões, facilitando a organização dos pedidos entre os entregadores.

---

# 🗺️ Modelagem do Grafo

A cidade utilizada na simulação possui cinco localidades:

- Centro;
- Norte;
- Sul;
- Leste;
- Oeste.

As ruas são representadas por arestas e possuem pesos correspondentes às distâncias estimadas.

## Grafo utilizado

```mermaid
graph TD
    Centro ---|4| Norte
    Centro ---|6| Sul
    Centro ---|3| Leste
    Centro ---|5| Oeste
    Norte ---|2| Leste
    Sul ---|2| Oeste
    Leste ---|4| Oeste- Documentação oficial do Scikit-Learn.
