# Dada una lista de enteros y un numero p,
# retornar la lista con cada una de sus elementos elevados a la potencia p.
 
import random
 
def potenciaLista(lista, p):
    return [n ** p for n in lista]
 
def imprimirLista(lista,nombre):
    for i in range(0,len(lista)):
        print nombre + "[" + str(i) + "]=" + str(lista[i])
 
def leerLista():
    lista=[]
    i=0
    while i < 5:
        lista.append(int(random.randint(0, 10)))
        i=i+1
    return lista
 
A=leerLista()
imprimirLista(A,"A")
cn=int(raw_input("Ingresa Exponente: "))
B=potenciaLista(A,cn)
imprimirLista(B,"B")