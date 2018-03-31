#! python3
"""[10] La zona extraña - 16 Puntos:
Se recibirán una serie de coordenadas y las canastas que se han encestado
 desde ellas. Habrá que devolver los puntos totales."""


def puntos(coordenada):
    y, x, canastas = [int(i) for i in coordenada.split(":")]
    if x < 3:
        return 3 * canastas
    x -= 3
    y = 3 - int(abs(3.5 - y))  # Establecemos una simetría por la mitad
    return zonas[y][x] * canastas

coordenadas = input().split(" ")
zonas = ((3, 3, 3, 2.5, 0, 0, 0),
         (3, 3, 2.5, 2, 2.5, 0, 0),
         (3, 2.5, 2, 2, 2, 2.5, 0),
         (2.5, 2, 2, 2, 2, 2, 2.5))
print("PUNTOS CONSEGUIDOS: %d" % sum(puntos(i) for i in coordenadas))
