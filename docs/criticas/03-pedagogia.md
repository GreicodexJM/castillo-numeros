# Crítica — pedagogía y regla de subida

Lo cerrado no se reabre: no humillar; el elogio es de proceso; firme exige acertar sola y en otro día; la duda no sube; dos fallos cortan el borde; con pocas partidas la hora y la postura no mandan; la tableta no sabe si está sentada o acostada.

El sistema de estados está enunciado y no es implementable. Hay un enum de cinco palabras y no hay una función. Quien programe hoy tiene que inventar días, ítems, relojes y causas. Eso, en un castillo que se prohíbe inventar el acierto, es inventar el saber.

Hay dos máquinas y no casan. La prosa del GDD y del capítulo de pedagogía habla de «primeros días», «lento para ella», «pocas partidas» y «el anterior». El capítulo de matemáticas exige bancos de ítems, discriminadores y puertas por id. `data/mecanicas.json` ya ha rellenado a escondidas segundos, cuentas y un `dias_fijados_por_el_gdd: null`. Implementar la prosa traiciona el JSON. Implementar el JSON traiciona la prosa. Implementar las puertas de matemáticas no cabe en la sesión de tres intentos. Ninguna de las tres opciones está cerrada.

## 1. Umbrales que faltan o se contradicen

### Días

«Otro día» no es una unidad. No se dice si es otra fecha local o veinticuatro horas. Una partida a las 23:50 y otra a las 00:10 pueden ser el cimiento de la llevada o la misma noche. Tampoco se dice cuántos otros días hacen falta. Firme, en el GDD, cabe en un solo acierto de una sola fecha distinta. Suelto pide «más de un día», que puede ser dos o veinte. Un acierto de hace un mes sigue valiendo: no hay caducidad. La ausencia no se castiga, y eso está bien; usar ese acierto viejo para abrir el préstamo es un hueco, y eso no está resuelto.

«Los primeros días» no tienen número. El JSON lo confiesa: `dias_fijados_por_el_gdd` es null. En el mismo JSON, «las dos primeras sesiones completas repiten el gesto». Dos sesiones no son «primeros días». Nadie ha dicho cuál de las dos reglas manda, ni qué pasa con los aciertos guardados cuando la observación termina. Si no cuentan, se tiran sin decirlo. Si cuentan de golpe, una cosecha que no podía subir aparece como firme el día en que el interruptor se gira. Las dos lecturas se pueden programar. Las dos no son el diseño.

Dentro de la observación hay otra contradicción. Si en esos días no manda ni la subida ni la bajada, el paso de sin ver a aprendiendo también está prohibido, porque es una subida. Si ese paso sí manda, porque es la lección y no un juicio, hay que decirlo. Hoy no está dicho. Sin esa frase, el suelo «una vez vista la idea, aprendiendo» no tiene fecha de entrada.

### Ítems

El capítulo de matemáticas no pide un acierto. Pide conjuntos. M04 pide contar 6, 7, 8, 9 y 10 distintos de los enseñados. M08 pide contar hasta 11, 12, 13, 14, 15 y 20, y escribir 11, 14 y 15. M12 pide cuatro sumas concretas, entre ellas 0+1 y 9+1. M23 pide cinco parejas distintas, «entre ellas una de las difíciles para ella». M44 no se fía de 32−17: exige además el discriminador 32−15, porque 15 y 27 y 23 no son el mismo error.

La sesión no puede recoger esos conjuntos. El borde son tres intentos, o cuatro si no hay fallos ni cansancio. Al segundo fallo se corta. Con la idea, el acertijo y el cierre, un banco de cinco ítems no entra en unos siete minutos. Nadie ha escrito el libro mayor que acumula ítems a través de sesiones. Sin ese libro, el enum se actualiza con el último evento: un 2+1 al día siguiente marca M12 firme y deja 0+1 y 9+1 sin ver. Eso es un hueco con apariencia de puerta.

El capítulo de pedagogía empeora el choque. Su tabla tiene 29 filas. La tabla normativa tiene 81 ids. La fila «sumar y restar 1 y 2, hasta 10» mete en un mismo estado M12, M13, M16 y M17. Un firme de esa fila, leído al pie de la letra, abre el hueco de la resta. El GDD dice que la tabla de 81 es normativa. El capítulo que debía decir cómo se sube no usa esos ids. No hay una lista de predecesores. «El anterior» no es un grafo. M28 no bloquea las decenas, dice matemáticas; «el anterior» de una cadena lineal sí las bloquearía. Las dos reglas están escritas. No pueden estar las dos en el código.

«Una de las difíciles para ella» no es un umbral. Es un círculo: para saber qué pareja es difícil hace falta un registro que el mismo párrafo no define. Si se elige a mano la pareja 9+1, se ha comparado con un niño tipo. Si se elige la que más ha fallado, con dos datos, el adaptador persigue un azar.

### Lento para ella

El GDD se contradice solo. «Lento y bien puede ser firme.» Y, en el párrafo siguiente, sostener más de 8 s es duda, y la duda no sube. Si lento es ese sostener, lento no puede ser firme. El capítulo de matemáticas separa las dos cosas: despacio no sube a suelto y no impide lo firme. El capítulo de pedagogía las vuelve a pegar: «Acertar despacio no sube de nivel. Despacio es lento para ella en ese paso (pausa larga o sostener mucho).» Y aún: sola «ni siquiera sube si hay duda o si va despacio para ella». Esa frase cierra la puerta que el GDD deja abierta. Quien obedezca el capítulo de pedagogía castiga a quien cuenta con la pieza en la mano. Quien obedezca el GDD no sabe qué número comparar.

8 s no es «para ella». Es un reloj absoluto, el mismo para quien ya suelta el amigo del 10 y para quien aún aparta piedras de una en una. El juego enseña a manipular y luego llama duda a la manipulación larga. Hasta que no haya una mediana de esa niña en ese micropaso, «para ella» no se puede calcular. El texto no dice cuántos aciertos hacen falta para tener mediana, ni qué pasa mientras no los hay. El JSON no lo arregla: copia los 8 s y declara a la vez `lento_y_bien_puede_ser_firme` y `lento_no_sube_a_suelto`.

La pausa larga, en prosa, no tiene segundos. En el JSON son 4 s, tres veces en el mismo intento. Tres pausas de 4 s no están en el GDD. Una sola lectura del capítulo de pedagogía puede cortar la sesión con una pausa, porque «si se encadenan» no dice cuántas.

### Cuándo manda la hora

No hay un cuándo. Hay una negativa con una puerta entornada. No mandan con pocas partidas. No mandan solas más adelante. «Pocas» no es un número. «Más adelante» no es una fecha. «No solas» significa que, juntas con otra señal, sí podrían mandar, y no se dice con cuál, ni a partir de qué sesión, ni qué cambiarían. El mismo capítulo dice que la hora no elige el micropaso y que una sesión de noche no es cansancio. El JSON va más lejos: el adaptador no puede usar la hora para cambiar el juego. El GDD dice «todavía» en el primer jugable. Tres fuerzas distintas. La única lectura que no infiere es: la hora no entra en ninguna función. Eso no está escrito como regla. Está escrito como escrúpulo.

No hay franjas. No hay zona horaria. No se dice si las 21:00 son noche. «No se insiste esa noche», en la frase del padre, usa la hora que el adaptador no puede usar.

### Cuándo manda la inclinación

Tampoco hay un cuándo. Los cubos están nombrados: de pie, plana, encima de la cara. No están los ángulos, ni cuántas lecturas hacen un cubo, ni qué se hace si el acelerómetro tiembla. Sin giroscopio, «de pie» es el cajón de lo que no es plana ni boca abajo. «Encima de la cara» es un nombre que ya empuja a la lectura que se prohíbe. El capítulo dice que no mandan con pocas partidas ni solas más adelante, y a la vez que no eligen micropaso, no acortan solas y no se cuentan al padre como conducta. «Solas» vuelve a dejar un uso conjunto sin definir. Si ese uso no existe, hay que escribir «nunca». Si existe, hay que escribir la función. Hoy no hay función, y un programador la inventará el día en que quiera «aprovechar» el dato.

### Otros umbrales rotos

El primer acierto del día no sube a firme. No se dice si es el primer acierto de esa fecha en todo el castillo o el primero de ese micropaso. El tramo de apertura es un acierto, o lo será cuando se ayude hasta el acierto. Si consume el cupo, el borde de ese día no puede firmar. Si no lo consume, hay que decir que ese tramo no es un acierto de subida. Las dos lecturas cambian el día en que se abre la llevada.

Solo se baja uno. Puede querer decir que no se salta un estado, o que en una sesión no se baja dos veces. El capítulo de pedagogía elige la lectura dura: cada fallo con duda de los dos del borde baja uno, y el segundo además corta. Suelto por la mañana puede ser frágil por la tarde. Eso es un precipicio, no un peldaño. El JSON dice que si el error sigue en otro día se baja como máximo uno, y la prosa dice que «no pasa de frágil», que desde suelto es bajar dos. Otra vez dos máquinas.

El cuarto intento pide «sin cansancio». Cansancio no tiene umbral en la prosa. El JSON añade un reloj de 300 s que el GDD no menciona. Tres condiciones, una de ellas fantasma.

## 2. Señales pedidas sin definición operativa

Se pide anotar, por ejercicio: sola, con ayuda o no; tiempo al primer toque; tiempo manipulando; pausas largas; duración de la sesión; hora de inicio; postura; duda. Varias de esas palabras no nombran un evento. Nombran una intención.

**Tiempo de juego.** «Unos siete minutos» no es un reloj. El JSON tiene 420 s para no abrir otro intento y 480 s para entrar en cierre. La prosa no los adopta. No se dice qué cuenta: el patio, la torre, el rato con la tableta abierta sin tocar, el acertijo. «Se acorta entre turnos» no dice cuántos segundos se quitan ni a partir de qué señal. Menos de quince segundos sin tocar una pieza no abre sesión. Eso no es la duración: es un filtro de entrada. Veinte segundos sin toque, en el JSON, es irse. Quince y veinte no son el mismo reloj y no miden el tiempo de juego. Sin una suma definida, «la sesión pasa de unos siete minutos» no se puede comprobar.

**Hora.** «Hora de inicio» no dice si es local, si lleva fecha, si se guarda el minuto o la franja. No hay regla de uso. Anotar sin decir la unidad ni la función es guardar un número para que alguien lo interprete después. Eso es lo contrario de no inferir.

**Orientación de la tableta.** Tres etiquetas, cero grados, cero muestras, cero regla de estabilidad. «Encima de la cara» no es una medida: es una escena. La tableta no sabe si está sentada o acostada, y eso está cerrado. Entonces el dato, si se guarda, tiene que ser un cubo del aparato con umbrales escritos, o no guardarse. Un cubo sin umbral lo rellena quien escribe el código, y lo rellena con la escena que el nombre sugiere.

**Tiempo de respuesta.** No existe como señal única y el texto lo trata como si existiera. Están mezclados el tiempo al primer toque, el tiempo con la pieza en movimiento, el agarre quieto y la pausa sin toque. No se dice cómo se parten. Un agarre de 9 s puede ser a la vez duda (más de 8 s), manipulación larga, pausa y «lento para ella». Cuatro contadores, un gesto. El tiempo al primer toque «se alarga» comparado con ella en ese paso a lo largo de la sesión. No hay ventana, ni ratio, ni mínimo de intentos. Con tres intentos de borde no hay una serie. Un primer toque lento, aislado, «solo se anota» si hay pocas partidas. «Pocas» sigue sin número. A partir de ahí, el mismo hecho puede cortar la sesión. El interruptor no está escrito.

**Duda al soltar o al devolver.** El GDD sí fija cuatro hechos: soltar a menos de 24 px del origen tras 1 s; cambiar de destino; sostener más de 8 s; desdecirse antes de 3 s. El capítulo de pedagogía repite los nombres y se deja los números. «Cambiar de destino» en el GDD no tiene ni distancia ni tiempo de permanencia. El JSON importa 0,4 s de otro capítulo. La crítica de pedagogía no puede dar por operativa una duda cuyo segundo hecho vive fuera del texto que la usa.

Devolver y desdecirse no están separados. Deshacerse antes de 3 s es duda, no error, y no se quita. Devolver piezas es cansancio y corta lo nuevo. El primer jugable corta «si devuelve piezas», sin cuenta. El JSON exige tres veces en un intento, o en dos intentos seguidos. Una devolución puede ser juego, duda y corte a la vez. El aire de 24 px entre piezas es el mismo número que la duda de soltar en el sitio. Una suelta en el hueco, a 20 px del origen y a 20 px de la losa, se puede clasificar como duda. En una pantalla de 1024×600, con piezas de 96 px, eso va a pasar. Cada falsa duda bloquea la subida, porque la duda no sube. El umbral motor está cerrado; el conflicto con el aire no está resuelto. Sin resolverlo, firme se vuelve inalcanzable por un error de layout.

**Abandono.** Puede ser salir de la sala, cerrar la tableta, veinte segundos sin toque, o irse después de tiempos largos. El GDD distingue no abrir sesión (quince segundos) de cerrar a medias (se guarda, no se inventa el acierto, al volver no se reanuda el fallo). El capítulo de pedagogía añade que, si el abandono llega después de tiempos largos, piezas devueltas o fallos encadenados, «queda anotado como corte por cansancio, no como falta de interés». La segunda mitad niega una inferencia y la primera la sustituye por otra. No se dice el orden: si el fallo ya bajó el estado y luego cierra la tableta, ¿el abandono borra esa bajada? No está escrito. «Se va» y «abandona» son dos nombres para un hecho sin identificador.

**Ayuda usada.** Tres peldaños, y ninguno tiene condición de entrada medible. No hay tabla de estado a peldaño. Frágil podría ser con ejemplo o sin él. Las dos se pueden defender con el texto. «Sola» exige que las piezas no se coloquen solas, que no haya modelo resuelto al lado y que la comprobación coincida. En el primer jugable la comprobación escrita puede no estar. Entonces sola es el gesto, y el gesto válido de cada id está en matemáticas, no en una máscara que el registro pueda aplicar.

«Un dedo ajeno señala el destino» no es una señal. No hay cámara. Dos toques no dicen de quién es el segundo. El capítulo afirma que el juego lo cuenta como ayuda y se lo dice al padre. Eso es escribir en el registro un hecho que el aparato no puede ver. Copiar el ejemplo «no cuenta como sola» y no se dice cómo se reconoce la copia: ¿misma trayectoria, mismos huecos, dentro de cuántos segundos del modelo? Sin esa regla, o todo acierto con el ejemplo en pantalla es ayuda —y entonces hay que decir que el ejemplo visible basta, sin hablar de dedos—, o el adaptador adivina la copia.

«Si sostiene mucho, el ejemplo puede volver.» «Puede» no es una transición. O vuelve al pasar de 8 s quietos, o no vuelve. Hoy un implementador elige, y las dos elecciones cambian si el día cuenta como sola.

## 3. Castigo, sobreajuste y huecos

El corte a los dos fallos protege. No basta. El adaptador, con las reglas tal como están, tiene tres modos de fallo, y los tres caben en el mismo enum.

### Castigo

El mismo gesto entra en varios contadores. Sostener, pausa, lento y duda pueden dispararse juntos. Si después falla, baja un estado, se enseña el gesto y, si es el segundo fallo, corta. Si además devolvió la pieza, el primer jugable ya tenía un corte por devolución. Una niña que prueba, suelta, vuelve a coger y tarda puede perder dos estados y la idea nueva en cuatro minutos. No se le dice que ha bajado. El castigo no necesita la palabra «mal» para ser un castigo: al día siguiente el ejemplo ha vuelto, el borde es más pequeño y la sala que ayer se abría ya no se abre. Ella no oye el estado. Nota el cambio.

Dos bajadas en un borde convierten suelto en frágil en una fecha. «Solo se baja uno» queda en nada si uno es por evento y no por día. Un cimiento que costó varias fechas se deshace en una tarde mala. Eso empuja a no intentar, que es la indefensión que el propio capítulo describe y luego no cierra con un tope.

El tramo «una que ya sabe» es, en el GDD, un sitio donde los tropiezos no cuentan para el corte y se ayuda hasta el acierto. En pedagogía, un fallo con duda en ese tramo baja un estado, y dos fallos cortan lo nuevo. Esa segunda regla humilla el repaso: la cuenta con la que se abre el día, elegida porque ya era suya, se convierte en examen. Si el repaso es de otro micropaso que el borde, además se baja un cimiento que hoy no se estaba enseñando. El JSON ya avisa de que el GDD manda y de que no se salta al cierre por tropiezos de ese tramo. El capítulo de pedagogía no se ha enterado. Mientras las dos frases existan, alguien implementará la que castiga.

Probar lo suelto puede destruir lo firme. Suelto exige quitar las piezas de apoyo. Si en esa prueba duda y falla, baja. No hay una prueba que no puntúe. El instrumento de la soltura es el mismo evento que deshace el cimiento. Quien va justa no llegará a suelto, y quien llega puede salir de firme por el propio criterio. Hace falta una regla de que el primer fallo sin duda de esa prueba no baja, y de que la prueba no se repite el mismo día. No está.

Ocho segundos quietos, leídos como duda, cierran firme a quien cuenta en la mano. La duda no sube, y eso no se reabre. Si casi todo contar real dispara la duda, la regla cerrada fabrica un techo falso: la llevada no se abre porque el diez nunca llega a firme, no porque el diez no esté. El hueco de más adelante sale de un umbral motor, no de un cimiento. Separar pieza quieta de pieza que se mueve no reabre la duda. Sin esa separación, el método que el castillo enseña es el método que el registro penaliza.

La frase al padre «Ha dudado y ha fallado» y «Ha acertado despacio para ella» trasladan el juicio a la mesa. Ella lee frases cortas: el propio capítulo lo dice. Si mira esa pantalla, el elogio de proceso no la protege. El castigo se ha mudado de sitio.

### Sobreajuste

«El siguiente es parecido» no tiene distancia. Parecido puede ser otra vez 8+5, que es el ejemplo que matemáticas prohíbe usar como prueba de firme. Tres parecidos en el mismo borde no suben, y eso está bien, pero ocupan los únicos intentos del día. El discriminador no entra. Matemáticas dice que, si el registro solo tiene ítems donde dos fallos coinciden, no se elige frase hasta ver un 32−15. Pedagogía dice que hay una frase para ese error, como si el error ya estuviera clasificado. El adaptador que obedece «parecido» puede no presentar nunca el discriminador. El adaptador que obedece la frase habla antes de saber qué error es. Las dos cosas enseñan mal: o se calla y se repite el ítem tramposo, o se dice «rompe la decena» cuando lo que hizo fue girar la resta.

Un acierto sola en otro día, sin libro de ítems, sobreajusta al contexto: misma sala, mismas piezas, a veces el mismo par. El mínimo cerrado —sola y en otro día— es necesario. No es suficiente. Matemáticas ya escribió la condición que falta (otros números, gesto coherente, discriminador) y la regla de estado no la lee. El enum no puede guardar un conjunto. Mientras el estado sea una sola palabra por micropaso, o se sobreajusta al último acierto o se espera a un conjunto que la sesión no puede llenar. Hace falta un libro de ítems vistos, con fecha, y una regla de cobertura. No es un refinamiento. Es la estructura de datos.

«Siempre el mismo» no tiene N ni ventana. Dos coincidencias pueden ser azar. Una coincidencia al día siguiente pone el techo en frágil y no abre el siguiente. Si el clasificador se equivoca, el techo persigue el error equivocado y el gesto correcto no se enseña. Matemáticas, en el préstamo, ya demuestra que sin discriminador no se puede elegir frase. Esa cautela no está en la regla de estados. Está en un párrafo de errores. El adaptador de estados no tiene por qué verla.

No hay calendario de repaso. «Lo firme se repasa» y la sesión solo tiene un hueco de «ya sabe». Con 81 ids, casi todo lo firme no se vuelve a ver. El hueco aparece el día en que, por azar, ese id sale, y entonces un fallo aislado no baja y un fallo con duda sí. La memoria a días vista queda en una frase. No hay una cola. Sin cola, el adaptador repasa lo de ayer, que es lo que más acaba de ver, y llama firme a lo reciente. Eso es sobreajuste de recencia.

### Huecos

La puerta de la llevada son M23, M24 y M25 firmes, y el pergamino sin llevada antes de mezclar. El préstamo añade M26. Esas puertas están bien elegidas. No están conectadas al enum. «Un paso nuevo solo si el anterior está firme» no dice cuál es el anterior de M41. Si es M40, se puede abrir la llevada con el puente sin firme. Si es «todo lo de antes», el nombre de la conmutativa bloquea, y matemáticas dice que no bloquea. El capítulo de pedagogía dice las dos cosas en páginas distintas: la cadena no se salta, y el nombre no es un estado más. Sin una arista por id, el hueco y el bloqueo injusto son la misma ambigüedad.

El círculo espera a que «sumar ya no da miedo» y, en el camino canónico, a no ir antes del mercado. Miedo no es un estado. Es la inferencia que el capítulo prohíbe. Si el padre pone «sin mercado», no se dice si el círculo espera para siempre. Un techo de monedas no debería esconder un juguete de suma. Hoy puede esconderlo, porque «no antes del mercado» no tiene excepción de techo. Eso es un hueco fabricado por una palanca que solo debía frenar.

Entrar en una sala ya encendida no tiene regla de oferta. Las luces no se apagan al bajar el estado. Si la sala ofrece el gesto que la encendió, la bajada no existe. Si ofrece el gesto más bajo, ella ve la sala de la llevada y recibe el diez, sin una frase que explique el cambio. «Volver a ver piedras no es volver a ser pequeña» es el principio correcto y no es una regla de qué pieza aparece. Sin esa regla, o se humilla con un retroceso mudo o se finge que el estado manda cuando la sala no lo obedece.

Los problemas de dos pasos fallan dos veces y se cierran con un paso. No se dice si esos fallos bajan el estado de las cuentas que ya estaban firmes. Si bajan, un cuento castiga un cimiento. Si no bajan, el problema de dos pasos no tiene estado, y la fila 27 de la tabla de pedagogía es decorativa. Otra vez 29 filas contra 81 ids, y un tercer objeto —el problema— sin sitio en el enum.

M72 dice que los grupos de 10 «deben ir rápido» si las decenas están firmes, y que si no van rápido se vuelve a M32. Rapidez sin umbral, y un salto de muchos ids hacia atrás que «solo se baja uno» no permite. Es un hueco escrito como consejo.

## 4. Qué no debe inferir, y dónde el texto ya infiere

No debe inferir emoción, postura del cuerpo, inteligencia, trastorno, comparación, carácter, ni que la hora o la inclinación expliquen el resultado. No debe llamar dependencia a pedir el ejemplo. No debe escribir «frustrada» en ningún sitio. Eso, como prohibición, está claro. El texto no la cumple.

El apartado se llama «Señales de frustración que el juego sí puede ver». La frase siguiente dice que el juego no ve la frustración. El título ya la ha visto. «En el aula suelen ir antes de que una niña deje de intentar» importa una lectura de patio escolar y la deja pegada a los eventos. Quien implemente el apartado hereda el título, no la negación.

«Cansancio» se usa como causa. El GDD define unos hechos visibles y luego llama al corte «corte por cansancio». Si cansancio fuera solo el nombre de la disyunción, no podría aparecer en «es cansancio o hueco». Esa frase, en el tramo de apertura, elige entre dos interiores que el aparato no ve. Devolver piezas «se toma como cansancio o como esto sobra, no como rabieta». Se ha descartado una inferencia y se han afirmado dos. «Está trabajando», cuando las piezas se mueven, es otra. «No como falta de interés», al abandonar, también. Negar un motivo no es quedarse en el hecho. El hecho es: salió, o devolvió tres piezas, o hubo dos fallos. El motivo sobra.

«Sumar ya no da miedo» es puerta del círculo. «Hacer dieces tiene que ser fácil» es puerta de la llevada, al lado de otra frase que sí sería operativa (el bloque anterior firme). «Fácil» y «miedo» no tienen id. «Una de las difíciles para ella» compara a la niña consigo misma sin decir el cálculo, o con un orden de dificultad que nadie ha declarado. M72 infiere que, si las decenas están firmes, los grupos de 10 van rápido, y si no van rápido el cimiento anterior es falso. Eso es leer un carácter del gesto —«esto ya lo sabía, luego si tarda es que no»— y saltar de sala.

«Evita una sala» infiere intención. No entrar no es evitar. La sala puede no estar elegible, puede estar empañada por el techo, puede no haber cabido en una sesión de siete minutos. El capítulo dice que no se infiere miedo ni pereza, y a continuación deja que el padre baje el techo «si esa sala está demasiado pronto». Demasiado pronto es el juicio que el juego dijo no hacer, encargado al padre sin un criterio. «No se insiste esa noche» añade un tiempo del día.

La jugadora tipo «se frustra con facilidad». Es una frase sobre nadie en concreto y aun así es un rasgo. El resto del capítulo prohíbe guardar rasgos. No hace falta un rasgo para diseñar el corte a los dos fallos. La frase sobra y empuja a leer cada devolución como confirmación del retrato.

El dedo del padre es la inferencia más grave, porque se presenta como telemetría. El juego no puede verlo. La frase que se le muestra afirma que ha ocurrido. Se le pide que no señale, y eso puede decirse siempre, como consejo fijo, sin pretender que el registro distinga dedos. Decir «mañana cuenta como ayuda» después de un acierto que el aparato vio como sola es falsificar el otro día. Es exactamente lo que se prohíbe cuando se le impide marcar a mano «esto ya lo sabe»: alterar sola. Aquí lo altera el texto, en la otra dirección, con la misma falta de evidencia.

«Ha acertado despacio para ella» infiere una norma personal que aún no se puede calcular, y la pone en la única pantalla que un adulto va a creer. El propio capítulo dice que en esa pantalla no hace falta la palabra lento y que no mira tiempos como boletín. La frase está en la lista de frases que el juego puede darle. Las dos páginas no pueden ser ciertas.

«El error de hoy es siempre el mismo» usa «siempre» para un día. Eso es una inferencia de rasgo de error con N igual a uno. Matemáticas pide una firma repetida y un discriminador. La frase del padre se adelanta.

La edad es una inferencia latente. No hay fecha de nacimiento. «La edad no sube de nivel» está escrito. También está escrito un camino de 6 a 7 y un techo de 8 a 10. Sin edad, o el techo se abre solo por predecesores firmes —y entonces la edad es un adorno que alguien acabará comprobando mal—, o no se abre nunca, porque el padre solo puede frenar, no abrir un tramo por edad. Las dos implementaciones caben en el texto. Una de ellas infiere la edad a partir del saber, que es la comparación que se prohíbe. Hay que decir que la edad no es una entrada.

«Encima de la cara» infiere una escena con un nombre. Aunque luego se niegue, el nombre es lo que va a salir en un resumen exportado «en crudo, sin conclusión». El crudo con ese nombre ya es la conclusión. Si el resumen existe, los cubos tienen que llamarse como medidas del aparato, o no exportarse. El capítulo de pedagogía permite el crudo en el resumen y lo veta en la pantalla habitual. El atajo queda abierto: quien quiera la conducta de la niña, exporta.

## 5. Papel del padre

### Qué frases ve

El capítulo da una lista de hechos, no un selector. Puede haber varias ciertas el mismo día: dudó y falló, la sesión se cortó, salió, y una sala no se abrió. «Una o dos frases» no dice cuáles ganan. Sin prioridad, el programador elige las más llamativas, que son las de fallo.

Estas no se pueden mostrar tal cual:

- «Ha acertado despacio para ella en este paso.» Exige una mediana que no existe y contradice el boletín prohibido.
- «Ha dudado y ha fallado.» «Dudado» es una etiqueta. El hecho, si se quiere decir, es motor: ha soltado la pieza y la ha vuelto a coger. Y solo si eso es verdad según la regla de los 3 s, no según un ánimo.
- «El error de hoy es siempre el mismo: se olvida de romper la decena.» «Siempre» miente si no hay N ni discriminador. El ejemplo es de un gesto que el primer jugable no tiene. No hay mapa de error_id a frase. Matemáticas tiene decenas de firmas. El padre recibe una.
- «Hoy no ha entrado en el Mercado. La sala sigue abierta. No hace falta entrarla esta noche.» La primera oración es una deuda. La última usa la noche. Si ella la lee, el capítulo ha hecho lo que prohíbe: insistir.
- «Si la pieza va adonde señala tu dedo, mañana cuenta como ayuda, no como sola.» Afirma un sensor que no existe.

Otras frases de la lista sí dicen hechos y el gesto siguiente, y se pueden leer en voz alta sin nombrar a la niña: la torre no ha perdido luz; lo hecho está guardado; esto no es una nota; si pregunta, que enseñe cómo ha hecho el diez. Esas pueden quedarse. La lista no está cerrada mientras las otras sigan al lado, ni mientras otro texto pueda acortar la lista por su cuenta. Hace falta un orden de prioridad y un máximo de dos, y cada frase tiene que ser segura si una niña de 6 años la lee por encima del hombro.

No está dicho qué ve si no hay nada que contar: el primer día, una sesión de quince segundos que no llegó a abrirse, un día en que solo decoró la torre. Silencio, o una frase fija de «no es una nota». Si no se elige, aparecerá un vacío que alguien rellena con un resumen de tiempos.

### Qué puede cambiar

Puede poner un techo. La lista del GDD y de pedagogía tiene cinco frenos: hasta 20, sin llevada, sin mercado, sin centenas, sin el signo de por. El capítulo de matemáticas tiene ocho cortes, por ids, que no coinciden con esos cinco. «Hasta 20» puede ser M22 o M29. «Sin llevada» puede dejar el pergamino sin llevada o cortar antes de las decenas. «Sin el signo de por» no dice si esconde el jardín o solo el signo. «Sin mercado» no dice si bloquea el círculo. Dos listas, ningún mapa. El padre cree que frena un bloque. El juego puede estar frenando otro.

«El techo solo frena o se mantiene» se puede leer como «no salta cimientos» o como «una vez puesto, no se quita». La segunda lectura, con el PIN olvidado, es un candado permanente. No está dicho que pueda quitarse. No está dicho que quitarlo no abre lo que aún no está firme: solo deja de esconder lo que ya podría ofrecerse. Sin esas dos frases, o el techo es irreversible o al quitarlo se salta un cimiento. Las dos son malas. Ninguna está cerrada.

No puede marcar un paso como sabido. Eso está bien y hay que conservarlo. No puede cerrar acertijos, apagar luces ni quitar adornos. También está bien. No está dicho si puede cambiar el PIN, borrar el registro, alargar la sesión o forzar el ejemplo. Si no se dice que no puede, podrá, porque la pantalla existe y alguien añadirá un ajuste «útil».

Exportar un resumen a mano no está definido. Puede ser copiar las frases o generar un fichero. El capítulo dice que el resumen son las frases, no puntuaciones, y que la hora y la inclinación, si salen, salen en crudo y solo en ese resumen. Eso es un boletín diferido. O el resumen es exactamente las mismas dos frases de la pantalla, sin hora y sin postura, o es un segundo producto que el capítulo aún no ha diseñado. Hoy es las dos cosas.

No hay regla de un solo jugador. «Lento para ella» y el otro día suponen una sola mano. Un hermano en la misma tableta pudre el libro de ítems. No hace falta detectarlo. Sí hace falta escribir que el aparato no distingue personas y que el diseño no promete hacerlo.

### Si el PIN se olvida

No está diseñado. Ni en el GDD ni en el capítulo de pedagogía hay longitud, reintento, PIN de fábrica ni recuperación. No se dice qué pasa al olvidarlo.

Eso no es un detalle de pantalla. Es un agujero de cuidado. Si olvidar el PIN borra el progreso para «empezar de nuevo», se apagan luces que el castillo prometió no apagar. Si olvidarlo bloquea el juego, se castiga a la niña por un secreto del adulto. Si no hay recuperación, el techo que ya estaba puesto sigue para siempre y nadie puede leer las frases ni quitar el freno. Las tres salidas son posibles porque ninguna está escrita. La única que no humilla es: la niña sigue jugando, las luces y el techo ya guardado siguen, no hay borrado, y la pantalla del padre permanece cerrada. Un cambio de PIN, si algún día existe, no toca el progreso. Mientras eso no esté en el documento único, el PIN es una trampa con forma de ajuste.

## Decisiones que el documento único debe cerrar

1. La observación dura 3 sesiones completas. En esas 3 no se sube a frágil, ni a firme, ni a suelto, y no se baja ningún estado. Sin ver pasa a aprendiendo si ella arrastra el modelo. Al terminar las 3, los aciertos de la observación no se aplican. Se empieza a contar desde la sesión 4.
2. Otro día es otra fecha local, no 24 horas. Un acierto sola de hace más de 14 fechas locales no sirve para subir. No baja el estado y no apaga luces.
3. Firme, además de sola y en otro día, exige 3 ítems distintos del banco de ese id, ninguno igual al ejemplo enseñado, en al menos 2 fechas, como máximo 2 ítems por fecha, sin ayuda, sin duda y sin ser cierre. Si el banco tiene discriminador, uno de los 3 es ese discriminador. Un mismo ítem no puede ser más de la mitad de los aciertos que alimentan la subida. El estado vive en el id M, no en las 29 filas. M12 firme no marca M13 firme.
4. El primer acierto sola de ese micropaso en esa fecha no sube a firme ni a suelto. El tramo «ya sabe» no es acierto de subida y no consume ese cupo.
5. Duda por sostener es pieza quieta: desplazamiento menor de 24 px durante más de 8 s. Eso no sube, porque es duda. Lento no es eso. Lento no se calcula hasta tener 6 aciertos sola de ese id. Lento es tiempo con la pieza en movimiento mayor que 1,5 veces la mediana de esos 6. Mientras no haya 6, lento no existe y no bloquea nada. Lento no impide frágil ni firme. Lento impide suelto. La frase que dice que despacio no sube de nivel no se implementa.
6. Suelto exige estar firme, sin piezas de apoyo, en 2 fechas distintas de la fecha en que pasó a firme, sin adivinanza, y con manipulación menor o igual que esa mediana. Con menos de 6 aciertos sola, suelto es imposible. El primer fallo sin duda de esa prueba no baja. Si el fallo es con duda, baja uno y la prueba no se repite en esa fecha.
7. Como máximo una bajada por micropaso y fecha local. El segundo fallo con duda del borde corta y enseña el gesto, y no baja otra vez. Suelto no llega a frágil en la misma fecha.
8. Los tropiezos de «ya sabe» no cortan, no bajan y no suben. No se implementa el corte por dos tropiezos de ese tramo.
9. El cierre, la repetición del modelo y el acertijo no cambian ningún estado de aritmética.
10. Cada id declara sus predecesores. No es el número anterior. Los nombres no tienen arista de bloqueo. Los acertijos no tienen arista hacia la aritmética. La llevada no se abre si M23, M24 o M25 no están firmes. El préstamo no se abre si, además, M26 o alguno de M38–M40 no está firme. No se abre ese bloque el mismo día en que se nombra la conmutativa.
11. «Fácil», «miedo» y «difícil para ella» no son entradas. El círculo no espera al mercado si el techo «sin mercado» está puesto. Ese techo no esconde el círculo.
12. La hora y la postura no son argumentos de ninguna función, ni antes ni después de 8 sesiones. No salen en frases ni en el resumen. Si el documento único no copia los ángulos del cubo, la postura no se anota. El cubo, si se anota, no se llama con una escena del cuerpo.
13. Menos de 15 s sin toque desde el patio no crea sesión. 20 s sin toque con la pieza ya presentada es abandono. A los 420 s entre turnos no se abre otro ítem de borde. A los 480 s se entra en cierre al soltar. Un arrastre no se corta. Tiempo de juego es la suma desde el primer toque de pieza hasta el último, sin el patio.
14. Se guardan por separado tiempo al primer toque, tiempo con desplazamiento de al menos 24 px, y pausas sin toque de al menos 4 s. No se suman en un solo «lento». Tres pausas de ese tamaño en el mismo intento cortan lo nuevo. Una no es un fallo y no corta.
15. Deshacerse antes de 3 s es duda y no cuenta como devolución. El corte por devolución exige 3 devoluciones al origen en el mismo intento, fuera de esa ventana. Una devolución no corta, tampoco en el primer jugable.
16. Abandono es salir de la sala, cerrar la tableta o esos 20 s. No baja estado y no es un fallo. No se anota falta de interés ni cansancio como causa: se anota el identificador del evento.
17. Ayuda usada significa solo que el ejemplo estaba en pantalla, o que el tramo es la repetición del modelo, o que el cierre está en el peldaño de ejemplo. No hay detección de dedo ajeno y no se informa de ella. Aprendiendo lleva ejemplo al lado. Frágil lleva piezas a la vista y ejemplo ausente. Firme lleva ejemplo ausente. Suelto lleva piezas de apoyo ausentes. Volver un peldaño no se anuncia.
18. Mismo error exige el mismo error_id en 2 ítems distintos y 2 fechas, y solo si el discriminador de esa familia ya se ha visto. Hasta entonces no hay frase y no hay techo de frágil. El techo, si llega, baja como máximo un estado por fecha y no salta de suelto a frágil. Mientras esté puesto, el sucesor no se abre. 32−17 sin un 32−15 no elige frase.
19. Un intento escribe como máximo una de estas etiquetas: duda, fallo, corte. No las tres. La pieza quieta no cuenta además como pausa ni como lento.
20. Parecido es el mismo id y otro ítem. Cada tercer parecido es el discriminador, si esa familia lo tiene. El tramo «ya sabe» es el id firme o frágil cuyo acierto sola es el más antiguo. Uno por sesión.
21. Una sala se dice evitada solo si era elegible y, en 3 de las últimas 5 sesiones abiertas, no se entró. Antes de eso, silencio. La frase no dice «no ha entrado» ni «esta noche». Dice que la sala sigue abierta.
22. El padre ve como máximo dos frases, con prioridad escrita, seguras si se leen en voz alta. En esa pantalla no aparecen: dudado, despacio, lento, siempre, frustrada, no ha entrado, retrasada, noche, tumbada. Si no hay hecho que contar, una sola frase fija: esto no es una nota.
23. El padre puede poner y quitar cualquiera de los cinco techos del GDD. Quitar un techo no salta cimientos: solo deja de frenar. Los ocho cortes de matemáticas se mapean a esos cinco en el documento único, o se descartan. No quedan las dos listas. «Sin el signo de por» esconde × y ÷, no los grupos. «Sin mercado» no esconde acertijos ni el círculo.
24. El PIN olvidado se cierra así: no hay PIN de fábrica; olvidarlo no borra luces, estados ni techo; no hay recuperación que vacíe el progreso; la niña sigue jugando; la pantalla del padre queda cerrada. Un cambio de PIN, si existe, no toca el progreso. Si no existe, se dice.
25. La edad no es una entrada. No hay campo de edad. M78 a M81 se abren por predecesores firmes y por no estar frenados. «8 a 10» no se comprueba.
26. Un aparato, una jugadora, y el documento dice que no distingue a otra persona. Entrar en una sala encendida ofrece el gesto más alto de esa sala que el estado y el techo permiten, sin frase de retroceso.
