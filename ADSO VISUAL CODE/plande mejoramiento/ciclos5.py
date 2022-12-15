""" Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña 
hasta que introduzca la contraseña correcta."""

text = "hola, mundo"

contraseña =""

while contraseña != text:
    contraseña = input("Introduce la contraseña: ")
print("Contraseña correcta")