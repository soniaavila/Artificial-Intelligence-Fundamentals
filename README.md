🚚 Otimização Inteligente de Rotas para a Sabor Express

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Python](https://img.shields.io/badge/python-3.13-blue)
![GitHub](https://img.shields.io/badge/github-repositório-black)

Projeto acadêmico desenvolvido para a disciplina Fundamentos da Inteligência Artificial.

🎓 Curso: Gestão da Tecnologia da Informação – UniFECAF

👩 Autora: Sonia Ávila de Oliveira - 


---
## Descrição do Projeto

Este projeto foi desenvolvido como atividade da disciplina Fundamentos da Inteligência Artificial.

O desafio consiste em desenvolver uma solução baseada em Inteligência Artificial para otimizar as rotas de entrega da empresa fictícia Sabor Express, um serviço de delivery localizado na região central da cidade.

Atualmente, as rotas são definidas manualmente pelos entregadores, utilizando apenas sua experiência. Essa abordagem pode gerar atrasos, aumento no consumo de combustível, percursos ineficientes e redução da satisfação dos clientes.

A proposta deste projeto é aplicar algoritmos clássicos de Inteligência Artificial para representar a cidade como um grafo, calcular rotas mais eficientes e agrupar entregas próximas, contribuindo para uma operação mais rápida, econômica e organizada.

---
## Objetivos
### Objetivo Geral

Desenvolver uma solução computacional utilizando algoritmos clássicos de Inteligência Artificial para otimizar as rotas de entrega da empresa Sabor Express.

## Objetivos Específicos

- Representar a cidade por meio de um grafo.
- Modelar bairros, ruas e pontos de entrega.
- Encontrar caminhos eficientes entre diferentes localidades.
- Comparar algoritmos clássicos de busca.
- Agrupar entregas utilizando técnicas de aprendizado não supervisionado.
- Avaliar os resultados obtidos.

---
## Ferramentas e Tecnologias

As seguintes tecnologias serão utilizadas durante o desenvolvimento do projeto:

- **Python 3.13** — linguagem utilizada para desenvolver toda a solução proposta.
- **NetworkX** — criação e manipulação do grafo utilizado pelos algoritmos de busca.
- **NumPy** — operações matemáticas e manipulação de dados numéricos.
- **Pandas** — leitura e tratamento dos arquivos CSV utilizados no projeto.
- **Matplotlib** — geração de gráficos e visualização dos resultados.
- **Scikit-Learn** — implementação do algoritmo K-Means para agrupamento das entregas.
- **Visual Studio Code** — ambiente de desenvolvimento utilizado para implementação e testes da aplicação.
- **Git** — controle de versão do projeto.
- **GitHub** — hospedagem e gerenciamento do repositório.

---

Estrutura do Projeto

O projeto foi organizado em diretórios para facilitar o desenvolvimento, manutenção e organização do código-fonte.

## Estrutura do Projeto

O projeto foi organizado em diretórios para facilitar o desenvolvimento.

- 📁 src
  - 📁 algorithms
  - 📁 models
  - 📁 utils
- 📁 data
- 📁 docs
- 📁 images
- 📁 notebooks
- 📁 tests
- 📄 README.md
- 📄 requirements.txt
- 📄 .gitignore

## Explicação das Pastas

📁 src/

A pasta src (source) reúne todo o código-fonte do projeto. Nela serão desenvolvidas as funcionalidades da aplicação, incluindo a implementação dos algoritmos de Inteligência Artificial, a modelagem do problema e as funções responsáveis pelo processamento dos dados.

📁 src/algorithms/

Nesta pasta serão implementados os algoritmos responsáveis pela resolução do problema proposto.

Entre os algoritmos previstos para este projeto estão:

Breadth-First Search (BFS);
Depth-First Search (DFS);
A*;
K-Means.

Cada algoritmo será desenvolvido em um módulo independente, facilitando sua manutenção, reutilização e comparação de desempenho.

📁 src/models/

A pasta models armazenará a representação computacional do cenário utilizado na aplicação.

Serão implementadas as estruturas responsáveis por representar:

bairros;
ruas;
pontos de entrega;
conexões entre localidades;
pesos das arestas (distância ou tempo).

Essas estruturas formarão o grafo utilizado pelos algoritmos.

📁 src/utils/

A pasta utils armazenará funções auxiliares utilizadas em diferentes partes da aplicação.

Entre elas poderão estar funções para:

leitura de arquivos;
manipulação de dados;
cálculos auxiliares;
geração de gráficos;
impressão dos resultados.

O objetivo é evitar repetição de código e aumentar a organização do projeto.

📁 data/

A pasta data armazenará todos os arquivos de dados utilizados pela aplicação.

Serão incluídos arquivos CSV contendo informações como:

bairros;
ruas;
pontos de entrega;
conexões entre localidades;
distâncias entre os pontos.

Esses dados servirão de base para construção do grafo.

📁 docs/

A pasta docs armazenará a documentação complementar do projeto.

Entre os documentos previstos estão:

diagramas;
fluxogramas;
documentação técnica;
anotações do desenvolvimento.
📁 images/

A pasta images armazenará todas as imagens utilizadas na documentação.

Entre elas:

diagramas;
gráficos;
fluxogramas;
capturas de tela;
imagens utilizadas no README.
📁 notebooks/

A pasta notebooks será utilizada para armazenar experimentos realizados com o Jupyter Notebook.

Ela poderá conter análises exploratórias, testes dos algoritmos e experimentações antes da implementação definitiva.

📁 tests/

A pasta tests conterá os testes desenvolvidos para validar a aplicação.

Os testes serão utilizados para verificar:

funcionamento dos algoritmos;
consistência dos resultados;
possíveis falhas durante o desenvolvimento.
📄 README.md

O arquivo README.md é o principal documento do projeto.

Ele apresenta:

descrição do problema;
objetivos;
tecnologias utilizadas;
estrutura do projeto;
algoritmos implementados;
instruções de execução;
resultados obtidos;
referências bibliográficas.
📄 requirements.txt

O arquivo requirements.txt lista todas as bibliotecas Python necessárias para executar o projeto.

As dependências podem ser instaladas por meio do comando:

pip install -r requirements.txt
📄 .gitignore

O arquivo .gitignore define quais arquivos e diretórios não devem ser enviados ao repositório Git.

Entre eles:

ambiente virtual (.venv);
arquivos temporários;
cache do Python;
configurações locais do ambiente.

Essa prática mantém o repositório organizado e evita o envio de arquivos desnecessários.

---
## Modelagem do Problema

O cenário será representado por um grafo ponderado, no qual:

cada vértice representa um bairro ou ponto de entrega;
cada aresta representa uma rua;
o peso da aresta representa a distância ou o tempo estimado entre dois pontos.

Essa representação permite aplicar algoritmos clássicos de busca para determinar rotas mais eficientes.

---
## Algoritmos Utilizados

Este projeto utilizará algoritmos clássicos estudados na disciplina.

| Algoritmo | Objetivo |
|-----------|----------|
| Breadth-First Search (BFS) | Busca em largura |
| Depth-First Search (DFS) | Busca em profundidade |
| A* | Encontrar o menor caminho |
| K-Means | Agrupar entregas por proximidade |

---
## Fluxo da Solução

Mapa da Cidade
       │
       ▼
Construção do Grafo
       │
       ▼
Aplicação dos Algoritmos
(BFS • DFS • A*)
       │
       ▼
Agrupamento com K-Means
       │
       ▼
Resultados e Análises

---
## Como Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/Artificial-Intelligence-Fundamentals.git
```

### 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 3. Executar o projeto

```bash
python src/main.py
```

---
## Resultados

Esta seção será atualizada conforme o desenvolvimento do projeto.

Serão apresentados:

- caminhos encontrados;
- comparação entre algoritmos;
- tempo de execução;
- gráficos;
- visualizações do grafo.

---

## Limitações

As limitações identificadas durante o desenvolvimento serão documentadas nesta seção.

Entre elas poderão estar:

- simplificação da malha urbana;
- utilização de dados simulados;
- ausência de informações de trânsito em tempo real.

---

## Melhorias Futuras

Como evolução do projeto, poderão ser implementadas:

- integração com APIs de mapas;
- utilização de dados reais de trânsito;
- otimização dinâmica das rotas;
- comparação entre heurísticas do algoritmo A*;
- utilização de aprendizado por reforço;
- desenvolvimento de interface gráfica.

---
## Referências

- Material da disciplina Fundamentos da Inteligência Artificial – UniFECAF.
- Russell, S.; Norvig, P. *Artificial Intelligence: A Modern Approach*.
- Documentação oficial do Python.
- Documentação oficial do NetworkX.
- Documentação oficial do Scikit-Learn.
