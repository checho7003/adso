"""Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos 
iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad 
y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no."""

num1= int(input("¿que edad tienes?"))
num2=float(input("¿Cuales son sus ingresos?"))
if num1 > 16 and num2 >= 1000:
    print("puedes cotizar")
else:
    print("no podes cotizar")

