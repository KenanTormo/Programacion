Numero = 8

print("Hola, intenta adivinar el numero en el que estoy pensando")

Intento_adivinar = input()
Intento_adivinar_traducido = int(Intento_adivinar)

if Intento_adivinar_traducido == Numero:
	print("Muy bien, lo has logrado")

if Intento_adivinar_traducido > Numero:
	print("Te has pasado, el numero es mas pequeño")
	
if Intento_adivinar_traducido < Numero:
	print("Te has quedado corto, el numero es mas grande")
	
print("Intentalo de nuevo, quiza en esta ocasion lo logres")

Intento_adivinar2 = input()
Intento_adivinar_traducido2 = int(Intento_adivinar2)

if Intento_adivinar_traducido2 == Numero:
	print("Muy bien, lo has logrado")


if Intento_adivinar_traducido2 > Numero and Intento_adivinar_traducido2 < Intento_adivinar_traducido:
	print("Te has pasado, el numero es mas pequeño")

elif Intento_adivinar_traducido2 > Numero and Intento_adivinar_traducido2 > Intento_adivinar_traducido:
	print("Se indicó que el número secreto era menor y usted introdujo un número mayor que la primera vez!!")
	
if Intento_adivinar_traducido2 < Numero and Intento_adivinar_traducido2 > Intento_adivinar_traducido:
	print("Te has quedado corto, el numero es mas grande")

elif Intento_adivinar_traducido2 < Numero and Intento_adivinar_traducido2 < Intento_adivinar_traducido:
	print("Se indicó que el número secreto era mayor y usted introdujo un número menor que la primera vez!!")
	
