# módulo bisect mantém uma lista ordenada sem ter que reordenar a lista após cada inserção

import bisect

def pesquisa_recursiva(A, item):
    """Implementa pesquisa binária usando bisect."""

    # Encontra o ponto onde o item deveria ser (ou está) inserido.
    i = bisect.bisect_left(lista, item)

    # Testa se o item está na lista.
    return i if i < len(lista) and lista[i] == item else -1
        
lista = [1, 7, 18, 23, 50, 99, 101, 200, 1000, 9999]

print("Pesquisa com sucesso:", pesquisa_recursiva(lista, 1))
print("Pesquisa com sucesso:", pesquisa_recursiva(lista, 7))
print("Pesquisa com sucesso:", pesquisa_recursiva(lista, 99))
print("Pesquisa com falha:", pesquisa_recursiva(lista, 100))





  
            
