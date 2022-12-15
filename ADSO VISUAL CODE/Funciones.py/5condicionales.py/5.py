# Pedir una nota de 0 a 10 y mostrarla de la forma: Insuficiente, Suficiente, Bien, 
# etc. Use la escala que prefiera, pero cerci�rese que tiene 5 valores.

def run(n):
    if n < 0:
        print("Nota inv�lida") 
    elif n < 3:
        print("Muy mal") # De 0 a 2 es muy mal.
    elif n < 5:
        print("Mal") # De 2 a 4 es mal.
    elif n < 7:
        print("Regular") # De 4 a 6 es regular.
    elif n < 9:
        print("Bien") # De 6 a 8 es bien.
    elif n < 11:
        print("Excelente") # De 8 a 10 es excelente.
    else: 
        print("Nota inv�lida")

nota = int(input("Digite la nota de 0 a 10 para saber como le fue: "))
print(run(nota))