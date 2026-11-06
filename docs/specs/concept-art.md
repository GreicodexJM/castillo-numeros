# Concept art — Estrella y el Castillo de los Números

Este texto fija el estilo, la cara y los encuadres. Obedece `docs/GDD.md`. Si un capítulo de experto dice otra cosa, manda el GDD. Los prompts cerrados, listos para pegar, están en `assets/concept/PROMPTS.md`.

No hay nombre ni foto de una persona real. El personaje es original. Nada de Disney ni de princesas de película. No se genera vídeo. No hay clip dentro del APK. Los generadores corren en el ordenador de desarrollo, nunca en el juego. El juego no pide red.

Si falta un dibujo, vale la silueta de `assets/concept/` o una forma de color del mismo tamaño. No se inventa detalle para tapar el hueco.

## Estilo fijado

Ilustración 2D plana, como gouache, sin degradados finos y sin textura menuda. Formas grandes, mucho aire, contraste alto, poco detalle. Se entiende en una pantalla de 7 pulgadas, a unos 171 dpi, sin acercar el dedo.

El tema es magia de las luces y un castillo cálido. No es un vestuario de princesa. La magia no es un rayo ni una varita: es una lámpara que se acuerda cuando las manos hacen el método.

- Cámara fija, casi frontal, con unos quince grados de picado para que se vean los huecos del nido. Sin gran angular, sin ángulo holandés, sin desenfoque. Todo nítido.
- Una sola luz de victoria, siempre el mismo ámbar. No hay un brillo más grande por acertar deprisa ni por no fallar.
- La sombra es corta y cálida. No hay sombra negra de interfaz.
- El aire entre piezas es de unos 24 px. Una frase, de hasta 12 palabras, va en una banda vacía. El dibujo no pinta letras: el texto lo pone el juego, y se ve aunque haya voz.
- Si una sala se enciende, la niebla de esa sala se aparta un poco. No huye. No hay pelea.

Paleta de este concept. Si más adelante existe `assets/palette.json`, los hex de producción salen de ahí; hasta entonces, estos son los que tienen que repetir los generadores.

| Uso | Hex | No significa |
|---|---|---|
| Aire, banda de frase, fondo de sala | `#F7EFE2` | no es una ficha en blanco |
| Niebla, cortina clara | `#E7DCC8` | no es noche, no es tormenta, no es un cuerpo |
| Pared de arenisca | `#E6C49A` | |
| Sombra cálida y tinta de silueta | `#3B2A22` | no es un marcador |
| Piel de Estrella | `#C4845A` | uniforme; no es un retrato |
| Pelo | `#3B2A22` | |
| Capa, calzas, un farol válido | `#C4533A` | no es rojo de error |
| Túnica | `#F4E6D0` | |
| Luz encendida, broche, chispa | `#F2D36B` | el mismo brillo siempre |
| Luz que sube al cerrar el diez | `#F0C43A` | |
| Piedra de luz | `#F6E7A8` | |
| Barra de diez | `#E08A2E` | |
| Placa de cien | `#C45C28` | |
| Moneda del juego | `#E6B15A` | no es dinero de casa |
| Luz dormida, todavía cálida | `#C9B79A` | no es un botón prohibido ni un gris de castigo |

Prohibido como color de fallo: rojo de aspa, negro de alarma, gris muerto, estrella vacía en gris.

## Cara que no cambia

Se genera primero la hoja de cara. Nada más se dibuja hasta que esa cara está aceptada. Todo lo demás usa esa referencia. Tripo, si se usa, solo saca vistas fijas de esta misma cara y de este mismo cuerpo. No inventa otra.

Estrella es aprendiz de magia de las luces. Se ve como una chica joven, no como quien juega y no como una reina. Cuerpo capaz de cargar piedras, sin cintura de muñeca. Manos grandes, cuatro dedos y pulgar, simples. Quien juega no se dibuja. No hay otros niños. No hay tendero.

Lo que no cambia de un dibujo a otro:

- Cara redonda. Piel ocre media `#C4845A`, uniforme, sin pecas, sin lunar, sin marca que parezca de una persona real.
- Ojos marrón oscuro `#3A2418`, medianos, almendrados y simples. Sin pestañas largas. Sin brillos en forma de estrella. Sin ojos enormes de película.
- Cejas suaves. Nunca fruncidas.
- Nariz pequeña y redonda.
- Boca pequeña. En curiosa, cerrada. En contenta, sonrisa corta, sin dientes y sin risa de cartel. En pensando, cerrada.
- Pelo castaño oscuro `#3B2A22`, corte justo por encima del hombro. Una trenza corta en su lado derecho: de frente, queda a la izquierda de la imagen. La trenza se ata con un trozo de tela del mismo terracota de la capa. No hay melena suelta de baile, ni flores, ni diadema.
- Capa corta terracota `#C4533A`, hasta la cintura, abierta, para poder moverse.
- Túnica crema `#F4E6D0` hasta la rodilla. Calzas terracota. Botas blandas `#5C3A2E`, sin tacón y sin hebilla.
- Broche de tela en estrella plana, `#F2D36B`, no una joya.
- Bolsa redonda de tela ocre en la cadera, con piedras de luz asomando. Es bolsa, no varita.

Tres caras, y ninguna más:

1. Curiosa. Cabeza un poco ladeada. Mira la pieza, no a cámara, salvo en la hoja de referencia. Cejas suaves, altas. Boca cerrada.
2. Contenta. Sonrisa corta. Puede juntar las manos una vez. No salta. No tapa el juguete. No hay confeti.
3. Pensando. Toca el broche. Mira las piezas. No es pena. No es espera con prisa.

Nunca: decepcionada, enfadada, triste, lágrima, suspiro, cabeza gacha, ceño, dedo que niega, boca abierta de susto. Un fallo no le cambia la cara: sigue curiosa, contenta o pensando.

No lleva corona, tiara, varita, vestido de baile, guantes de gala ni zapatos de cristal. No se parece a una princesa de película. No se parece a una persona real. No se le pone nombre de nadie.

En el primer jugable solo hacen falta curiosa y pensando. Contenta se reserva para cuando la luz sube, y aun así es pequeña.

## Escala y encuadre

Pantalla de diseño: 1024×600, horizontal, a pantalla completa. Con la barra del sistema, lo importante cabe en unos 1024×552. Margen de aire: 24 px. Nada crítico en los 48 px de abajo.

Relación para generadores que no aceptan píxeles: 17:10, y se recorta a 1024×600. La banda de frase queda dentro del área útil.

- Piezas y botones: unos 96 px. Por debajo de eso no se generan.
- En hacer el diez, cada hueco del nido cabe una piedra de unos 96 px. Cinco huecos y cuatro aires de 24 px ocupan unos 576 px. Estrella queda al lado, sin montarse encima.
- En pantalla de juego, Estrella mide unos 320 px de alto si está sentada y no más de 400 si está de pie. La cara, no la cabeza entera, se lee a 96 px. Si la cara no se lee, está mal encuadrada.
- Una idea por imagen. El juguete, la frase en banda vacía, la vuelta al patio. Nada de marcador al lado.

El dibujo no escribe. Ni frases, ni cifras, ni el 10, ni «1,30 €», ni firmas. Las cifras grandes, cuando toquen, las pone el juego. Un generador que meta letras se descarta.

## Qué se ve

### Primera pantalla

No hay logotipo, ni espera, ni «pulsa para empezar». Es el patio, ya.

Estrella sentada en un escalón de arenisca, curiosa, con un farol apagado grande en el regazo. El farol no es una nota: está apagado porque aún no se ha colocado, no porque alguien haya fallado. Una puerta tibia, grande, la de Piedras de luz. La torre al fondo, pared completa, sin ganchos vacíos y sin fila de objetos que falten. La niebla es una cortina crema, baja y quieta, al pie de la pared. No tiene ojos.

La banda de abajo va vacía. La frase la pone el capítulo de relato, no este dibujo.

No se camina. No hay mapa dentro de la primera pantalla: es el lugar, visto una vez.

### Mapa

Una sola pantalla, el Patio. Vista fija. No hay personaje recorriendo un camino.

Se puede elegir, y solo eso se dibuja como cosa que se toca:

- Piedras de luz: puerta tibia, lámpara ámbar, nido leído en grande.
- Acertijos: un cordón y un arcón, no una puerta cerrada. Esta sala no se cierra nunca.
- Torre: la pared con lo ya colocado. El primer día puede no haber nada, y aun así la pared está bien. No se dibujan clavos vacíos.

Lo que no se puede elegir no aparece como botón prohibido, ni en gris, ni con candado, ni como hueco vacío de sala. No hay cuadrícula de nueve puertas. El resto del castillo es pared cálida y niebla suave, escenario, no control.

La campana del padre no se destaca. No lleva rótulo. No sale el PIN. Eso no es una imagen de quien juega.

### Hacer el diez

Sala Piedras de luz. Un nido de diez huecos, dos filas de cinco, huecos a la vista, borde grueso. Piedras de luz sueltas en un montón bajo, cada una la silueta de `piedra.svg`, irregulares, cálidas, con una luz grande en el centro. Caben bajo el dedo.

La imagen de la décima: nueve piedras ya dentro, la décima camino del último hueco, el borde del nido empezando a encenderse en `#F0C43A`. La luz sube hacia el techo de la sala. Estrella, al lado, pensando, toca el broche. No coloca ella la última piedra.

La imagen de la oncena: el nido ya tiene diez y ya está encendido. Una piedra de más queda fuera. La luz no crece. No hay aspa, no hay rojo, no hay sonido dibujado. Estrella mira esa piedra con curiosidad, no con pena.

El numeral llega después, como comprobación, y no se pinta en estas imágenes. No hay cuatro opciones. No hay un único sitio que brille como trampa: brillan el borde y la luz, cuando el gesto cierra el diez.

No entra la llevada. No entra el euro. No hay problema con historia. No hay chispa, ni barra, ni placa, ni moneda en esta sala.

### Acertijo del primer día

Cordón a la altura de la mano, no pegado al borde. Cuentas grandes de dos formas: piedra y estrella. La estrella del collar es de cinco puntas, maciza, con un agujero grande para el cordón. No lleva la lengüeta de la llevada. No es una estrella vacía de marcador.

En el cordón ya se lee: piedra, estrella, piedra, estrella, y un hueco grande. La siguiente sale de un arcón con cuentas de más, de las dos formas, no de dos botones. Quien juega no se dibuja. No hay mano de foto.

Si la cuenta no sigue, en el juego vuelve al arcón. En el dibujo de concept no hace falta pintar ese momento. Si se pinta, es silencio y cara de pensar, sin aspa.

### Torre

La torre ya está bien. Pared cálida, completa. Estrella acerca un farol. Abajo, dos faroles del mismo tamaño: uno ámbar `#F0C43A` y uno terracota `#C4533A`. Los dos valen. Ninguno es el de no haberse equivocado. Ninguno está gris. No hay hueco marcado del que no se eligió.

El farol es el adorno del primer jugable. No es una cinta. Si un capítulo pone la cinta primero, manda el GDD: el primer día se coloca un farol.

### Niebla

Una cortina clara `#E7DCC8`, baja, quieta, como vaho en un cristal en un día suave. Sin ojos, sin boca, sin manos, sin cara escondida en el blanco. No es un monstruo. No es un villano. No crece. No traga salas. Cuando una lámpara se enciende, se aparta un poco y se queda quieta.

No se dice oscuridad en el dibujo. No hay noche cerrada. No hay rayo. No hay bosque negro.

## Piezas

Siluetas en `assets/concept/`. Se leen a 96 px por el contorno, no por un detalle de dentro. No llevan texto. No se cuentan puntitos para saber el valor: el valor lo da la forma.

| Archivo | Qué es | Cómo se lee a 96 px | Cuándo se ve |
|---|---|---|---|
| `piedra.svg` | Piedra de luz. La pieza del nido y la cuenta oscura o clara del collar, por la forma | Bloque irregular, más ancho que alto, con una luz redonda grande | Primer jugable |
| `chispa.svg` | Unidad del pergamino, la cuenta fina | Punta arriba, cintura, base ancha. No es piedra y no es estrella | Más adelante. No en el primer jugable |
| `barra-diez.svg` | Diez ya junto. Una pieza, no diez piedras | Barra larga tumbada, con una muesca grande. No se cuentan los cortes | Cuando haya decenas. No en el primer jugable |
| `placa-cien.svg` | Cien como losa | Cuadrado con una cruz gruesa. No es una rejilla de cien celdas | Cuando haya centenas. No en el primer jugable |
| `moneda.svg` | Moneda del juego | Disco perfecto, aro grueso, centro macizo. Sin cifra y sin símbolo de euro | Mercado. No en el primer jugable |
| `estrella-llevada.svg` | La una que salta de columna | Estrella de cinco puntas, maciza, con lengüeta grande a la izquierda | Cuando hacer dieces ya es fácil. No en el primer jugable |

La lengüeta mira a la izquierda porque, en el pergamino, la llevada salta una columna hacia las decenas, no dos. No es una flecha de interfaz. No es una estrella vacía. No es el broche: el broche es pequeño, de tela, y va en la capa. No es la cuenta del collar: esa tiene agujero y no tiene lengüeta.

La chispa no sustituye a la piedra del nido. El nido se llena con piedras.

La moneda no es dinero de casa. No hay billetes. El valor, cuando toque, lo dirán el tamaño y una cifra grande puesta por el juego, no un grabado menudo. En la silueta no hay cifra: sirve para 1, 2, 5, 10, 20 y 50 céntimos y para 1 y 2 euros. La de euro es más grande que la de céntimo. El dibujo de concept de la silueta es una sola, la grande.

## Qué no puede aparecer

En todas las imágenes, sin excepción:

- Disney, princesa de película, corona, tiara, varita, vestido de baile, zapatos de cristal, castillo de parque, canción, animal que habla.
- Foto, retrato o nombre de una persona real. Cualquier cara que no sea la de Estrella, ya fijada.
- Cara triste, enfadada, decepcionada, llorosa, con ceño o con la cabeza gacha.
- Monstruo, ojos en la niebla, boca en la niebla, villano, noche de tormenta.
- Vidas, corazones, reloj, cuenta atrás, estrellas vacías, marcador, porcentaje, aspa, rojo de error, confeti, salto de victoria que tape el juguete.
- Cuatro opciones, botones de respuesta, candado, botón gris de «no puedes», hueco vacío de sala o de adorno.
- Letras, números, logotipos, firmas, marcas de agua, texto diminuto.
- Estilo anime de ojos grandes, fotorrealismo, 3D de pantalla, pixel art, filigrana, detalle que no se lea a 96 px.
- Vídeo, tira de fotogramas, pantalla de cine.

## Imágenes a generar

Orden cerrado. La 01 se acepta antes de lanzar el resto. El resto repite la cara de la 01 y no la redescubre. No generar las salas que no están en esta lista.

| Id | Archivo previsto | Relación | Píxeles | Para qué |
|---|---|---|---|---|
| 01 | `estrella-cara` | 1:1 | 1024×1024 | Fijar la cara. No va tal cual al APK |
| 02 | `estrella-cuerpo` | 3:4 | 768×1024 | Cuerpo, ropa, dos poses del primer jugable |
| 03 | `primera-pantalla` | 17:10 | 1024×600 | Lo primero que se ve |
| 04 | `mapa-patio` | 17:10 | 1024×600 | El Patio, solo lo que se puede elegir |
| 05 | `piedras-hacer-diez` | 17:10 | 1024×600 | La décima enciende el nido |
| 06 | `piedras-oncena` | 17:10 | 1024×600 | La de más no enciende |
| 07 | `acertijo-collar` | 17:10 | 1024×600 | Piedra, estrella, piedra, estrella |
| 08 | `torre-farol` | 17:10 | 1024×600 | Ella coloca un farol. Los dos colores valen |
| 09 | `niebla` | 1:1 | 1024×1024 | La cortina, para que no le pinten cara |
| 10 | `piezas` | 1:1 | 1024×1024 | Las seis siluetas, pintadas, sin mezclarlas con el primer jugable |

Los prompts de abajo son los mismos que en `assets/concept/PROMPTS.md`.

### 01 — estrella-cara

Relación 1:1. 1024×1024. Primera de todas.

Español:

Ilustración 2D plana, como gouache, bordes claros, formas grandes, poco detalle, contraste alto, fondo liso `#F7EFE2`. Hoja de referencia de un personaje original de ficción, aprendiz de magia de las luces, no basada en ninguna persona real. Tres cabezas grandes del mismo personaje, de frente, con aire entre ellas: curiosa, contenta y pensando. Cara redonda, piel ocre media uniforme `#C4845A`, sin pecas y sin lunar. Ojos marrón oscuro medianos, sin pestañas largas y sin brillos de estrella. Cejas suaves, nunca fruncidas. Nariz pequeña y redonda. Boca pequeña: curiosa, cerrada y cabeza un poco ladeada; contenta, sonrisa corta sin dientes; pensando, cerrada, mirada baja hacia donde estaría una pieza. Pelo castaño oscuro `#3B2A22`, corte justo por encima del hombro, una trenza corta en su lado derecho, a la izquierda de la imagen, atada con tela terracota. Cuello de capa corta terracota `#C4533A`. Broche de tela en estrella plana `#F2D36B`, no una joya. Sin letras, sin números y sin marca de agua.

English:

Flat 2D illustration, gouache-like, clear edges, large shapes, little detail, high contrast, plain background `#F7EFE2`. Reference sheet of an original fictional character, an apprentice of light magic, not based on any real person. Three large front-facing heads of the same character, with air between them: curious, glad, and thinking. Round face, even medium-ochre skin `#C4845A`, no freckles and no beauty mark. Medium dark-brown eyes, no long lashes and no star-shaped catchlights. Soft brows, never furrowed. Small round nose. Small mouth: curious, closed, head tilted a little; glad, a short smile with no teeth; thinking, closed, gaze lowered toward where a piece would be. Dark chestnut hair `#3B2A22`, cut just above the shoulders, one short braid on her right side, on the left of the image, tied with terracotta cloth. Neck of a short terracotta cape `#C4533A`. Flat cloth star brooch `#F2D36B`, not a jewel. No letters, no numbers, and no watermark.

No puede aparecer: Disney, princesa de película, corona, tiara, varita, vestido de baile, foto real, cara triste, enfadada o llorosa, texto.

### 02 — estrella-cuerpo

Relación 3:4. 768×1024. Después de aceptar la 01.

Español:

Misma aprendiz que la hoja de cara aceptada, misma piel, mismo pelo, misma trenza corta en su lado derecho, misma boca pequeña. Ilustración 2D plana, fondo `#F7EFE2`. Dos figuras de cuerpo entero con mucho aire: de pie, curiosa, cabeza ladeada, mirando una piedra de luz que tiene en la mano; y sentada, pensando, tocando el broche. Capa corta terracota `#C4533A` hasta la cintura, abierta. Túnica crema `#F4E6D0` hasta la rodilla. Calzas terracota. Botas blandas sin tacón. Bolsa redonda ocre en la cadera, con piedras asomando. Manos grandes y simples. Cuerpo capaz, sin cintura de muñeca. Sin corona y sin varita. Sin letras.

English:

The same apprentice as the accepted face sheet, same skin, same hair, same short braid on her right side, same small mouth. Flat 2D illustration, background `#F7EFE2`. Two full-body figures with plenty of air: standing, curious, head tilted, looking at a light-stone in her hand; and seated, thinking, touching the brooch. Short terracotta cape `#C4533A` to the waist, open. Cream tunic `#F4E6D0` to the knee. Terracotta leggings. Soft boots with no heel. Round ochre bag at the hip, stones peeking out. Large simple hands. A sturdy body, no doll waist. No crown and no wand. No letters.

No puede aparecer: melena de baile, diadema, otra cara distinta a la 01, pose triste, salto, confeti, texto.

### 03 — primera-pantalla

Relación 17:10. 1024×600. Recortar a esa medida.

Español:

Misma aprendiz que la hoja de cara, curiosa, sentada en un escalón de arenisca `#E6C49A`, farol apagado grande en el regazo, sin corona y sin varita. Patio de castillo cálido, ilustración 2D plana, mucho aire, contraste alto, poco detalle. Una sola puerta tibia grande. Torre al fondo con la pared completa, sin ganchos vacíos. Niebla crema `#E7DCC8` baja, como una cortina, sin ojos. Banda vacía abajo para una frase, sin letras. Vista fija, no se camina. Sombras cortas y cálidas.

English:

The same apprentice as the face sheet, curious, seated on a sandstone step `#E6C49A`, a large unlit lantern in her lap, no crown and no wand. Warm castle courtyard, flat 2D illustration, lots of air, high contrast, little detail. One large warm door. Tower in the background with a complete wall, no empty hooks. Low cream fog `#E7DCC8`, like a curtain, with no eyes. An empty band at the bottom for one sentence, no letters. Fixed view, nobody walking. Short warm shadows.

No puede aparecer: logotipo, botón de empezar, candado, salas en gris, reloj, marcador, texto, cara triste.

### 04 — mapa-patio

Relación 17:10. 1024×600.

Español:

Mapa de un solo patio, vista fija, ilustración 2D plana, cálida, formas grandes. Tres cosas que se pueden elegir, grandes y separadas por aire: una puerta de piedras con lámpara ámbar, un cordón con cuentas junto a un arcón, y una torre con la pared ya bien, con un farol colocado o sin nada todavía, nunca con clavos vacíos. El resto es pared de arenisca y niebla crema, no una cuadrícula de salas cerradas. Estrella, la misma cara aceptada, a un lado, curiosa, sin tapar las tres cosas. Sin candados, sin botones grises, sin texto.

English:

Map of a single courtyard, fixed view, flat warm 2D illustration, large shapes. Three choosable things, large and separated by air: a stone door with an amber lamp, a cord with beads beside a chest, and a tower whose wall is already fine, with one lantern placed or with nothing yet, never with empty hooks. The rest is sandstone wall and cream fog, not a grid of closed rooms. Estrella, the same accepted face, at one side, curious, not covering the three things. No locks, no grey buttons, no text.

No puede aparecer: nueve puertas, candado, hueco vacío de sala, camino para caminar, PIN, texto, marcador.

### 05 — piedras-hacer-diez

Relación 17:10. 1024×600.

Español:

Sala de piedras de luz, ilustración 2D plana, mucho aire, contraste alto. Un nido grande de diez huecos en dos filas de cinco, huecos visibles, borde grueso. Nueve piedras irregulares de color `#F6E7A8` ya dentro, cada una con una luz redonda grande. La décima piedra va hacia el último hueco. El borde del nido empieza a encenderse en ámbar `#F0C43A`, la misma luz de siempre, subiendo un poco hacia el techo. Estrella, misma cara aceptada, al lado, pensando, toca el broche y no coloca la piedra. Banda vacía para una frase. Sin cifras, sin cuatro opciones, sin reloj.

English:

Light-stone room, flat 2D illustration, lots of air, high contrast. One large nest of ten holes in two rows of five, holes visible, thick rim. Nine irregular stones in `#F6E7A8` already inside, each with a large round light. The tenth stone is moving toward the last hole. The nest rim is starting to light in amber `#F0C43A`, the same light as always, rising a little toward the ceiling. Estrella, the same accepted face, beside it, thinking, touching the brooch and not placing the stone. An empty band for one sentence. No digits, no four choices, no clock.

No puede aparecer: llevada, monedas, texto, aspa, rojo de error, Estrella resolviéndolo por ella, estrella vacía.

### 06 — piedras-oncena

Relación 17:10. 1024×600.

Español:

La misma sala y el mismo nido de la imagen anterior, ya con diez piedras y el borde encendido en el mismo ámbar `#F0C43A`. Una oncena piedra, igual de grande, queda fuera del nido. La luz no crece y no cambia de color. Estrella, misma cara, curiosa, mira esa piedra de más. Silencio visual: sin aspa, sin rojo, sin cara de pena, sin texto y sin cifras.

English:

The same room and the same nest as the previous image, already holding ten stones, rim lit in the same amber `#F0C43A`. An eleventh stone, just as large, stays outside the nest. The light does not grow and does not change color. Estrella, the same face, curious, looks at that extra stone. Visual silence: no cross, no red, no sad face, no text and no digits.

No puede aparecer: castigo, sonido dibujado, ceño, marcador, botón de deshacer.

### 07 — acertijo-collar

Relación 17:10. 1024×600.

Español:

Patio de acertijos, ilustración 2D plana, formas grandes. Un cordón a la altura de la mano, no en el borde de la pantalla. En el cordón, de izquierda a derecha: piedra irregular, estrella maciza de cinco puntas con agujero grande, piedra, estrella, y un hueco grande. La estrella del collar no tiene lengüeta. Un arcón abierto con más piedras y más estrellas, no dos botones. Estrella, misma cara, pensando, mira el cordón y no cuelga ella la cuenta. Sin mano de otra persona. Sin texto.

English:

Puzzle courtyard, flat 2D illustration, large shapes. A cord at hand height, not at the screen edge. On the cord, left to right: irregular stone, solid five-point star with a large hole, stone, star, and one large empty gap. The necklace star has no tab. An open chest with extra stones and extra stars, not two buttons. Estrella, the same face, thinking, looks at the cord and does not hang the bead herself. No other person's hand. No text.

No puede aparecer: cuatro opciones, estrella vacía de marcador, lengüeta de llevada, resta disfrazada, texto, cara triste.

### 08 — torre-farol

Relación 17:10. 1024×600.

Español:

Pared cálida de la torre, ya completa, sin clavos vacíos y sin fila de huecos. Estrella, misma cara, curiosa, acerca un farol grande. Abajo, dos faroles del mismo tamaño para elegir: uno ámbar `#F0C43A` y uno terracota `#C4533A`. Los dos valen igual. Ninguno está gris. Ninguno es premio por no fallar. Mucho aire. Ilustración 2D plana. Sin texto y sin contar los faroles.

English:

Warm tower wall, already complete, no empty hooks and no row of gaps. Estrella, the same face, curious, brings a large lantern close. Below, two lanterns of the same size to choose from: one amber `#F0C43A` and one terracotta `#C4533A`. Both are equally valid. Neither is grey. Neither is a prize for not failing. Lots of air. Flat 2D illustration. No text and no counting of lanterns.

No puede aparecer: cinta como único premio, estrellas vacías, marcador de adornos, farol gris de castigo, texto.

### 09 — niebla

Relación 1:1. 1024×1024.

Español:

Estudio de la niebla del castillo, ilustración 2D plana. Una cortina baja, quieta, color crema `#E7DCC8`, como vaho en un cristal en un día suave, sobre pared de arenisca. A un lado, una lámpara ámbar encendida y la cortina un poco apartada, sin huir. La niebla no tiene ojos, ni boca, ni manos, ni cara, ni cuerpo. No es noche. No es tormenta. Sin texto.

English:

Study of the castle fog, flat 2D illustration. A low, still curtain, cream `#E7DCC8`, like breath on glass on a mild day, against a sandstone wall. At one side, a lit amber lamp and the curtain drawn back a little, not fleeing. The fog has no eyes, no mouth, no hands, no face, and no body. It is not night. It is not a storm. No text.

No puede aparecer: monstruo, villano, ojos escondidos, dientes, rayo, bosque negro, texto.

### 10 — piezas

Relación 1:1. 1024×1024. No es una pantalla de juego. Es la hoja para no cambiar las siluetas.

Español:

Hoja de seis piezas sueltas, ilustración 2D plana, fondo `#F7EFE2`, mucho aire, cada pieza grande. De izquierda a derecha y de arriba abajo: una piedra irregular `#F6E7A8` con luz redonda; una chispa en punta `#F2D36B`, ancha de base; una barra larga tumbada `#E08A2E` con una muesca grande; una placa cuadrada `#C45C28` con una cruz gruesa oscura; una moneda circular `#E6B15A` con aro grueso y centro macizo, sin cifra; una estrella maciza de cinco puntas `#F2D36B` con una lengüeta grande hacia la izquierda. Sin letras, sin números, sin Estrella, sin nido.

English:

Sheet of six loose pieces, flat 2D illustration, background `#F7EFE2`, lots of air, each piece large. Left to right, top to bottom: one irregular stone `#F6E7A8` with a round light; one pointed spark `#F2D36B`, wide at the base; one long horizontal bar `#E08A2E` with a single large notch; one square plate `#C45C28` with a thick dark cross; one round coin `#E6B15A` with a thick rim and a solid center, no digit; one solid five-point star `#F2D36B` with a large tab to the left. No letters, no numbers, no Estrella, no nest.

No puede aparecer: texto diminuto, símbolo de euro, billete, rejilla de cien celdas, estrella solo en contorno, diez puntitos para contar.

## Salas que no se generan todavía

No hace falta prompt todavía. Cuando se abran, heredan esta cara, esta paleta y esta cámara. No se redescubre el estilo.

- Espejo: marco grueso y un paño con dos montones. Solo suma. El paño se voltea. No es una balanza de resta.
- Círculo: alfombra redonda, tres montones pequeños, una cinta ancha. No se abre en la misma imagen que el Espejo.
- Pergamino: varillas en vertical, cuentas gordas y cuentas finas. La primera imagen de esa sala no salta. La estrellita con lengüeta llega en otra imagen, más tarde, y salta una sola columna.
- Mercado: puesto sin tendero, lo atiende la lámpara. Monedas grandes. Sin billetes. Sin caja registradora.
- Jardín: dos o tres macetas, no doce. No hay fila que se desplace fuera de la pantalla.
- Tesoro: un cofre y cuencos. Los cuencos no son niños. La sobra no se pinta como fallo.

## Sustitutos si falta el dibujo

Mismo tamaño que la pieza de verdad. Color plano. Sin detalle de relleno.

| Falta | Forma |
|---|---|
| Estrella | Círculo `#C4845A` de unos 96 px y un punto `#F2D36B` de broche. Solo hasta tener la cara |
| Piedra | `piedra.svg` |
| Chispa | `chispa.svg` |
| Diez | `barra-diez.svg` |
| Cien | `placa-cien.svg` |
| Moneda | `moneda.svg` |
| Llevada | `estrella-llevada.svg` |
| Nido | Rectángulo redondo `#E6C49A` con diez círculos en dos filas de cinco |
| Farol | Círculo `#F0C43A` o `#C4533A`, los dos válidos |
| Niebla | Rectángulo `#E7DCC8` sin ojos |
| Puerta | Rectángulo redondo `#E6C49A` con un círculo ámbar |

## Tripo y lo que no se hace

Tripo solo para vistas fijas de la cara ya aceptada, del cuerpo ya aceptado y del farol. Esas vistas se quedan en imagen plana. No entra un modelo 3D en la tableta. No se genera vídeo. No se sube una foto de una persona real para parecerse a ella. Si el generador cambia la trenza de lado, el color de piel o el tamaño de los ojos, se tira y se repite con la hoja 01.
