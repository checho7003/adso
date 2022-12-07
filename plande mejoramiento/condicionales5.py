"""Determinar cuánto es el desceunto, si la cantidad de lapices son 50 o más, 
existe un descuento de 7%, teniendo en cuenta que el costo por lápiz es de 500 ; de lo 
contrario no hay descuento."""

lapices = 50
descuento = 0.7
precio = 500
concha = int(input("¿cuantos lapices quiere?"))
if concha >= lapices:
    oper = int(concha * precio )
    oper1 = oper * descuento
    oper2= oper - oper1
    print("este es el desceunto de su compra:",oper2 )
else:
    print("No tiene desceunento ")
