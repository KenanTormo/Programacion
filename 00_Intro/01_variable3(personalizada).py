print("En que año naciste?")
Edad_actual = input()
Edad = int(Edad_actual)

print("En que años estamos?")
Año_actual = input()
Año = int(Año_actual)

Edad_final = Año - Edad
print("Tienes o cumpliras: ", Edad_final, " años")

if Edad_final >= 18: print("Eres mayor de edad")

else: print("Aun eres menor de edad")

if Edad_final <= 3:
	print("Aun no has comenzado la escuela")
	
elif Edad_final >= 12 and Edad_final <= 15:
	print("Estas en la ESO")
	
elif Edad_final == 16:
	print("Has acabado, o vas a acabar la ESO")
	
elif Edad_final > 16:
	print("Has acabado la ESO")

else:
	print("Estas en la escuela primaria")
