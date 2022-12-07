"""Escribir un programa que pida al usuario una palabra y muestre por pantalla el 
número de veces que contiene cada vocal."""

palabra= input("Introduce una palabra: ")
vocales = ['a', 'e', 'i', 'o', 'u']
for i in vocales: 
    num = 0
    for j in palabra: 
        if j == i:
            num += 1
    print("La vocal " + str(i) + " aparece " + str(num) + " veces")