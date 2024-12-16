def MFKnapsack(n, W, Weights, Values):
    # Criando a tabela F com n+1 linhas (uma p/ cada item + caso inicial) e W+1 (uma p/ cada capacidade de 0 até W) colunas, inicializando todos os valores com -1
    F = [[-1]*(W+1) for _ in range(n+1)]

    # Casos base, inicializando primeira linha e primeira coluna com zero 
    for i in range(n + 1): 
        F[i][0] = 0  # Linha 0: Capacidade 0 -> valor 0
    for j in range(W + 1):
        F[0][j] = 0  # Coluna 0: Nenhum item -> valor 0

    # Função auxiliar (recursiva) para preencher a tabela
    def helper(i, j):
        # Caso base: se não há itens ou a capacidade é zero
        if i == 0 or j == 0:
            return 0

        # Se o valor já foi calculado anteriormente, retorna o valor armazenado
        if F[i][j] != -1:
            return F[i][j]

        # Se o peso do item atual é maior que a capacidade restante da mochila, não pode incluir o item
        if Weights[i-1] > j:
            F[i][j] = helper(i-1, j)  # Apenas considera os itens anteriores
        else:
            # Calcula o valor máximo considerando duas opções:
            # 1. Não incluir o item atual
            # 2. Incluir o item atual e somar seu valor
            F[i][j] = max(
                helper(i-1, j),  # Não inclui o item atual
                Values[i-1] + helper(i-1, j-Weights[i-1])  # Inclui o item atual
            )
        
        return F[i][j]

    # Chama a função auxiliar para resolver o problema
    return helper(n, W)


# Exemplo 1 de teste
n1 = 4  # Número de itens
W1 = 7  # Capacidade da mochila
Weights1 = [1, 3, 4, 5]  # Pesos dos itens
Values1 = [1, 4, 5, 7]   # Valores dos itens

resultado1 = MFKnapsack(n1, W1, Weights1, Values1)
print("Exemplo 1 - Valor ótimo da mochila:", resultado1)

# Exemplo 2 de teste
n2 = 3  # Número de itens
W2 = 5  # Capacidade da mochila
Weights2 = [2, 2, 3]  # Pesos dos itens
Values2 = [3, 4, 5]   # Valores dos itens

resultado2 = MFKnapsack(n2, W2, Weights2, Values2)
print("Exemplo 2 - Valor ótimo da mochila:", resultado2)

# Exemplo 3 de teste
n3 = 5  # Número de itens
W3 = 10  # Capacidade da mochila
Weights3 = [2, 3, 4, 5, 6]  # Pesos dos itens
Values3 = [3, 4, 5, 8, 9]   # Valores dos itens

resultado3 = MFKnapsack(n3, W3, Weights3, Values3)
print("Exemplo 3 - Valor ótimo da mochila:", resultado3)
