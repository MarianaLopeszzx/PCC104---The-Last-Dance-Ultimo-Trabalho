#Conjunto 3 - Algoritmos Gulosos - Algoritmo de Primm

def prim(graph):
    # Número de vértices no grafo
    num_vertices = len(graph)
    
    # Inicialização
    in_tree = [False] * num_vertices  # Marca se o vértice já está na árvore geradora
    in_tree[0] = True  # Começamos com o vértice 0 na árvore
    edges = []  # Lista para armazenar as arestas da árvore geradora mínima
    total_weight = 0  # Peso total da árvore geradora mínima
    
    # Enquanto nem todos os vértices estiverem na árvore
    while len(edges) < num_vertices - 1:
        min_edge = None  # Armazena a aresta de menor peso
        min_weight = float('inf')  # Inicializa o peso mínimo com infinito
        
        # Percorre todos os vértices para achar a aresta de menor peso
        for u in range(num_vertices):  # Para cada vértice `u`
            if in_tree[u]:  # Se o vértice `u` já está na árvore geradora
                for v in range(num_vertices):  # Verifica os vértices adjacentes `v`
                    weight = graph[u][v]  # Peso da aresta de `u` para `v`
                    if not in_tree[v] and weight < min_weight and weight > 0:
                        min_edge = (u, v)  # Aresta de menor peso encontrada
                        min_weight = weight  # Atualiza o peso mínimo
        
        # Adiciona a aresta de menor peso à árvore
        u, v = min_edge
        edges.append(min_edge)  # Adiciona a aresta à lista de arestas
        total_weight += min_weight  # Atualiza o peso total
        in_tree[v] = True  # Marca o vértice como incluído na árvore
    
    return edges, total_weight


# Exemplo 1 (grafo com 6 vértices):
graph1 = [
    [0, 1, 4, 0, 0, 0],
    [1, 0, 2, 6, 0, 0],
    [4, 2, 0, 3, 5, 0],
    [0, 6, 3, 0, 4, 2],
    [0, 0, 5, 4, 0, 7],
    [0, 0, 0, 2, 7, 0]
]

edges1, total_weight1 = prim(graph1)
print("Arestas da árvore geradora mínima:", edges1)
print("Peso total da árvore:", total_weight1)

# Exemplo 2 (grafo com 5 vértices):
graph2 = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

edges2, total_weight2 = prim(graph2)
print("Arestas da árvore geradora mínima:", edges2)
print("Peso total da árvore:", total_weight2)

# Exemplo 3 (grafo com 4 vértices):
graph3 = [
    [0, 10, 0, 0],
    [10, 0, 5, 0],
    [0, 5, 0, 2],
    [0, 0, 2, 0]
]

edges3, total_weight3 = prim(graph3)
print("Arestas da árvore geradora mínima:", edges3)
print("Peso total da árvore:", total_weight3)
