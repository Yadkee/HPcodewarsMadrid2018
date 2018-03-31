#! python3
"""[7] Piedra, papel, tijeras - 8 Puntos:
Se recibirán múltiples elecciones de dos jugadores separadas por una barra '/'
 (En el problema original se usaba una pipe '|' y esto hizo que tuvieran que
 validar el problema a mano pues al ejecutar un comando con este símbolo la
 consola lo interpreta como que la salida del comando uno debe ser usada
 en el comando dos. Algo que no se aplica en este caso).
 TL;DR: El pipe da problemas así que usaremos barras."""

opciones = ["piedra", "papel", "tijeras"]
estamosEnElConcurso = False
inputs = []
# En el concurso todo el input es introducido a la vez y has de dejar de leer
#  cuando encuentres un EOFError pero nosotros introduciremos el input línea
#  a línea y marcaremos el final con una línea vacía.
if estamosEnElConcurso:
    while True:
        try:
            inputs.append(input())
        except EOFError:
            break
else:
    inp = input()
    while inp:
        inputs.append(inp)
        inp = input()


def gana_el_primero(opcion1, opcion2):
    return (opcion1 == opciones[0] and opcion2 == opciones[2] or
            opcion1 == opciones[1] and opcion2 == opciones[0] or
            opcion1 == opciones[2] and opcion2 == opciones[1])

victoriasJug1 = sum(1 for i in inputs if gana_el_primero(*i.split("/")))
victoriasJug2 = sum(1 for i in inputs if gana_el_primero(*i.split("/")[::-1]))
print("Victorias Pau Gasol: %d" % victoriasJug1)
print("Victorias Marc Gasol: %d" % victoriasJug2)
print("Empates: %d" % (len(inputs) - victoriasJug1 - victoriasJug2))
