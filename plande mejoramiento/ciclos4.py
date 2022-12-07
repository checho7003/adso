""" Escribir un programa que pida al usuario una palabra y luego muestre 
por pantalla una a una las letras de la palabra introducida empezando por la última. """

palabra = input("escriba una palabra: ")
for hl in range(len(palabra)-1, -1, -1):
    print(palabra[hl])