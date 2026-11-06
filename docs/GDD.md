# Documento de diseño — Estrella y el Castillo de los Números

Este archivo es el diseño. Si un capítulo viejo, un spec o un prompt dice otra cosa, manda esto. Los capítulos de `docs/expertos/` y las críticas de `docs/criticas/` son el historial de la primera pasada, no una segunda biblia.

Idioma de pantalla: español de España. Una frase, hasta doce palabras, o silencio. No hay preguntas que se contesten con la boca.

## 1. Qué es

Estrella es aprendiz de magia de las luces. En el dibujo parece de unos once años, no de seis y no adulta. Melena a la mandíbula, flequillo recto, sin trenza y sin coleta. Piel `#E2A56B`. Pelo `#4A2E24`. Ojos `#3F2A22`. Boca `#C46A52`. Capa `#C85A32`. Túnica `#F4E2C0`. Broche de tela `#F2C14E` en el cuello, no en el pecho. Sin corona, sin varita, sin Disney.

Tres caras y ninguna más: curiosa, contenta, pensando. No existe celebrando. Un fallo no le cambia la cara. La pieza que vuelve es la señal de fallo. Hasta que haya tres poses que se distingan a 96 px, no se usa la cara como señal.

Su magia no adivina. La lámpara se enciende cuando las manos hacen el gesto. Escribir el número, si aparece, es después de la luz.

La niebla es una cortina crema `#E7DCC8`, sin ojos, sin voz y sin cuerpo. No crece si no se juega. No se nombra miedo, monstruo, oscuridad ni peligro.

El castillo solo gana luz. No hay vidas, reloj en pantalla, marcador, estrellas vacías ni sonido de error.

## 2. Aparato y coordenadas

Fire 7, 1024×600, horizontal bloqueado. Si el sistema pide vertical, el juego no gira: sigue en horizontal, letterbox, piezas sin rotar.

Área útil: x 48–976, y 24–552. Los 48 px de abajo no llevan nada que se toque.

Origen arriba a la izquierda. Un rectángulo es `x, y, w, h` en píxeles de ese viewport.

Un dedo. El segundo dedo no suelta la pieza del primero, no pulsa atrás y no abre una sala. Se ignora.

Soltar vale si el centro de la pieza queda a 36 px o menos del centro del hueco. Ningún hueco se preilumina. No hay botón de listo.

Un toque quieto, sin mover 24 px, no es un intento. La piedra no parece un botón: es irregular, el botón es un arco. Si no se distingue, no se publica esa pieza.

Sin audio o con el mute, el acierto no espera a la campanada. Bastan el pulso de 1,2 s y el texto 4 s.

## 3. Reloj interno

No se dibuja. No corta un arrastre.

- Tiempo de juego: desde el primer toque de pieza hasta el último, sin el patio.
- A los 420 s entre turnos no se abre otro ítem de borde.
- A los 480 s, al soltar la pieza que ya tiene en la mano, se entra en el cierre. Si a los 400 s sigue en el collar y la pieza avanza, se respeta la mano hasta la suelta.
- 20 s sin toque, con la pieza ya presentada y no en la mano: abandono. En la misma sentada se va al cierre. Si la tableta se cerró, se guarda y no se inventa el acierto. No son dos caminos a la vez.
- Menos de 15 s en una sala sin tocar una pieza no abre sesión y no cuenta como sala evitada.

## 4. Sesión

Orden, si nada se tuerce:

1. Una que ya sabe. Los tropiezos de aquí no cortan, no bajan y no suben. Se ayuda hasta el acierto.
2. Idea de hoy, 20 s. Si ella coge una piedra, el modelo cede y ya es su turno. No se dice «espera».
3. Tres intentos de borde. Cuatro solo si van sin fallos y sin corte. Al segundo fallo se salta al cierre. No hay tercero.
4. Un acertijo, solo si no hubo corte. No cambia estados de aritmética.
5. Cierre: una que puede hacer, ella suelta la pieza. Ese acierto no sube de estado.
6. Un adorno, entre dos, los dos válidos. Lo coloca ella.

Frase del corte, la única: «Seguimos con una que ya sabes.»

El acierto del cierre lo hace ella. Estrella no coloca la última pieza. No se dice que el acierto es de las dos.

Menos de 15 s sin toque desde el patio no crea sesión.

## 5. Primer jugable, pantallas

Nombre único del objeto: nido. No se dice caja, losa ni cuenco.

### 5.1 Patio

Tres cosas, 160×160, y ninguna más el primer día.

| Cosa | Rectángulo |
|---|---|
| Nido (Piedras) | 160, 180, 160, 160 |
| Collar (Acertijos) | 432, 180, 160, 160 |
| Torre | 704, 180, 160, 160 |
| Campana | 880, 24, 96, 96 |

La campana es solo ese rectángulo. Pulsación de 1,5 s. No mide 48 px. Un dedo que coge una ventana no la alcanza.

Lo que no está abierto no se dibuja. No hay candado ni hueco gris. Cuando más adelante haya más salas, como máximo cuatro ventanas de 96 px por fila, aire 24 px. Ocho de 96 no caben en una fila y no se prometen.

Con un cierre pendiente, el patio muestra la bandeja de ese cierre o las ventanas, no las dos.

### 5.2 Nido

| Zona | Rectángulo |
|---|---|
| Marco del nido | 80, 108, 500, 220 |
| Hueco columna c, fila r | x = 100 + c×92, y = 128 + r×92, 80×80. c = 0..4, r = 0..1 |
| Celda del montón c, r | x = 640 + c×96, y = 120 + r×96, 96×96. Dentro, piedra de 72. c = 0..1, r = 0..2. Seis piedras |
| Estrella | 848, 280, 112, 150 |
| Banda de frase | 96, 468, 832, 56 |
| Paño del ejemplo, si está | 80, 24, 200, 72. No se toca. No tapa un hueco de ella |

En su turno hay un solo nido que su dedo llena. El andamio de 7 y 3 son los huecos vacíos, no piedras marcadas. No los dos: si brillan las que hay que mover, se acierta sin mirar el nido.

El pulso ámbar, 1,2 s, nace en el instante de la suelta válida, en el borde del nido de ella. No convive con otro pulso. Resetear el paño del ejemplo se apaga en 0,4 s, sin ese pulso, para que no parezca que ha roto el castillo.

Pieza rechazada: vuelve en 0,4 s, en silencio. El paso de un nido ya encendido al nido del intento siguiente no usa ese retorno.

Oncena, la primera vez: silencio, cara curiosa, la piedra vuelve. No hay frase.

### 5.3 Collar

Pantalla propia. Fundido. No hay cordón de camino al salir del nido.

| Zona | Rectángulo |
|---|---|
| Cordón | 96, 220, 640, 96 |
| Gancho i, i = 0..4 | x = 120 + i×120, y = 228, 80×80 |
| Arcón | 800, 180, 160, 220 |

En el cordón: piedra, estrella, piedra, estrella, hueco. La siguiente es una piedra, colgada desde el arcón. No hay dos botones. No se dice que el hueco pide estrella. No es luz y oscura.

### 5.4 Torre

Pared ya completa. Sin ganchos vacíos. El farol se suelta en 704, 180, 160, 160. Ahí se ve entero. Un segundo adorno no se dibuja hasta el día en que se gana. No hay silueta de lo que falta. No hay rejilla y pared libre a la vez: es pared libre.

El farol se gana por un solo hecho: ella ha encendido el cierre con su dedo en esa sentada. También si el borde se saltó. No se gana por no haberse equivocado.

### 5.5 Padre

Misma campana. PIN de cuatro cifras que él elige la primera vez. No hay PIN de fábrica. No hay cambio de PIN en esta versión. Olvidarlo no borra luces, estados ni techo. No hay recuperación que vacíe el progreso. La niña sigue jugando. La pantalla del padre queda cerrada.

En el primer jugable el padre ve una sola frase, o ninguna: «Esto no es una nota.» Estrella no está en esa pantalla. Ella no dice padre, PIN ni aparato.

## 6. Cuatro finales del primer día

Números, en este orden, si nada se tuerce:

1. Ya sabe: tres piedras, las junta. Un hueco con tres. No es el nido de diez.
2. Idea: Estrella llena el nido de diez en el paño. Ella repite 7 y 3 en su nido.
3. Borde: 8, luego 5, luego 9. Cada uno completa diez.
4. Collar: piedra, estrella, piedra, estrella. Ella cuelga una piedra.
5. Cierre: nido con nueve, ella pone una.
6. Farol, entre ámbar y terracota, los dos válidos.

### Si falla dos veces en el borde

El segundo fallo no enciende. Silencio. La pieza vuelve. Frase: «Seguimos con una que ya sabes.» No hay collar. No hay farol todavía. Cierre: el nido de nueve, ella pone una. Después el farol. Entre el segundo fallo y esa luz no hay brillo nuevo ni puerta de premio.

Los fallos de «ya sabe» no cuentan para este corte.

### Si se cansa

Señales que cortan lo nuevo, y no se nombran: tres devoluciones al origen en el mismo intento, fuera de la ventana de 3 s; o tres pausas de 4 s sin toque en el mismo intento; o el segundo fallo. Una devolución no corta. Una pausa no corta.

No se le saca la pieza de la mano. Al soltar, si el corte ya estaba pedido, se va al cierre con la misma frase. El juguete no se bloquea con un cartel.

### Si se va a medias

Se guarda en cada suelta. No se inventa el acierto. Al volver, otra fecha o la misma, no está el borde a medias. Está la cuenta que ya sabe. Lo encendido sigue encendido.

### Día siguiente

Misma entrada, y solo esta: «Me alegro de verte.» «Tus luces siguen encendidas.» «No hay que recuperar nada.» Luego una que ya sabe. No se dice «la cinta sigue» si el adorno fue un farol. No se dice «te echaba de menos» ni «se ha apagado».

Día 2, mismo tablero, otros números: ya sabe, cuatro piedras; idea, 6 y 4; borde, 9, luego 2, luego 8; collar igual; cierre, nueve y una.

Si en quince segundos no toca una pieza, no hay saludo y no hay sesión.

## 7. Voz del primer jugable

Solo estas. Lo demás no se graba todavía. Si falta el fichero, se ve el texto.

| Id | Cuándo | Frase |
|---|---|---|
| V01 | Primera llegada, si ha tocado una pieza | Hola. Soy Estrella. |
| V02 | Después, una vez | Mi magia no adivina. |
| V03 | Entrar al nido | Aquí las piedras se juntan y se separan. |
| V04 | Corte | Seguimos con una que ya sabes. |
| V05 | Volver otro día | Me alegro de verte. |
| V06 | Volver otro día | Tus luces siguen encendidas. |
| V07 | Volver otro día | No hay que recuperar nada. |
| V08 | Disco lleno, si cabe texto | Seguimos. Hoy no se ha guardado. |

No se dice: mal, incorrecto, eres un genio, casi, date prisa, esto es fácil, otra vez, has pagado, ya sabes hacer el diez, cerramos con una fácil, no pasa nada, ni una frase con ¿. La duda no hereda frase de fallo. El acierto de persona no existe. La oncena, la primera vez, no tiene frase.

Más adelante, cuando esa sala exista, y no antes: «Me llevo una.» «Pido prestada una decena.» «Estas monedas son del juego.» «No se compra de verdad.»

## 8. Luz, fallo, duda

Un intento escribe como máximo una etiqueta: duda, fallo o corte. No las tres.

Duda, y no sube:

- Suelta a menos de 24 px del origen tras tenerla 1 s.
- Cambia de destino.
- La pieza está quieta, menos de 24 px, más de 8 s. Eso no es además una pausa ni un lento.
- Se desdice antes de 3 s. Eso no es una devolución.

Devolución: vuelve al origen después de 3 s, ya había salido. Tres en el mismo intento cortan lo nuevo. Una no corta.

Fallo: suelta, habiendo movido, en un sitio que no enciende. La segunda pieza que el material rechaza en el mismo intento es el fallo. Un método equivocado dejado 3 s, sin desdecirse, es fallo a la primera.

Ayuda usada significa solo esto: el paño del ejemplo está en pantalla, o el tramo es la repetición del modelo, o el cierre está en el peldaño de ejemplo. No hay detección de otro dedo de otra persona.

Andamio, sin anunciarlo:

- Aprendiendo: ejemplo al lado.
- Frágil: piezas a la vista, ejemplo ausente.
- Firme: ejemplo ausente.
- Suelto: sin piezas de apoyo.

## 9. Algoritmos

Locales. Ella no los ve. No se le dice que ha subido ni que ha bajado. La edad no es una entrada. No hay campo de edad.

### 9.1 Observación

Las tres primeras sesiones completas solo observan. No se sube a frágil, ni a firme, ni a suelto, y no se baja. Sin ver pasa a aprendiendo si ella arrastra el modelo. Al terminar las tres, esos aciertos no se aplican. Se empieza a contar en la sesión 4.

Desde la sesión 1 sí mandan el cierre en acierto, el corte a los dos fallos del borde y el corte por cansancio. Enseñar el gesto si duda y falla es ayuda, no un juicio, y también manda desde el día 1.

### 9.2 Estados

Sin ver, aprendiendo, frágil, firme, suelto. El estado vive en el id del micropaso, no en la sala. M12 firme no marca M13 firme. Solo se sube uno. Solo se baja uno. El suelo, una vez vista la idea, es aprendiendo. Bajar no quita luces ni adornos.

Otro día es otra fecha local, no 24 horas.

Sube:

- A aprendiendo: arrastra el modelo.
- A frágil: acierta sola, hoy, moviendo piezas, sin ayuda y sin duda. No vale el cierre ni la repetición del modelo.
- A firme: 3 ítems distintos del banco de ese id, ninguno igual al ejemplo, en al menos 2 fechas, como máximo 2 ítems por fecha, sin ayuda, sin duda y sin ser cierre. Si el banco tiene discriminador, uno de los 3 es ese. Un mismo ítem no es más de la mitad de los aciertos que alimentan la subida. Un acierto solo de hace más de 14 fechas no sirve para subir. No baja el estado y no apaga luces.
- A suelto: ya firme, sin piezas de apoyo, en 2 fechas distintas de la fecha en que pasó a firme, sin adivinanza, y con el tiempo de manipulación menor o igual que su mediana. Hacen falta 6 aciertos sola de ese id. Si no hay 6, suelto es imposible.

El primer acierto sola de ese id en esa fecha no sube a firme ni a suelto. El tramo «ya sabe» no consume ese cupo.

Lento no existe hasta esos 6 aciertos. Lento es tiempo con la pieza en movimiento mayor que 1,5 veces la mediana de esos 6. Lento no impide frágil ni firme. Lento impide suelto. «Despacio no sube de nivel» no se implementa.

Baja:

- Como máximo una bajada por id y fecha.
- Si duda y falla: baja uno y se enseña el gesto. Si ya estaba aprendiendo, se queda y vuelve el ejemplo.
- El segundo fallo con duda del borde corta y enseña el gesto, y no baja otra vez.
- Suelto no llega a frágil en la misma fecha.
- El primer fallo sin duda de la prueba de suelto no baja. Si es con duda, baja uno y la prueba no se repite esa fecha.
- Un fallo aislado sin duda no tira un cimiento firme.

El cierre, la repetición del modelo y el acertijo no cambian ningún estado de aritmética.

### 9.3 Error sistemático

Mismo `error_id` en 2 ítems distintos y 2 fechas, y solo si el discriminador de esa familia ya se ha visto. Hasta entonces no hay frase y no hay techo. El techo, si llega, baja como máximo un estado por fecha. Mientras esté puesto, el sucesor no se abre.

32−17 no separa errores. El discriminador es 32−15: bien 17, girar 23, olvidar el descuento 27. Sin el discriminador no se elige frase.

### 9.4 Qué toca

Cada sesión, desde la cuarta:

- Ya sabe: el id firme o frágil cuyo acierto sola es el más antiguo. Uno.
- Borde: el id en aprendiendo o frágil con predecesores firmes, el más antiguo. Si no hay, el siguiente sin ver cuyo predecesor está firme.
- Repaso: va dentro de «ya sabe», no es un tramo extra.
- Acertijo: uno cuyo cimiento de compañía está al menos en aprendiendo, y que no esconda una cuenta por encima del borde.

Parecido, si acertó dudando: el mismo id, otro ítem. Cada tercer parecido es el discriminador, si existe.

Un paso nuevo solo si cada predecesor está firme. Los predecesores se declaran en el id. No es «el número anterior». Los nombres no bloquean. Los acertijos no tienen arista hacia la aritmética.

No se abre un bloque el mismo día en que se nombra la conmutativa.

### 9.5 Qué puede cambiar y qué no

Pueden cambiar: el id, el tamaño de los números dentro de ese id, si el ejemplo está, la frase de ayuda de ese `error_id`, si hoy hay idea nueva, y la duración al cortar.

No pueden: quitar luces, poner cronómetro, cerrar acertijos, enseñar un marcador, enviar datos fuera, usar la hora, usar la inclinación, usar la edad.

La hora y la inclinación se anotan y no son argumentos de ninguna función. No salen en frases ni en el resumen. No se llaman sentada, acostada, noche ni tumbada.

### 9.6 Sala evitada

Solo si era elegible y, en 3 de las últimas 5 sesiones abiertas, no se entró. Antes, silencio. La ventana no lleva marca. La frase del padre, si cabe en el cupo de dos, es: «La sala sigue abierta.» No dice «no ha entrado».

## 10. Telemetría

Un aparato, una jugadora. No se distingue a otra persona. No hay cámara ni micrófono. No sale del aparato.

Se guarda en cada suelta y en cada cambio de estado, en `user://progreso.json`. Si no cabe en disco: no se inventa el acierto, no hay sonido de error, y si cabe texto se ve V08. Lo que ya estaba guardado no se toca.

### 10.1 Evento de intento

```
{
  "id": "M23",
  "item": "7+3",
  "fecha": "2026-11-06",
  "t0": 0,
  "primer_toque_ms": 0,
  "moviendo_ms": 0,
  "pausas_4s": 0,
  "etiqueta": "duda|fallo|corte|acierto|nada",
  "sola": true,
  "ejemplo": false,
  "cierre": false,
  "duda": [],
  "devoluciones": 0,
  "error_id": "",
  "tilt": "plana|de_pie|encima|desconocida"
}
```

`duda` es una lista de: `origen`, `destino`, `quieta`, `desdice`. Como máximo una etiqueta de juicio.

Tiempos separados, no sumados en un «lento»: hasta el primer toque; con desplazamiento de al menos 24 px; pausas sin toque de al menos 4 s.

### 10.2 Inclinación

Una muestra por segundo, mediana de cinco, al empezar la sesión y si el cubo cambia. No es la postura del cuerpo.

- `plana`: el eje que sale de la pantalla es el mayor y la pantalla mira hacia arriba.
- `encima`: ese mismo eje es el mayor y la pantalla mira hacia abajo.
- `de_pie`: el mayor está en el plano de la pantalla.
- `desconocida`: magnitud menor de 5, o ruido.

No cambia sala, tiempo ni frase.

### 10.3 Sesión

Hora local de inicio. Duración de juego, definida arriba. Salas abiertas. Sala propuesta y no entrada. Cierre pendiente, sí o no. Farol ganado, sí o no. Techos del padre. Estados por id. Fecha del último acierto sola por id. Contador de sesiones completas.

Eso es el plan que decide la vuelta. Si no está en el guardado, no se usa al abrir: se entra por una que ya sabe y no hay cierre pendiente.

### 10.4 Padre

Como máximo dos frases, en este orden, y solo si el hecho es de las sesiones ya contadas, no de la observación:

1. Si un sucesor no se abre por un error sistemático: «Seguimos con el gesto de antes.»
2. Si una sala se evita, según la regla: «La sala sigue abierta.»
3. Si no hay nada de eso: «Esto no es una nota.»

No aparecen: dudado, despacio, lento, siempre, frustrada, no ha entrado, retrasada, noche, tumbada, ni un número.

Techos, cinco, y solo estos. Ponerlos frena. Quitarlos no salta cimientos.

| Techo | Qué esconde |
|---|---|
| Hasta 20 | Decenas, centenas, llevada, préstamo |
| Sin llevada | Llevada y préstamo |
| Sin mercado | Mercado, masa, capacidad, billetes |
| Sin centenas | Tres cifras y céntimos que exigen el cien |
| Sin signo de por | Los signos × y ÷. No esconde los grupos ni el reparto con piezas |

«Sin mercado» no esconde acertijos ni el círculo. El círculo no espera al mercado.

## 11. Currículo

1º de Primaria, primer ciclo LOMLOE, recortado a lo que este castillo enseña con las manos. Lo que no entra se dice aquí, no se deja implícito.

No entran: millares, fracciones, negativos, tablas del 3, 4, 6, 7, 8 y 9, cuarto de hora, conversiones de unidades, media, probabilidad, gráfica con ejes, billetes de 20, 50 y 100, grado, simetría, porcentaje. El cuarto de hora no entra. Los meses de memoria no entran.

Billetes de 5 y de 10 solo en el techo, como papel de juego que se cambia por monedas. Frase de monedas, también ahí: «Estas monedas son del juego.» «No se compra de verdad.»

### 11.1 Números y operaciones

El mapa M01–M81 del capítulo de matemáticas sigue vigente en ejemplos, errores y discriminadores, con estas puertas y no otras:

- Llevada (M41) espera a M23, M24 y M25 firmes. No el mismo día en que se nombra la conmutativa.
- Préstamo (M44) espera además a M26 y a un pergamino sin salto (M38, M39 o M40) firme.
- Centenas esperan a las decenas.
- Céntimos que exigen el cien esperan a la centena. Los euros enteros no.
- Círculo (M65) espera a que sumar dentro del 10 esté firme. No espera al mercado.
- Signos × y ÷ después del gesto. Grupos del 2, del 5 y del 10. No se nombra la conmutativa de la multiplicación.
- Sobra (M81) es techo. No es un fallo. No se parte la piedra.

Estimación, hasta 20, en Acertijos: señala el montón que parece mayor y luego empareja. Si la fila larga engaña, el empareje manda. No es una resta.

Igual y no igual: dos bandejas. El igual no es una flecha. Un símbolo tapa un montón; ella iguala el otro lado y luego se destapa. Eso es el dato desconocido. No es una ecuación escrita.

### 11.2 Medida, espacio, datos y tiempo

Viven en Acertijos o en el Mercado, como juguetes. No hay esfera de doce números, ni regla con centímetros, ni ejes.

| Tema | Dónde | Gesto | No es |
|---|---|---|---|
| Longitud | Acertijos, cuando ya compara montones | Dos cintas alineadas por un extremo. Señala la que sobresale. Más tarde, cubrir una cinta con piezas iguales y contarlas | Las varillas del pergamino. El centímetro el primer día |
| Masa | Mercado, sin esperar a la centena | Balanza. Cuelga piezas hasta nivelar. Baja el lado que pesa más | La tableta no pesa |
| Capacidad | Mercado, misma puerta | Llenar con vasos iguales y contar vasos. Cabe más el que necesita más vasos | La caja de diez no es un litro |
| Hora | Acertijos, cuando cuente hasta 12 | Dos piezas gordas: la larga al 12 o al 6, la corta a la hora. En punto y y media | Cronómetro, cuenta atrás, reloj del patio |
| Ayer, hoy, mañana | Acertijos | Tres fichas en una tira. Coloca la de hoy | El calendario entero |
| Semana | Techo | Tira de siete, después de las tres fichas | Los meses |
| Figuras planas | Acertijos | Aparta círculo, cuadrado, triángulo y rectángulo. Luego recorre el borde con el dedo | Contar lados para que la luz espere un nombre. La sala Círculo no vale |
| Cuerpos | Acertijos | Empuja. La esfera y el cilindro cruzan una raya. El cubo se queda | 3D, giroscopio |
| Posición | Acertijos, escena fija | Suelta la pieza a la izquierda, a la derecha, delante, detrás, cerca o lejos de Estrella. La izquierda es la de Estrella, marcada | La columna de las unidades. Caminar por el patio |
| Instrucciones | Acertijos | Ordena dos o tres losas: coge, pon, enciende. El dedo recorre la buena sin pisar la mala | Un lenguaje de programación |
| Recuento | Acertijos, contar hasta 10 firme | Un palito por objeto. El quinto cruza el grupo. Lee cuántos hay de cada clase | El mismo gesto que contar piedras del nido |
| Pictograma | Acertijos, otro día | Apila una figura igual por objeto. Señala dónde hay más y lo comprueba emparejando | Sus aciertos, sus luces, sus días. Si la columna mide el saber, se tira |

Metro, kilo y litro son el nombre de después, cuando el gesto ya se ve. No hay conversiones.

### 11.3 Problemas con historia

Cuando la cuenta ya se hace con las manos. Un paso, con dibujo, y el juguete de esa sala. Dos pasos, techo, con los dos momentos dibujados. No hay «tenía algunas». No hay tres pasos.

## 12. Salas que vienen después

Misma pantalla útil. Cada una es una pantalla, no un pasillo.

**Espejo.** Un solo gesto: cruzar los dos montones. Origen 160, 200, 200, 160. Destino 560, 200, 200, 160. No hay un segundo gesto de borde de paño. Solo sumas. Si aparece una resta, no se cruza y no es un fallo trampa: no se ofrece.

**Círculo.** Tres montones, 160×140, en 96, 200; 400, 200; 704, 200. La cinta se suelta en la zona entre dos, no «alrededor». Se ve qué dos quedaron enlazados. Rodear con el dedo no es el gesto. Solo sumas, total como máximo 12, sumandos de 1 a 5.

**Pergamino.** Tres varillas, x 200, 420 y 640, y 140, 80×280. La cuenta soltada en la varilla de al lado vuelve. El salto es una estrella con lengüeta que ella arrastra a la varilla siguiente, un salto, no dos a la vez con dos sumandos. En el préstamo, las diez sueltas se ven en 200, 80, 400, 80, o ese día no se enseña el préstamo. «Me llevo una» es una decena que salta. No se dice «me llevo dos». La decena rota no se devuelve.

**Mercado, primer día de la sala.** Paño 96, 200, 280, 160. Monedas de 1 y de 2 en 420, 200, 280, 160. Cesto 740, 200, 160, 160. Se cubre un precio de 2 con una de 2 o con dos de 1. La de más vuelve a un sitio visible. Las diez monedas de céntimo no entran hasta que quepan con el paño, sin desplazar. Balanza y vasos son otra visita, no el mismo día que el primer euro.

**Jardín.** Como máximo cinco macetas de 120×100 en una fila, semilla de 48 dentro, bolsa 800, 300, 140, 120. La semilla de más se saca con el dedo. Diez semillas de 96 en una maceta no es una respuesta. Diez grupos se cuentan en la recta, no se plantan todos a 96 px.

**Tesoro.** Tres cuencos de 180×140. La gema de arriba se mueve a otro cuenco. La victoria no es la altura si las gemas no se cogen. No hay niños rivales. La sobra, en el techo, se queda en un cofre pequeño y no es un fallo.

**Torre, más adelante.** Los adornos que no caben enteros a 96 px pasan a un arcón. El arcón no muestra siluetas vacías. No hay rareza por partida perfecta.

## 13. Fuera

Multijugador, anuncios, compras, cuentas, diagnóstico, comparación, red, 3D en la tableta, vídeo en el APK, Vulkan, PIN de fábrica, cambio de PIN, recuperación que borre el progreso, preguntas orales, marcador disfrazado de pictograma, reloj de sesión, y cualquier frase que elogie a la persona o nombre una emoción de ella.
