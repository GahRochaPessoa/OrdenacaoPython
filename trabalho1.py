import random
import timeit
import sys

sys.setrecursionlimit(10000)


def bubbleSort(lista2):
    for x in range(len(lista2)-1, 0, -1):
        for i in range(x):
            if lista2[i] > lista2[i+1]:
                aux = lista2[i]
                lista2[i] = lista2[i+1]
                lista2[i+1] = aux
    return lista2


def quickSort(lista1, iniVet, fimVet):
    i = iniVet
    j = fimVet
    pivo = lista1[fimVet]

    while i <= j:
        while lista1[i] < pivo:
            i += 1
        while lista1[j] > pivo:
            j -= 1
        if i <= j:
            aux = lista1[i]
            lista1[i] = lista1[j]
            lista1[j] = aux
            i += 1
            j -= 1
    if iniVet < j:
        quickSort(lista1, iniVet, j)
    if i < fimVet:
        quickSort(lista1, i, fimVet)
    return lista1


lista = []
for i in range(10000):
    lista.append(random.randint(1, 100000))
lista1 = []
lista2 = []
menu = int(input('Digite um numero para as operações no menu\n'
                 '1-Ordenar com QuickSort\n'
                 '2-Ordenar com BubbleSort\n'
                 '3-Sair\n'))
while menu != 3:
    if menu == 1:
        lista1 = lista
        fim = len(lista1) - 1
        inicio = timeit.default_timer()
        quickSort(lista1, 0, fim)
        final = timeit.default_timer()
        print('\nA lista desOrdenada é:'+str(lista)+'\n')
        print('\nA lista Ordenada é:'+str(lista1)+'\n')
        print('Duração: %f' % (final-inicio))

    elif menu == 2:
        lista2 = lista
        inicio = timeit.default_timer()
        bubbleSort(lista2)
        final = timeit.default_timer()
        print('\nA lista Ordenada é:'+str(lista2)+'\n')
        print('Duração: %f' % (final-inicio))

    menu = int(input('Digite um numero para as operações no menu\n'
                     '1-Ordenar com QuickSort\n'
                     '2-Ordenar com BubbleSort\n'
                     '3-Sair\n'))
