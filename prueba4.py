# Retornar la union de a y b.
 
import random
 
def unirLista(lista_a, lista_b):
 
    lista_a.sort(cmp=None, key=None, reverse=False)
    lista_b.sort(cmp=None, key=None, reverse=False)
    lista_nueva=[]
    for i in lista_a:
        if i not in lista_nueva:
            lista_nueva.append(i)
 
    for i in lista_b:
        if i not in lista_nueva:
            lista_nueva.append(i)
 
    return lista_nueva
 
def imprimirLista(lista,nombre):
    for i in range(0,len(lista)):
        print nombre+"[" + str(i) + "]=" + str(lista[i])
 
def leerLista():
    lista=[]
 
    i=0
    while i < 5:
        lista.append(int(random.randint(0, 10)))
        i=i+1
    return lista
 
A=leerLista()
B=leerLista()
C=unirLista(A, B)
imprimirLista(A,"A")
imprimirLista(B,"B")
imprimirLista(C,"C")