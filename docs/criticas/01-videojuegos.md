# Crítica de dirección — Estrella y el Castillo de los Números

El capítulo de juego no dirige. Repite las ocho reglas, les pone segundos y las vuelve a copiar al final. No hay una pantalla que se pueda montar en 1024×552. Un programador que obedezca ese texto y a la vez el GDD, las mecánicas, la interfaz y la programación tiene que inventar el juego. Inventar es lo que este encargo prohíbe.

Lo cerrado no se discute: el castillo solo gana luz; no hay vidas, reloj en pantalla, marcador ni sonido de error; la sesión que ella termina acaba en un acierto suyo; firme es sola y en otro día; sin cámara ni micrófono; datos locales. La crítica es que, con eso ya dicho, el capítulo no dice qué se ve.

## Contradicciones

Cada una obliga a elegir. Hoy no hay dueño.

1. **Dos fallos en la cuenta que ya sabe.** El GDD (hacia la línea 59) dice que los tropiezos de ese tramo no cuentan para el corte y que se ayuda hasta el acierto. Las mecánicas (hacia la línea 60) lo repiten y avisan de que el capítulo de juego no se sigue. Ese capítulo, en la tabla de `YA_SABE` (hacia la línea 267) y en la regla 4 (hacia la línea 281), manda al cierre al segundo fallo. Lo vuelve a colar en los aportes (hacia la línea 613). Un mismo fallo es ayuda o es corte según el archivo que se abra.

2. **El primer acertijo no es el mismo objeto.** El GDD (hacia la línea 77) y las mecánicas (hacia la línea 164) ensartan piedra, estrella, piedra, estrella. El capítulo (hacia la línea 539, y otra vez hacia la 623) cuelga faroles en círculo, estrella, círculo, estrella. La programación (hacia la línea 182) declara que esos faroles no se implementan. El banco de acertijos ya tuvo que corregir al capítulo. Un director que el encargo manda no puede dejar el juguete del primer día en dos formas.

3. **La partida de referencia no es una.** El GDD (hacia la línea 85) juega tres, un diez, 7 y 3, borde 8, 5 y 9, collar, farol. El relato de la primera sesión pide ocho y dos, un borde distinto, una ficha escrita del diez y una cinta. El audio repite ocho y dos. La programación (hacia la línea 180) tira el guion y se queda con el GDD. El capítulo de juego no mata la cinta ni la ficha: no las nombra. Quien construya por el relato construye otro primer día.

4. **Cuándo se gana el farol.** El capítulo (hacia la línea 227) lo da por haber tocado una pieza. Más abajo (hacia la línea 447) también lo da por completar Acertijos y salir. Las mecánicas (hacia la línea 129) suman las dos vías. La programación (hacia la línea 234) dice que el collar no nace un adorno, y (hacia la línea 248) lo ata a llegar al cierre. Tres hechos distintos encienden el mismo premio. El banco de acertijos, además, hace que el collar se alce y se cuelgue de un clavo de la torre: un premio que el capítulo no ha dibujado y que la programación niega.

5. **Cuándo se enciende una sala.** El capítulo (hacia la línea 91 y la 225) enciende la sala al primer cierre completado allí. La programación (hacia la línea 250) enciende Acertijos al completar el collar, no al cierre de la sesión. Si ella solo ensarta y sale, una spec la deja en niebla y la otra la enciende.

6. **Las puertas de sala no son las del GDD.** El GDD (hacia la línea 97) abre el Mercado cuando el cambio de diez por uno se entiende y la resta pequeña está firme. El capítulo (hacia la línea 184) lo abre cuando las centenas están firmes, y prohíbe adelantarlo. El GDD (hacia la línea 98) no abre el Círculo antes del Mercado en el camino canónico, y no habla de miedo como dato. El capítulo (hacia las líneas 156-162) lo abre con tres hechos que no incluyen el Mercado, y puede abrirlo antes. El Tesoro, en el capítulo (hacia la línea 200), se abre con el Jardín en frágil. La regla 8, firme antes de un paso nuevo, queda en papel. El Espejo del GDD vive en el tramo de hasta 20; el capítulo (hacia la línea 148) espera a que pasar por el 10 esté firme. No es ampliar. Es otro orden.

7. **El aire y las ocho ventanas no caben.** El GDD fija aire de 24 px. El capítulo (hacia la línea 81) baja a 16 px entre ventanas y (hacia la línea 93) afirma que ocho ventanas de 96 px caben en 1024. La interfaz usa margen de 96 px y un rectángulo de 832: con aire de 24 caben siete en una fila, no ocho. La programación separa las dos ventanas del corte con 24 px. El patio del producto, el que el capítulo promete sin desplazamiento, no existe en los píxeles que la interfaz ya contó.

8. **Ganchos que no se dibujan y ganchos que sí.** El capítulo (hacia la línea 114) pone seis ganchos en el producto y cuatro en el corte, de 96 px. La programación (hacia la línea 107) no dibuja ganchos vacíos, deja soltar en cualquier sitio de la pared y acepta torcido y encima de otro. La interfaz prohíbe ganchos vacíos en el patio (hacia la línea 105) y, en el cierre (hacia la línea 205), pide una rejilla de dos por dos. El banco de acertijos (hacia la línea 87) quiere el gancho vacío a la vista. Vacío es a la vez la respuesta del collar y la estrella vacía prohibida. Nadie ha separado las dos formas.

9. **La campana no mide lo mismo.** La programación (hacia la línea 95) la quiere de 96 px. La interfaz (hacia la línea 107) la pone en 48×48, fuera del rectángulo de contenido. El capítulo (hacia la línea 484) no da tamaño. Un botón de 48 px rompe la regla de 96 px que el GDD cerró. Un botón de 96 px en zona de pulgar es el accidente que la interfaz intenta evitar. Las dos specs no pueden ser verdad.

10. **El imán no tiene un radio.** La interfaz (hacia la línea 26) engancha a unos 48 px y dice que el imán no acerca a la respuesta. La programación (hacia la línea 265) usa 72 px de viewport y el mismo radio para colocar. El capítulo no habla de imán. Soltar «en un destino» no es una prueba que se pueda escribir.

11. **La escalera del cierre no tiene los mismos peldaños.** El capítulo (hacia las líneas 401-407) nombra C0, C1 y C2, y dice que no hay C3. La programación (hacia la línea 244) dice que no hay C2. La interfaz se queda en dos peldaños y no usa esos nombres. Un estado que existe en un archivo y no en el otro no se programa.

12. **Veinte segundos sin toque.** En el intento (hacia la línea 298) es abandono: se guarda y la próxima apertura es otra cuenta. En el cansancio (hacia la línea 423) es corte, y el corte trae un acierto fácil en la misma sentada. Salir ahora o salir luego no es un detalle. Es la pantalla siguiente.

13. **El día 2 afirma y niega firme.** El capítulo (hacia la línea 73) dice que, si ese segundo día sale sola, el micropaso puede quedar firme al guardar, y en la frase siguiente dice que el acierto de hoy, solo, no basta. El GDD (hacia la línea 110) ya cerró el tránsito: sola, en otro día, sin ejemplo y sin duda. El párrafo no se puede codificar.

14. **Los primeros días no son un número, y aun así mandan.** El GDD (hacia la línea 106) no dice cuántos. Las mecánicas (hacia la línea 142) congelan subida y bajada hasta que se fije. La programación (hacia la línea 226) permite anotar frágil si acierta sola hoy, y deja `observando` en verdadero. El capítulo (hacia la línea 393) no sube a firme ni a suelto y no baja lo no establecido, pero no prohíbe frágil. Tres políticas.

15. **1,5 y 1,6.** Subir se frena a 1,5 veces la mediana (hacia la línea 316). El cansancio corta a 1,6 (hacia la línea 424). El GDD no trae ninguna de las dos. Las mecánicas no las copian. La programación, en el corte, no usa mediana. Un umbral que solo vive en el capítulo, y además duplicado, no es una regla: es un borrador.

16. **Ocho palabras y doce.** El minuto del capítulo (hacia la línea 23) cabe en ocho. El GDD admite doce. La interfaz (hacia la línea 34) dice que doce es el tope y que ocho bastan. Una frase de diez palabras es legal e ilegal a la vez.

17. **Estrella, ante la pieza que no cabe.** La interfaz (hacia la línea 154) la quiere curiosa si el material rechaza la pieza. El capítulo (hacia la línea 330) y la programación (hacia la línea 208) la quieren pensando. Son dos poses. Solo hay tres, y no sobra una.

18. **El nombre del juguete.** Caja en el GDD, losa en el capítulo y en la interfaz, nido en la programación, cuenco en la frase que la programación cita del relato. Una niña de seis años no arrastra al mismo sitio si la frase dice cuenco y el dibujo es una rejilla de diez huecos.

## Pantallas y estados que no están diseñados

Un estado con duración no es una pantalla. Hace falta qué se ve, qué se toca y qué pasa. Esto no está.

**Patio con cierre pendiente.** La interfaz (hacia la línea 121) quita la elección y pone la bandeja en el patio. El capítulo (hacia la línea 411) dice que no es un candado: la torre puede recibir un adorno ya ganado y Acertijos se puede abrir. La maquetación del patio (interfaz, hacia las líneas 99-107) no tiene celda para un nido de 576×216. Estrella ocupa 200×200, la torre 228×248, hay frase, silencio y ventanas. La bandeja no cabe. Nadie ha dicho si las ventanas siguen, si se apagan sin parecer botón prohibido, o si el patio deja de ser patio.

**Patio con farol en el umbral.** La interfaz (hacia la línea 123) cambia la idea a colocarlo y deja las ventanas tocables. Eso son dos ideas en la pantalla que la propia interfaz (hacia la línea 30) limita a una. El capítulo no dice dónde está el farol que espera: no hay rectángulo, no hay frase única, no hay qué pasa si el dedo entra en Piedras con el farol a medias.

**Demostración de veinte segundos.** El capítulo quiere a Estrella llenando su losa, no la bandeja de la niña. La interfaz la pone a 96×96 en el borde y, en la demo, al centro, tapando el juguete. Un segundo nido de dos filas de cinco, a 96 px y aire de 24, mide 576×216. Al lado del de ella no cabe en 832 px de ancho. Encoger las piedras del ejemplo por debajo de 88 px rompe el mínimo del propio capítulo (hacia la línea 494). «En su lado» no es una composición. Tampoco está qué toca ella durante esos 20 s: la regla de la tabla (hacia la línea 42) dice que si empieza a arrastrar el modelo cede, y la tabla de estados (hacia la línea 268) dice que sus piezas aún no están. No puede arrastrar lo que no se ha puesto.

**Montón de sobra.** Hacen falta al menos seis piedras de 96 px para que vaciar no sea el método. A la derecha de una losa de 576 px quedan unos 256 px. Abajo del juguete, dentro del rectángulo, quedan unos 24 px. La interfaz (hacia la línea 140) lo admite («si no cupiera») y propone el centro-abajo, que tampoco cabe. La programación (hacia la línea 99) lo quiere al centro, por encima del margen. No hay pila: no se dice si se solapan, cuál está encima, si se puede coger la de abajo, ni si una piedra tapada es un destino. La pieza que no cabe en la pantalla no tiene dueño. Es el caso límite del propio primer jugable.

**Los tres segundos después de soltar.** El juicio espera (capítulo, hacia la línea 311). No se dice si la losa sigue apagada, si ya pulsa, o si el pulso se deshace al desdecirse. Una espera de 3 s con la losa apagada se lee como fallo. Una luz inmediata que luego se apaga usa el lenguaje del error, que está prohibido. Sin ese fotograma el minuto no arranca. El mismo hueco existe al pasar de un borde encendido al siguiente nido (8, luego 5, luego 9): si las piedras vuelven en 0,4 s, el acierto y el rechazo se ven igual. Ese tránsito no está en ningún estado.

**Entrada de 4 s.** No hay piezas. «Se salta al tocar» no dice tocar qué. La frase, la puerta de vuelta y el vacío no son el mismo gesto. Si el toque a la frase repite la voz, no puede además saltar la entrada. Dos usos, un control.

**Acertijo corto de 40 s.** Aparece a los 420 s (capítulo, hacia la línea 287). No se dice si es el mismo collar con menos tiempo, si se quitan cuentas, o si la ayuda llega antes. Un tope no es un juguete.

**Torre del quinto día.** El corte tiene cuatro ganchos en el capítulo y cero ganchos en la programación. Al quinto farol el capítulo manda al arcón. El arcón de la torre no está en la lista de pantallas del primer jugable (interfaz, hacia las líneas 263-272). No se sabe si se ve, si se toca, ni cómo se saca una pieza sin que el hueco que deja parezca una estrella vacía.

**Padre.** Hay teclado, frases y techo en la interfaz. No hay pantalla de «elige el PIN y repítelo», que la programación (hacia la línea 441) da por hecha la primera vez. No hay qué ve él si las dos frases no caben a 32 px en una línea de doce palabras. No hay cómo sabe que la campana existe: sin rótulo, a 48 px, en un margen. El capítulo (hacia la línea 488) dice que sin esa pantalla el registro de duda no tiene lector, y no diseña el descubrimiento.

**Ala de niebla.** El sentido de la frase, en el capítulo (hacia la línea 83), es «esta sala espera». La programación (hacia la línea 93) prohíbe inventar esa frase y ofrece otra, «si cabe». Tocar el bulto cambia la pose a curiosa y no abre lección. No está si la frase del patio se sustituye, si suena, o si el toque se traga.

**Poses en el tiempo.** Curiosa, contenta y pensando están nombradas por estado, no por fotograma. No hay pose durante los 3 s de desdecirse, ni durante el retorno de 0,4 s, ni durante el fundido de 0,4 s, ni cuando la oncena vuelve y todavía no es fallo. «Pensando» con la cabeza ladeada, a 96 px de busto, no se lee. El capítulo no dice la distancia mínima a la que esa pose se distingue del fallo emocional que prohíbe.

## Bucles que siguen sin poder construirse

### Un minuto

El minuto del capítulo (hacia las líneas 19-30) es un esquema de examen disfrazado de tiempos. No es un intento jugable.

- A los 0 s no se sabe qué piezas hay ni dónde. Depende del tramo, y el minuto finge una sola puesta en escena.
- La espera del primer toque no tiene techo dentro del minuto. El abandono a los 20 s vive en otro apartado y contradice al cansancio, como ya se ha dicho.
- Arrastrar no tiene radio, ni pila, ni segundo dedo, ni qué pasa si suelta entre dos huecos.
- Los 3 s de desdecirse no tienen imagen. Sin esa imagen no hay juicio.
- El acierto suma pulso de 1,2 s, campanada de 0,4 s y pose contenta de 1 s. No se dice si van seguidos o a la vez. Seguidos son 2,6 s de los 50. A la vez, la campanada acaba antes que la luz y la pose no coincide con nada. El presupuesto de la sesión está hecho con una suma que no incluye este beat.
- El fallo es «la pieza vuelve». No dice a qué mano, si el dedo la sigue, ni qué ve si ya no la quiere.
- Entre un acierto y el intento siguiente no hay estado. El minuto «se sigue» y no enseña el tablero nuevo.
- «La configuración enciende la luz» no es un predicado. En hacer el diez, casi: la décima. En el Espejo, el Círculo, el collar y el cierre, el capítulo no da la configuración que un juez pueda evaluar en un fotograma. Un minuto genérico para nueve salas no se construye ni una vez.

La partida de referencia del GDD no se puede andar sobre estas pantallas. La demo no cabe, el montón no cabe, el salto de 8 a 5 no tiene movimiento, y el collar del capítulo no es el collar del GDD.

### Una sesión

La máquina (hacia la línea 255) es el camino feliz más una flecha. No están el cierre pendiente al abrir, la entrada por Acertijos, el corte a los 420 s, el salto a los 480 s, la salida a los 15 s, ni el ya-sabe que el GDD no corta. La tabla de estados y la lista de reglas de paso no coinciden con el dibujo. Quien implemente el dibujo construye otra sesión.

El ya-sabe, además, tiene un tope de 80 s que el GDD no cerró. Si a los 80 s no hay acierto, el capítulo (hacia la línea 283) sale «según las reglas de fallo». Esas reglas, en el mismo capítulo, incluyen ir al cierre. El GDD pide ayuda hasta el acierto. La sesión puede acabar sin haber encendido la cuenta que «ya sabe», y el cierre es otra cuenta. No está si la primera se da por hecha. Las mecánicas dicen que no. El capítulo no elige.

El corte por dos fallos del borde sí está cerrado. Lo que no está es la pantalla del corte: la frase «Seguimos con una que ya sabes.» ¿sobre el nido que acaba de fallar, sobre un nido ya limpio, o sobre un fundido? Si las piedras mal puestas vuelan en silencio, el puente suena a castigo. Si se quedan, el cierre no es «una que puede hacer»: es el tablero del fallo.

`IDEA_REPITE` «no puede fallar la sesión» (hacia la línea 284). A los 40 s se acercan las piezas. Acercarlas es un imán hacia la respuesta, que el mismo capítulo prohíbe en los riesgos (hacia la línea 567). No se dice cuántos píxeles se acercan ni si eso cuenta como ayuda antes de soltar.

El cuarto intento exige reloj interno por debajo de 300 s. El GDD solo pide cero fallos y sin cansancio. El capítulo añade una puerta. Las mecánicas dicen «si el reloj va holgado», sin el 300. Tres textos, tres cortes.

No hay guion de la sesión que se tuerce. La de referencia es «si nada se tuerce». La niña de este encargo es la que se tuerce. Esa sesión no está dibujada.

### Una semana

No hay semana. Hay un ejemplo de cinco días (hacia las líneas 69-75) y la prohibición de calendario, que es correcta y deja el ejemplo sin soporte.

- No existe un contador de «día de la semana» y no debe existir. Entonces «un día de la semana el acertijo puede ir primero» no tiene quién lo decida ni qué cambia en el patio ese día.
- «Otro día» no está definido en el capítulo. La programación usa la fecha local. El capítulo no lo cita. Una partida a las 23:50 y otra a las 00:10 puede ser firme o no serlo, según el archivo.
- El plan que el capítulo enumera (hacia la línea 445: sala propuesta, micropasos, idea nueva, techo) no está en `sesion_abierta.json`. Sin esos campos, evitar una sala tres veces no se puede contar, y la frase del padre no tiene de qué salir.
- Al volver, el capítulo dice dos cosas: la primera cuenta es una que ya sabe (hacia la línea 77) y, si hay cierre pendiente, el patio muestra esa bandeja (hacia la línea 476). No dice si encender esa bandeja cierra la visita o abre la sesión entera de ese día. Sin eso, el martes no tiene primera pantalla.
- Si el cierre pendiente se arrastra tres fechas porque ni con ejemplo enciende, no hay siguiente peldaño, no hay frase de padre para ese hecho y no hay salida que no sea mentir el acierto. La semana se queda clavada. El capítulo no la ha mirado.
- Firme, frágil y «primeros días» no tienen duración común. El adaptador de las mecánicas no sube ni baja. El de la programación anota frágil. La semana no puede decidir si el jueves hay idea nueva.

Un bucle de semana se construye con campos, una pantalla de vuelta y una sola regla de firme. Aquí hay un relato de ritmo y un esquema que no lo guarda.

## Casos límite sin dueño

**Cerrar la tableta.** Hay tres capas y no casan. El GDD (hacia la línea 66) guarda, no inventa el acierto y, al volver, entra por una cuenta que ya sabe. El capítulo distingue menos de 15 s, toque sin cierre, cierre a medias y torre (hacia las líneas 465-470), y además deja el cierre pendiente en el patio (hacia la línea 409). La interfaz convierte ese pendiente en la única idea del patio. Nadie dice qué pasa si se cierra durante la demo, sin haber tocado pieza, a los 18 s: la regla de los 15 s abre sesión o no según se lea el «menos de». Nadie dice si `fail_count` se pone a cero al guardar la salida o se queda en el fichero y corta el primer borde del día siguiente. Una pieza en el aire se tira, eso sí está en la programación. El resto es interpretación.

**Volver al día siguiente.** No hay pantalla de vuelta. Hay frases del GDD y dos máquinas incompatibles: bandeja pendiente que bloquea el patio, o misión nueva por una que ya sabe. No está la hora a la que «ayer» caduca. No está si el farol del umbral se coloca antes, después, o en la misma pantalla que la bandeja. No está si una bajada ya escrita se enseña otra vez con el ejemplo o se calla. El capítulo dice que no se baja dos veces por lo mismo y no dice cómo se reconoce «lo mismo» al abrir.

**Evitar una sala.** El capítulo (hacia la línea 104) avisa al padre a la tercera sesión en la que, habiéndosele propuesto, entra en otra. La ventana propuesta no lleva marca (hacia la línea 446): ella no puede saber que la evita. «Propuesta» no es un campo guardado. La frase que el padre leería no está en la lista cerrada de la programación (hacia las líneas 444-451). Tres sesiones de solo Acertijos están narradas (hacia la línea 447) y no tienen copia ni contador. Sin marca, sin campo y sin frase, el caso no es de nadie.

**PIN olvidado.** Fallar el PIN devuelve al patio, a la tercera también, sin espera. Correcto para un toque de ella. No hay restablecimiento. No hay PIN de fábrica. Si el padre olvida las cuatro cifras, el rincón queda cerrado para siempre y el registro de duda se queda sin lector, que es la razón por la que el capítulo mete esa pantalla en el primer jugable. Nadie ha escrito esa salida, ni la negativa a tenerla.

**Disco lleno.** El plan avisa de que el disco de la Fire estaba al 91 %. El capítulo no tiene caso. La programación escribe en temporal, vuelca y guarda un `.bak`, y no dice qué ve ella si el temporal no cabe. Un fallo de disco no puede sonar a error, no puede inventar el acierto y no puede borrar la luz. Hoy puede hacer cualquiera de las tres, porque no hay pantalla ni frase. El único escritor de `user://` no tiene dueño cuando no puede escribir.

**Sin audio.** El GDD ya dijo que el texto se ve. El capítulo lo repite y, en el minuto, exige campanada. No separa fichero ausente, altavoz del patio en silencio, volumen del aparato a cero y campanada que no cupo en el APK. No dice si el juicio espera al sonido. La interfaz dice que la victoria sigue siendo visual con el sonido quitado; el minuto no. Dentro de la sala no hay altavoz (interfaz, hacia la línea 101). Si entró con voz y el aparato se queda mudo a mitad, no hay control y no hay frase que lo explique. Estrella no puede hablar del aparato. Entonces la frase no puede decirlo. El caso sigue sin dueño.

**Pieza que no cabe.** La oncena que vuelve está descrita. La piedra que se suelta entre dos huecos, la que tapa otra en el montón, la que el imán de 48 px no coge y el de 72 px sí, y la que en la torre cae encima de otra, no. «Encima de otro vale» y «gancho libre» no pueden ser la misma regla. En el collar, el gancho vacío se ve; en la torre, un gancho vacío está prohibido. La misma palabra nombra un juguete y un marcador. Nadie ha dibujado la diferencia.

**Dos dedos.** La programación (hacia la línea 477) ignora el segundo. La interfaz (hacia la línea 85) dice que no cancela el arrastre y que un apoyo no rompe el turno. No dice qué pasa si el segundo dedo toca la puerta de vuelta, la frase o una ventana mientras el primero arrastra. El capítulo no menciona el segundo dedo. En una Fire, el apoyo de la otra mano es el caso normal, no el raro. Sin dueño, el gesto de 96 px se rompe en el primer minuto real.

**Giro accidental.** La programación fija el paisaje y dice que inclinar no mueve piezas. No dice qué se ve si la tableta pasa a vertical: barras negras, juego de lado, o una pantalla que pida girar. Esa pantalla sería una segunda idea, y no existe. El capítulo gasta un apartado en tres cubos de postura que no cambian el juego y no gasta una línea en el giro que sí cambia lo que ella ve. Un gesto de dos dedos que rote una pieza tampoco está prohibido ni ignorado. El aparato no tiene giroscopio; el dedo sí puede torcer. La pieza no tiene regla de rotación.

## Qué sobra

Sobra todo lo que no decide una pantalla.

- Las ocho reglas están en el cuerpo, otra vez en «Reglas de oro» y otra vez en los aportes. Los aportes (desde la línea 600) son el mismo capítulo encogido. No cierran nada que el cuerpo haya dejado abierto. Se pueden tirar enteros.
- El ensayo de cada sala, «qué se hace / qué no se hace», repite la tabla del GDD. No da un rectángulo, no da un verbo con pieza en la mano, no da el fotograma del acierto. Nueve salas resumidas no son nueve juguetes.
- Los riesgos (hacia las líneas 557-587) vuelven a contar las defensas que las reglas ya dicen. No añaden un caso que el cuerpo no haya nombrado, y se dejan fuera los que sí faltan: disco, PIN, giro, segundo dedo.
- La economía de la torre repite, en cuatro listas, que no se quita lo ganado. El catálogo de ocho adornos no dice tamaño, solape ni qué se ve cuando no caben. Es inventario, no juego.
- La tabla de errores `E_CONTEO` a `E_PATRON` es del relato. Aquí no dice en qué píxel aparece la frase ni cuánto convive con el retorno de la pieza. Ocupa espacio de director y no dirige.
- Los tres cubos del acelerómetro no cambian una sala, un tiempo ni una frase. Están mejor, y de sobra, en la programación. En un capítulo de juego son volumen.
- El ritmo de cinco días es un cuento. No es un plan de construcción. Contarlo como bucle hace creer que la semana existe.
- Los hex de sala (hacia la línea 216) son de dirección de arte. Copiarlos no diseña el patio.
- «Qué no es una sala» y la lista de fuera de producto repiten el GDD. No hace falta una tercera vez para no construir el multijugador.

Lo que falta, en el sitio de todo eso, es una hoja por pantalla del primer jugable: patio, piedras en cada tramo, collar, torre, vuelta, padre. En cada hoja, un dibujo con píxeles, la frase literal, el dedo que vale y el fotograma del sí y del no. Hasta que eso no esté, el capítulo no es dirección. Es un acta de las reglas que ya estaban escritas.

## Decisiones que el documento único debe cerrar

1. Dos fallos en la cuenta que ya sabe no saltan al cierre ni suman el corte del borde.
2. El acertijo del primer jugable es piedra, estrella, piedra, estrella, desde un arcón, y el adorno de ese día es un farol, no una cinta ni una ficha escrita.
3. La losa pasa al pulso en un único instante, en milisegundos desde la suelta, y ese instante no convive con otro.
4. El paso de un nido ya encendido al nido inicial del intento siguiente no usa el retorno de 0,4 s de la pieza rechazada.
5. El nido de ella, el ejemplo de Estrella y el montón de al menos seis piedras tienen rectángulos que caben a la vez en 832×360 sin pisar los 48 px de abajo.
6. El aire entre ventanas del patio es 24 px, y ocho ventanas de 96 px no se prometen en una sola fila.
7. La campana del padre tiene un solo rectángulo en píxeles, el mismo en interfaz y en programación.
8. El radio de soltar tiene un solo valor en píxeles de viewport y no preilumina el hueco correcto.
9. Con cierre pendiente, el patio muestra o la bandeja o las ventanas, no las dos en la misma composición.
10. Cerrar la tableta durante el borde tiene un solo camino de vuelta, y ese camino no reanuda el borde ni inventa el acierto.
11. Veinte segundos sin toque al presentar o abren el cierre en la misma sentada o guardan y salen, y no las dos.
12. Otro día es otra fecha local, y un acierto solo en esa fecha pasa de frágil a firme sin una segunda frase que lo niegue.
13. Los primeros días son un número entero de sesiones completas, y durante ellas el adaptador no anota frágil y no baja.
14. El farol se gana por un solo hecho, escrito igual en el capítulo de juego, en mecánicas y en programación.
15. La torre del primer jugable no dibuja ganchos vacíos, y el quinto farol tiene un sitio visible que no es un hueco de colección.
16. El segundo dedo no suelta la pieza del primero, no pulsa la vuelta y no abre otra sala.
17. Si la tableta gira a vertical, lo que se ve no es el juego de lado ni una pieza girada, y esa pantalla está descrita o se declara que el sistema no gira.
18. Si el guardado no cabe en disco, no se inventa el acierto, no hay sonido de error, y la pantalla es silencio o una frase literal ya escrita.
19. Un PIN olvidado no borra luces ni adornos, y el documento dice si el rincón se restablece en el aparato o queda cerrado.
20. Sin fichero de audio o con el altavoz mudo, el juicio de acierto no espera a la campanada: bastan el pulso de 1,2 s y el texto durante 4 s.
21. Evitar la sala propuesta tres sesiones produce una frase que ya está en la lista del padre, y la ventana no lleva marca.
22. El acertijo de 40 s es el mismo collar con tope de 40 s, o no existe; no hay un tercer juguete.
23. Hacer el diez tiene un solo nombre en la frase y en el dibujo, no caja, losa, nido y cuenco a la vez.
24. Más de 15 s en una sala sin tocar una pieza no abre sesión y no cuenta como sala evitada.
25. El plan de sesión que decide la vuelta (sala propuesta, micropaso, cierre pendiente, farol en umbral) está en el guardado local, o no se usa al abrir.
