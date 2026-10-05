Nota1ev_input = input("Que has sacado en la primera evaluacion? ")
Nota2ev_input = input("Que has sacado en la segunda evaluacion? ")
Nota3ev_input = input("Que has sacado en la tercera evaluacion? ")
Nota1ev = int(Nota1ev_input)
Nota2ev = int(Nota2ev_input)
Nota3ev = int(Nota3ev_input)

Media = ( Nota1ev + Nota2ev + Nota3ev ) / 3
print("Tu media es: ", Media)
evaluacion_continua = input("Tienes evaluacion continua? si/no ")


if Media >= 9.5:
	print("No necesitas presentarte a nada, felicidades!")
if Nota2ev >= 9 and Nota3ev >= 9 and evaluacion_continua == "si":
	print("No necesitas presentarte a nada, felicidades!")
