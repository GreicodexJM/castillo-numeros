# UI y UX — Estrella y el Castillo de los Números

Este capítulo obedece a `docs/GDD.md`. Si una medida de aquí chocara con el GDD, manda el GDD. `BRIEF.md` fija el aparato. Los capítulos de expertos amplían el gesto; aquí se fija qué se ve, qué se toca y qué no se dibuja.

Idioma de toda la interfaz: español de España. Una frase, luego silencio. El texto se ve aunque haya voz. Si falta el audio, se ve el texto. La frase no se sustituye por un pitido.

Estrella no habla del padre, del PIN, de las notas ni del aparato. En su boca solo entran las frases ya cerradas en `docs/expertos/02-relato.md`. Este capítulo no inventa frases nuevas para ella.

## Lienzo

Diseño 1024×600, horizontal, pantalla completa. El área útil, con la barra de sistema, es 1024×552. El origen es la esquina superior izquierda de esa área útil. Los 48 px de abajo de los 600, si la barra aparece, quedan vacíos. Ahí no vive nada que ella deba ver ni tocar.

| Medida | Valor | Dónde |
|---|---|---|
| Área útil | 1024×552 | Toda la composición |
| Margen (blanco) | 96 px | Los cuatro lados del área útil |
| Rectángulo de contenido | x 96, y 96, 832×360 | Todo lo que ella debe tocar, menos la excepción de la campana |
| Botón | 96×96 px | Puerta, silencio, ventana, gancho, tecla del padre |
| Pieza | 96×96 px | Lado corto. La del turno puede crecer a 112 si el aire de 24 sigue cabiendo |
| Aire | 24 px | Entre dos controles que no deban pulsarse juntos |
| Frase | 32 px como mínimo, una línea | Banda de frase |
| Numeral, si el polvo lo dibuja | 48 px como mínimo | En el sitio de la luz, no en una casilla |

El blanco de 96 px es margen de pantalla, no un hueco de marcador. El aire de 24 px es la separación entre controles. No se confunde con la duda: soltar a 24 px o menos del origen, tras tener la pieza 1 s, es un gesto del registro, no un margen de maquetación.

Imán al soltar una pieza en un nido, una bandeja o un gancho: del orden de media pieza, 48 px. No se exige puntería de 8 px. Ese imán no enciende el único píxel correcto. No acerca la pieza a la respuesta.

## Una idea por pantalla

En cada pantalla hay una sola cosa que hacer, dicha por una sola frase.

Cabe en la pantalla: el juguete de ese turno, la frase, Estrella en un borde, y la puerta de vuelta si no estamos en el patio. No cabe un segundo objetivo, una pista al lado, un contador ni el mapa.

Si una frase del relato no cabe en una línea de 32 px dentro de su banda, la frase está mal asignada a esa banda. No se baja la letra. No se parte en un párrafo. Ocho palabras bastan. Doce es el tope del GDD.

El texto y la voz dicen la misma frase. El gesto, si Estrella lo hace, dice lo mismo. Con uno de los tres basta para seguir. Tocar la frase la repite. No hace falta otro botón de «oír» dentro de la sala. Estrella no repite en bucle: una espera larga, una repetición, y se calla.

La frase permanece al menos 4 s. Ella puede seguir al tocar, nunca antes de 0,8 s.

## Lo que no se dibuja

En la pantalla de ella no hay, ni en un borde, ni un instante, ni «porque ya es mayor»:

- marcador, puntos, barras, porcentaje, «3 de 5», nivel, racha, récord;
- vidas, corazones, energía;
- estrellas vacías, siluetas de lo que falta, colección numerada;
- cronómetro, reloj, vela, cielo que oscurece, barra de tiempo, cuenta atrás;
- sonido de error, aspa, temblor, confeti, rojo de alarma;
- «¿Seguro que quieres salir?»;
- cuatro opciones, sí/no como único gesto, teclado del sistema;
- botón de listo, botón de pista, botón de saltar la explicación;
- candado, botón gris, sala cerrada dibujada como hueco;
- la palabra «repaso», la palabra «lento», cualquier comparación.

El fallo no usa color de alarma. Usa ausencia de luz y una pieza que vuelve. Quien no distinga un color sigue viendo la forma y el movimiento. La columna, cuando exista, lleva letra (U, D, C), no solo color.

El color no es la única pista en ningún control:

| Cosa | Forma, además del color |
|---|---|
| Botón | Ventana con arco y alféizar. Asset `assets/ui/boton.svg` |
| Pieza | Piedra con canto y corte. Asset `assets/ui/pieza.svg` |
| Marco | Vanos y esquinas cuadradas. Asset `assets/ui/marco.svg` |
| Sala encendida | Luz en el vano y marco cerrado |
| Sala disponible | Niebla dentro del vano, sin candado y sin gris de botón muerto |
| Ala que aún no toca | Un solo bulto, sin rejilla de huecos |
| Silencio | Altavoz con barra cruzada. Con voz, altavoz sin barra |
| Fallo | La pieza vuelve en 0,4 s. El marco no se enciende |
| Acierto | El marco o la losa dan un pulso de luz de 1,2 s |

Sustituto si falta un dibujo: la forma de color de ese asset, al mismo tamaño tocable. La partida no espera al dibujo.

## Assets

| Archivo | Tamaño del lienzo | Uso |
|---|---|---|
| `assets/ui/boton.svg` | 96×96 | Cromo de todo botón. La ventana en arco lo distingue de la pieza |
| `assets/ui/pieza.svg` | 96×96 | Piedra de luz. El corte la distingue del botón |
| `assets/ui/marco.svg` | 384×256, vano a 24 px del borde | Marco de sala y de bandeja. Se estira al rectángulo de contenido conservando 48 px de esquina |

Paleta plana, la de las salas. Tinta `#2C2416`. Luz `#F4C56D`. Piedra `#F2E2A0`. Patio `#1E2A4A`. Pergamino `#F3E6C8`. No hay filtro, desenfoque ni rojo de error en estos archivos. Contraste: tinta sobre luz, o crema `#FFF8E8` sobre patio.

## Mano

Un dedo basta. El segundo dedo no cancela el arrastre, no abre un menú y no es un gesto que haya que aprender. Un apoyo accidental no rompe el turno.

Un toque quieto no es un arrastre y no es una respuesta. La pieza no se entera. No hay doble toque como única manera de hacer nada. No hay mantener pulsado para ganar. La única pulsación larga del producto es la campana del padre, y no está en la zona del pulgar.

El montón nace abajo, al centro del rectángulo de contenido, no en una esquina. Da igual la mano. Nada de desplazar un tablero más grande que la pantalla. Si no cabe, sobran piezas.

La puerta de vuelta mide 96×96, está siempre dentro de la sala, y un toque basta. Guarda y vuelve al patio. No pregunta. En el patio, el botón atrás de la tableta guarda y sale. No hay botón de salir dibujado. Menos de 15 s sin tocar una pieza no abre sesión.

## Mapa — Patio de la Niebla

Una sola pantalla. No se camina. No hay logotipo ni «pulsa para empezar».

Idea de la pantalla: elegir una ventana que ya se puede tocar. Frase de Estrella, una, del relato. En el primer día puede ser la de encender el nido. No se añade un objetivo de torre en la misma frase.

| Control | Rectángulo | Notas |
|---|---|---|
| Frase | 96, 96, 712×64 | 32 px, una línea. Tocarla repite la voz |
| Silencio | 832, 96, 96×96 | Solo en el patio. Se guarda. Dentro de la sala no está |
| Estrella | 96, 184, 200×200 | Curiosa o contenta. Nunca tapa una ventana |
| Ventanas | fila y = 232, 96×96, aire 24 | Solo salas disponibles o encendidas |
| Torre | 700, 184, 228×248 | Llama de casa siempre encendida. Adornos ya colocados. Sin ganchos vacíos |
| Ala de niebla | el hueco que sobre, un solo bulto | No es botón prohibido. Tocarla no abre lección |
| Campana | 928, 16, 48×48 | Ver rincón del padre. Fuera del rectángulo de contenido |

Primer jugable: dos ventanas, Piedras de luz y Acertijos. No se dibujan las otras seis. El ala es un bulto, no seis candados.

Cuando quepan más salas, siguen siendo ventanas del mismo edificio, sin desplazamiento. Cabén en dos filas dentro del rectángulo de contenido: hasta siete de 96 px con aire de 24 (7×96 + 6×24 = 816, dentro de 832). Estrella pasa al borde, a 96 px, para no tapar la fila. La torre enseña la llama y lo ya colocado, no una colección.

Tres estados de ventana, y ninguno es una nota:

- Niebla de ala. Aún no toca. No es un fallo.
- Disponible. Se ve, con niebla dentro, sin candado.
- Encendida. El vano tiene luz. No se apaga por fallar, por salir ni por no volver.

Disponible no es encendida. El primer día Piedras y Acertijos están disponibles. Se encienden al primer cierre que ella completa allí, con ayuda o sin ella. La luz no mide lo sola que fue.

Si hay un cierre pendiente, el patio no pide elegir sala. Muestra esa bandeja, que es una cuenta que ya sabe. Una idea: cerrarla con las manos. Acertijos puede esperar. No hay diálogo de bloqueo.

Si un adorno espera en el umbral, la idea pasa a ser colocarlo. Las ventanas siguen visibles y se pueden tocar: entrar en una sala no destruye el adorno. La frase, si habla, habla de una sola cosa. No se dice «te falta colocarlo».

El silencio es un altavoz de 96 px. Calla el sonido y deja el texto. No es un modo castigo. Con el sonido quitado, la victoria sigue siendo visual: el marco se enciende.

## Sala

Se entra por una ventana. Fundido de 0,4 s. Una pantalla, sin vídeo, sin segunda capa de fondo que haya que recorrer.

Idea de la pantalla: el verbo de esa sala. En el primer jugable, anidar en Piedras, o ensartar en Acertijos. La frase es la del guion de la sala, o una del banco si el turno es de fallo, duda o acierto. Nunca las dos a la vez.

| Control | Rectángulo | Notas |
|---|---|---|
| Vuelta | 96, 96, 96×96 | Arco de puerta sobre `boton.svg`. Un toque. Sin «¿seguro?» |
| Frase | 216, 108, 592×72 | 32 px. Empieza a 24 px de la puerta |
| Estrella | 832, 96, 96×96 | Busto en el borde. No tapa el nido. En la demostración ocupa el centro 20 s y vuelve al borde |
| Juguete | 96, 216, 832×240 | Nido, cordón o bandeja. Una sola cosa |

Piedras, primer jugable. La losa es de dos filas de cinco. Cada hueco y cada piedra, 96 px; aire 24. La losa mide 5×96 + 4×24 = 576 de ancho y 2×96 + 24 = 216 de alto. Cabe en el juguete. El montón de sobra, de al menos seis piedras, nace a la derecha de la losa o, si no cupiera, en el centro-abajo sin montar los huecos. Vaciar el montón no es el método.

La décima enciende la losa. Esa es la comprobación. No hay teclado. La oncena vuelve sola. Un numeral, si el polvo dibuja el 10, sale en el sitio de la luz a 48 px o más, un instante, y no abre una casilla.

Acertijos, primer jugable. Cordón a la altura de la mano, no en el borde. Cuentas de 96 px. Ella cuelga la siguiente desde un arcón. El arcón no es una pareja de botones. No se numera «1 de 4».

Estrella tiene tres poses y ninguna más: curiosa, contenta, pensando. Pensando es la cabeza un poco ladeada, la boca serena. No existe pose de decepción, enfado ni tristeza, ni en un fallo, ni al salir, ni al volver.

No hay botón de listo. No hay botón de ayuda. No hay silencio dentro de la sala: se eligió en el patio, y la frase escrita sigue.

## Fallo

No es otra pantalla. Es el mismo juguete, sin cromo nuevo.

Un fallo no pone aspa, no tiembla, no suena, no resta una vida, no apaga una luz de otro día y no llena una estrella vacía. Estrella está pensando. Curiosa, si el material es el que no admite la pieza. Nunca decepcionada, enfadada ni triste.

Dos maneras de no encender, y no pesan igual:

1. El material no admite la pieza. La oncena en la losa de diez, la cuenta que no sigue el collar. Vuelve sola en 0,4 s, en silencio. La primera vez en ese intento no es fallo: es el juguete. La segunda vez en el mismo intento sí lo es.
2. Ella deja un método equivocado y no lo retira en 3 s. Eso es fallo a la primera. Si se desdice dentro de los 3 s, no es fallo. Deshacer no suena a error.

En pantalla, en ese orden, y nada más:

1. La pieza vuelve a la mano o se queda donde el juguete la deja para que ella la mueva. Movimiento de 0,4 s.
2. El marco no enciende. No pasa a rojo.
3. Una frase del banco de fallo, o la del guion de esa sala. Habla de las piezas, no de la persona. Luego silencio.
4. Si toca ayuda visual, el ejemplo aparece en el lado de Estrella. No antes de que la frase haya podido leerse.

No se dice «mal», «incorrecto», «casi», «date prisa», «esto es fácil», ni un consuelo que elogie a la persona. No se repite la misma frase en el mismo intento. No se dicen dos frases de fallo seguidas sin una ayuda visual en medio.

A la segunda vez del borde no hay tercera frase de fallo. Se dice la frase puente, literal, y se va al cierre: «Seguimos con una que ya sabes.» No nombra cansancio ni fallo. No hay un tercero.

Dudar no es fallar. Si la duda se ve —suelta en el sitio, cambia de destino, sostiene más de 8 s, se desdice antes de 3 s— la frase sale del banco de duda, no del de fallo. No se le dice que ha dudado. Sostener mucho no le quita la pieza. No hay reloj.

Un toque a un número, o al vacío, no enciende nada y no es fallo. Estrella, pensando. Se sigue en el mismo turno.

El acertijo fallido no suma fallo del borde y no baja la aritmética. En pantalla se ve igual: silencio, pieza que vuelve, una frase de piezas.

## Ayuda

No es un menú ni un botón. Son tres peldaños del mismo juguete. Se retira uno, no todos. No se anuncia. No hay pantalla de «ahora sin ayuda». Si la ayuda vuelve, Estrella pone otra vez el ejemplo en su lado, curiosa. Ella no oye «has bajado».

1. Piezas a la vista. Las que ella mueve no se esconden. Si se esconden, no hay gesto.
2. Ejemplo al lado. Estrella hace el mismo tipo de gesto en su lado. No deja la solución puesta en la bandeja de la niña. El ejemplo usa `pieza.svg` sobre un paño distinto del de ella: otra forma de soporte, no solo un color más pálido. Copiar el ejemplo es con ayuda.
3. Solo el gesto. El ejemplo no está. Nadie dice que sea un examen. Si sostiene mucho, el ejemplo puede volver sin una palabra de fallo.

Entre medias no hay cuatro opciones, ni un hueco para tachar, ni una pieza que solo haya que soltar en el único sitio que brilla. El brillo, si hace falta en el cierre, es de toda la losa, no de la respuesta.

La frase de ayuda es una, del banco o del guion, y sigue a la vista. La duda no hereda frases de fallo. El acierto no elogia a la persona: nombra el gesto.

En el primer jugable, quedarse corta no es fallo, porque no hay botón de listo. A los 8 s sin toque, después de haber movido algo, el ejemplo aparece al lado. Es ayuda, no una regañina.

## Cierre

El cierre es una cuenta que ella puede hacer. La hace ella. Estrella no coloca la última pieza en su bandeja. No hay una película de victoria si ella solo mira.

Misma sala, misma puerta de vuelta, una frase. La bandeja se presenta a un gesto que sí es un gesto: la última piedra de un diez que ya se ve en filas, no un imán al píxel correcto. Zona amplia, 120 px, dentro del juguete. El marco espera apagado hasta que su mano enciende.

Escalera, sin llamarla así en pantalla:

1. Una que ya ha hecho sola. Si aún no existe, contar tres piedras. Piezas a la vista.
2. Si la colocación no enciende, o pasan 15 s sin un movimiento con destino: el ejemplo aparece en el lado de Estrella. Se queda ese peldaño. No hay un tercero. No hay botón de saltar. No suma fallo del borde.

El acierto de cierre enciende el marco con el mismo pulso de 1,2 s y la misma campanada suave de 0,4 s que cualquier otro acierto. No crece si fue deprisa. No hay confeti. La frase nombra el gesto, o es la de cierre del guion. No se acumulan tres halagos.

Después, una sola idea nueva: colocar un adorno. Dos adornos, los dos válidos, abajo, al centro, 96×96 con aire de 24. Si la mano lo pide, 112, siempre que el aire siga en 24. Ganchos de 96 en una rejilla de dos por dos, aire 24, no una fila de siluetas vacías de toda la colección. Frase ya escrita: «¿Dónde lo pones?» Ella elige cuál y dónde. Da igual cuál. Lo colocado no se quita por haber fallado antes. Si sale antes de soltarlo, el adorno espera en el umbral, ya suyo.

Si cierra la tableta antes de encender esa luz, no se inventa el acierto. No hay pantalla de «progreso perdido». Al volver, la bandeja pendiente es la idea del patio. No se reanuda el fallo.

## Rincón del padre

Ella no tiene puerta de ajustes. No hay rótulo «padres». No hay botón de 96 px en la zona del pulgar que lleve al PIN.

La entrada es una pulsación larga de 1,5 s en la campana de la torre, rectángulo 928, 16, 48×48. Está en el margen superior, fuera del arrastre y fuera del alcance fácil. Un toque corto no hace nada. No hay texto junto a la campana.

El PIN es de 4 cifras, local. El teclado lo dibuja el juego. No usa `pieza.svg` y no es un problema de mates. No abre el teclado del sistema: taparía el patio y parecería una ficha.

Pantalla del PIN. Una idea: cuatro cifras.

| Control | Rectángulo | Notas |
|---|---|---|
| Vuelta | 96, 96, 96×96 | Al patio, sin confirmar y sin frase de error |
| Cifras | centradas en y 96, cuatro cajas de 64, aire 24, numeral 48 | Lo escrito se ve. La caja vacía es un cuadrado, no una estrella |
| Borrar | 832, 96, 96×96 | Quita una cifra. No es una pieza |
| Teclas | desde x 224, y 184; 96×96; aire 24 | Dos filas: 1 2 3 4 5 y 6 7 8 9 0. Cromo de `boton.svg` |

5×96 + 4×24 = 576 de ancho. 2×96 + 24 = 216 de alto. Cabe en el rectángulo de contenido, debajo de las cifras.

Si el PIN no es el suyo: silencio y patio. No se escribe «mal» ni «incorrecto». A la tercera vez seguida, patio también. No hay espera, no hay cuenta atrás, no hay bloqueo: un castigo de tiempo castigaría un toque accidental de ella.

Pantalla de frases, en texto plano, solo si el PIN entra. Una idea: leer. Una o dos frases, 32 px, del tipo ya cerrado: hechos y el gesto siguiente. Sin porcentajes, sin media, sin semáforo, sin gráfica, sin «lenta», sin emoción, sin diagnóstico, sin comparación. Ella no ve esta pantalla. Estrella no está.

Un botón de 96, «Techo», lleva a la pantalla de techo. No se mezcla el techo con las frases: serían dos ideas, y un vistazo no debe parecer un boletín.

Pantalla de techo. Una idea: frenar. El techo solo frena o se mantiene. No salta cimientos. No abre la llevada si hacer dieces no está firme. No apaga luces, no cierra Acertijos, no quita adornos, no marca a mano «esto ya lo sabe».

Cinco frenos, en pastillas de 96 px de alto y el ancho de su texto, aire 24, dentro del rectángulo de contenido:

- Hasta 20
- Sin llevada
- Sin mercado
- Sin centenas
- Sin el signo de por

Elegido y no elegido se distinguen por el relleno del arco y por un cuadrado en la pastilla, no solo por el color, y no por una estrella. El texto de la pastilla no cambia a un elogio.

La exportación de un resumen a mano no entra en el primer jugable. Hasta entonces no se dibuja el botón: un botón gris sería una puerta prohibida. Cuando exista, el resumen son las frases, no un fichero de puntuaciones, y el juego no lo envía.

Volver al patio no pide confirmación. Lo que el padre haya frenado sigue frenado. La niebla de lo que el techo retrasa es la misma niebla de «viene después». Estrella no dice «tu padre no te deja».

## Movimiento

Poco. El aparato es una Fire 7 con 2 GB.

- Fundido entre pantallas: 0,4 s.
- Pieza que vuelve: 0,4 s, en silencio.
- Pulso de luz al encender: 1,2 s. Igual con ayuda o sin ella.
- Campanada suave: 0,4 s. La misma siempre. No crece con la prisa.
- Como mucho 40 sprites en movimiento y 12 partículas al encender. Si no cabe, se quita adorno, no se quita el gesto.
- Una espera de carga a mitad de intento no pasa de 1 s.

No hay temblor, no hay parpadeo de error, no hay Estrella que bostece para marcar el tiempo. El reloj interno no se dibuja. No corta un arrastre a medias. Se acorta entre turnos.

## Primer jugable, pantallas

Solo estas, y solo con los sustitutos de color si falta el dibujo:

1. Patio, con llama, dos ventanas, ala de niebla, silencio y campana muda.
2. Piedras: losa de dos filas de cinco, montón, frase, vuelta, Estrella.
3. El mismo juguete en fallo, en ayuda y en cierre. Sin cromo nuevo.
4. Acertijos: cordón, arcón, cuentas. No dos botones.
5. Torre: dos adornos y ganchos para colocar uno.
6. PIN y, si entra, frases y techo. Sin exportación.

No entra la llevada, ni el euro, ni un problema con historia, ni un marcador que «ayude a probar».
