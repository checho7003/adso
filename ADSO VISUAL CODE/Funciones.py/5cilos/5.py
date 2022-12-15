#Determinar cuales son los multiplos de 5 comprendidos entre 1 y N. 


#multiplos = 0
def run():
    for i in range(1,numero + 1,1):
        if i % 5 == 0:
            print(i)
numero = int(input("Digite un n�mero: ")) # N�mero maximo N
run()
