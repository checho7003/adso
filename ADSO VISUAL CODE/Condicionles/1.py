#Escriba un programa que resuelva la f�rmula cuadr�tica, dados 3 n�meros.
#a*x**2+b*x+c=0
#F�RMULA G: x = -b +- ra�z b** - 4*a*c / 2*a

import math

a = int(input("Digite el primer valor"))
b = int(input("Digite el segundo valor"))
c = int(input("Digite el tercer valor"))

if ((b**2) - 4 * a * c) < 0:
    ("No se puede solucionar") # El resultado debe ser mayor a 0
else:
    x1=(-b+math.sqrt(b**2-(4*a*c)))/(2*a) 
    x2=(-b-math.sqrt(b**2-(4*a*c)))/(2*a)
                                            # Las veces que pasa la grafica por el eje x
print(x1)
print(x2)