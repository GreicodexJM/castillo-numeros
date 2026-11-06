# Dirección de juego — Estrella y el Castillo de los Números

Este documento fija cómo se juega. El encargo cerrado manda. Aquí no se le quita una luz, no se le pone un cronómetro en pantalla y no se inventa otro juego para los 8–10 años. Lo que se añade son salas, tiempos, máquinas de estados y reglas que se pueden programar.

La jugadora de referencia tiene 6 o 7 años, primero de Primaria, lee frases cortas y se frustra con facilidad. El mismo castillo sirve hasta los 10 sin cambiar de producto. No hay nombre de una niña real en el juego, ni foto, ni edad escrita en pantalla.

La tableta es una Fire 7 en horizontal. El área útil, con la barra de sistema, cabe en 1024×552. Por eso cada sala es una sola pantalla, sin recorrer un mapa, sin vídeo y sin más de dos capas de fondo. Los botones y las ventanas que se tocan miden unos 96 px. Si falta un dibujo, se usa el color plano de esa sala. El progreso vive en `user://`. El juego no pide internet, cámara ni micrófono.

## Fantasía de una frase

Estrella, aprendiz de magia, enciende las salas del castillo entendiendo cómo se juntan, se parten y se ordenan los números, y con cada sesión adorna su torre.

Estrella es un personaje original. No se parece a una princesa de cine ni a un castillo de parque. El edificio es bajo, cálido, de ventanas grandes y torre redonda. La niebla no es un monstruo ni un villano: es lo que apaga las ventanas que aún no se han entendido. Una ventana se enciende cuando el método se ha hecho con las manos, no cuando se ha acertado un número a ciegas.

Ella tiene tres poses y ninguna más: curiosa, contenta, pensando. Pensando es la cabeza un poco ladeada, la boca serena, nunca el ceño, nunca la espalda vuelta, nunca un suspiro. No existe pose de decepción, enfado ni tristeza, ni en un fallo, ni al salir, ni al volver al día siguiente.

## Bucles

### Un minuto

Un minuto de juego es un intento. No es una pregunta de examen. Dura unos 50 s si ella va a su ritmo, y no tiene reloj.

1. De 0 a 2 s: aparecen las piezas y una sola frase, u ocho palabras como mucho. Estrella está curiosa o contenta.
2. A la espera del primer toque. Ese tiempo se anota. No se muestra.
3. Ella arrastra. El tiempo manipulando se anota aparte de las pausas de 4 s o más.
4. Al soltar, hay 3 s para desdecirse. Deshacer no suena a error.
5. Si la configuración enciende la luz, la sala da un pulso de 1,2 s y suena la campanada suave, 0,4 s. La misma campanada si fue sola o con ayuda. Estrella, contenta, 1 s. Se sigue.
6. Si no enciende, la pieza vuelve en 0,4 s, en silencio. Estrella pensando. No hay aspa, no hay zumbido, no hay «mal».

Un minuto no acaba en una nota. Acaba en luz o en una pieza que ha vuelto a la mano.

### Una sesión

Se diseña para unos 7 minutos (420 s de reloj interno). Siete minutos no es un cupo que haya que rellenar ni un mínimo que haya que aguantar. Si el recorrido se cumple antes, se acaba. Si se alarga, se acorta hacia el cierre. Ella no ve la cuenta.

El reloj interno no se dibuja. No hay vela, ni cielo que oscurezca, ni Estrella que bostece para marcar el tiempo.

| Tramo | Qué es | Duración | Tope interno |
|---|---|---|---|
| Entrada | La sala se abre. Sin cuenta | 4 s, se salta al tocar | 4 s |
| Ya sabe | Una cuenta que ya puede hacer | 60 s | 80 s |
| Idea, modelo | Estrella hace el gesto en su lado | 20 s | 20 s. Si ella empieza a arrastrar, el modelo cede |
| Idea, repetición | Ella repite el gesto arrastrando | 40 s | 50 s. Si no arrastra, se acercan las piezas. No se alarga el discurso |
| Borde | Tres intentos del mismo micropaso. Cuatro solo si van cero fallos, no hay cansancio y el reloj interno va por debajo de 300 s | unos 50 s cada uno | no se abre otro si el reloj interno ha pasado de 420 s |
| Acertijo | Un juguete de lógica, no una resta disfrazada | 70 s | 90 s |
| Cierre | Una que puede hacer, con sus manos | 45 s | no se abandona el cierre por tiempo mientras la app siga abierta; a los 480 s se entra en él |
| Torre | Coloca un adorno, si quiere | 20 s | 30 s. Si sale, el adorno espera |

Suma de los objetivos, con tres intentos de borde: 4 + 60 + 20 + 40 + 150 + 70 + 45 + 20 = 409 s. Cabe en los 7 minutos. El cuarto intento solo existe si la sesión aún va holgada.

Orden fijo, el del encargo:

1. Una cuenta que ya sabe.
2. La idea de hoy, unos veinte segundos, y la repite ella arrastrando.
3. Tres o cuatro intentos del borde.
4. Un acertijo que no parece un examen.
5. Cierre con una que puede hacer.

Si en el paso 3 falla dos veces, se salta al cierre. No hay un tercer fallo «para asegurarse». El acertijo de hoy puede no caber. La sala Acertijos no se cierra por eso.

El repaso no es un sexto tramo. La cuenta que ya sabe es el repaso. Si hay dos micropasos firmes, el de la apertura es el que más conviene repasarse; no se añaden minutos para examinar los dos.

Una idea nueva solo si el micropaso anterior está firme. Si no lo está, el tramo de la idea dura igual los 20 s, pero es el mismo gesto de ayer, no un cimiento distinto. En una sesión no hay dos ideas nuevas.

### Una semana

Una semana no es una racha. No hay calendario, ni días vacíos, ni «tres seguidos». Si no abre la tableta, no se apaga nada y Estrella no nombra la ausencia.

Si vuelve cinco días, el ritmo de 6–7 años es este. No es obligatorio.

1. Día en que el anterior ya está firme, y el techo del padre lo permite: una idea nueva, 20 s, ella la arrastra, tres intentos, un acertijo, un cierre, un adorno.
2. Día siguiente: no hay idea nueva. Firme pide otro día, así que este día repite el gesto. La apertura es una que ya sabe. El borde es parecido, no mayor.
3. Si ese segundo día sale sola, sin duda y sin el ejemplo al lado, el micropaso puede quedar firme al guardar. Mañana podrá haber idea nueva. El acierto de hoy, solo, no basta.
4. Si no queda firme, se sigue en el mismo gesto. El castillo se decora igual. Jugar no está bloqueado por no estar firme. Estar firme solo decide si mañana hay idea nueva.
5. Un día de la semana el acertijo puede ir primero, si ella entra por esa ventana. No se le debe una sesión de mates por haber preferido Acertijos.

Al volver después de varios días, la primera cuenta es una que ya sabe, no el borde en el que se quedó. La frase de vuelta habla de la luz que sigue. No dice cuánto tiempo faltó, no dice «por fin», no dice «te echaba de menos».

## Mapa del castillo

Una sola pantalla, el Patio de la Niebla. No se camina. Estrella está en el patio, a la izquierda, de unos 200 px. La Torre de Estrella ocupa la derecha y ya tiene una llama de casa desde la primera apertura: no es un premio, es el hogar, y no se apaga. Arriba, las ventanas del castillo. Cada ventana que se pueda tocar mide 96 px, con al menos 16 px entre una y otra. Nada importante vive en los 48 px de abajo: ahí cae la barra de sistema.

No se dibujan ocho huecos vacíos. Una fila de ventanas apagadas parecería un marcador. Se ven solo las salas disponibles o encendidas, y un ala de niebla para lo que aún no toca. El ala es un solo bulto, no seis candados. Tocar el ala no abre lección. Estrella, curiosa: el sentido de la frase es «esta sala espera». No cuenta como evitar una sala, porque esa sala no estaba abierta.

Tres estados de ventana, y ninguno es una nota:

- **Niebla de ala.** Aún no toca. No es un fallo.
- **Disponible.** Se puede entrar. La ventana se ve, con niebla dentro, sin candado y sin gris de botón muerto.
- **Encendida.** El método se ha hecho al menos una vez con las manos, aunque fuera con ayuda. La luz no se apaga.

Disponible no es lo mismo que encendida. El primer día Piedras de luz y Acertijos están disponibles, no encendidas. Se encienden al primer cierre que ella completa allí.

Si más adelante hay muchas salas abiertas, siguen siendo ventanas del mismo edificio, no un menú con scroll. Ocho ventanas de 96 px caben en 1024. No hace falta desplazamiento.

Ella elige, en el patio:

- qué ventana abierta tocar;
- cuál de dos adornos, los dos del mismo valor;
- en qué gancho de la torre colocarlo;
- en Acertijos, cuál de dos juguetes del mismo peldaño de lógica.

Ella no elige el cimiento siguiente, no apaga luces, no abre el techo y no tiene un selector de dificultad. El único freno externo es el techo del padre.

Evitar una sala abierta no la cierra. Si durante tres sesiones se le propone y ella entra en otra, el padre lee una frase: la puerta sigue abierta. No se insiste esa noche con una deuda. No se infiere miedo ni pereza.

El botón atrás de la tableta, dentro de una sala, guarda y vuelve al patio. No pregunta «¿seguro?». En el patio, guarda y sale del juego. No hay diálogo de abandono.

### Patio de la Niebla

Se llega, se elige ventana, se ve la torre. No hay combate, salto, inventario ni árbol de diálogos. No es una sala de cuentas. Un toque accidental que no mueve piezas y dura menos de 15 s no abre sesión: no deja deuda ni adorno.

### Torre de Estrella

Se decora. No se calcula. Los ganchos miden 96 px. En el producto hay seis. En el primer jugable, cuatro. Si todos están llenos, el adorno que se quita pasa al arcón de la base y se puede volver a poner. Nada se destruye.

### Piedras de luz

Ala izquierda, planta baja. Es la sala de sentir los números, del diez y de las decenas como piezas. La entrada de la sala —ver de 1 a 5 sin contar, contar de uno en uno, más, menos e igual, recta hasta 20— no es otra sala. Es el mismo suelo, a la izquierda de la losa.

Qué se hace:

- arrastrar piedras a una bandeja;
- juntar hasta 10 en la losa de dos filas de cinco;
- partir un grupo para pasar por el 10 (8+5 = 8+2+3);
- poner un salto de uno en la recta, hasta 20;
- más tarde, barras de decena y losas de centena. 23 son 2 decenas y 3 unidades, y también 20+3.

Qué no se hace:

- el algoritmo en columnas (eso es el Pergamino);
- euros, grupos ni reparto;
- cuatro opciones;
- un teclado como camino para adivinar;
- restar dándole la vuelta, ni llamar a eso un truco del Espejo.

La victoria visible es la losa, la recta o la bandeja que se enciende porque los grupos están bien, no porque se haya pulsado un número.

Se abre el día 1. En el producto, la primera idea nueva es ver de 1 a 5, no la llevada. Hacer el 10 llega cuando el diez como grupo toca, no antes de que existir el contar. El primer jugable, que es un corte de construcción, sí entra por hacer el 10: lo pide el encargo del primer hito. Eso no borra la entrada de la sala en el producto terminado.

### Espejo

Pasillo entre el patio y la sala redonda. Dos montones. Ella los cambia de lado. La luz del espejo sigue igual, porque la suma no mira el orden.

Qué se hace: dar la vuelta a una suma para empezar por el mayor. El nombre «conmutativa» se dice solo cuando ese cambio ya está firme, y en una frase de Estrella, no en un cartel de lección. El nombre no bloquea el paso siguiente.

Qué no se hace: restar. 7−3 no es 3−7. No hay un sí/no como único gesto: tiene que cambiar los montones con la mano. No se abre el día 1.

Se abre cuando pasar por el 10 está firme. Antes de eso, el cambio de lado no significa nada.

### Círculo

Sala redonda, ventana alta. Tres números pequeños. Ella junta dos con las manos, como un paréntesis, y luego el tercero. (2+3)+1 al lado de 2+(3+1). Solo suma.

Qué no se hace: la asociativa de la resta. (7−3)−1 no es 7−(3−1). No entra el día 1. No entra con números grandes. No lleva cartel de «asociativa» hasta que el gesto está firme.

Se abre cuando se cumplen los tres hechos, y no antes. No se dice que «ya no tiene miedo»: el juego no ve el miedo.

1. Amigos del 10, firme.
2. Pasar por el 10, firme.
3. Las últimas tres sesiones que tuvieron una suma en el borde no se cortaron por cansancio ni por dos fallos.

No hace falta haber terminado el Tesoro. La asociativa es de la suma, no del reparto. Si los tres hechos no están, la ventana sigue en el ala de niebla.

### Pergamino

Sala alta, un pergamino, no una ficha. Columnas de derecha a izquierda, como en el colegio: unidades, decenas, centenas. Ella arrastra a la columna. Alinear es el método.

Tres momentos, y no se entra por el tercero:

1. Sin llevada. 23+14, unidades con unidades, decenas con decenas. Se abre cuando sumar decenas sueltas está firme.
2. Llevada. Solo cuando hacer dieces ya es fácil (amigos del 10 firme y pasar por el 10 firme) y el pergamino sin llevada está firme. Estrella salta de columna. La frase del colegio es «me llevo una». El diez que ella ha hecho salta de verdad a la columna de al lado.
3. Préstamo. Cuando la llevada está firme. Una decena se rompe en 10 unidades. La frase es «pido prestada una decena». La resta no se lleva al Espejo ni al Círculo para «darle la vuelta».

Qué no se hace: empezar por la llevada, parecer un examen con líneas para rellenar, mezclar céntimos, abrir esta sala en el primer jugable.

### Mercado

Puesto junto a la puerta del patio. No es una tienda que cobre de verdad ni un tendero que se decepcione. Las piezas son monedas de 1, 2, 5, 10, 20 y 50 céntimos, y monedas de 1 y 2 euros.

Qué se hace: primero precios en euros enteros, solo monedas de 1 y 2 euros. Después, céntimos. Cambiar 10 por 1 es el mismo gesto del diez, no una mate nueva. Ella construye el precio en la bandeja. El farol del puesto se enciende cuando las bandejas coinciden.

Qué no se hace: «no te llega», quitarle monedas como castigo, mezclar céntimos el primer día de Mercado, un precio que exija un préstamo que aún no está firme.

Se abre cuando las centenas están firmes, que es su puesto en el orden. El techo del padre puede retrasarlo. No puede adelantarlo saltándose las centenas.

### Jardín

Arriates. Ella hace grupos iguales: tres arriates de dos flores, no una cuenta escrita. Las tablas del producto son la del 2, la del 5 y la del 10. El signo × aparece después de agrupar sola en dos días distintos. El nombre «tabla del 2» es techo de 8–10, cuando el grupo ya está firme, y no sustituye a las flores.

Qué no se hace: 7×8, la canción de la tabla antes del grupo, el signo el primer día, otra sala distinta para los mayores.

Se abre cuando los céntimos están firmes. Hasta entonces la ventana sigue en la niebla.

### Tesoro

Cofres y gemas. Ella reparte de una en una hasta que cada cofre tiene lo mismo. El signo ÷ llega después del gesto, y no bloquea si el gesto ya está firme.

La sobra no entra en el juego de 6–7 como examen. En el techo de 8–10, la gema que sobra se sienta en un cojín. El reparto igual se enciende igual. La sobra no es un fallo ni un castigo. No hay división larga.

Se abre cuando los grupos del Jardín están al menos frágiles: el gesto de agrupar ya se ha visto. No el día 1.

### Acertijos

Claustro de la izquierda. Abierta el día 1. No se cierra nunca, ni por dos fallos de mates, ni por un techo del padre, ni por no jugar.

Qué se hace, en paralelo desde el primer día: seguir un patrón colocando piezas, quitar la que sobra arrastrándola a un tapete (no con un botón), ordenar, igualar dos bandejas, recorrer un camino con una sola condición.

Los problemas con historia no viven aquí hasta que la cuenta ya se hace con las manos. Primero un paso, con dibujo, en la sala de ese gesto. Dos pasos, mucho más tarde, y solo en el techo de 8–10, con los dos gestos ya firmes.

Qué no se hace: esconder una resta difícil, puntuar, numerar «1 de 4», cerrar la sala, usar el acertijo para saltar un cimiento. Fallar un acertijo no baja un micropaso de aritmética. Acertarlo tampoco lo salta.

### Qué no es una sala

No hay sala de ajustes para ella, ni sala de notas, ni sala de tienda, ni sala multijugador. El silencio es un altavoz de 96 px en una esquina del patio: calla todo el sonido y deja el texto. El padre no tiene puerta visible. Entra con una pulsación larga, dicha más abajo.

Colores planos, si falta el dibujo: patio `#1E2A4A` con luz `#F4C56D`; Piedras `#3D4F8A` y piedras `#F2E2A0`; Espejo `#7EC8C3`; Círculo `#E7A6C8`; Pergamino `#F3E6C8` con tinta `#2C2416`; Mercado `#E07A3D`; Jardín `#7DAF6A`; Tesoro `#C6A15B`; Acertijos `#8E7CC3`. Formas grandes, mucho aire, contraste alto, poco detalle.

## Economía de la torre

No hay moneda, energía, racha, duplicados ni rareza. No hay nada que comprar. El premio es adornar la torre, y se gana por jugar, no por hacerlo perfecto.

Se gana:

- **Llama de casa.** Está encendida desde la primera apertura. No se gana. No se pierde.
- **Luz de sala.** La primera vez que ella completa un cierre en esa sala moviendo piezas, con ayuda o sin ella. Una sola vez. No mide lo sola que fue. Lo solo vive en el registro, que ella no ve.
- **Objeto de sala.** Cuando un micropaso de esa sala queda firme, aparece una pieza nueva del método: la recta, la barra de decena, la columna C, el cojín de la sobra. Aparece y se queda. No es un marcador de huecos vacíos. Lo que aún no toca simplemente no está.
- **Adorno de torre.** Uno por sesión en la que ella ha tocado una pieza. El mismo valor siempre. No hay adorno mejor por hacerlo perfecto, ni adorno de menos por haber ido con ayuda.

Catálogo, ocho piezas, sin orden de rareza: farol de ventana, estandarte, cojín, maceta, alfombra, campana, libro abierto, estrella de cristal. La estrella de cristal es un adorno, no una puntuación. No hay estrellas vacías al lado. En el primer jugable bastan cuatro: farol, estandarte, cojín y maceta.

Cada sesión le ofrece dos, al azar de las que aún no tiene a la vista. Ella elige una. Da igual cuál. La coloca en un gancho libre. Si sale antes de colocarla, queda en el umbral de la torre, ya suya. La próxima vez puede ponerla sin repetir la sesión. Si los ganchos están llenos, el cambio pasa por el arcón. Del arcón no se tira nada.

No se puede perder:

- la llama de casa;
- una luz de sala ya encendida;
- un objeto de sala ya aparecido;
- un adorno colocado, en el umbral o en el arcón;
- un micropaso ya visto (no vuelve a «sin ver»);
- la sala Acertijos;
- lo guardado en `user://`.

Bajar un peldaño de maestría no quita luz ni adorno. No jugar no quita luz ni adorno. Salir a medias no quita lo ya ganado. No hay vidas que perder.

El adorno no se enseña antes de la cuenta como cebo de rareza. No hay sala que pague más que otra. La torre se visita unos 20 s, después del cierre, o al volver, si el adorno esperaba. No es una tienda.

## Máquina de estados de la sesión

Ella no ve el nombre de los estados. No se le dice que ha subido ni que ha bajado.

Estados de sesión: `PATIO`, `ENTRADA`, `YA_SABE`, `IDEA_DEMO`, `IDEA_REPITE`, `BORDE`, `ACERTIJO`, `CIERRE`, `TORRE`, `GUARDADO`.

Estados de un intento: `PRESENTA`, `TOCA`, `MUEVE`, `SUELTA`, `JUICIO`.

```
PATIO → ENTRADA → YA_SABE → IDEA_DEMO → IDEA_REPITE → BORDE → ACERTIJO → CIERRE → TORRE → GUARDADO → PATIO
                                              |                    |
                                              |                    +-- 2 fallos, o cansancio fuerte --> CIERRE
                                              |
                                              +-- hoy no hay idea nueva: DEMO de 20 s del mismo gesto, no de otro
```

| Estado | Entra cuando | Sale cuando | Duración | Qué ve ella |
|---|---|---|---|---|
| `PATIO` | Al abrir, o al guardar | Toca una ventana disponible o encendida | la que ella quiera | Castillo, torre, niebla. Sin marcador |
| `ENTRADA` | Entra en una sala | Pasan 4 s o ella toca | 4 s | Estrella curiosa. Una frase. Sin piezas de cuenta todavía |
| `YA_SABE` | Tras la entrada | Acierto, o dos fallos, o tope 80 s | 60 s | Una cuenta de un micropaso que ya puede hacer. Si no existe ninguno, contar 3 piedras con el ejemplo al lado |
| `IDEA_DEMO` | Tras un ya-sabe que no ha cortado el día | 20 s, o ella empieza a arrastrar | 20 s | Estrella hace el gesto en su lado. No en la bandeja de la niña |
| `IDEA_REPITE` | Acaba el modelo | Ella suelta el gesto, o 40 s, o se acercan las piezas y ella suelta | 40 s | Sus piezas. Repetir el modelo es aprendiendo, no un acierto solo |
| `BORDE` | Tras la repetición | 3 intentos, o 4 si cabe, o 2 fallos, o cansancio, o reloj | 50 s × intento | Un solo micropaso. Piezas. Sin «1/4» |
| `ACERTIJO` | Borde terminado sin 2 fallos y sin cansancio fuerte, y el reloj interno por debajo de 480 s | Acierto con sus manos, o 90 s, o cansancio | 70 s | Juguete de patrón, bandejas o camino. Sin numerar |
| `CIERRE` | Toca por orden, por 2 fallos, por cansancio o por reloj | Ella enciende la luz con sus manos | 45 s | Una que puede hacer. Ejemplo al lado si hace falta. Estrella no la resuelve |
| `TORRE` | Tras el cierre, si hay adorno pendiente | Lo coloca, o sale | 20 s | Dos adornos iguales de valor, ganchos libres |
| `GUARDADO` | Al colocar, o al salir habiendo guardado | Vuelve a `PATIO` o cierra la app | instantáneo | Nada nuevo. La luz sigue |

Reglas de paso entre estados:

1. `YA_SABE` acertada sola y sin duda: se mantiene lo firme, no se sube a suelto por ser la primera del día, y se sigue a la idea.
2. `YA_SABE` acertada con duda, o despacio para ella en ese paso: no se sube. Hoy no hay idea nueva. El borde, si se llega, es parecido.
3. `YA_SABE` fallada dudando una vez: ese micropaso baja un peldaño, si ya estaba establecido. No hay idea nueva. Vuelve el gesto (el modelo de 20 s es ese gesto, no el siguiente). Si aún no estaba establecido, no se baja: se enseña el gesto igual, porque es ayuda.
4. `YA_SABE` fallada dos veces: se corta lo nuevo y se va a `CIERRE`. No se abre el borde.
5. `YA_SABE` fallada una vez sin duda: no baja un cimiento firme. Hoy no hay idea nueva. Si ese error es siempre el mismo, hay frase de ese error.
6. A los 80 s de `YA_SABE` sin cierre de intento, se pasa a la idea o al cierre según las reglas de fallo. No se queda atrapada en la apertura.
7. `IDEA_REPITE` no puede fallar la sesión. Si a los 40 s no ha arrastrado, las piezas se acercan a su mano. Soltar el gesto con el ejemplo al lado cuenta como con ayuda.
8. El cuarto intento de `BORDE` solo se abre si van 0 fallos, no hay señal fuerte de cansancio y el reloj interno es menor de 300 s. Si no, tres.
9. Al segundo fallo de `BORDE`, se va a `CIERRE`. Se salta `ACERTIJO`. No se busca un tercero.
10. A los 420 s, si no está en `CIERRE` ni en `TORRE`, no se abre otro intento. Se termina la suelta en curso (como mucho 15 s más) y, si van menos de 2 fallos y no hay cansancio fuerte, se hace un acertijo corto de 40 s. Si no, a `CIERRE`.
11. A los 480 s, tras la suelta en curso, se va a `CIERRE`.
12. El acierto de `CIERRE` no sube de peldaño. Sirve para que el último gesto sea poder hacerlo.
13. `ACERTIJO` fallido no suma fallo de borde y no baja aritmética.
14. Hoy hay idea nueva solo si el anterior está firme, el techo del padre no lo frena, y la apertura no la ha cancelado. En las dos primeras sesiones completas, no hay idea nueva: se repite el gesto, para que exista un otro día.

### Intento del borde

`PRESENTA`: piezas en el origen. Estrella contenta o pensando, nunca triste.

- Primer toque: `TOCA`. Se anota el tiempo al primer toque.
- 20 s sin toque: abandono. Se guarda. No es un fallo de carácter. La próxima apertura será una que ya sabe, no este problema.
- Tocar un número, o tocar el vacío esperando que el juego complete: no enciende nada. No es fallo. Estrella, pensando. El sentido de la frase es «enséñamelo con las piedras». Se sigue en `TOCA`.

`TOCA` → `MUEVE` cuando una pieza cambia de sitio.

- Sostener la misma pieza 8 s o más: duda «sostiene mucho». Una frase corta, si hace falta, de gesto. No hay reloj. No se le dice que se dé prisa.
- Soltar sin haber movido: no es acierto. Vuelve a `TOCA`.

`MUEVE` → `SUELTA` al levantar el dedo en un destino.

- Devolver al origen: se puede. Es dudar o deshacer, no un error con sonido. Tres devoluciones en el mismo intento, o devolución en dos intentos seguidos: cansancio. Se corta lo nuevo.
- Cambiar de destino antes de soltar: al soltar se anota «cambia de destino».

`SUELTA`: 3 s para cogerla otra vez y retirarla. Si se desdice, es duda, se vuelve a `MUEVE`, no es fallo. Deshacer no se quita para «que se decida».

`JUICIO`, si no se desdice:

- **Acierto.** La luz se enciende porque la configuración muestra el método, y ella ha movido piezas. Si el ejemplo estaba al lado, es con ayuda: no sube. Si hubo cualquier duda en el intento, es acierto con duda: no sube, y el siguiente es parecido. Si no hubo duda, ni ejemplo, ni prisa vacía, es sola. Aun así, un acierto de hoy no cruza a firme ni a suelto. Firme mira otro día.
- **Despacio.** Si ya hay al menos cuatro intentos previos de ese micropaso y el tiempo manipulando pasa de 1,5 veces su mediana, o si hubo pausa larga o un sostener de 8 s, el acierto no sube. No se le dice. «Lento» no sale en su pantalla. Si hiciera falta decírselo al padre, es un hecho: ha acertado despacio para ella en ese paso. No se sube.
- **Adivinar.** Manipular menos de 0,8 s sin un gesto reconocible, o escribir el número antes de mover, no cuenta. Obliga a mover piezas. No es un fallo con sonido. No sube. Un gesto correcto hecho deprisa sí cuenta: la prisa prohibida es la que no enseña el método.
- **Fallo.** Definido abajo. `fail_count` suma 1.

Escribir el número, cuando exista, es solo la comprobación, y solo aparece después del gesto. Si el gesto enciende la luz y la cifra no coincide, no se apaga la luz. Estrella señala la cifra, curiosa. Ella puede corregirla. Si no lo hace en 8 s, se anota «gesto sí, cifra no» y el intento sigue siendo acierto del método. En el primer jugable no hay teclado: la comprobación es la losa encendida.

## Fallo, ayuda y cierre

### Qué es un fallo

No hay botón de «listo». Un botón de listo parecería una ficha, y un único sitio que brilla sería adivinar.

Hay dos formas de no encender, y no pesan igual.

**El material no admite la pieza.** La oncena piedra en la losa de 10, la unidad puesta en la columna de las decenas, la gema que no cabe en un reparto ya igual. Vuelve sola en 0,4 s, en silencio. La primera vez en ese intento no es fallo: es el juguete. Estrella pensando. La segunda vez en el mismo intento es un fallo.

**Ella deja un método equivocado y no lo retira en 3 s.** Grupos desiguales que sí caben, dos bandejas que no pesan igual, un farol que no sigue el patrón y ella da por colocado. Eso es fallo a la primera, porque no es un límite del material: es una respuesta. Si se desdice dentro de los 3 s, no es fallo.

Con dos fallos en el borde se salta al cierre. Cada uno de esos fallos, si llevó duda, baja un peldaño y enseña el gesto antes de seguir. El segundo, además, corta. Un fallo sin duda no baja por sí solo. Si el error es siempre el mismo, hay una frase para ese error. Si ese mismo error sigue en otro día, el micropaso no pasa de frágil y no se abre el siguiente. Se repite el gesto. No se cambia de sala para taparlo.

Errores con frase propia, un identificador cada uno, para no mezclarlos. La frase la pone el relato, con estas palabras de colegio cuando toca:

| Id | Error | Sentido de la frase |
|---|---|---|
| `E_CONTEO` | Se salta una piedra o la cuenta dos veces | Señalar cada una, una vez |
| `E_DIEZ` | Se pasa de 10 o se queda en otro grupo | Un grupo de diez |
| `E_LADO` | En el Espejo, cambia el orden y espera otra luz | La suma no cambia al darla la vuelta |
| `E_RESTA_ORDEN` | Intenta restar al revés | 7−3 no es 3−7. No se enseña en el Espejo |
| `E_COLUMNA` | Desalinea U, D o C | Unidades con unidades |
| `E_LLEVADA` | Hace el diez y no salta de columna | Me llevo una |
| `E_PRESTAMO` | Resta cruzando sin romper la decena | Pido prestada una decena. Se rompe en diez unidades |
| `E_MONEDA` | Trata 10 céntimos como 10 euros, o al revés | Diez de estos son uno de esos |
| `E_GRUPO` | Los grupos no son iguales | Los mismos en cada grupo |
| `E_REPARTO` | Un cofre se lleva de más | De una en una, hasta igualar |
| `E_SOBRA` | Esconde lo que sobra, como si fuera un fallo | La sobra se queda en el cojín. El reparto sí se ha encendido |
| `E_PATRON` | Repite el patrón un paso atrás | El que toca ahora, no el de antes |

`E_RESTA_ORDEN` no abre el Espejo ni el Círculo. Esas salas no se usan para «arreglar» una resta.

### Duda al soltar

Se anota al soltar una pieza. Ella no lo ve. No se le dice que ha dudado.

- **Suelta en el sitio.** Acaba a 24 px o menos del origen, después de tenerla en la mano 1 s o más. No es acierto ni fallo.
- **Cambia de destino.** Durante ese agarre, la pieza entró en el radio de la bandeja A durante 0,4 s o más, y se suelta en la bandeja B, distinta.
- **Sostiene mucho.** El agarre dura 8 s o más.
- **Se desdice.** Antes de 3 s, vuelve a cogerla y la saca del destino.

Cualquiera de las cuatro marca el intento como duda.

Si luego acierta: no sube, el siguiente es parecido, y hoy no se retira más ayuda. Si luego falla en el borde: baja un peldaño y se enseña el gesto. Soltar en el sitio, por sí solo, no es el fallo; lo es si después el intento falla.

Una pausa de 4 s o más entre toques se guarda aparte. No se suma al tiempo manipulando. Una pausa no es un fallo. Tres pausas largas en el mismo intento, junto con tiempos que se alargan, entran en el cansancio. Mover piedras un buen rato, si las piezas avanzan, es trabajar: no se corta por eso solo.

### Ayuda

Tres peldaños. Se retira uno, no todos. No se anuncia. No hay pantalla de «ahora sin ayuda». Si la ayuda vuelve, no es un castigo ni una bajada de torre: Estrella pone otra vez el ejemplo en su lado, curiosa. Ella no oye «has bajado».

1. **Piezas a la vista.** Las que ella mueve no se esconden nunca. Si se esconden, no hay gesto. «Piezas a la vista», cuando el registro lo cambia, significa el modelo y los apoyos, no la bandeja de ella.
2. **Ejemplo al lado.** Estrella hace el mismo tipo de gesto en su lado. No deja la solución puesta en la bandeja de la niña. Copiar el ejemplo es con ayuda, y con ayuda no se sube.
3. **Solo el gesto.** El ejemplo no está. Nadie dice que sea un examen. Si sostiene mucho, el ejemplo puede volver sin una palabra de fallo.

Entre medias no hay cuatro opciones, ni hueco para tachar, ni una pieza que solo haya que soltar en el único sitio que brilla. Los destinos son bandejas, columnas, cofres o ganchos del patrón: sitios del método, no una respuesta iluminada.

Quién sube y quién no:

- **Sola:** ella mueve las piezas, el ejemplo no está haciendo el trabajo, la luz coincide con el gesto, no hay duda y no va despacio para ella en ese paso. Solo esto alimenta una subida, y ni así cruza a firme o a suelto en el mismo día.
- **Con ayuda:** ejemplo al lado, o el problema ya dejado a una pieza por el cierre, o la repetición del modelo. Se guarda. No sube. Enciende la sala la primera vez igual: la luz no es un diploma de «sola».
- **No:** no hay gesto válido. No se dice en voz alta. No es una frase sobre su carácter.

Peldaños de maestría, de menor a mayor: sin ver, aprendiendo, frágil, firme, suelto. Ella no los ve. Solo se sube uno. Solo se baja uno. Una vez vista la idea, el suelo es aprendiendo: no se vuelve a sin ver y no se apaga la luz.

- Sin ver → aprendiendo: se muestra la idea 20 s y ella la arrastra.
- Aprendiendo → frágil: acierta sola, hoy, moviendo piezas. No vale copiar el ejemplo.
- Frágil → firme: acierta sola en otro día, sin el ejemplo al lado y sin duda. Un acierto hoy no basta.
- Firme → suelto: acierta sola en más de un día, sin piezas de apoyo, a su ritmo de ese paso, sin pausa larga y sin adivinanza. Seguro no es suelto. Acertar despacio no hace este tránsito.
- Duda y falla: baja uno. De suelto a firme, de firme a frágil, de frágil a aprendiendo. Si ya estaba aprendiendo, se queda y vuelve el ejemplo.
- Los primeros días el registro observa: no sube a firme ni a suelto con esa cosecha, y no baja un cimiento que aún no estaba establecido. Enseñar el gesto no espera. Las reglas de la sesión no esperan.

Lo firme se repasa. Repasar es la apertura de la sesión, no un examen desde cero. Si el repaso sale solo y sin duda, sigue firme. Si sale despacio o dudando y acierta, no sube. Si el repaso se falla dudando, baja de firme a frágil. Un fallo aislado, sin duda, no tira el cimiento.

### Cierre

El cierre es una cuenta que ella puede hacer. La hace ella. Estrella no gana por ella, no coloca la última pieza en su bandeja y no hay una película de victoria si ella solo mira. Eso dejaría la sesión en un acierto falso, y al día siguiente el gesto no sería suyo.

Escalera, sin llamarla así en pantalla:

1. **C0.** Un micropaso que ya ha hecho sola. Si aún no existe, contar tres piedras. Piezas a la vista. Unos 15 s para el primer movimiento.
2. **C1.** Si la colocación no enciende, o pasan 15 s sin un movimiento con destino: el ejemplo aparece en el lado de Estrella. La bandeja de ella se presenta a un solo movimiento que sí es un gesto (la última piedra de un diez que ya se ve en filas, no un imán). Zona amplia, 120 px, pero no es el único píxel que brilla. El brillo, si hace falta, es de toda la losa, no de la respuesta.
3. **C2.** Si otra colocación no enciende: se queda en C1. No hay C3. No hay botón de saltar. No suma fallo de borde. No baja peldaño por ser el cierre. Se anota con ayuda cuando el ejemplo está fuera.

El cierre no puede devolverla al borde. No puede hundir la sesión. Tampoco se resuelve solo.

Si cierra la tableta antes de encender esa luz, el cierre queda pendiente. No se da por hecho. La próxima vez el patio tiene esa bandeja, que es una que ya sabe, no el problema que falló. Estrella no recuerda el fallo. La frase, si la hay, habla de la luz que sigue.

Hasta que esa bandeja se enciende con su mano, no empieza una idea nueva. No es un candado: la torre se puede adornar si el adorno ya se ganó por haber jugado, y Acertijos se puede abrir para un patrón corto. Las salas de mates, si se tocan, muestran la bandeja del cierre, no el borde abandonado. Un toque no hace nada vacío. No hay diálogo de bloqueo.

Así la sesión jugada acaba en un acierto que ella hace, ahora o al volver, aunque se haya acortado. Un cierre pendiente no se apila. Solo hay una sesión abierta.

### Cansancio

El juego no ve que esté frustrada. Ve hechos. No escribe «frustrada» en ningún sitio, ni se lo dice a ella, ni se lo dice al padre.

Se corta lo nuevo, y viene un acierto fácil que ella hace, si ocurre cualquiera de estos:

- devuelve piezas: 3 veces en un intento, o en dos intentos seguidos;
- encadena fallos: el segundo del borde, que ya obliga al cierre;
- abandona: 20 s sin toque en `PRESENTA`, sale de la sala, o cierra la tableta;
- las pausas largas se encadenan y, habiendo ya cuatro intentos previos de ese micropaso, los tiempos van a más de 1,6 veces su mediana;
- el reloj interno pasa de unos 7 minutos.

No se corta solo porque manipule mucho rato si las piezas avanzan. No se corta por un primer toque lento aislado cuando aún hay pocas partidas: eso solo se anota. Con pocas partidas, el cansancio que sí manda es devolver, encadenar fallos, abandonar y pasar de los 7 minutos. Esos no necesitan una mediana.

El corte no quita luz, no quita adorno y no es una bajada de castillo. Cambia la duración y apaga la idea nueva de hoy. Nada más.

### Acertijos dentro de la máquina

`ACERTIJO` tiene la misma máquina de soltar, con estas diferencias:

- no incrementa `fail_count` del borde;
- no baja peldaños de aritmética;
- no sube peldaños de aritmética;
- si se alarga de 90 s, o encadena dos rechazos y además hay cansancio, se va al cierre;
- el segundo rechazo trae el ejemplo al lado de Estrella, y ella coloca en su fila. Eso es con ayuda del acertijo, no una nota.

## Entrada y salida de misión

Una misión es una sesión. Se arma en el aparato, al entrar en el patio, sin internet. Ella no ve el plan.

El plan lleva: identificador, día local, sala propuesta, micropaso de la apertura, micropaso del borde, si hoy hay idea nueva, tamaño de los números, si el ejemplo empieza visible, identificador del acertijo, techo del padre. Nada de esto se elige mirando la hora ni la inclinación de la tableta.

La sala propuesta es la del borde. Su ventana está disponible, no marcada con un «¡haz esto!». Si ella entra en otra sala ya abierta, la sesión se adapta: la apertura y el repaso pueden hacerse allí; la idea nueva no se enseña en una sala que no es la suya; no se sustituye el borde por un cimiento posterior. Si entra en Acertijos primero, juega el acertijo y después puede ir a la sala de hoy. Si se queda en Acertijos y sale, el acertijo que ella ha completado con las manos vale como acierto de esa visita, se guarda el adorno, y la idea de mates espera. No se le cierra Acertijos para obligarla. El padre, si esto se repite tres sesiones, lo ve en una frase.

### Qué se guarda

En cada cambio de estado y en cada suelta, se escribe `user://sesion_abierta.json`. Al terminar de verdad, se vuelca a `user://progreso.json` y se borra la sesión abierta. Guardar es local. No se envía nada.

Por ejercicio, y solo esto: sola, con ayuda o no; tiempo al primer toque; tiempo manipulando; pausas largas aparte; duración de la sesión; hora de inicio; postura de la tableta; duda. La duda es una o varias de: suelta en el sitio, cambia de destino, sostiene mucho, se desdice.

La postura es del aparato, no del cuerpo. Se toma con el acelerómetro, al empezar la sesión y en cada cambio de estado. No hay giroscopio y no hace falta. Tres cubos:

- **Plana.** La gravedad cae cerca de la normal de la pantalla, pantalla hacia arriba, a menos de 25°.
- **Encima de la cara.** La normal de la pantalla mira hacia abajo, a menos de 35° de la vertical invertida. Eso no significa que ella esté acostada.
- **De pie.** El resto: sujeta en vertical o inclinada.

Esos tres datos no eligen micropaso, no acortan la sesión y no se le cuentan al padre como conducta. Ni con pocas partidas ni más adelante. En la pantalla habitual del padre no aparecen. Si algún día el resumen exportado los lleva, van en crudo, sin conclusión.

También se guardan `fail_count`, la fase, la sala, si ya hubo toque, si el cierre se encendió, y si el adorno está pendiente. Una pieza que estaba en el aire al matar la app se tira del intento en curso: no es fallo ni acierto.

### Cerrar la tableta a medias

- Menos de 15 s y sin tocar una pieza: no hubo sesión. No queda bandeja, no queda adorno, no queda reproche.
- Tocó una pieza y no llegó a encender el cierre: la sesión sigue abierta. El adorno, si ya se ganó por jugar, espera en el umbral. El borde no se reanuda. No se conserva el `fail_count` como deuda visible. Lo ya escrito en el registro se queda, incluidas las bajadas que de verdad ocurrieron, para no bajarla dos veces por lo mismo al volver.
- Estaba en el cierre: el cierre sigue pendiente, con la ayuda ya en el peldaño en que iba, nunca más dura que C1.
- Estaba en la torre: el adorno sigue en el umbral o en el gancho, según hubiera soltado.

Matar la app es lo mismo que el botón atrás. No hay pantalla de «progreso perdido».

### Volver

Al abrir, si hay cierre pendiente, el patio muestra esa bandeja. Es una que ya sabe. No es el fallo. Estrella está contenta o curiosa. No hay frase de abandono.

Si no hay nada pendiente, la misión nueva empieza por una que ya sabe. Aunque ayer se cortara en el borde. Aunque lleve días sin venir.

La luz está como estaba. El adorno del umbral se puede colocar sin repetir cuentas. No se gana otro por colocarlo: ya era de aquella sesión.

### Padre

Pulsación larga de 1,5 s en la campana de la torre. No hay rótulo «padres». El PIN es de 4 cifras, local, con un teclado que no usa las piedras del juego: no es un problema de mates. Si el PIN falla, silencio y patio. A la tercera vez seguida, patio también. No hay espera de castigo: un bloqueo temporal castigaría un toque accidental de ella.

Él lee frases, no notas. Una o dos. Hechos y el gesto siguiente. Puede poner un techo, y el techo solo frena o se mantiene: hasta 20, sin llevada, sin mercado, sin centenas, sin el signo de por. No salta cimientos. No abre la llevada si hacer dieces no está firme. No cierra Acertijos. No apaga luces. No quita adornos. No marca a mano «esto ya lo sabe».

Puede exportar un resumen a mano. El resumen son esas frases, no un fichero de puntuaciones. El juego no lo envía. La exportación no entra en el primer jugable. La pantalla de frases, sí: si no, el registro de duda no tiene lector.

No se le dan porcentajes, niveles, semáforos, gráficas, emociones, diagnósticos ni comparaciones. No se le dice que iba retrasada, ni que la tableta estaba encima de la cara y por eso falló.

## Ritmo de 6 a 7 y techo de 8 a 10

De 6 a 7 años el ritmo es el de la tabla de la sesión. Una idea en pantalla. Frases de unas ocho palabras. Piezas de 88 px como mínimo, botones de 96 px, separación de 16 px. El cuarto intento es un lujo, no una norma. No hay problemas de dos pasos. No hay signo × ni ÷. No hay nombre de conmutativa ni de asociativa. La voz, si está, es lenta. Si no está el audio, se ve el texto: permanece al menos 4 s, y ella puede seguir al tocar, nunca antes de 0,8 s, para no cortar a quien lee despacio ni atrapar a quien ya ha leído.

De 8 a 10 no hay otro castillo, otro menú ni otro régimen. Se abre el techo dentro de las mismas salas:

- Piedras de luz y Pergamino: centenas con más soltura, el mismo gesto, números un poco mayores.
- Acertijos y la sala del gesto: un problema de dos pasos, con dibujo, mucho más tarde, solo si el de un paso está firme.
- Jardín: la tabla del 2, del 5 y del 10 ya nombrada, sin quitar las flores.
- Tesoro: la sobra en el cojín, explicada, sin castigo, cuando el reparto exacto está firme.
- Círculo: tres números pequeños cuya suma no pasa de 20. Sigue siendo suma.

No se añade la tabla del 7. No se añade un cronómetro «porque ya es mayor». No se añaden vidas. No se compara con otros niños. «Lento» sigue significando lento para ella en ese paso, y ni siquiera esa palabra sale en pantalla. El padre puede dejar el techo bajo: el juego no empuja hacia las centenas para parecer más serio.

La ayuda se retira por el estado del micropaso, no por la edad. Un paso nuevo que esté aprendiendo vuelve a las piedras, aunque lleve meses en el castillo. Volver a ver piedras no es volver a ser pequeña.

## Primer jugable

El primer jugable no es el producto terminado y no es permiso para saltarse cimientos. Es el corte con el que se prueba el bucle. No empieza por la llevada.

Entra:

- Estrella, tres poses, ninguna de fallo emocional.
- Patio de la Niebla, llama de casa, ala de niebla sin candados.
- Torre de Estrella, cuatro ganchos, cuatro adornos del mismo valor.
- Piedras de luz, solo hacer el 10.
- Acertijos, un patrón de faroles que se continúa colocando, no eligiendo entre dos botones.
- La máquina de sesión entera, cierre incluido, siempre con un acierto que ella hace.
- El registro de duda al soltar una pieza.
- El corte por cansancio.
- Guardar y reanudar como está escrito arriba.
- Hora y postura anotadas, sin mandar.
- Pantalla del padre en texto plano, con PIN y frases. Sin exportación.
- Texto si falta el audio. Color plano si falta el dibujo.
- Altavoz de silencio.

Hacer el 10, en esta pantalla:

- Losa de dos filas de cinco. Así el 5 se ve, sin convertirlo en un examen de decir el número.
- En el borde, la losa empieza con 6, 7, 8 o 9 piedras. El montón de sobra tiene al menos 6. Vaciar el montón no es el método: hay que parar en 10.
- La décima piedra enciende la losa. Esa es la comprobación. No hay teclado.
- La oncena vuelve sola. La primera vez no es fallo. La segunda en el mismo intento es `E_DIEZ`.
- Quedarse corta no es fallo: no hay botón de listo. A los 8 s sin toque, después de haber movido algo, el ejemplo aparece al lado. Si además devuelve piezas o se va, manda el cansancio, no una nota.
- La apertura, si aún no hay nada firme, es contar tres piedras con el ejemplo al lado. Cuenta como con ayuda. No bloquea el día.
- El modelo de 20 s es Estrella llenando su losa. Luego ella la suya.

El patrón del primer jugable:

- Cuatro faroles ya colgados: círculo, estrella, círculo, estrella. El quinto gancho vacío.
- El arcón tiene cuatro círculos y cuatro estrellas. No es una pareja de botones.
- El farol que sigue el patrón enciende la fila.
- El que no, vuelve en 0,4 s, en silencio. Al segundo, ejemplo en la fila de Estrella y ella coloca en la suya.
- No esconde una resta. No baja el diez. Dura unos 70 s, y a los 90 s se va al cierre.

Queda fuera del primer jugable, sin borrarlo del producto:

- Espejo, Círculo, Pergamino, Mercado, Jardín y Tesoro como salas en las que se entra. Solo el ala de niebla.
- Ver de 1 a 5, la recta hasta 20 y más-menos-igual como ideas propias. Entran en cuanto el bucle está probado, en la entrada de Piedras, antes de abrir otra sala. El corte las roza (filas de cinco, contar tres) y no las da por enseñadas.
- Llevada, préstamo, centenas, euros, céntimos, grupos, reparto, sobra.
- Problemas con historia, de un paso y de dos.
- Los nombres difíciles y los signos × y ÷.
- Exportación, vídeo, anuncios, cuentas, multijugador.

Las dos primeras sesiones del corte repiten hacer el 10. No adelantan. Firme, si llega, será en otro día, y aun así el corte no abre el Pergamino.

## Riesgos de diseño

### Que el premio importe más que la cuenta

Se fabrica si un adorno es más raro por hacerlo perfecto, si una sala paga más, si el adorno se enseña antes como cebo, o si hay que hacerlo perfecto para no perderlo.

Defensa: un adorno por sesión jugada, siempre del mismo valor, elegido entre dos que no cambian la cuenta. La torre dura unos 20 s y va después del gesto, no antes. La luz de sala se enciende una vez y no se apaga. No hay racha que proteger. Si ella solo quiere Acertijos, adorna igual —el premio no se usa de palanca— y el padre ve que la sala de mates sigue abierta. No se le cierra el juego hasta que «se merezca» la torre.

### Que pueda adivinar

Se fabrica con cuatro opciones, con un sí/no, con un teclado antes del gesto, con un único destino que brilla, o con un imán que acierta al acercar el dedo.

Defensa: no hay cuatro opciones en ninguna sala. En el primer jugable ni siquiera hay cifra que pulsar. El montón de sobra tiene piezas de más, para que «arrastrar todo» no sea la respuesta. Escribir el número, más adelante, solo comprueba, y solo sale después del gesto. Adivinar deprisa no cuenta y obliga a mover piezas, sin sonido de error. El cierre ayuda con el ejemplo al lado, no con un píxel correcto. La primera vez que una sala se enciende puede ser con ayuda; lo que no puede ser es sin haber movido piezas.

### Que una sala se sienta a examen

Se fabrica con «1/4», con estrellas vacías, con reloj, con vidas, con aspa roja, con «¿seguro que sales?», con Estrella triste, con un cartel de propiedad antes del gesto, con el pergamino maquetado como una ficha, o con un acertijo que en realidad es una resta que aún no está firme.

Defensa: una idea en pantalla. Sin marcador, sin cronómetro visible, sin sonido de error, sin vidas, sin estrellas vacías. El pergamino es un pergamino. Acertijos es un claustro de piezas, abierto desde el día 1, y no se cierra. El cierre es una que puede hacer, no una pregunta de recuperación. El padre está detrás de una campana, no de un boletín que ella pueda abrir. No se le dice que ha subido, ni que ha bajado, ni que ayer lo hacía mejor.

### Que el cierre sea una película

Se fabrica si, para asegurar el acierto, Estrella termina el gesto mientras ella mira. Entonces la sesión «acaba bien» y el gesto no es suyo. Al día siguiente el hueco sigue, y ella ha aprendido que da igual lo que haga.

Defensa: el cierre lo hace ella, aunque sea una sola piedra, aunque el ejemplo esté al lado, aunque haya que dejarlo pendiente hasta la próxima apertura. Pendiente no es perdido. Falso no es acierto.

### Que la tableta no pueda con el juego

Se fabrica con un mapa que se recorre, con vídeo, con muchas partículas, con una carga a mitad de sesión.

Defensa: una pantalla por sala, fundido de 0,4 s, como mucho 40 sprites en movimiento, como mucho 12 partículas al encender una luz, sin vídeo, sin segunda voz encima de la primera. Si falta un dibujo, color plano. El APK del producto debe quedar por debajo de 80 MB, y el corte, muy por debajo de 40. Una espera de carga a mitad de intento no pasa de 1 s; si no cabe el arte, se quita arte, no se quita el gesto.

## Reglas de oro

1. El castillo solo gana luz: una sala encendida no se apaga por fallar, por salir ni por no volver.
2. No hay vidas, cronómetro en pantalla, estrellas vacías, sonido de error ni marcador.
3. Toda sesión jugada acaba en un acierto que ella hace con las manos, aunque se acorte y aunque sea con ayuda. Estrella no gana por ella.
4. Se enciende un método moviendo piezas, no se adivina un número. No hay cuatro opciones ni un único sitio que brilla. Escribir el número, si aparece, es solo la comprobación.
5. Dos fallos en el borde saltan al cierre. No hay un tercero. El acertijo de esa sesión puede esperar. Acertijos no se cierra nunca.
6. La torre se decora por jugar, no por hacerlo perfecto. Lo colocado no se quita. Lo pendiente no se pierde.
7. Estrella, ante un fallo, solo está curiosa, contenta o pensando. Nunca decepcionada, enfadada ni triste.
8. Un paso nuevo solo si el anterior está firme. Firme pide acertar sola y en otro día. El techo de 8 a 10 años abre el mismo castillo; no hay otro juego.

## Aportes al documento único

Estrella, aprendiz de magia, enciende las salas del castillo entendiendo cómo se juntan, se parten y se ordenan los números, y con cada sesión adorna su torre. El castillo es bajo, de ventanas grandes y torre redonda. La niebla no es un monstruo. Una sala se enciende por un método hecho con las manos, no por un número acertado a ciegas. Estrella solo está curiosa, contenta o pensando. No hay pose de decepción, enfado ni tristeza.

Un minuto de juego es un intento de unos 50 s, sin reloj: aparecen las piezas, ella arrastra, al soltar hay 3 s para desdecirse, y o la luz da un pulso de 1,2 s con la misma campanada suave (0,4 s) o la pieza vuelve en 0,4 s en silencio. Una sesión se diseña para unos 7 minutos y no se rellena si acaba antes. Entrada 4 s; una que ya sabe, 60 s (tope 80 s); modelo de la idea, 20 s; ella lo repite arrastrando, 40 s; tres intentos de borde de unos 50 s, o cuatro solo si van cero fallos, no hay cansancio y el reloj interno va por debajo de 300 s; acertijo 70 s (tope 90 s); cierre 45 s; torre 20 s. A los 420 s no se abre otro intento. A los 480 s se entra en el cierre. El reloj interno no se dibuja. Una semana no es una racha: si no viene, la luz sigue; al volver, la primera cuenta es una que ya sabe.

El mapa es una sola pantalla, el Patio de la Niebla, ventanas de 96 px. No se camina y no se dibujan huecos vacíos. Salas: Piedras de luz (descomposición, valor de posición, hacer el 10, recta hasta 20; no el algoritmo en columnas), Espejo (dar la vuelta a una suma; nunca a una resta; el nombre «conmutativa» cuando el gesto está firme), Círculo (asociativa solo de la suma, tres números pequeños, cuando amigos del 10 y pasar por el 10 están firmes y las últimas tres sumas de borde no se cortaron), Pergamino (alinear U, D y C; llevada solo después, «me llevo una»; préstamo, «pido prestada una decena»; no se abre por la llevada), Mercado (primero euros enteros; luego monedas de 1, 2, 5, 10, 20 y 50 céntimos y de 1 y 2 euros; cambiar 10 por 1), Jardín (grupos iguales del 2, del 5 y del 10; el signo × después del gesto), Tesoro (reparto justo de una en una; la sobra, más tarde, en un cojín, sin castigo), Acertijos (patrones, qué sobra, ordenar, dos bandejas, un camino; abierta el día 1 y no se cierra). La Torre de Estrella se decora y no calcula.

La torre no tiene moneda ni rareza. Un adorno por sesión en la que ella ha tocado una pieza, siempre del mismo valor, elegido entre dos. Seis ganchos en el producto, cuatro en el primer jugable. Lo que no cabe pasa al arcón y no se destruye. La luz de una sala se enciende la primera vez que ella completa allí un cierre con las manos, con ayuda o sin ella, y no se apaga. Bajar un peldaño no quita luz ni adorno. No jugar tampoco.

Reglas de la sesión, numeradas:

1. Orden: una que ya sabe, idea de hoy (20 s y ella la arrastra), tres o cuatro intentos del borde, un acertijo, cierre. El repaso es la apertura, no un tramo extra.
2. Si la apertura se falla dudando, ese micropaso baja un peldaño si ya estaba establecido, no hay idea nueva y vuelve el gesto. Si se falla dos veces, se va al cierre.
3. Dos fallos en el borde saltan al cierre. No hay tercero. El acertijo de hoy puede esperar. Acertijos, la sala, no se cierra. Un acertijo no baja ni sube la aritmética.
4. El cierre lo hace ella con las manos. Estrella pone el ejemplo en su lado si hace falta, y no coloca la última pieza por ella. Ese acierto no sube de peldaño. Si cierra la tableta antes, la bandeja espera; al volver no se reanuda el fallo.
5. Una idea nueva solo si el anterior está firme, el techo no lo frena y la apertura no la ha cancelado. Firme es sola, en otro día, sin ejemplo y sin duda. Las dos primeras sesiones repiten el gesto.
6. Se corta lo nuevo si devuelve piezas (3 en un intento, o en dos seguidos), encadena dos fallos, abandona (20 s sin toque, sale o cierra la tableta), o el reloj interno pasa de unos 7 minutos. Con mediana ya suya, también si las pausas se encadenan y los tiempos pasan de 1,6 veces lo suyo. Manipular mucho rato, si las piezas avanzan, no corta.
7. Duda, al soltar: suelta en el sitio (a 24 px del origen tras 1 s), cambia de destino (0,4 s sobre otra bandeja), sostiene mucho (8 s), se desdice (antes de 3 s). Si acierta dudando, el siguiente es parecido y no sube. Si duda y falla, baja un peldaño y se enseña el gesto.
8. No hay cuatro opciones, ni botón de listo, ni un único sitio que brilla. La segunda pieza que el material rechaza en el mismo intento es un fallo. Un método equivocado dejado 3 s, sin desdecirse, es un fallo a la primera. Adivinar sin mover piezas no cuenta y no suena a error.
9. Puede salir cuando quiera. Se guarda en cada cambio de estado y en cada suelta, en `user://`. Menos de 15 s sin tocar una pieza no abre sesión. Hora y postura de la tableta se anotan y no mandan, ni solas más adelante. La tableta no sabe si ella está sentada o acostada.
10. El padre entra con una pulsación de 1,5 s en la campana, PIN local, y lee frases. El techo solo frena: hasta 20, sin llevada, sin mercado, sin centenas, sin el signo de por. No apaga luces, no cierra Acertijos, no quita adornos.

El primer jugable es Estrella, la torre, Piedras de luz haciendo el 10 (losa de dos filas de cinco, montón de sobra con al menos 6, la décima enciende, la segunda oncena es fallo), un patrón de faroles en Acertijos (círculo, estrella, círculo, estrella, y ella cuelga el siguiente desde un arcón, no desde dos botones), el cierre siempre en un acierto suyo, la duda al soltar y el corte por cansancio. No entra la llevada. No se borra, para el producto, ver de 1 a 5, contar, más-menos-igual ni la recta hasta 20: viven en la entrada de Piedras antes de abrir otra sala.

De 8 a 10 años el mismo castillo abre centenas con más soltura, problemas de dos pasos mucho más tarde, las tablas del 2, del 5 y del 10 ya nombradas, y el reparto con sobra explicada sin castigo. No hay cronómetro nuevo ni otro juego.

Reglas de oro del castillo:

1. El castillo solo gana luz: una sala encendida no se apaga por fallar, por salir ni por no volver.
2. No hay vidas, cronómetro en pantalla, estrellas vacías, sonido de error ni marcador.
3. Toda sesión jugada acaba en un acierto que ella hace con las manos, aunque se acorte y aunque sea con ayuda. Estrella no gana por ella.
4. Se enciende un método moviendo piezas, no se adivina un número. No hay cuatro opciones ni un único sitio que brilla. Escribir el número, si aparece, es solo la comprobación.
5. Dos fallos en el borde saltan al cierre. No hay un tercero. El acertijo de esa sesión puede esperar. Acertijos no se cierra nunca.
6. La torre se decora por jugar, no por hacerlo perfecto. Lo colocado no se quita. Lo pendiente no se pierde.
7. Estrella, ante un fallo, solo está curiosa, contenta o pensando. Nunca decepcionada, enfadada ni triste.
8. Un paso nuevo solo si el anterior está firme. Firme pide acertar sola y en otro día. El techo de 8 a 10 años abre el mismo castillo; no hay otro juego.
