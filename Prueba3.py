# Eliminar la primera ocurrencia de value en la lista.
 
import random
 
def eliminarElemento(lista, value):
    lista.remove(value)
 
def imprimirLista(lista,nombre):
    for i in range(0,len(lista)):
        print nombre + "[" + str(i) + "]=" + str(lista[i])
 
def leerLista():
    lista=[]
 
    i=0
    while i < 10:
        lista.append(int(random.randint(0, 10)))
        i=i+1
    return lista
 
A=leerLista()
imprimirLista(A,"A")
cn=int(raw_input("Valor a liminar: "))
eliminarElemento(A,cn)
imprimirLista(A,"A")