#! python3
"""[8] All Star 3 Point Contest - 10 Puntos:
Se recibirán dos coordenadas (una por línea) y se deberán calcular el ángulo
inicial y la velocidad a los que se ha de tirar la bola.
L = raiz(x^2 + y^2)
A = 90 - 4 * h * L
V = raiz(9.81 * L * tan(pi * A / 180))"""
from math import sqrt as raiz
from math import tan
from math import pi

x = float(input())
y = float(input())
L = raiz(x ** 2 + y ** 2)
A = 90 - 4 * 1.15 * L
V = raiz(9.81 * L * tan(pi * A / 180))
print("Angulo: %.6f Velocidad: %.6f" % (A, V))
