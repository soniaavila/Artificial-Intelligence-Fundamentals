# 🚚 Otimização Inteligente de Rotas para a Sabor Express

![Status](https://img.shields.io/badge/status-finalizado-green)
![Python](https://img.shields.io/badge/python-3.13-blue)
![GitHub](https://img.shields.io/badge/github-repositório-black)

Projeto acadêmico desenvolvido para a disciplina **Fundamentos da Inteligência Artificial**.

**Curso:** Gestão da Tecnologia da Informação – UniFECAF  
**Autora:** Sonia Ávila de Oliveira

---

## 📌 Descrição do Projeto

A **Sabor Express** é uma empresa fictícia de delivery de alimentos localizada na região central de uma cidade.

Durante os horários de maior demanda, a empresa enfrenta dificuldades para definir rotas eficientes para seus entregadores. A definição manual dos percursos pode resultar em:

- atrasos nas entregas;
- percursos maiores que o necessário;
- aumento do consumo de combustível;
- utilização ineficiente dos entregadores;
- redução da satisfação dos clientes.

Diante desse cenário, este projeto propõe uma solução baseada em **algoritmos clássicos de Inteligência Artificial**, utilizando grafos, algoritmos de busca e aprendizado não supervisionado.

A cidade é representada como um **grafo ponderado**, no qual os pontos representam localidades e as conexões representam ruas. Os pesos das conexões representam as distâncias estimadas entre os pontos.

A solução utiliza os algoritmos **BFS, DFS e A\*** para analisar diferentes estratégias de busca e utiliza o **K-Means** para agrupar localidades em zonas de entrega.

---

# 🎯 Objetivos

## Objetivo Geral

Desenvolver uma solução computacional utilizando algoritmos clássicos de Inteligência Artificial para auxiliar na análise e otimização das rotas de entrega da empresa fictícia Sabor Express.

## Objetivos Específicos

- Representar a cidade por meio de um grafo ponderado;
- Modelar localidades e conexões entre os pontos;
- Utilizar algoritmos de busca para percorrer o grafo;
- Encontrar caminhos de menor custo entre localidades;
- Comparar o comportamento dos algoritmos BFS, DFS e A*;
- Agrupar localidades utilizando K-Means;
- Organizar as localidades em zonas de entrega;
- Avaliar os resultados obtidos;
- Demonstrar a aplicação de técnicas de Inteligência Artificial em um cenário logístico.

---

# 🧠 Abordagem da Solução

A solução foi dividida em duas etapas principais.

## 1. Busca de rotas

A cidade foi modelada como um grafo utilizando a biblioteca **NetworkX**.

Foram utilizados três algoritmos de busca:

- **BFS (Breadth-First Search)** – Busca em Largura;
- **DFS (Depth-First Search)** – Busca em Profundidade;
- **A\* (A-Star)** – Busca pelo menor caminho utilizando custo e heurística.

Os algoritmos permitem analisar diferentes formas de percorrer o grafo e encontrar caminhos entre os pontos da cidade.

## 2. Agrupamento das entregas

Para representar uma situação com vários pedidos, foi utilizado o algoritmo **K-Means**, pertencente à área de aprendizado não supervisionado.

As localidades possuem coordenadas utilizadas para realizar o agrupamento.

Neste projeto foram utilizadas **2 zonas de entrega**.

---

# 🗺️ Modelagem do Grafo

A cidade utilizada na simulação possui cinco localidades:

- Centro;
- Norte;
- Sul;
- Leste;
- Oeste.

As ruas são representadas por arestas e possuem pesos correspondentes às distâncias estimadas.

## Grafo da Cidade

![Grafo da Cidade](images/grafo_cidade.png)

### Representação das conexões

| Origem | Destino | Distância |
|---|---|---:|
| Centro | Norte | 4 |
| Centro | Sul | 6 |
| Centro | Leste | 3 |
| Centro | Oeste | 5 |
| Norte | Leste | 2 |
| Sul | Oeste | 2 |
| Leste | Oeste | 4 |

Os valores utilizados são fictícios e têm como objetivo representar uma pequena malha urbana para fins acadêmicos.

---

# 📍 Dados das Localidades

As coordenadas utilizadas para o agrupamento com K-Means estão armazenadas no arquivo:

```text
data/pontos_entrega.csv
As localidades utilizadas no projeto são:

Centro
Norte
Sul
Leste
Oeste
🔎 Algoritmos Implementados
BFS – Busca em Largura

O algoritmo BFS percorre o grafo explorando os nós por níveis, visitando primeiro os pontos mais próximos do ponto de origem em termos de quantidade de conexões.

Execução
python -m src.algorithms.bfs
Resultado obtido
Busca em Largura (BFS)
----------------------
Ponto de origem: Centro
Ordem de visitação:
['Centro', 'Norte', 'Sul', 'Leste', 'Oeste']
DFS – Busca em Profundidade

O algoritmo DFS explora um caminho em profundidade antes de retornar e explorar outras possibilidades.

Execução
python -m src.algorithms.dfs
Resultado obtido
Busca em Profundidade (DFS)
--------------------------
Ponto de origem: Centro
Ordem de visitação:
['Centro', 'Norte', 'Leste', 'Oeste', 'Sul']
A* – Busca pelo Menor Caminho

O algoritmo A* utiliza o custo das conexões e uma função heurística para encontrar um caminho de menor custo entre dois pontos.

No exemplo utilizado, o ponto de origem é Centro e o destino é Oeste.

Execução
python -m src.algorithms.astar
Resultado obtido
Busca A* (A-Star)
-----------------
Ponto de origem: Centro
Destino: Oeste
Caminho encontrado: ['Centro', 'Oeste']
Custo total: 5

O resultado demonstra que o caminho direto entre Centro e Oeste possui custo total igual a 5.

🤖 K-Means – Agrupamento de Entregas

O algoritmo K-Means foi utilizado para agrupar as localidades em 2 zonas de entrega.

Execução
python -m src.algorithms.kmeans
Resultado obtido
K-Means - Agrupamento de Entregas
---------------------------------
Quantidade de zonas: 2

Zona 1:
['Centro', 'Norte', 'Leste']

Zona 2:
['Sul', 'Oeste']

O agrupamento permite representar uma possível divisão das localidades entre regiões de atendimento.

🧪 Testes Automatizados

O projeto possui testes automatizados utilizando a biblioteca Pytest.

Foram criados testes para os principais algoritmos implementados:

test_bfs.py
test_dfs.py
test_astar.py
test_kmeans.py

Os testes têm como objetivo verificar se as funções principais dos algoritmos retornam resultados compatíveis com os dados utilizados no projeto.

Executando os testes

Com o ambiente virtual ativado, execute:

python -m pytest
Resultado da validação

Os testes foram executados com sucesso:

================ test session starts ================

collected 4 items

tests/test_astar.py .
tests/test_bfs.py .
tests/test_dfs.py .
tests/test_kmeans.py .

================= 4 passed =================
Resultado

4 testes passaram com sucesso.

Isso confirma que os quatro módulos principais possuem testes automatizados funcionando:

Teste	Resultado
A*	✅ PASSOU
BFS	✅ PASSOU
DFS	✅ PASSOU
K-Means	✅ PASSOU
▶️ Como Executar o Projeto
1. Clonar o repositório
git clone https://github.com/soniaavila/Artificial-Intelligence-Fundamentals.git

Depois entre na pasta:

cd Artificial-Intelligence-Fundamentals
2. Criar o ambiente virtual
python -m venv .venv
3. Ativar o ambiente virtual no Windows
.venv\Scripts\Activate.ps1
4. Instalar as dependências
pip install -r requirements.txt
5. Executar o programa principal
python -m src.main
6. Executar os testes
python -m pytest
🖥️ Execução Principal

O programa principal reúne os resultados dos algoritmos em uma única execução.

Comando:

python -m src.main

Resultado validado:

==================================================
SABOR EXPRESS
Otimização Inteligente de Rotas
==================================================

BFS - Busca em Largura
----------------------
Ponto de origem: Centro
Ordem de visitação:
['Centro', 'Norte', 'Sul', 'Leste', 'Oeste']

DFS - Busca em Profundidade
---------------------------
Ponto de origem: Centro
Ordem de visitação:
['Centro', 'Norte', 'Leste', 'Oeste', 'Sul']

A* - Menor Caminho
------------------
Ponto de origem: Centro
Destino: Oeste
Caminho encontrado: ['Centro', 'Oeste']
Custo total: 5

K-Means - Agrupamento de Entregas
---------------------------------
Quantidade de zonas: 2

Zona 1:
['Centro', 'Norte', 'Leste']

Zona 2:
['Sul', 'Oeste']

==================================================
Execução finalizada com sucesso!
==================================================
📁 Estrutura do Projeto
Artificial-Intelligence-Fundamentals/
│
├── data/
│   └── pontos_entrega.csv
│
├── images/
│   └── grafo_cidade.png
│
├── src/
│   ├── algorithms/
│   │   ├── astar.py
│   │   ├── bfs.py
│   │   ├── dfs.py
│   │   └── kmeans.py
│   │
│   ├── models/
│   │   └── city_graph.py
│   │
│   └── main.py
│
├── tests/
│   ├── test_astar.py
│   ├── test_bfs.py
│   ├── test_dfs.py
│   └── test_kmeans.py
│
├── README.md
└── requirements.txt
🛠️ Tecnologias Utilizadas
Python 3.13
NetworkX
Scikit-learn
Pytest
Git
GitHub
Visual Studio Code
📊 Resultados

A implementação permitiu demonstrar, em um cenário simplificado, diferentes técnicas de Inteligência Artificial aplicadas a um problema de logística.

Os resultados obtidos foram:

Algoritmo	Aplicação	Resultado
BFS	Busca em largura	Percurso dos pontos a partir do Centro
DFS	Busca em profundidade	Percurso dos pontos a partir do Centro
A*	Menor caminho	Centro → Oeste, custo 5
K-Means	Agrupamento	2 zonas de entrega

Os testes automatizados também apresentaram resultado positivo, com 4 testes executados e 4 aprovados.

🎓 Conclusão

O projeto demonstrou a aplicação de algoritmos clássicos de Inteligência Artificial em um cenário de otimização de rotas para uma empresa fictícia de delivery.

A utilização de BFS e DFS permitiu analisar diferentes estratégias de exploração do grafo. O A* possibilitou encontrar um caminho de menor custo entre dois pontos considerando os pesos das conexões. Já o K-Means permitiu agrupar as localidades em zonas de entrega.

Além da implementação dos algoritmos, foram realizados testes automatizados, garantindo uma validação básica do funcionamento das principais funcionalidades.

Dessa forma, o projeto demonstra como conceitos de Inteligência Artificial podem ser aplicados a problemas relacionados à logística e organização de entregas.

👩‍💻 Autoria

Sonia Ávila de Oliveira

Gestão da Tecnologia da Informação
UniFECAF

Projeto acadêmico – Fundamentos da Inteligência Artificial
