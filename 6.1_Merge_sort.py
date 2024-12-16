#Conjunto 1 - Dividir e Conquistar - Merge Sort

#Parte 1: Dividir
def merge_sort(A):
    if len(A) > 1:
        mid = len(A)//2 #Encontra o meio do array dividindo por 2

        #Divide o array em duas partes
        B = A[:mid] #Primeira metade do array em B
        C = A[mid:] #Segunda metade do array em C

        #Divide novamente cada metade do array
        merge_sort(B)
        merge_sort(C)

        #Combina e ordena as metades chamando a função merge
        merge(B, C, A)

#Parte 2: Conquistar (ordenar)
def merge(B, C, A):
    i, j, k = 0, 0, 0 #Definição dos ponteiros para os arrays B, C e A
    p, q = len(B), len(C)

    #Compara os elementos e adiciona o menor em A
    while i<p and j<q: #Enquanto ainda houver elementos em B e C
        if B[i] <= C[j]: #Se o elemento na posição i em B for menor que o elemento na posição j em C
            A[k] = B[i] #Insere B[i] em A
            i+=1 #Incrementa i, próxima posição de B
        else:
            A[k] = C[j]#Do contrário, insere C[j] em A
            j+=1 #Incrementa j, próxima posição de C
        k+=1 # Incrementa k para mover para a próxima posição de A

    #Se ainda restarem elementos em B e C, copiam eles para A
    while i < p: #Copia os elementos restantes de B (se existirem)
        A[k] = B[i]
        i+=1
        k+=1
    while j < q: #Copia os elementos restantes de C (se existirem)
        A[k] = C[j]
        j+=1
        k+=1

# Implementação dos 3 testes
A1 = [8, 3, 2, 9, 7, 1, 5, 4]  # Array 1 com números distintos e tamanho par
print(f"Primeiro array: {A1}")
merge_sort(A1)
print(f"Primeiro array ordenado: {A1}\n")

A2 = [2, 2, 3, 1, 2, 4]  # Array 2 com números repetidos e tamanho par
print(f"Segundo array: {A2}")
merge_sort(A2)
print(f"Segundo array ordenado: {A2}\n")

A3 = [5, 3, 8, 6, 2]  # Array 3 com tamanho ímpar
print(f"Terceiro array: {A3}")
merge_sort(A3)
print(f"Terceiro array ordenado: {A3}")