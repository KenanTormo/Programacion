Numero = 8
Tiempo_Bucle = 0
Intentos = 0

print("Hola, intenta adivinar el numero en el que estoy pensando")

while Tiempo_Bucle == 0 and Intentos < 5:
	Intento_adivinar = input()
	Intento_adivinar_traducido = int(Intento_adivinar)

	if Intento_adivinar_traducido == Numero:
		print("Muy bien, lo has logrado")
		Tiempo_Bucle = 1
		Intentos += 1
		print("Numero de intentos restantes: ", 5 - Intentos)
	if Intento_adivinar_traducido > Numero:
		print("Te has pasado, el numero es mas pequeño")
		Intentos += 1
		print("Numero de intentos restantes: ", 5 - Intentos)
	if Intento_adivinar_traducido < Numero:
		print("Te has quedado corto, el numero es mas grande")
		Intentos += 1
		print("Numero de intentos restantes: ", 5 - Intentos)
