# genetic
Uma implementação do Algoritmo Genético em Python para resolver o problema da mochila.

# Sumário
1. [O Problema da Mochila](#o-problema-da-mochila)
2. [Algoritmo Genético](#algoritmo-genético)
3. [Implementação](#implementação)

# O Problema da Mochila
Suponha que você tem 3 classes de itens, 1, 2 e 3, cada um com um custo e um valor associados. Seu objetivo é encher uma mochila com uma combinação de itens destas 3 classes de forma a conseguir o maior valor, sendo que o custo máximo é 20.

| Classe | Custo | Valor |
|--------|-------|-------|
|    1   |   3   |   40  |
|    2   |   5   |  100  |
|    3   |   2   |   50  |

Logo, a função do valor total que pode ser colocado na mochila é a seguinte:
$$f(x) = 3x_1+5x_2+2x_3 \leq 20$$

Restrições:
+ $`x_1 = 3 `$
+ $`x_2 = 2 `$
+ $`x_3 = 5 `$

# Algoritmo Genético
...

# Implementação
## Arquitetura
...

## Como rodar
### 1. Instalar dependências
```bash
source venv.sh
```

### 2. Rodar código
```bash
cd src
python3 main.py
```