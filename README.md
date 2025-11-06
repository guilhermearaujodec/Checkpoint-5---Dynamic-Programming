# 💰 Checkpoint — Problema da Troca de Moedas (Coin Change Problem)

## 👥 Integrantes do Grupo
| Nome Completo | RM |
|----------------|----|
| Guilherme Araujo de Carvalho | 558926 |
| Augusto Douglas Nogueira de Mendonça | 558371 |
| Gabriel Vasquez Queiroz da Silva | 557056 |
| Gustavo Oliveira Ribeiro | 559163 |

---

## 🧩 Introdução e Contextualização do Problema

O **Problema da Troca de Moedas (Coin Change Problem)** é um dos desafios mais clássicos da **Computação e Otimização Combinatória**.  
Seu objetivo é **determinar a menor quantidade de moedas necessárias** para formar um determinado montante `M`, considerando um conjunto de moedas disponíveis em **quantidade ilimitada**.

Esse problema é uma base importante para entender o funcionamento de técnicas como **recursão**, **memoização** e **programação dinâmica**, sendo amplamente utilizado em problemas de otimização de sistemas reais — como troco em caixas eletrônicos, alocação de recursos e cálculos financeiros automatizados.

---

## 🎯 Natureza do Problema

### ✅ Objetivo Principal
Encontrar a **combinação de moedas de menor quantidade** cuja soma seja igual ao montante desejado `M`.

### ⚙️ Premissas
- As moedas possuem **valor inteiro positivo**.
- A **quantidade de moedas é ilimitada**.
- Se não for possível atingir o valor exato de `M`, o algoritmo deve retornar **-1**.

### 🧮 Classificação
Este é um **Problema de Otimização**, pois busca **minimizar** o número de moedas usadas entre todas as combinações possíveis.

---

## 🧠 Definição de Programação Dinâmica (PD)

A **Programação Dinâmica (PD)** é uma técnica de otimização que resolve problemas complexos dividindo-os em **subproblemas menores**, cujas soluções são **armazenadas e reutilizadas** para evitar recomputações desnecessárias.

### 🔹 Subestrutura Ótima
Um problema apresenta **subestrutura ótima** quando a **solução ótima global pode ser construída a partir das soluções ótimas dos subproblemas**.  
No caso da Troca de Moedas:
> A solução ótima para `M` depende das soluções ótimas de `M - moeda` para cada moeda disponível.

### 🔹 Subproblemas Sobrepostos
São situações onde o mesmo subproblema é resolvido várias vezes durante a execução.  
Por exemplo, ao calcular a melhor forma de atingir `M = 6`, o algoritmo pode calcular `M = 3` diversas vezes — o que justifica o uso da **memoização** e da **PD Bottom-Up**.

Essas duas propriedades (subestrutura ótima + subproblemas sobrepostos) tornam a PD uma técnica poderosa para resolver o Coin Change Problem.

---

## 🔍 Análise Detalhada das Abordagens

Foram desenvolvidas **quatro abordagens** para resolver o problema, conforme solicitado:  
1. Estratégia Gulosa (Iterativa)  
2. Recursiva Pura (Sem Memoização)  
3. Recursiva com Memoização (Top Down)  
4. Programação Dinâmica (Bottom Up)  

---

### 🥇 Função 1 — Estratégia Gulosa (Iterativa)

#### 🧩 Conceito
A estratégia gulosa escolhe **sempre a maior moeda possível** que não exceda o montante restante.  
É um método rápido e simples, mas **não garante** a solução ótima em todos os casos.

#### 💡 Análise Crítica
Esse método só funciona perfeitamente em sistemas de moedas com **propriedades específicas** (como o sistema monetário brasileiro ou americano).  
Em sistemas arbitrários, ele pode **falhar**, pois a escolha localmente ótima (maior moeda) nem sempre leva à solução globalmente ótima.

#### 🧪 Exemplo de Falha
Para o caso:
```python
M = 6
moedas = [1, 3, 4]
````

* **Gulosa:** escolhe 4 + 1 + 1 → **3 moedas**
* **Ótima (PD):** escolhe 3 + 3 → **2 moedas**

> 🔴 A estratégia gulosa falha neste exemplo.

#### ⚙️ Complexidade

| Notação        | Descrição                     |
| -------------- | ----------------------------- |
| **O(n log n)** | Devido à ordenação das moedas |
| **Ω(n)**       | Caso ótimo                    |
| **Θ(n log n)** | Caso médio                    |

---

### 🧩 Função 2 — Recursiva Pura (Sem Memoização)

#### 🧠 Conceito

A abordagem recursiva pura resolve o problema testando **todas as combinações possíveis** de moedas.
Ela é garantidamente correta, mas extremamente **ineficiente**, pois recalcula os mesmos subproblemas muitas vezes.

#### 🌳 Estrutura de Recursão

Para `M = 6` e `moedas = [1,3,4]`, o algoritmo gera uma **árvore recursiva** onde os mesmos valores (`M = 3`, `M = 2`, etc.) são recalculados várias vezes.

#### 📉 Desempenho

O crescimento é **exponencial** — cada subchamada pode gerar várias outras.
Logo, é impraticável para valores grandes de `M`.

#### ⚙️ Complexidade

| Notação    | Descrição                          |
| ---------- | ---------------------------------- |
| **O(n^M)** | Exponencial (todas as combinações) |
| **Ω(1)**   | Caso base (M = 0)                  |
| **Θ(n^M)** | Complexidade média geral           |

---

### 🧠 Função 3 — Recursiva com Memoização (Top Down)

#### 🧩 Conceito

A memoização utiliza uma **tabela (ou dicionário)** para **armazenar resultados intermediários**, evitando o reprocessamento de subproblemas já resolvidos.

#### 🔗 Ligação com a PD

A memoização é uma forma de **Programação Dinâmica Top Down**, pois o problema é resolvido de cima para baixo (a partir de `M`) e as soluções são armazenadas para reutilização.

#### 🚀 Melhoria de Desempenho

Com memoização, cada submontante é calculado **apenas uma vez**, reduzindo drasticamente o custo computacional.

#### ⚙️ Complexidade

| Notação      | Descrição                                   |
| ------------ | ------------------------------------------- |
| **O(M × n)** | Cada subproblema é resolvido apenas uma vez |
| **Ω(M)**     | Todos os subproblemas são acessados         |
| **Θ(M × n)** | Eficiência geral da abordagem               |

---

### 🧩 Função 4 — Programação Dinâmica (Bottom Up)

#### 🧠 Conceito

Nesta versão, o algoritmo constrói uma **tabela (`dp`) iterativa**, onde `dp[i]` representa o **menor número de moedas necessário para atingir o valor `i`**.

Cada solução é construída **de baixo para cima**, aproveitando os resultados anteriores.

#### 🔄 Fluxo do Algoritmo

Para cada valor `i` de 1 até `M`, o algoritmo verifica todas as moedas:

```
dp[i] = min(dp[i], dp[i - moeda] + 1)
```

Se `dp[M]` permanecer infinito, significa que o montante não pode ser formado.

#### ⚙️ Complexidade

| Notação      | Descrição                               |
| ------------ | --------------------------------------- |
| **O(M × n)** | Percorre todos os submontantes e moedas |
| **Ω(M)**     | Caso de acesso direto                   |
| **Θ(M × n)** | Complexidade média geral                |

#### ⚡ Vantagem sobre Memoização

A versão Bottom-Up é **ligeiramente mais eficiente** por eliminar a sobrecarga de chamadas recursivas, além de ser **iterativa e determinística**.

---

## 📊 Resumo Comparativo das Abordagens

| Método                        | Estratégia            | Garante Solução Ótima | Complexidade de Tempo | Observações                           |
| :---------------------------- | :-------------------- | :-------------------- | :-------------------- | :------------------------------------ |
| **Gulosa**                    | Iterativa             | ❌ Não                 | O(n log n)            | Rápida, mas falha em certos casos     |
| **Recursiva Pura**            | Recursiva             | ✅ Sim                 | O(n^M)                | Muito lenta para grandes M            |
| **Recursiva + Memoização**    | Recursiva (Top Down)  | ✅ Sim                 | O(M × n)              | Boa performance e fácil implementação |
| **Programação Dinâmica (PD)** | Iterativa (Bottom Up) | ✅ Sim                 | O(M × n)              | Melhor desempenho geral               |

---

## 🧪 Demonstração de Testes

```python
qtdeMoedas(6, [1,3,4])          # → 3 (falha)
qtdeMoedasRec(6, [1,3,4])       # → 2
qtdeMoedasRecMemo(6, [1,3,4])   # → 2
qtdeMoedasPD(6, [1,3,4])        # → 2
```

---

## 🧾 Conclusão

A **Programação Dinâmica (Bottom-Up)** se destaca como a **melhor abordagem** para resolver o Problema da Troca de Moedas.
Ela oferece o **equilíbrio ideal entre desempenho e precisão**, evitando recalcular subproblemas e garantindo sempre a **solução ótima**.

A evolução entre as quatro abordagens demonstra de forma clara o avanço da eficiência:

> Estratégia Gulosa (Iterativa) → Recursiva Pura → Memoização (Top Down) → PD (Bottom Up)

A **Programação Dinâmica** é uma das ferramentas mais importantes da Ciência da Computação moderna, especialmente em **problemas de otimização** onde há **subestrutura ótima e subproblemas sobrepostos**.

---

🧠 **Resumo Final:**

> A PD transforma problemas exponenciais em soluções polinomiais, sendo um dos pilares da otimização algorítmica e da eficiência computacional.

