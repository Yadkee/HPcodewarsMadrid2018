#! python3

"""[4] Calienta, que sales - 4 Puntos:
  Se recibirán dos nombres y dos valores booleanos representando
   si el balón está inmóvil y el reloj detenido respectivamente.
  La sustitución será legal cuando los dos valores sean 1.
  Sino se pitará técnica y se explicará el motivo.

  El formato es:
   'Sustitución legal: JugadorQueEntra sustituyes a JugadorQueSale'
   o bien
   'Falta técnica: Balón en movimiento, Reloj no detenido - JugadorQueEntra sigues en el banquillo'"""

JugadorQueSale, JugadorQueEntra, EstadoBalón, EstadoReloj = input().split(" ")

if EstadoBalón == EstadoReloj == "1":
    print("Sustitución legal: %s sustituyes a %s" %
          (JugadorQueEntra, JugadorQueSale))
elif EstadoBalón == EstadoReloj == "0":
    print("Falta técnica: Balón en movimiento, Reloj no detenido - %s"
          " sigues en el banquillo" % JugadorQueEntra)
elif EstadoBalón == "0" and EstadoReloj == "1":
    print("Falta técnica: Balón en movimiento - %s sigues en el banquillo" %
          JugadorQueEntra)
else:
    print("Falta técnica: Reloj no detenido - %s sigues en el banquillo" %
          JugadorQueEntra)