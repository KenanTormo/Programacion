import random
Tiempo_Bucle = 0
Puntuacion = 0
Puntuacion_rival = 0

print("Hola, juguemos a piedra, papel o tijeras.")

print("Para jugar, debes escribir en la consola Piedra, Papel o Tijeras")

while Puntuacion < 3 and Puntuacion_rival < 3:
	print(Puntuacion, "-", Puntuacion_rival)
	Tiempo_Bucle = 0
	while Tiempo_Bucle == 0:
		Numero = random.randint(1, 3)
		Intento_adivinar = input()

		if Intento_adivinar == "Piedra" and Numero == 1:
			print("He sacado piedra, vaya, hemos empatado")
			Tiempo_Bucle = 1
			
		if Intento_adivinar == "Piedra" and Numero == 2:
			print("He sacado papel, perdiste, gano yo!")
			Tiempo_Bucle = 1
			Puntuacion_rival += 1
		if Intento_adivinar == "Piedra" and Numero == 3:
			print("He sacado tijeras, perdi... ganas tu!")
			Tiempo_Bucle = 1
			Puntuacion += 1
		if Intento_adivinar == "Papel" and Numero == 1:
			print("He sacado piedra, perdi... ganas tu!")
			Tiempo_Bucle = 1
			Puntuacion += 1
		if Intento_adivinar == "Papel" and Numero == 2:
			print("He sacado papel, vaya, hemos empatado")
			Tiempo_Bucle = 1
			
		if Intento_adivinar == "Papel" and Numero == 3:
			print("He sacado tijeras, perdiste, gano yo!")
			Tiempo_Bucle = 1
			Puntuacion_rival += 1
		if Intento_adivinar == "Tijeras" and Numero == 1:
			print("He sacado piedra, perdiste, gano yo!")
			Tiempo_Bucle = 1
			Puntuacion_rival += 1
		if Intento_adivinar == "Tijeras" and Numero == 2:
			print("He sacado papel, perdi... ganas tu!")
			Tiempo_Bucle = 1
			Puntuacion += 1
		if Intento_adivinar == "Tijeras" and Numero == 3:
			print("He sacado tijeras, vaya, hemos empatado")
			Tiempo_Bucle = 1
			
print("Puntuación final:", Puntuacion, "-", Puntuacion_rival)
	
