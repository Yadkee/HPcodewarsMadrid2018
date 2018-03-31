# WIP
# [[0] ¡Bienvenidos a CodeWars! - 1 Punto](/problemas/problema00.py)
```
Este es un ejercicio obligatorio, sin el cual no se podrá continuar con el resto.
¡Bienvenidos a CodeWars! Vamos a empezar la competición con un regalo.
Debéis desarrollar un programa que muestre por pantalla el siguiente mensaje de bienvenida:
Welcome to CodeWars!
```
###### Entrada
>No se requiere
###### Salida
>Welcome to CodeWars!
##### Solución
Simplemente consiste en devolver la cadena de texto "Welcome to CodeWars!" y para ello usamos la función print()

# [[1] ¡Bienvenidos a CodeWars! (Expert mode) - 2 Puntos](/problemas/problema01.py)
```
Coged vuestras toallas y secad el sudor de vuestras frentes después del ejercicio anterior.
Este es el primer problema serlo ...
Debéis desarrollar un programa que muestre por pantalla un mensaje de bienvenida personalizado para
vuestro equipo.
```
###### Entrada
>Nombre de equipo, por ejemplo:

>WarríorsTeam
###### Salida
>Welcome to CodeWars WarríorsTeam
##### Solución
En esta ocasión hemos de hacer uso de la función input() para pedirle al usuario el nombre del equipo. Finalmente llamamos a la función print() con los parámetros separados por comas. Ten en cuenta que al unir los parámetros python introducirá un espacio entre ellos.

# [[2] ¿Naciste en año impar? ¡Pues no juegas! - 4 Puntos](/problemas/problema02.py)
```
Uno de los más conocidos clubes de Baloncesto de Madrid ha resurgido, pero el entrenador nuevo es muy
supersticioso con los números. Piensa que los números Impares le traen mala suerte, y quiere que durante
un partido nunca haya más jugadores nacidos en año impar que en año par en la pista.
Implementad un programa que reciba como parámetro de entrada las cinco fechas de nacimiento, separadas
por coma, de los cinco jugadores que están en la pista, y devuelva:
• "You win", si hay más jugadores nacidos en año par.
• "You lose", si hay más jugadores nacidos en año impar.
• "Invalid number of players", si el programa recibe un número de años de nacimiento distinto de 5
```
###### Entrada
>1980,1983,1983,1981,1986

>1986,2000,1993,1982,1986

>1982,1997,1987,1982

>1982,2001,1973,1982,1985,1980
###### Salida
>You lose

>You win

>Invalid number of players

>Invalid number of players
##### Solución
Ahora recibimos varios números en un mismo input(). Para separarlos usamos el método "".split() poniendo la coma como separador. A continuación verificamos que el número de años sea 5.

Para determinar el número de impares sumamos 1 por cada año de nacimiento si ese año es impar (n & 1 verifica si un número es impar mirando su último bit en binario. Si este bit es 1 es que es impar).

Por último devolvemos si hemos ganado o perdido.

# [[3] El árbitro no sabe contar - 4 Puntos](/problemas/problema03.py)
```
Al finalizar el partido de baloncesto, el árbitro ha recibido un balonazo en la cabeza con la mala suerte de
que ha perdido su capacidad para ordenar números. Por tanto, no sabe qué equipo ha ganado el partido
porque no sabe qué número de puntos es mayor.
Ayudémosle con un sencillo programa que reciba dos parámetros enteros, y decida cuál de los equipos es el
ganador.
Deberá sacar como salida;
• "Equipo A ganador", si el primer parámetro es mayor que el segundo.
• "Equipo B ganador", si el segundo parámetro es mayor que el primero.
• "Sejuega prorroga", si los parámetros son iguales.
```
###### Entrada
>88 90
###### Salida
>Equipo B ganador
##### Solución
Para separar ambos valores y convertirlos en número enteros creamos una lista que convierte en número (usando int()) las cadenas de texto resultantes de partir el input por el espacio.

Ahora simplemente queda comparar qué valor es mayor y devolver la decisión del árbitro.

# [[4] Calienta, que sales - 4 Puntos](/problemas/problema04.py)
```
En baloncesto se permiten un número ilimitado de sustituciones durante el juego. Eso sí, ios cambios deben
ser notificados al anotador oficial, que será el encargado de dar permiso al jugador para entrar en la cancha.
Además, para que la sustitución sea legal, el balón debe estar inmóvil y el reloj detenido. En caso contrario,
se pita falta técnica.
Debéis desarrollar un programa que indique si un cambio ha sido legal o si se debe pitar falta técnica, junto
con los motivos para pitarla.
El formato de entrada es:
JugadorQueSale JugadorQueEntra EstadoBalón EstadoReloj
Donde,
EstadoBalón vale 0 si el balón está en movimiento y 1 si el balón está detenido.
EstadoReloj vale 0 si el reloj no se ha detenido y 1 si el reloj está detenido.
El formato de salida es:
Sustitución legal: JugadorQueEntra sustituyes a JugadorQueSale
EstadoReloj
o bien
Falta técnica: Balón en movimiento, Reloj no detenido - JugadorQueEntra sigues en el banquillo
```
###### Entrada
>Paco Fran 0 0

>Jose Lucas 0 1

>Alicia Lucía 1 0

>Marta Sara 1 1
###### Salida
>Falta técnica: Balón en movimiento, Reloj no detenido - Fran sigues en el banquillo

>Falta técnica: Balón en movimiento - Lucas sigues en el banquillo

>Falta técnica: Reloj no detenido - Lucía sigues en el banquillo

>Sustitución legal: Sara sustituyes a Marta
##### Solución
Primero separamos los valores. A esto le suceden los cuatro casos posibles y los mensajes que se han de devolver en cada caso.

# [[5] El Villarato - 6 Puntos](/problemas/problema05.py)
```
Un grupo de clberdelincuentes ha conseguido hackear la base de datos con los resultados deportivos de la
actual temporada de la Liga Colegial. Desafortunadamente los servidores que alojaban esta Información no
disponían de un sistema de copia de seguridad que garantizase la recuperación de los datos originales en
caso de pérdida. Desde la organización se solicita la colaboración de los equipos participantes en el torneo
HP CodeWars para identificar a los equipos que han sido víctimas del hackeo.
Pero, ¿qué han hecho los ciberdelincuentes? Han modificado la base de datos de resultados de modo que
algunos equipos han sufrido modificaciones en los puntos a favor y puntos en contra obtenidos en los 3
primeros partidos de la liga.
Debéis desarrollar un programa que reciba los marcadores de los 3 primeros encuentros, así como los puntos
a favor y puntos en contra. Si los valores de puntos para cada equipo no coinciden con la suma obtenida
según los marcadores, el equipo ha sido hackeado. En caso contrario, la puntuación es correcta.
La entrada de datos está compuesta por:
1. Los marcadores de los 3 primeros encuentros.
2. Puntos a favor.
3. Puntos en contra.
marcadorPartido1 marcadorPartido2 marcadorPartido3 PuntosAFavor PuntosEnContra
La salida estará formada por:
• Un mensaje Indicando si el equipo ha sido hackeado, "Este equipo ha sido hackeado: o la puntuación
es correcta, "Puntuación Correcta".
• La diferencia de puntos a favor.
• La diferencia de puntos en contra.
La diferencia de puntos debe mostrarse Junto con un símbolo "+" o un símbolo "-", dependiendo de la
diferencia con los puntos reales.
```
###### Entrada
>50-20 50-20 50-20 150 60

>50-20 50-20 50-20 250 100

>50-20 50-20 50-20 100 50

>50-20 50-20 50-20 150 70
###### Salida
>Puntuación Correcta

>Este equipo ha sido hackeado: PF: +100 PC: +40

>Este equipo ha sido hackeado: PF: -50 PC: -10

>Este equipo ha sido hackeado: PC: +10
##### Solución
Parto el input en espacios y divido los tres primeros bloques en tuplas de valores enteros (los marcadores). Así mismo llamo balance a los últimos dos bloques. A continuación calculo la diferencia como la diferencia de los balances con la suma de los marcadores.

Por último solo queda devolver la cadena de texto adecuada con la diferencia cuando sea necesaria. Nótese el "%+d" cuando introduzco los valores en la cadena, el más indica que se ha de mostrar el signo aun cuando sean valores positivos.
