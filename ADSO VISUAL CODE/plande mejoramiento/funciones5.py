""" pedir un numero e imprimir su correspondiente factorial"""
def run():
    num1=int(input("ponga el numero que desee:\n"))
    num= 1
    oper = 1
    while num <= num1:
        oper = oper * num
        num += 1
    return "este es el numero..",oper
print(run())