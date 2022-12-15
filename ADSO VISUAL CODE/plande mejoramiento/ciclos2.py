"""Escribir un programa que muestre el eco de todo lo que el usuario introduzca 
hasta que el usuario escriba “salir” que terminará.."""

while True:
    palabra = input("digite un texto: ")
    if palabra == "salir":
        break
    print(palabra)