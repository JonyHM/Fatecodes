from time import perf_counter
from random import shuffle

vetorIndice = 2000
tempoTotal = 0

# Códigos retirados das explicações das aulas destas estruturas
def selecao(v):
  resp = []
  while v:
    m = min(v)
    resp.append(m)
    v.remove(m)
  return resp

def merge(e, d):
    r = []
    i, j = 0, 0
    while i < len(e) and j < len(d):
        if e[i] <= d[j]:
            r.append(e[i])
            i += 1
        else:
            r.append(d[j])
            j += 1
    r += e[i:]
    r += d[j:]
    return r

def mergesort(v):
    if len(v) <= 1:
        return v
    else:
        m = len(v) // 2
        e = mergesort(v[:m])
        d = mergesort(v[m:])
        return merge(e, d)

def quicksort(lista):
    if len(lista) <= 1: 
        return lista
    
    pivô = lista[0]
    iguais  = [x for x in lista if x == pivô]
    menores = [x for x in lista if x <  pivô]
    maiores = [x for x in lista if x >  pivô]
    return quicksort(menores) + \
           iguais + quicksort(maiores)

# Formatação da tabela
print('{:-^67}'.format("-"))
print('{:<}{:^65}{:>}'.format('|', 'Tempo de Execucao', '|'))
print('{:-^67}'.format("-"))
print('{:<}{:^8}{:<}{:^14}{:^14}{:^14}{:^14}{:>}'.format('|', 'Indice', '|', 'Selecao', 'MergeSort', 'QuickSort', 'Sort(Nativo)', '|'))
print('{:-^67}'.format("-"))

# "Main"
while tempoTotal < 30:
    tempoTotal = 0

    # Gerando o vetor, com índice variável, embaralhando
    #e copiando o vetor inicial
    vetorInicial = list(range(vetorIndice))
    shuffle(vetorInicial)
    copia = vetorInicial

    # O Código a seguir calcula o tempo de execução de
    #todos os métodos e depois os soma para uma variável de tempo total
    
    #SELEÇÃO
    inicio = perf_counter()
    selecao(copia)
    fim = perf_counter()
    selec = fim - inicio
        
    #MERGESORT
    inicio = perf_counter()
    mergesort(copia)
    fim = perf_counter()
    merg = fim - inicio
    
    #QUICKSORT
    inicio = perf_counter()
    quicksort(copia)
    fim = perf_counter()
    quick = fim - inicio
    
    #SORT
    inicio = perf_counter()
    copia.sort()
    fimo = perf_counter()
    sort = fimo - inicio
    
    tempoTotal = selec + merg + quick + sort

    print('{:<}{:^8}{:<}{:^14.8f}{:^14.8f}{:^14.8f}{:^14.8f}{:>}'.format('|', vetorIndice, '|', selec, merg, quick, sort, '|'))
   
    vetorIndice += 2000
    
print('{:-^67}'.format("-"))
