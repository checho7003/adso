""" La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no,
y en función de su respuesta le muestre un menú con los ingredientes disponibles 
para que elija.
Solo se puede eligir un ingrediente además de la mozzarella y el 
tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la 
pizza elegida es vegetariana o no y todos los ingredientes que lleva. """

print("bienvenidos a Bella Napoli. ¿que tipo de pizza desea pedir?")
menu1 = int(input("1 pizza vegetariana o 2 pizza de la casa: "))
if menu1 == 1:
    print("estos son ingredeinetes que puedes ponerle a tu pizza: \n\t1 tofu\n\t2 pimiento\n")
    ingredientes = input("agrega el ingredeinte que deseas: ")
    print("Tu pizza sera de: mozarrella, tomate y ", end= ".")
    if ingredientes == 1:
        print("tofu")
    else:
        print("pimiento")
else:
    print("estos son los igredientes que puedes ponerle a tu pizza: \n\t1 peperoni\n\t2 salmon\n\t3 jamon\n ")
    ingredientes2 = input("agrega el ingredeinte que deseas: ")
    print("Tu pizza se ra de: mozarrella, tomate y. ", end= ".")
    if ingredientes2 == 1:
        print("peperoni")
    elif ingredientes2 == 2:
        print("salmon")
    else:
        print("jamon")