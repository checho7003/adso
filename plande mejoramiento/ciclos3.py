""" pedir un numero e imprimir su correspondiente factorial"""

num1=int(input("ponga el numero que desee:\n"))
num= 1
oper = 1
while num <= num1:
    oper = oper * num
    num += 1
print("este es el numero..",oper)
