print('hola mundo \n')

puntos = {'A':10.0,'B':8.0,'C':5.0}
numeroCursos = 0
totalPuntos = 0
fin = False

#
while not fin:
  nota = input('Ingrese una nota \n')
  if nota == '':
    fin = True
  elif nota not in puntos:
    print('Nota desconocida')
  else:
    numeroCursos += 1
    totalPuntos += puntos[nota]

if numeroCursos > 0:
  print('su promedio es {0}'.format(totalPuntos/numeroCursos))