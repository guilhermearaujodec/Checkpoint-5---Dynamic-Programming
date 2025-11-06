# ==========================================================
# CHECKPOINT - Problema da Troca de Moedas
# ==========================================================

# Integrantes do Grupo:

# Nome: Augusto Mendonça                        RM: 558371
# Nome: Gabriel Vasquez Queiroz da Silva        RM: 557056    
# Nome: Guilherme Araujo de Carvalho            RM: 558926
# Nome: Gustavo Oliveira                        RM: 559163
# ==========================================================

def qtdeMoedas(M, moedas):
    """
    Determina a menor quantidade de moedas necessária para atingir o montante M
    usando a estratégia gulosa (iterativa).

    Parâmetros:
    - M (int): valor total a ser atingido.
    - moedas (list[int]): valores disponíveis das moedas.

    Retorno:
    - int: quantidade mínima de moedas (ou -1 se for impossível formar o montante).

    Complexidade:
    - O: O(n log n)  (ordenação das moedas)
    - Ω: Ω(n)
    - Θ: Θ(n log n)
    """
    moedas.sort(reverse=True)
    count = 0
    for moeda in moedas:
        if M >= moeda:
            count += M // moeda
            M = M % moeda
    return count if M == 0 else -1


# ==========================================================
def qtdeMoedasRec(M, moedas):
    """
    Resolve o problema da troca de moedas de forma recursiva pura (sem memoização).

    Parâmetros:
    - M (int): montante desejado.
    - moedas (list[int]): valores das moedas disponíveis.

    Retorno:
    - int: número mínimo de moedas ou -1 se impossível.

    Complexidade:
    - O: O(n^M) (exponencial)
    - Ω: Ω(1)
    - Θ: Θ(n^M)
    """
    if M == 0:
        return 0
    if M < 0:
        return float('inf')

    menor = float('inf')
    for moeda in moedas:
        qtd = qtdeMoedasRec(M - moeda, moedas)
        menor = min(menor, qtd + 1)

    return menor if menor != float('inf') else -1


# ==========================================================
def qtdeMoedasRecMemo(M, moedas, memo=None):
    """
    Resolve o problema da troca de moedas usando recursão com memoização (Top Down).

    Parâmetros:
    - M (int): montante desejado.
    - moedas (list[int]): valores das moedas disponíveis.
    - memo (dict): dicionário usado para armazenar subproblemas já resolvidos.

    Retorno:
    - int: número mínimo de moedas ou -1 se impossível.

    Complexidade:
    - O: O(M * n)
    - Ω: Ω(M)
    - Θ: Θ(M * n)
    """
    if memo is None:
        memo = {}

    if M in memo:
        return memo[M]
    if M == 0:
        return 0
    if M < 0:
        return float('inf')

    menor = float('inf')
    for moeda in moedas:
        qtd = qtdeMoedasRecMemo(M - moeda, moedas, memo)
        menor = min(menor, qtd + 1)

    memo[M] = menor
    return menor if menor != float('inf') else -1


# ==========================================================
def qtdeMoedasPD(M, moedas):
    """
    Resolve o problema da troca de moedas usando Programação Dinâmica (Bottom Up).

    Parâmetros:
    - M (int): montante desejado.
    - moedas (list[int]): valores das moedas disponíveis.

    Retorno:
    - int: número mínimo de moedas ou -1 se impossível.

    Complexidade:
    - O: O(M * n)
    - Ω: Ω(M)
    - Θ: Θ(M * n)
    """
    dp = [float('inf')] * (M + 1)
    dp[0] = 0  # zero moedas para zero montante

    for i in range(1, M + 1):
        for moeda in moedas:
            if i - moeda >= 0:
                dp[i] = min(dp[i], dp[i - moeda] + 1)

    return dp[M] if dp[M] != float('inf') else -1


# ==========================================================
# TESTES DE EXEMPLO
if __name__ == "__main__":
    moedas = [1, 3, 4]
    M = 6
    print("Gulosa:", qtdeMoedas(M, moedas))
    print("Recursiva:", qtdeMoedasRec(M, moedas))
    print("Memoização:", qtdeMoedasRecMemo(M, moedas))
    print("PD (Bottom-Up):", qtdeMoedasPD(M, moedas))