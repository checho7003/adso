# Cree un programa que calcule el �rea, longitud, di�metro y circunferencia de un c�rculo.

radio = float(input("Escriba el Radio del c�rculo: "))
area = 3.14 * radio ** 2 # a = pi * r**2
longitud = 2 * 3.14 * radio # l = 2*pi*r
diametro = 2 * radio # d = 2*r
circunferencia = diametro * 3.14 # c = d*pi
print("El �rea del c�rculo es: ", area)
print("La longitud del c�rculo es: ", round(longitud,1))
print("El di�metro del c�rculo es: ", diametro)
print("La circunferencia del c�rculo es: ", round(circunferencia))


