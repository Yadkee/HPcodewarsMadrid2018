#! python3

"""[3] El árbitro no sabe contar - 4 Puntos:
  Recibirás las puntuaciones de dos equipos y debes devolver lo siguiente.
  • "Equipo A ganador", si el primer parámetro es mayor que el segundo.
  • "Equipo B ganador", si el segundo parámetro es mayor que el primero.
  • "Se juega prorroga", si los parámetros son iguales."""

valorA, valorB = tuple(int(i) for i in input().split(" "))

if valorA > valorB:
    print("Equipo A ganador")
elif valorB > valorA:
    print("Equipo B ganador")
else:
    print("Se juega prorroga")
