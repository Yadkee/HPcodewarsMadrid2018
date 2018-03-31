#! python3
"""[12] El General Manager rata - 23 Puntos:
Se recibirán el nombre del equipo, el número de integrantes y las
 habilidades de cada uno de los jugadores.
Se deben devolver la alineación y la calificación total del equipo."""

coeficientes = ((0, 0.2, 0.45, 0.15, 0.2, 0),
                (0, 0.45, 0.15, 0.35, 0.05, 0),
                (0.2, 0.3, 0, 0.3, 0.1, 0.1),
                (0.4, 0, 0, 0.05, 0.25, 0.30),
                (0.2, 0, 0, 0, 0.3, 0.5))
nombreDelEquipo = input()[1:-1]
numeroDeJugadores = int(input()[1:-1])
jugadores = [input()[1:-1].split(" ", 1) for _ in range(numeroDeJugadores)]

listaAlineacion = []
for puesto in range(5):
    opciones = []
    for nombre, habilidades in jugadores:
        if nombre in (i[0] for i in listaAlineacion):  # Ya está cogido
            continue
        habilidades = [int(i) for i in habilidades.split(" ")]
        valor = sum(habilidades[i] * coeficientes[puesto][i] for i in range(6))
        opciones.append((nombre, valor))
    listaAlineacion.append(max(opciones, key=lambda x: x[1]))

alineacion = " ".join(i[0] for i in listaAlineacion)
calificacion = round(sum(i[1] for i in listaAlineacion) / numeroDeJugadores)
print("Alineación de %s: %s. Calificación %d." % (nombreDelEquipo,
                                                  alineacion,
                                                  min(calificacion, 5)))
