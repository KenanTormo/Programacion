Año = 2026
Año_Nacimiento_input = input("Cuando nacio el cliente? ")
Año_Nacimiento = int(Año_Nacimiento_input)
Edad = Año - Año_Nacimiento
Edad_Minima = 18
Edad_Permiso = 14

if Edad >= Edad_Minima:
	print("Puede pasar")
	
if Edad >= Edad_Permiso and Edad < Edad_Minima:
	print("Tiene permiso de sus padres? si/no")
	Permiso_Padres = input()
	if Permiso_Padres == "si":
		print("Puede pasar")
	elif Permiso_Padres == "no":
		print("No puede pasar")
		print("Motivo: El cliente es menor de edad")
if Edad < Edad_Permiso:
	print("Tiene permiso de sus padres? si/no")
	Permiso_Padres = input()
	print("No puede pasar bajo ningun concepto")
	print("Motivo: El cliente es menor de edad")

