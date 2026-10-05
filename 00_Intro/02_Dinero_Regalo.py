bucle = 10
vuelta = 0
dinero_total = 0


while vuelta < bucle:

	cantidad = int(input("Introduce la cantidad de dinero: "))
	dinero_total = dinero_total + cantidad
	print("Dinero total: ", dinero_total)
	
	vuelta += 1
	
