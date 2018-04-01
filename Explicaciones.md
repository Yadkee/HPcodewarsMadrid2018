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
Partimos el input en espacios y dividimos los tres primeros bloques en tuplas de valores enteros (los marcadores). Así mismo llamamos balance a los últimos dos bloques. A continuación calculamos la diferencia como la diferencia de los balances con la suma de los marcadores.

Por último solo queda devolver la cadena de texto adecuada con la diferencia cuando sea necesaria. Nótese el "%+d" cuando introducimos los valores en la cadena, el más indica que se ha de mostrar el signo aun cuando sean valores positivos.

# [[6] Los mejores del partido - 6 Puntos](/problemas/problema06.py)
```
El entrenador del equipo de baloncesto es un poco nulo con las cuentas, y suele olvidar quiénes son los
máximos anotadores y asistentes al final de los partidos
Se pide hacer un programa que lea el número de jugadores seguido de una linea con la información para cada
jugador.
El formato de entrada será:
    Nº de jugadores a valorar por el entrenador
    NombreJugador1;Puntos;Asistencias
Teniendo en cuenta que puede haber un empate entre varios jugadores, el programa deberá:
• Calcular el máximo anotador.
• Calcular el máximo asistente del partido.
El formato de salida será:
    El máximo anotador es NombreJugador
    El máximo asistente es NombreJugador
Y en caso de empate se mostrarán los mensajes en plural y con los nombres de los jugadores separados por punto y coma (;):
    Los máximos anotadores son NombreJugador1;NombreJugador2
    Los máximos asistentes son NombreJugador1;NombreJugodor2
```
###### Entrada
>2

>Borja;24;12

>Alejandro;12;12
###### Salida
>El máximo anotador es Borja

>Los máximos asistentes son Borja;Alejandro
##### Solución
Tomamos el input de tantos jugadores como nos hayan dicho que hay y separamos la cadena inicial partiendola por el punto y coma.

Iteramos por cada uno de los jugadores. Si supera al máximo anotador se proclama máximo a sí mismo. Si empata se suma a la lista. Lo mismo pasa con los asistentes.

Finalmente se devuelve el resultado en el formato pedido. Nótese el uso de ";".join(lista) para unir todas las cadenas de una lista poniendo un punto y coma como separador. También es relevante el índice lista[::2] que significa que se han de tomar los valores de la lista de dos en dos.

# [[7] Piedra, papel, tijeras - 8 Puntos](/problemas/problema07.py)
```
¡Empate!, ¡empate!, ¡hay empate!
Y así amigos, con el vozarrón de Navarro nos hemos despertado esta mañana. No, tranquilos, no es el
resultado de ningún partido. Como sabéis, ya nos eliminaron la semana pasada, pero seguimos con el espíritu
alegre, ¡porque tenemos todavía la mítica porra de temporada!
A principios de cada año, nos apostamos una buena cenorra, que por supuesto, paga el que menos resultados
haya acertado ese año.
¡Resulta que tenemos empate! ¡Los hermanos Gasol se la juegan!
Ahora en el momento, se nos ha ocurrido que, para elegir al perdedor, vamos a echar un clásico de "piedra,
papel y tijeras".
¿Cómo que no habéis jugado nunca? Ay, ay, ay...
Os recuerdos las reglas:
• Piedra gana a tijeras
• Tijeras ganas a papel
• Papel gana a piedra
Los dos contrincantes, a la de tres, van haciendo los gestos con sus manos del objeto que quieran usar y el que menos rondas gane ¡paga la cena!
En realidad, ya hemos jugado las rondas, pero con los nervios del momento, se nos ha olvidado hacer el recuento :(
¿Nos echáis una mano? Tenemos anotados los resultados de las rondas y estamos buscando un programa que nos diga a quien le toca llenarnos el estómago este año.
```
###### Entrada
>piedra/papel

>tijeras/papel

>papel/papel

>tijeras/tijeras

>papel/tijeras
###### Salida
>Victorias Pau Gasol: 1

>Victorias Marc Gasol: 2

>Empates: 2
##### Solución
Creamos una lista con las opciones y como no estamos en el concurso realmente y vamos a introducir los inputs a mano iremos añadiendo inputs hasta que el usuario meta una línea en blanco.

Definimos una función que tiene como parámetros las elecciones de dos jugadores y devuelve True siempre y cuando el primero gane.

Definimos las victorias del jugador como la suma de todos los casos donde gane el primero. Lo mismo hacemos para el segundo pero en este caso los valores entrarán al revés ([::-1]) de modo que la opción del segundo jugador será el parámetro opción1 en la función gana_el_primero().

Por último devolvemos todos los valores. El número de empates lo hemos calculado como el número total de casos menos las victorias de ambos jugadores.

# [[8] All Star 3 Point Contest - 10 Puntos](/problemas/problema08.py)
```
En el Aii Star de este año se va a realizar una demostración en el concurso de tiros triples, donde un robot de
última generación competirá contra los mejores triplistas del mundo.
Nuestra misión será la de crear un programa que calcule la velocidad y ángulo iniciales que se deben emplear
para meter canasta desde unas coordenadas introducidas como parámetro de entrada. Los ingenieros
mecánicos que han desarrollado el robot han tenido problemas en el suministro de energía, por lo que
deberemos buscar la trayectoria para la cuál sea necesario emplear una menor velocidad inicial
(consumiendo menos energía).
Para ello, se ha pedido ayuda a un comité de expertos científicos que nos han pasado las siguientes
ecuaciones para calcular los parámetros de salida.
A = 90 - 4 * h * L
V = raiz(9.81 * L * tan(pi * A / 180))
La distancia entre el robot y la canasta, designado en las ecuaciones y esquema como L, vendrá dado por la
raíz cuadrada de la suma de las coordenadas del robot, introducidas como parámetros de entrada al
programa, al cuadrado, es decir:
L = raiz(x^2 + y^2)
PD: En el dibujo se ve que la diferencia de alturas entre la canasta y la persona es de 1.15m. Este es el valor de h.
```
###### Entrada
>5

>5
###### Salida
>Angulo: 57.473088 Velocidad: 10.429376
##### Solución
Este problema consiste simplemente en sustituir unas fórmulas y devolver el valor resultante.

La función float() devuelve decimales al contrario de int() que devuelve valores enteros.

Por otra parte el formato ".6f" indica que queremos 6 decimales en nuestra cadena de texto.

# [[9] Nos robaron la cartera - 10 Puntos](/problemas/problema09.py)
```
¡Extra! ¡Extra! ¡Oleada de robos en la Comunidad de Madrid! Durante el partido entre Real Madrid y Barcelona
correspondiente a la Final de la Copa del Rey de Baloncesto, varios equipos de la Copa Colegial fueron
víctimas de diversos robos de material deportivo en sus instalaciones. Ante estos acontecimientos, se ha
decidido aumentar la seguridad en los centros deportivos estableciendo contraseñas de acceso a las
taquillas.
Cada jugador debe establecer la contraseña de su taquilla, pero debe ser una contraseña segura.
Debéis desarrollar un programa que valide una contraseña según las siguientes reglas:
• Regla 1: La contraseña debe tener una longitud mínima de 8 caracteres.
• Regla 2: La contraseña debe incluir al menos 1 dígito [0-9].
• Regla 3: La contraseña debe incluir al menos una letra minúscula [a-z].
• Regla 4: La contraseña debe incluir al menos una letra mayúscula [A-Z].
• Regla 5: La contraseña debe incluir al menos uno de estos 3 símbolos especiales [%, &, @].
```
###### Entrada
>soypepu

>P4uG4s@l16
###### Salida
>PASSWORD ERROR! Rule 1, Rule 2, Rule 4, Rule 5

>PASSWORD OK!
##### Solución
Para este problema vamos a usar el módulo re (regular expressions) que permite encontrar patrones en una cadena de texto.

En el propio enunciado se nos dan los patrones así que es tan sencillo como ir buscando cada uno de ellos y en caso de que no estén añadir el número de la regla a una lista.

Devolvemos la cadena que corresponda. En el caso del error se unen todos los errores detectados separados por una coma y un espacio con el método ", ".join(lista)

# [[10] La zona extraña - 16 Puntos](/problemas/problema10.py)
```
Se ha organizado un torneo de baloncesto en una pista con unas dimensiones y unas zonas de lanzamiento
especiales.
Vamos a considerar que:
• La mitad de la cancha de baloncesto es un tablero de 8 filas y 10 columnas.
• Las canastas desde la zona blanca tienen un valor de 3 puntos.
• Las canastas desde la zona roja tienen un valor de 2.5 puntos.
• Las canastas desde la zona verde tienen un valor de 2 puntos.
• Las canastas desde la zona negra no suman puntos al marcador.
Debéis desarrollar un programa que permita calcular el número de puntos totales conseguidos según las
canastas encestadas en cada una de las zonas.
```
Para ver el mapa acude al [pdf](/Problemas%20HP%20CodeWars%20Madrid%202018.pdf)
```
Donde el punto de color morado es la canasta y los números que se muestran en el tablero se corresponden
con el número de canastas encestadas desde esa casilla.
A continuación, la entrada de datos se corresponde con la posición en pista desde donde se ha encestado (fila
y columna separadas por dos puntos y el número de canastas encestadas:
Fila:Columna:NúmeroDeCanastas
La salida debe mostrarse de la siguiente forma:
PUNTOS CONSEGUIDOS: TotaldePuntos
Las entradas y salidas que aparecen a continuación se corresponden con los datos representados en el
dibujo de la pista-tablero
```
###### Entrada
>2:0:5 3:2:2 3:3:3 2:9:1 7:6:1
###### Salida
>PUNTOS CONSEGUIDOS: 31
##### Solución
Definimos una función que devuelva los puntos de una cantidad de canastas tiradas desde las coordenadas x e y. Viendo el mapa sabemos que para x < 3 siempre estamos en zona blanca. También vemos que el mapa es simétrico con el eje en y = 3.5. Con estas simplificaciones y con los puntos definidos en la lista zonas podemos devolver los valores adecuados.

Ya solo falta devolver los puntos como la suma de los puntos de cada una de las coordenadas desde las que se ha tirado.

# [[11] Seguridad en las cuentas - 17 Puntos](/problemas/problema11.py)
```
Recientemente habéis sido contratados por la ACB para formar parte del equipo de seguridad Informática
que gestiona las cuentas bancarias de los clubs de esta competición.
Una de vuestras primeras tareas es implementar un sistema de seguridad para garantizar que sólo los
usuarios acreditados puedan acceder a la información de estas cuentas, usando un sistema de usuario y
contraseña. Dichas contraseñas no se guardarán en texto plano, sino que se guardará un hash de las mismas.
Un hash es el resultado de una función que mapea datos de tamaño arbitrario a datos de tamaño fijo. La
ventaja de utilizarlo para guardar contraseñas es que éstas no están almacenadas en formato legible, sino
que lo que se almacena es su hash. Cuando los usuarios introducen su contraseña, se calcula su hash y se
comprueba si es el mismo que el almacenado, decidiendo así si la contraseña es correcta o no.

El hash utilizado para guardar las contraseñas es la salida de la función Fowler-Noll-Vo, en su variante FNV-1.
Dicho hash se basa en lo siguiente (pseudocódigo):
    hash = FNV_offset_basis
    for each byte_of_data to be hashed
        hash = hash x FNV_prifne
        hash = hash XOR byte__of_data y
    return hash
Como podéis ver consiste en inicializar el hash a un número fijo, y luego, para cada byte de los datos, dicho
hash se va multiplicando por un número primo y haciendo XOR (GR exclusivo, operador en los lenguajes
de programación comunes) con el byte en cuestión. La versión de FNV-I a utilizar es la de 32 bits, cuyos
valores clave son:
• FNV_offset_basis = 2166136261
• FNV_prime = 16777619
Desarrollad un programa que tome por entrada estándar valores de usuario y contraseña separados en
líneas diferentes, y produzca como salida valores del tipo usuraio:hash_hexadecimal - es común almacenar
tos hashes como secuencias hexadecimales en vez de números-.
Pista: Utilizad una función incluida en el lenguaje de programación para convertir un número a una cadena
hexadecimal, no implementéis vosotros mismos dicha conversión.
```
###### Entrada
>luis

>hola
###### Salida
>luis:bca068e7
##### Solución
En primer lugar hemos escrito la función hash tal y como la describe el pseudocódigo (recuerda que a *= b es lo mismo que a = a * b).

A continuación simplemente pedimos nombre y contraseña y devolvemos la cadena esperada, uniendo nombre y los últimos 8 dígitos del hash con dos puntos. La función hex() devuelve la representación exadecimal de un valor entero. Los índices negativos empiezan a contar por la derecha de modo que [-8:] significa tomar los últimos 8 caractéres.

# [[12] El General Manager rata - 23 Puntos](/problemas/problema12.py)
Enunciado extremadamente largo, para verlo acude al [pdf](/Problemas%20HP%20CodeWars%20Madrid%202018.pdf)
###### Entrada
><EquipoA>

><7>

><Durant 8 10 8 9 8 7>

><Davis 10 6 7 7 9 10>

><James 9 10 8 9 8 9>

><Cousins 10 4 4 5 9 10>

><Irving 6 9 10 10 8 4>

><Westbrook 5 10 8 10 7 4>

><Love 7 10 6 4 5 8>
###### Salida
>Alineación de EquipoA: Irving Westbrook James Davis Cousins. Calificación 5.
##### Solución
En primer lugar hemos definido la tabla de coeficientes usada para calcular las mejores skills en cada puesto. A continuación hemos tomado el nombre del equipo, el número de jugadores y los jugadores elimiando el primer y último caracter con [1:-1] (para quitar los "<" y ">").

A continuación hemos iterado por los cinco puestos posibles, hemos calculado los valores de cada uno de los jugadores que no están seleccionados para un puesto anterior y lo hemos añadido a una lista de opciones. De esta lista de opciones se toma el mejor jugador atendiendo al valor del jugador en dicha posición.

Por último creamos una cadena de texto uniendo cada jugador de la alineación y determinamos la media que será la calificación media del equipo. Devolvemos estos valores y... hemos ganado la HP Codewars de Madrid 2018. ¿Os apetecen unos kit-kat para celebrarlo?