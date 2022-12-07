"""Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
y muestre por pantalla el número de veces que aparece la letra en la frase. """

frase = input("dime una frase: ")
letra = input("Dame una letra: ")
num = 0
for l in frase:
    if l == letra:
        num+=1
print("la letra ", str(letra),  " aparece ", int(num),  " veces en la frase: ", str(frase))