#Llenar una lista de tama�o aleatorio entre 10 y 25 elementos. Llene la lista con n�meros 
#aleatorios. Solicite al usuario un n�mero para buscar en la lista. Diga cuantas veces est� y en que 
#posiciones esta. Si no esta agreguelo al final de la lista.

import random

'''tama�o = random.randint(10,25)
lista = []
for i in range(tama�o):
    lista.insert(i,round(random.random()*100))
print("Lista: ",lista)'''

lista = [round(random.random()*100) for i in range(random.randint(10,25))] #C�digo m�s corto - eficiente
print('Lista:',lista)

numero = int(input("Ingrese un n�mero para buscar en la lista: "))

veces = 0
posiciones = []

for i in range(len(lista)):
    if numero == lista[i]:
        veces += 1
        posiciones.append(i)
if veces > 0:
    print("El n�mero ingresado est�",veces,"veces.","\nLas posiciones del n�mero son: ",posiciones)
else:
    print("El n�mero no est� en la lista, as� que fue agregado.")
    lista.append(numero)
    print("Lista: ",lista)