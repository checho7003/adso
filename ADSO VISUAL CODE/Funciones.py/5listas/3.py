#Llenar una lista de tama�o aleatorio entre 10 y 25 elementos. Llene la lista con n�meros 
#aleatorios. Sume los pares y saque el promedio de los impares

import random

'''tama�o = random.randint(10,25)
lista = []
for i in range(tama�o):
    lista.insert(i,round(random.random()*100))
print("Lista: ",lista)'''

lista = [round(random.random()*100) for i in range(random.randint(10,25))] #C�digo m�s corto - eficiente
print('Lista:',lista)

def run():
    sumapar = 0
    pares = []
    impares = []
    sumaimpar = 0

    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            pares.append(lista[i])
            sumapar += lista[i] 
        else:
            impares.append(lista[i])
            sumaimpar += lista[i]
    print("Pares: ",pares,"\nSuma de los pares = ",sumapar)
    print("Impares: ",impares,"\nPromedio de los impares = ",sumaimpar // len(impares))
run()