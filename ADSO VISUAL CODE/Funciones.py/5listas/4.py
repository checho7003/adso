#Llenar una lista de tama�o aleatorio entre 10 y 25 elementos. Llene la lista con n�meros 
#aleatorios. Muestre cuales y cuantos son primos

import random

'''tama�o = random.randint(10,25)
lista = []
for i in range(tama�o):
    lista.insert(i,round(random.random()*100))
print(lista," Tama�o: ",i + 1)'''

lista = [round(random.random()*100) for i in range(random.randint(10,25))] #C�digo m�s corto - eficiente
print(lista,' tama�o:', len(lista))
def run():
    primos = []

    for i in range(len(lista)):
        divisores = 0
        for j in range(1,101):
            if lista[i] % j == 0:
                divisores += 1
        if divisores == 2:
            primos.append(lista[i])
    print("Hay",len(primos),"numeros primos","\nSon los siguientes: ",primos)

run()