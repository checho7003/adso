# Escribe un programa que pida tres n�meros y que escriba si son los tres 
# iguales, si hay dos iguales o si son los tres distintos.

def iguales(a,b,c):
    if a == b == c:
        print("hay tres n�meros iguales")
    elif a == b or a == c or b == c:
        print("Hay dos n�meros iguales")
    else:
        print("Los tres n�meros son distintos")
    
num1 = int(input("Digite el primer n�mero: "))
num2 = int(input("Digite el segundo n�mero: "))
num3 = int(input("Digite el tercer n�mero: "))

iguales(num1,num2,num3)