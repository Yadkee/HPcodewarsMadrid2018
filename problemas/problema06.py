#! python3
"""[6] Los mejores del partido - 6 Puntos:
  Se recibirá la cantidad de jugadores que hay que valorar y luego cada una
   de las líneas con el nombre, los puntos y las asistencias de cada jugador.
  Se deberá calcular el máximo anotador y el máximo asistente del partido."""

nJugadores = int(input())
jugadores = [input().split(";") for _ in range(nJugadores)]

maxAnotador = ["", 0]
maxAsistente = ["", 0]
for jugador in jugadores:
    puntos = int(jugador[1])
    asistencias = int(jugador[2])
    if puntos > maxAnotador[1]:
        maxAnotador = [jugador[0], puntos]
    elif puntos == maxAnotador[1]:
        maxAnotador.extend((jugador[0], puntos))
    if asistencias > maxAsistente[1]:
        maxAsistente = [jugador[0], asistencias]
    elif asistencias == maxAsistente[1]:
        maxAsistente.extend((jugador[0], asistencias))

if len(maxAnotador) == 2:
    print("El máximo anotador es %s" % maxAnotador[0])
else:
    print("Los máximos anotadores son %s" % ";".join(maxAnotador[::2]))
if len(maxAsistente) == 2:
    print("El máximo asistente es %s" % maxAsistente[0])
else:
    print("Los máximos asistentes son %s" % ";".join(maxAsistente[::2]))
