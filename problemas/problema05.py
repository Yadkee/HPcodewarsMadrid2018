#! python3
"""[5] El Villarato - 6 Puntos:
  Se recibirán los resultados de 3 partidos y la suma de puntos
   a favor y en contra.
  Se deberá determinar si la suma es correcta y sino devolver la diferencia."""

inp = input().split(" ")
marcadores = [[int(j) for j in i.split("-")] for i in inp[:3]]
balance = (int(inp[3]), int(inp[4]))
diferencias = tuple(balance[j] - sum(i[j] for i in marcadores) for j in (0, 1))

if diferencias[0] == diferencias[1] == 0:
    print("Puntuación Correcta")
elif diferencias[0] == 0:
    print("Este equipo ha sido hackeado: PC: %+d" % diferencias[1])
elif diferencias[0] == 0:
    print("Este equipo ha sido hackeado: PF: %+d" % diferencias[0])
else:
    print("Este equipo ha sido hackeado: PF: %+d PC: %+d" % diferencias)
