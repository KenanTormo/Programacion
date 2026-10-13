notas = [ 5, 3, 3, 5, 10, 9]
posicion = 0
maximo = notas[0]
for i in range(1, len(notas)):
    if notas[i] > maximo:
        maximo = notas[i]

minimo = notas[0]
for a in range(1, len(notas)):
    if notas[a] < minimo:
        minimo = notas[a]

print("La nota mas baja es:", minimo)
