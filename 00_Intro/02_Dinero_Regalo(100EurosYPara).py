bucle = 10
vuelta = 0
dinero_total = 0
dinero_necesario = int(input("Cuanto dinero se necesita? "))
dinero_necesario_resta = dinero_necesario


while vuelta < bucle:

	cantidad = int(input("Introduce la cantidad de dinero: "))
	dinero_total = dinero_total + cantidad
	dinero_necesario_resta = dinero_necesario - dinero_total
	print("Amigos restantes :", bucle - vuelta - 1)
	print("Dinero restante necesario: ", dinero_necesario - dinero_total)
	

	vuelta += 1
	if dinero_necesario_resta <= 0:
		vuelta = bucle 

