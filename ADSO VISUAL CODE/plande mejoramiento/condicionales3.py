"""Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y la edad. 
El grupo A esta formado por las mujeres con edad menor a 15 años y los hombres con una edad mayor a 15
y el grupo B por el resto. Escribir un programa que pregunte al usuario su edad y sexo, y muestre por pantalla el grupo que le corresponde. """

edad=int(input("que edad tiene?: "))
sexo=input("que tipo de sexo eres?: \n\t mujer\n\t hombre\n")
if edad <= 15 and sexo == "mujer":
    print("ustde pertenese al grupo: A")
elif edad >=15 and sexo == "hombre":
    print("usted pertenese al grupo A")
else:
    print("usted pertenese al grupo B")

