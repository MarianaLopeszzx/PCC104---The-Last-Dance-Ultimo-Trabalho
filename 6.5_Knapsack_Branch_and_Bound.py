#Classe para organizar informações da árvore de decisão
class Node:
    def __init__(self, level, profit, weight, bound):
        self.level = level  # Nível na árvore (índice do item considerado)
        self.profit = profit  # Lucro total acumulado até este nó
        self.weight = weight  # Peso total acumulado até este nó
        self.bound = bound  # Limite superior estimado que pode ser obtido a partir deste nó

#Função para calcular o limite superior de um nó
def calculate_bound(node, n, W, items):
    if node.weight >= W: #Se o peso acumulado (node.weight) excede a capacidade W, o limite é 0
        return 0 

    bound = node.profit #Inicializa 'bound' como o lucro atual
    total_weight = node.weight #Inicializa 'total_weight' com o peso acumulado até o momento
    j = node.level + 1 #Determina o próximo item a ser considerado

    # Adicionar itens enquanto houver capacidade
    while j < n and total_weight + items[j][1] <= W: 
        total_weight += items[j][1] #Adiciona o peso do item j ao peso total acumulado
        bound += items[j][0] #Adiciona o valor do item j ao limite superior de lucro
        j += 1 #Incrementa o índice j para passar ao próximo item na lista.

    if j < n: #Se ainda há itens a serem considerados
        bound += (W - total_weight) * (items[j][0] / items[j][1]) #Calcula o limite

    return bound #retorna o limite

def knapsack_branch_and_bound(values, weights, W):
    n = len(values)
  
    #Criando lista resultante contendo os pares (valor,peso); 
    #Pegando cada par e calculando a razão;
    #Função sorted ordena os pares de acordo com a razão valor/peso, ficando os com maior razão primeiro
    items = sorted(zip(values, weights), key=lambda x: x[0] / x[1], reverse=True) 

    # Lista para armazenar nós (substituindo a fila de prioridade)
    nodes = []

    # Criar o nó raiz
    root = Node(level=-1, profit=0, weight=0, bound=0)
    root.bound = calculate_bound(root, n, W, items)
    nodes.append(root)

    max_profit = 0

    while nodes:
        # Selecionar o nó com maior bound manualmente
        nodes.sort(key=lambda x: x.bound, reverse=True)
        current = nodes.pop(0)  # Remover o nó com maior bound

        if current.bound > max_profit:  # Apenas explorar se promissor
            # Próximo nível (próximo item)
            level = current.level + 1

            # **Incluir o item atual**
            if level < n:
                profit_incl = current.profit + items[level][0]
                weight_incl = current.weight + items[level][1]

                if weight_incl <= W and profit_incl > max_profit:
                    max_profit = profit_incl

                bound_incl = calculate_bound(Node(level, profit_incl, weight_incl, 0), n, W, items)
                if bound_incl > max_profit:
                    nodes.append(Node(level, profit_incl, weight_incl, bound_incl))

            # **Excluir o item atual**
            profit_excl = current.profit
            weight_excl = current.weight

            bound_excl = calculate_bound(Node(level, profit_excl, weight_excl, 0), n, W, items)
            if bound_excl > max_profit:
                nodes.append(Node(level, profit_excl, weight_excl, bound_excl))

    return max_profit

# Exemplo de uso
values = [40, 42, 25, 12]  # Valores dos itens
weights = [4, 7, 5, 3]  # Pesos dos itens
capacity = 10  # Capacidade da mochila

result = knapsack_branch_and_bound(values, weights, capacity)
print("Máximo valor que pode ser obtido:", result)
