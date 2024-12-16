def backtrack(nums, target, start, subset, current_sum):
    #nums: lista ordenada de números para gerar subconjuntos
    #target: A soma alvo
    #start: indice atual em 'nums'
    #subset: subconjunto atual de números
    #current_sum: soma dos elementos no subconjunto atual

    # Se a soma atual for igual ao alvo, encontramos uma solução e imprimimos o subconjunto
    if current_sum == target:
        print("Solução encontrada:", subset)
        return
    #Se a soma exceder o alvo, esse caminho é interrompido
    if current_sum > target:
        return

    # Explorando as opções
    for i in range(start, len(nums)):
        subset.append(nums[i])  # Adicionamos o elemento nums[i] ao subconjunto atual 
        backtrack(nums, target, i + 1, subset, current_sum + nums[i])  # Chamamos a função recursivamente passando
                                                                       # para o próximo item e somando o valor do elem atual
        subset.pop()  # Remove-se o ultimo elemento do subconjunto para desfazer a escolha

def subset_sum(nums, target):
    # Preparar os dados e chamar o backtracking
    nums.sort() # Organiza o conjunto em ordem crescente
    backtrack(nums, target, 0, [], 0) #Chamada inicial

    #start = 0: Começamos a explorar a lista desde o primeiro elemento.
    #subset = []: O subconjunto atual está vazio no início.
    #current_sum = 0: A soma do subconjunto atual é inicialmente zero.

# Exemplo 1
nums1 = [3, 5, 6, 7]
target1 = 15
print(f"Exemplo 1, soma {target1}")
subset_sum(nums1, target1)

# Exemplo 2 
nums2 = [1, 2, 3, 4, 5]
target2 = 6
print(f"Exemplo 2, soma {target2}")
subset_sum(nums2, target2)

# Exemplo 3 
nums3 = [2, 4, 6, 10]
target3 = 16
print(f"Exemplo 3, soma {target3}")
subset_sum(nums3, target3)
