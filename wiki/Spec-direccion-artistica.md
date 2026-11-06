# Dirección artística — Estrella y el Castillo de los Números

Este texto obedece `Documento-de-diseno` y el encargo cerrado del repositorio. Si choca con ellos, mandan ellos. Los colores planos de sala ya fijados en `Juego` no se cambian. La paleta de trabajo es `assets/palette.json`. Si un generador necesita un color que no está ahí, no lo inventa: usa el sustituto plano de la sala.

Idioma del material: español de España. No hay foto ni nombre de una niña real. Los generadores corren en el ordenador de desarrollo, nunca en el juego.

## Promesa visual

Castillo bajo, cálido, de ventanas grandes y torre redonda. Formas grandes, mucho aire, contraste alto, poco detalle. Se entiende de un vistazo en una Fire 7 en horizontal.

Estrella es aprendiz de magia de las luces. Personaje original. No es una princesa de película ni un castillo de parque. No lleva corona ni varita. Su magia no adivina: enciende lo que las manos entienden.

La niebla es una cortina clara, baja y quieta. No tiene ojos, boca ni manos. No es un monstruo. No crece si no se juega. No se espanta: se aparta un poco cuando una lámpara entiende.

## Aparato y texturas

Fire 7 (2022), KFQUWI. 2 GB de RAM; en reposo quedan unos 620 MB. GPU Mali-G52. La memoria de vídeo es la misma RAM. Godot 4.7.2, renderer Compatibility, OpenGL ES 3. Sin Vulkan. Sin 3D en la tableta. Sin vídeo dentro del APK.

Pantalla 1024×600. Área útil, con la barra, unos 1024×552. Nada importante vive en los 48 px de abajo.

El juego cabe holgado por debajo de 40 MB y nunca pasa de 80. El dibujo comprimido de todo el producto no pasa de 8 MB. Si no cabe, se quita dibujo, no el gesto.

### Tamaños máximos

Una sola sala en memoria. Al salir se suelta su fondo y su atlas. No se precargan las ocho salas.

| Uso | Máximo | En pantalla | Notas |
|---|---|---|---|
| Fondo de la sala en curso | 1024×512 | 1024×552 | Una sola textura. Potencia de dos. Lo que sobre, color plano. |
| Atlas de piezas de esa sala | 512×512 | — | Se suelta al salir. |
| Hoja de Estrella | 512×512 | unos 200 px en el patio | Como mucho cuatro poses. |
| Pieza, moneda, adorno, botón | 128×128 | unos 96 px | No hace falta más: no hay zoom. |
| Atlas de interfaz | 512×512 | — | Uno para todo el juego. |
| Partícula de luz | 32×32 | — | Va dentro de un atlas. Como mucho 12 al encender. |
| Cualquier otra | 256×256 | — | Si no está en esta tabla, no pasa de aquí. |

Prohibido en textura: 1024×1024 salvo que sea el fondo ya recortado a 1024×512; 2048; 4096; vídeo; malla en el APK; mipmaps. Una textura de 2048×2048 en RGBA son 16 MB, más que todo el presupuesto de dibujo.

Presupuesto residente: 16 MB como equivalentes sin comprimir, u 8 MB en ETC2. El fondo de 1024×512 en RGBA son 2 MB; en ETC2, medio mega. No se cargan dos fondos a la vez.

Importación en Godot: `vram_compressed` (ETC2), sin mipmaps, filtro lineal, sin repetir. Tope de tamaño 512, salvo el fondo, que puede llegar a 1024 en el lado largo. RGBA sin comprimir solo si el borde alfa se rompe, y entonces 256×256 como tope.

Como mucho dos capas de fondo. Como mucho 40 sprites en movimiento. Como mucho 12 partículas, y solo al encender una luz. Esas partículas son discos del mismo ámbar. No son confeti.

## Paleta

Los códigos de sala son los del capítulo de juego, para que el sustituto plano y el dibujo no discutan. El resto fija a Estrella y a la letra. Uso completo en `assets/palette.json`.

| Id | Hex | Uso |
|---|---|---|
| noche_patio | `#1E2A4A` | Patio, si falta el dibujo. |
| luz_encendida | `#F4C56D` | Pulso de lámpara, llama de casa, forro de la capa. |
| sala_piedras | `#3D4F8A` | Suelo de Piedras de luz. |
| piedra | `#F2E2A0` | Piedra de luz y broche de tela. |
| sala_espejo | `#7EC8C3` | Sala Espejo. |
| sala_circulo | `#E7A6C8` | Sala Círculo. |
| sala_pergamino | `#F3E6C8` | Papel del pergamino. |
| tinta | `#2C2416` | Letra, cifras y columnas. |
| sala_mercado | `#E07A3D` | Puesto del mercado. No es un fallo. |
| sala_jardin | `#7DAF6A` | Jardín. No es un semáforo de bien. |
| sala_tesoro | `#C6A15B` | Tesoro. |
| sala_acertijos | `#8E7CC3` | Acertijos. |
| niebla | `#D5DCE8` | Cortina clara. Sin ojos. |
| crema_texto | `#F7F1E4` | Texto sobre fondo oscuro. |
| piel | `#C6866A` | Piel de Estrella. Siempre esta. |
| pelo | `#3F2A22` | Pelo y cejas. Siempre este. |
| iris | `#5A3A2E` | Iris. Siempre este. |
| boca | `#A15A52` | Boca pequeña. No es rojo de fallo. |
| blanco_ojo | `#F3EBE3` | Blanco del ojo. No es blanco puro. |
| capa | `#C45C4A` | Capa corta. Ropa, no aviso. |
| botas | `#5C4038` | Botas blandas. |
| sombra | `#152033` | Separar una forma grande del fondo. |

Texto: tinta `#2C2416` sobre claro, o crema `#F7F1E4` sobre noche y sobre Piedras. Nunca gris sobre niebla. La frase se lee sin la voz. Cuerpo de letra de al menos 28 px, mejor 32. Una frase, hasta 12 palabras.

No hay color de fallo en la paleta. No se añade.

## El color no es la única pista

El color ayuda. No basta. Cada cosa que ella tiene que distinguir lleva además forma, letra, sitio o número escrito.

- **Columnas.** Unidades, decenas y centenas llevan la letra U, D y C, grande. El sitio es el del colegio: unidades a la derecha, decenas en el centro, centenas a la izquierda. La pieza también cambia: piedra suelta, barra de diez, placa de cien. Una columna sin letra no se publica. Pintar la columna de otro color no sustituye a la letra.
- **Monedas.** Llevan el número escrito: 1, 2, 5, 10, 20, 50, y 1 € o 2 €. El tamaño cambia con el valor. El color del metal no basta. No hay billetes. Se escribe 1,30 €.
- **Salas.** Cada ventana tiene la forma de su juguete (nido, marco, círculo, pergamino, puesto, maceta, cofre, cordón) y, si hay sitio, el nombre. El tinte de la sala no basta.
- **Ventanas.** Niebla de ala, disponible y encendida se distinguen por lo que hay dentro (cortina, cristal con vaho, llama), no por un gris de botón muerto ni por un semáforo.
- **Acertijos.** El primer patrón es piedra, estrella, piedra, estrella: forma y pieza, no solo color. Un patrón de color lleva también la forma, o el nombre en la pieza.
- **Más, menos e igual.** Se ven emparejando. La fila más larga no manda. El color no dice cuál es más.
- **Luz de acierto.** Es siempre el mismo ámbar `#F4C56D`, en cualquier sala. El verde del jardín no significa bien. El naranja del mercado no significa mal. El rosa de la boca no significa enfado.
- **Estados de saber.** Sin ver, aprendiendo, frágil, firme y suelto no se pintan. Ella no los ve. El padre no recibe un semáforo.

La capa terracota está siempre. Un fallo no la pone más roja. La sombra no apaga una sala ni marca un botón prohibido.

## Escala de formas

La pieza es más grande que el adorno. El juguete es más grande que Estrella cuando se está jugando. El aire no es un marco decorativo: es sitio para el dedo.

| Cosa | Tamaño | Aire |
|---|---|---|
| Botón, ventana, gancho, piedra, moneda | unos 96 px | 24 px |
| Pieza que se arrastra | 88 px como mínimo | 24 px |
| Hueco del nido | cabe una piedra de 96 px | dos filas de cinco |
| Estrella en el patio | unos 200 px de alto | a la izquierda; no tapa ventanas |
| Estrella dentro de una sala | como mucho 160 px | al lado; el juguete manda |
| Letra y cifra | 28 px como mínimo | no pegada al borde |
| Marca que no se toca | 48 px como mínimo | si baja de eso, no informa |
| Toque | — | nada importante en los 48 px de abajo |

Entre ventanas del patio caben 24 px de aire. Ocho ventanas de 96 px siguen cabiendo en 1024. No hay desplazamiento.

Lo que no se puede elegir no se dibuja como botón prohibido, candado ni hueco vacío. El ala que aún no toca es un solo bulto de niebla, no seis ventanas apagadas.

Superficies lisas. Poco adorno menudo. Un ribete que no se distinga a 1024×552 no se dibuja. El detalle pequeño no lleva información: si solo se entiende ampliando, no existe.

## Luz del castillo

El castillo solo gana luz. Una sala encendida no se apaga por fallar, por salir ni por no volver.

Tres estados de ventana, y ninguno es una nota:

1. **Niebla de ala.** Aún no toca. Un bulto, no un candado. Tocarla no abre lección.
2. **Disponible.** La ventana se ve, con niebla dentro. Sin candado y sin gris de botón muerto. El primer día, Piedras de luz y Acertijos están así, no encendidas.
3. **Encendida.** El método se ha hecho al menos una vez con las manos, con ayuda o sin ella. La luz se queda.

La llama de casa, en la torre, está encendida desde la primera apertura. No es un premio. No se apaga. Ganar una sala no la enciende y no puede apagarla.

Cuando las manos encienden una luz:

1. La lámpara de esa sala da un pulso de 1,2 s. El color es `#F4C56D`, el mismo si fue sola, con ayuda, despacio o deprisa. No hay un brillo más grande por hacerlo perfecto ni por ir rápido.
2. El pulso es un disco de unos 64 px que llega a unos 96 px. No blanquea la pantalla. Las piezas siguen viéndose.
3. Como mucho 12 partículas, discos del mismo ámbar, ya en el atlas. Sin confeti, sin lluvia de estrellas, sin temblor.
4. La niebla de esa sala se aparta un poco. No huye, no gruñe, no pierde una pelea. El resto del castillo no cambia.
5. Estrella está contenta 1 s. Puede dar una palmada suave, una sola. No salta por encima de las piezas.
6. La próxima vez que se vea el patio, esa ventana sigue encendida.

Si el gesto no enciende, la pieza vuelve en 0,4 s, en silencio, como si rodara. Sin aspa, sin zumbido, sin flash, sin temblor, sin rojo. Estrella piensa. La luz que ya había no baja.

La misma campanada suave, 0,4 s, en todo acierto. No hay sonido de error. El cielo no oscurece para marcar el tiempo. No hay vela ni reloj dibujado.

## Cara de Estrella, fija entre generadores

Primero se fija la cara. Todo lo demás usa esa referencia. Hasta que exista la hoja, no se genera otra Estrella: vale una forma de color del mismo tamaño, piel `#C6866A` y capa `#C45C4A`.

Hoja única: `assets/personajes/referencia/estrella-cara.png`. Si el archivo no está, Gemini, Grok y Tripo no inventan una cara «mientras tanto».

La hoja manda sobre el texto. El texto manda sobre un generador que quiera mejorar el parecido. Una imagen nueva se descarta si la cara no coincide con la hoja, aunque el resto esté bien.

### Lo que no cambia nunca

- Óvalo suave, más ancho que una cara de moda. Barbilla redonda, no en punta.
- Se lee como aprendiz joven. No como una niña de 6 años y no como una reina. La misma edad en todos los dibujos.
- Piel `#C6866A`. Sin pecas que aparezcan y desaparezcan. Sin maquillaje. Sin brillo de porcelana.
- Ojos marrones `#5A3A2E`, medianos. El alto del ojo es cerca de un quinto de la cara, no un tercio. La separación entre ojos es el ancho de un ojo. Blancos `#F3EBE3`. Sin estrellas en el iris. Sin pestañas de abanico.
- Cejas cortas `#3F2A22`, casi horizontales. Nunca fruncidas. Nunca en arco de alarma.
- Nariz pequeña y simple, sin fosas dibujadas.
- Boca pequeña `#A15A52`, cerrada. En contenta, las comisuras suben un poco y no se ven dientes.
- Orejas apenas visibles. Sin pendientes.
- Pelo `#3F2A22`. Flequillo recto que acaba encima de las cejas y no tapa los ojos. Media melena que acaba en la clavícula, igual por los dos lados. Raya a la izquierda de ella. Sin coletero, sin diadema, sin trenza que cambie de hombro, sin mechón suelto.
- Cabeza cerca de un quinto del cuerpo, no un tercio. Manos capaces de coger una piedra, no manoplas.
- Capa corta `#C45C4A`, hasta la cadera, forro `#F4C56D`. Broche de tela en forma de estrella, `#F2E2A0`, en el pecho, no en la cabeza. Bolsa de piedras al costado. Botas blandas `#5C4038`.

### Lo que sí puede cambiar

Solo hay tres caras. Ninguna es de fallo.

| Dibujo | Cara | Qué se mueve |
|---|---|---|
| Quieta | Curiosa | Reposo. Mira una pieza. Sonríe poco. |
| Señalando | Curiosa | El dedo señala la pieza, no a quien juega. La cara no cambia. |
| Pensando | Pensando | Cabeza un poco ladeada. Boca serena. La mano toca el broche. |
| Contenta | Contenta | Sonrisa pequeña, sin dientes. Una palmada como mucho. |

Pensando no es ceño, ni espalda vuelta, ni suspiro, ni cabeza gacha. Contenta no es un salto que tape las piezas. No existe pose de decepción, enfado ni tristeza, ni al fallar, ni al salir, ni al volver.

### Bloque que se copia

Se pega tal cual, en los tres generadores. No se parafrasea. No se añade «más expresiva», «más bonita», «estilo cuento» ni «ojos grandes».

Español, fuente:

> Estrella, aprendiz joven de magia de las luces, personaje original. Misma cara que la hoja de referencia: óvalo ancho, barbilla redonda, piel #C6866A, ojos marrones medianos #5A3A2E separados un ojo, cejas cortas casi rectas, nariz simple, boca pequeña cerrada, flequillo recto, media melena castaña #3F2A22 hasta la clavícula, raya a su izquierda. Capa corta #C45C4A, broche de tela en forma de estrella en el pecho, botas blandas. Sin corona, sin varita, sin diadema, sin pendientes, sin vestido de baile. Curiosa, contenta o pensando. Nunca triste, enfadada ni decepcionada. Formas grandes, poco detalle, luz cálida. No es una princesa de película.

Inglés, copia del mismo bloque, no otro diseño:

> Estrella, a young apprentice of light magic, original character. Same face as the reference sheet: wide oval, round chin, skin #C6866A, medium brown eyes #5A3A2E one eye apart, short nearly straight brows, simple nose, small closed mouth, straight bangs, warm-brown hair #3F2A22 ending at the collarbone, parting on her left. Short cape #C45C4A, cloth star brooch on the chest, soft boots. No crown, no wand, no tiara, no earrings, no ballgown. Curious, glad, or thinking. Never sad, angry, or disappointed. Large shapes, little detail, warm light. Not a movie princess.

Si el generador solo acepta uno, se usa el español. La hoja de referencia va adjunta siempre. Un prompt sin la hoja no se lanza.

### Gemini y Grok

- Una cara por tanda. No una hoja de «variaciones».
- La relación de aspecto de la cara de referencia no se recorta a un primer plano distinto: frente, a la altura de los ojos, misma distancia.
- No pedir estilo de estudio de animación, ojos enormes, chispas en el iris ni «cute».
- Si el resultado cambia el flequillo, el tono de piel, el tamaño del ojo o la edad, se descarta entero. No se corrige con otro generador.

### Tripo

- Solo vistas fijas. Esas vistas no entran como malla en el APK. Si hace falta un dibujo, se exporta un PNG y se compara con la hoja.
- Cámaras cerradas: frente, tres cuartos izquierda, tres cuartos derecha. Misma distancia. Sin contrapicado.
- No reestilizar. No pedir una expresión nueva. No cambiar el peinado para que «funcione en 3D».
- Si la vista fija no coincide con la hoja, se tira. No se vuelve a generar «parecida» sin la misma referencia.

### Lista de descarte

Basta una para tirar la imagen:

- Ojos más grandes o más separados que en la hoja.
- Pelo más largo que la clavícula, de otro color, o sin el flequillo recto.
- Piel de otro tono.
- Corona, varita, diadema, alas, pendientes, vestido de cola.
- Ceño, lágrima, boca hacia abajo, cabeza gacha, dedo que niega.
- Parecido reconocible a una princesa de película o a un castillo de parque.
- Confeti, temblor o un rojo usado como fallo.
- Un detalle menor de 24 px que sea la única pista de algo.

## Prohibido

- Confeti, lluvia de estrellas, explosión más grande si va deprisa.
- Temblor de pantalla, de sprite o de cámara, en el fallo y en el acierto.
- Rojo de error, aspa, flash de fallo, zumbido, botón gris muerto.
- Detalle pequeño. Nada que informe por debajo de 24 px. Nada importante por debajo de 48 px si no se toca, ni por debajo de 88 px si se arrastra.
- Estilo Disney y cualquier princesa o castillo con marca. Ojos de un tercio de la cara. Vestido de baile. Chispas de hada.
- Corona. Varita. Diadema. Alas.
- Estrellas vacías, vidas, marcador, cronómetro, vela que se apaga, cielo que anochece para meter prisa.
- Niebla con ojos, boca o manos. Monstruo. Villano.
- Cara triste, enfadada o decepcionada. Lágrima. Ceño. Suspiro dibujado.
- Foto de una niña real. Nombre real. Vídeo dentro del APK. 3D en la tableta.
- Huecos vacíos de salas cerradas. Candados. Semáforo sobre el saber.

## Sustituto

Si falta un dibujo, una forma de color del mismo tamaño, con el hex de su sala o de su pieza. La forma conserva el tamaño de la tabla de escala. Un sustituto no es una excusa para bajar de 88 px una pieza que se arrastra.

Estrella, si falta el dibujo, es un óvalo `#C6866A` de la altura dicha, con un rectángulo de capa `#C45C4A`. No se le pone una cara improvisada.

## Primer jugable, solo esto

- Estrella, curiosa o pensando, sin corona ni varita. Contenta solo al encender.
- Patio con llama de casa ya encendida. Torre a la derecha. Ala de niebla en un solo bulto.
- Piedras de luz: nido de dos filas de cinco. La décima enciende. Una de más, si el gesto era llenar diez, no enciende y vuelve en silencio.
- Acertijo: piedra, estrella, piedra, estrella. Ella cuelga la siguiente desde un arcón.
- Un farol que ella coloca en la torre. El farol no es una puntuación.
- El pulso de 1,2 s, igual siempre. Sin confeti y sin temblor.

No entra la llevada, ni el euro, ni un problema con historia, ni el resto de salas como sitios donde entrar. Esas puertas, si se ven, son niebla.
