#Pedir un n?mero entre 0 y 9.999 y decir cuantas cifras tiene. Cuando el n?mero 
#exceda los l?mites emita un mensaje y finalice el programa.

def cifras(n):
    if n < 0 or n > 9999:
        print("El n?mero est? por fuera de los par?metros")
    else:
        print("Su n?mero tiene",len(str(n)),"cifras.")
    
numero = int(input("Digite un n?mero entre 0 y 9.999: "))
cifras(numero)