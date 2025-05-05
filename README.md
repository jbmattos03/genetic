# genetic
Uma implementação do Algoritmo Genético em Python para resolver o problema da mochila.

# Sumário
1. [O Problema da Mochila](#o-problema-da-mochila)
2. [Algoritmo Genético](#algoritmo-genético)
3. [Implementação](#implementação)

# O Problema da Mochila
Suponha que você tem $n$ classes de itens, cada uma com um **peso** $p$, uma **quantidade máxima** $q$ e um **valor** $v$ associados. Seu objetivo é encher uma mochila com uma combinação de itens destas $n$$ classes de forma a conseguir o **maior valor**, sendo que o peso máximo é $m$.

Ex.: $n = 10$

| Classe |  Peso | Valor | Qtd Máxima |
|--------|-------|-------|------------|
|    1   |   2   |   40  |     5      |
|    2   |   3   |   50  |     4      |
|    3   |   4   |   65  |     3      |
|    4   |   5   |   80  |     2      |
|    5   |   7   |  110  |     1      |
|    6   |   1   |   15  |     6      |
|    7   |   6   |   90  |     2      |
|    8   |  4.5  |   70  |     3      |
|    9   |  3.5  |   60  |     4      |
|   10   |  2.5  |   55  |     5      |

Seu objetivo é encontrar o maior valor $v$ de forma que:

$$v_{max}(n) = \sum_{i=1}^{n} v(i) \times q(i) \leq \sum_{i=1}^{n} p(i) \times q(i)$$

# Algoritmo Genético
Um algoritmo genético tenta imitar a biologia da evolução das espécies para resolver um problema.

## Estrutura
+ Genes: Um fragmento da solução
	+ Ex.: Um valor de um vetor solução
+ Cromossomos: Uma solução
+ População: Conjunto de cromossomos
+ Gerações: Iterações do algoritmo
+ Seleção de pais:
	+ Roleta: 
		+ Soma-se o fitness value de todos os cromossomos
		+ É sorteado um número aleatório
		+ Soma-se o fitness value dos cromossomos um a um, e o cromossomo para o qual a soma supera o número aleatório é selecionado
		+ Elitismo: Melhores pais são preservados ao longo das gerações
+ Crossover: Operação que envolve a troca de genes por dois cromossomos pais, gerando dois novos cromossomos
	+ Taxa de crossover: Probabilidade de um cromossomo selecionado participar da geração de novos membros via crossover
+ Mutação: Probabilidade aleatória de um gene ser modificado

## Especificidades da implementação

Esta implementação do algoritmo genético utiliza a técnica da roleta para selecionar os pais em cada geração. 
+ Cada cromossomo pai cruza com o próximo na lista de selecionados. 
+ A lista é ordenada por ordem cronológica de seleções.
+ A seleção é realizada sem elitismo.

# Implementação
## Arquitetura
Esta implementação utiliza OOP para organização e modularização do código, com cada classe sendo seu próprio módulo em arquivos separados. A lógica principal do algoritmo se encontra no módulo `genetic_algorithm.py`, e a função que vai inicializar as classes, rodar o algoritmo e imprimir os resultados se encontra em `main.py`.

## Como rodar
```bash
cd src
python3 main.py
```