#Llenar una lista de tama�o aleatorio entre 10 y 25 elementos. Llene la lista con n�meros 
#aleatorios. Encuentre la suma y el promedio de los n�meros de la lista

import random

'''tama�o = random.randint(10,25)
lista = []
for i in range(tama�o):
    lista.insert(i,round(random.random()*100))
print(lista," Tama�o: ",i + 1)'''

lista = [round(random.random()*100) for i in range(random.randint(10,25))] #C�digo m�s corto - eficiente
print(lista,' tama�o:', len(lista))

suma = 0
promedio = 0

for i in range(len(lista)):
    suma += lista[i]
    promedio = suma // len(lista)
print("La suma es: ",suma,"\nEl promedio es: ",promedio)