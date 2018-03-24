#! python3

"""[2] ¿Naciste en año impar? ¡Pues no juegas! - 4 Puntos:
  Recibirás 5 años de nacimiento y debes devolver lo siguiente.
    • "You win", si hay más jugadores nacidos en año par.
    • "You lose", si hay más jugadores nacidos en año impar.
    • "Invalid number of players", si el programa recibe un número
    de años de nacimiento distinto de 5"""

añosDeNacimiento = input("Introduce los 5 años de nacimiento: ").split(",")

if len(añosDeNacimiento) != 5:
    print("Invalid number of players")
else:
    nImpares = sum(1 for i in añosDeNacimiento if int(i) & 1)
    if nImpares > 2:
        print("You lose")
    else:
        print("You win")
