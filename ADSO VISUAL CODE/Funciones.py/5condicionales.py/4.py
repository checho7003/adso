# Cree un programa que calcule el �rea, longitud, di�metro y circunferencia de un c�rculo.

def calcTriangulo(r):
    area = 3.14 * radio ** 2 # a = pi * r**2
    longitud = 2 * 3.14 * radio # l = 2*pi*r
    diametro = 2 * radio # d = 2*r
    circunferencia = diametro * 3.14 # c = d*pi
    return area,longitud,diametro,circunferencia

radio = float(input("Escriba el Radio del c�rculo: "))
print(calcTriangulo(radio))