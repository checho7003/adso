#Llenar una lista de tama�o aleatorio entre 10 y 25 elementos. Llene la lista con n�meros 
#aleatorios. Solicite al usuario un n�mero para buscar en la lista. Diga cuantas veces est� y en que 
#posiciones esta. Si no est� agr�guelo al final de la lista.

import random

def ramdonlist(lis):
    lis = [round(random.random()*100) for i in range(random.randint(10,25))] #Comprensi�n
    print(lis,' tama�o:', len(lis))

lista = []
ramdonlist(lista)