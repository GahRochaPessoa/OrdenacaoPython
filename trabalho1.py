import random
import timeit


def bubbleSort(lista):
    for x in range(len(lista)-1, 0, -1):
        for i in range(x):
            if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
    return lista


def quickSort(lista, iniVet, fimVet):
    i = iniVet
    j = fimVet
    pivo = lista[fimVet]

    while i <= j:
        while lista[i] < pivo:
            i += 1
        while lista[j] > pivo:
            j -= 1
        if i <= j:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux
            i += 1
            j -= 1
    if iniVet < j:
        quickSort(lista, iniVet, j)
    if i < fimVet:
        quickSort(lista, i, fimVet)
    return lista


lista = []
for i in range(10000):
    lista.append(random.randint(1, 100000))
menu = int(input('Digite um numero para as operações no menu\n'
                 '1-Ordenar com BubbleSort\n'
                 '2-Ordenar com QuickSort\n'
                 '3-Sair\n'))
while menu != 3:
    if menu == 1:
        inicio = timeit.default_timer()
        bubbleSort(lista)
        final = timeit.default_timer()
        print('\nA lista Ordenada é:'+str(lista)+'\n')
        print('Duração: %f' % (final-inicio))
    elif menu == 2:
        fim = len(lista) - 1
        inicio = timeit.default_timer()
        quickSort(lista, 0, fim)
        final = timeit.default_timer()
        print('\nA lista Ordenada é:'+str(lista)+'\n')
        print('Duração: %f' % (final-inicio))
    menu = int(input('Digite um numero para as operações no menu\n'
                     '1-Ordenar com BubbleSort\n'
                     '2-Ordenar com QuickSort\n'
                     '3-Sair\n'))
