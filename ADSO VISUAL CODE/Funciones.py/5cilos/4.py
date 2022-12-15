#Determinar los divisores de un numero introducido por teclado

def run():
    n = int(input("Ingrese un numero. "))

    for i in range(1,n+1):
        if n % i == 0:
            return i
print(run())