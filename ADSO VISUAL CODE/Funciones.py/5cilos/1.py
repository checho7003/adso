#Calcular la operaci�n x^n sin utilizar la funci�n pow

def calcPotencia(n,p):
    elevado = n
    while p > 1:
        elevado *= n
        p -= 1
    return elevado

numero = int(input('Ingrese un n�mero: '))
potencia = int(input('Ingrese la potencia: '))

print(calcPotencia(numero,potencia))