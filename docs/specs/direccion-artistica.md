# Dirección artística

Este documento no cambia el juego. Dice **cómo se dibuja** lo que el documento de diseño (`docs/GDD.md`) ya decidió: qué hay en pantalla, dónde y de qué tamaño. Si hay conflicto, manda el GDD.

La referencia cerrada es la cara de Estrella (`assets/personajes/estrella-cara.png`, fijada el 2026-11-06). Todo lo demás se dibuja para que parezca del mismo mundo que esa cara.

Placas de referencia ya dibujadas:

| Archivo | Qué es |
|---|---|
| `assets/pantallas/nido-1024x600.png` | La pantalla del nido, a tamaño real |
| `assets/pantallas/nido-zonas-1024x600.png` | La misma, con las seis zonas numeradas |
| `tools/mockup_nido.py` | El código que la dibuja: si cambia una coordenada, se regenera |

## 1. Estilo, medido sobre la cara fijada

Lo que la cara fijada hace y hay que repetir:

- **Relleno plano.** Un color por forma y, como mucho, **un** segundo tono más oscuro en la mitad de abajo. No hay degradados, no hay texturas, no hay ruido.
- **Línea de contorno continua y gruesa**, de un solo color, `#33160D`. Cierra la forma entera. No hay líneas sueltas ni bocetos.
- **Formas grandes, poco detalle.** Una piedra tiene una silueta y una faceta, nada más. Si un detalle no se ve a tamaño de juego, no se dibuja.
- **Sin brillos ni reflejos.** La cara fijada no tiene destellos en los ojos y el broche no brilla. Nada en el juego tiene brillo especular.
- **Sin sombra proyectada**, salvo una mancha plana bajo lo que se apoya (Estrella, el nido en la pared no lleva).
- **Contraste alto** entre forma y fondo. Ninguna pieza se pierde contra la pared.

Grosor de línea según el tamaño de la pieza, para que el trazo no se coma la forma:

| Pieza | Línea |
|---|---|
| 400 px o más | 6 px |
| 96 a 200 px | 4 px |
| 48 a 96 px | 3 px |
| menos de 48 px | 2 px |

## 2. Paleta

`assets/palette.json` es la lista cerrada. Los colores de Estrella están **medidos** sobre la cara fijada, no elegidos a ojo:

| Uso | Hex |
|---|---|
| Piel | `#E59D65` |
| Pelo y cejas | `#502920` |
| Iris | `#502920` |
| Boca | `#C55733` |
| Capa | `#BF502F` |
| Túnica | `#F1D5AB` |
| Broche de tela | `#F4C254` |
| Costura | `#C45C28` |
| Contorno | `#33160D` |
| Pared de la sala | `#F5EDE2` |
| Suelo de Piedras de luz | `#3D4F8A` |
| Piedra de luz | `#F2E2A0`, sombra `#D8C173` |
| Nido | `#C4925C` |
| Pulso de acierto | `#F4C56D` |

Dos avisos que la cara fijada deja abiertos y no se arreglan dibujando:

- El **iris es del mismo tono que el pelo**. No se separa sin volver a fijar la imagen.
- El **amarillo del broche tira a dorado**. Se acepta mientras se lea como tela cosida; si en el juego parece una medalla, se rehace solo esa pieza, no la cara.

## 3. Cómo se construye cada pieza del primer jugable

Todas las medidas de sitio están en el apartado 5 del GDD. Aquí va solo la construcción.

### Piedra de luz

- Silueta de canto rodado **irregular**, ni círculo ni cuadrado ni hexágono. Trece vértices con radio desigual; la forma es la misma siempre, para que se reconozca.
- Relleno `#F2E2A0`, faceta `#D8C173` en la mitad inferior, contorno 3 px.
- Tres tamaños y ninguno más: **72 px** en el montón, **68 px** dentro de un hueco, **8 a 10 px** en el paño del ejemplo.
- No lleva número, ni letra, ni marca. La cantidad se ve contando, no leyendo.
- No parece un botón: no tiene borde recto, ni relleno de color de marca, ni sombra de relieve.

### Nido

- Marco redondeado de 500×220, `#C4925C`, contorno 6 px, y un segundo trazo interior `#AA7846` a 10 px del borde.
- Dentro, **dos filas de cinco huecos** de 80×80, radio 22, hueco vacío en `#F5EDE2` con contorno 4 px. Separación 92 px.
- El nido se reconoce por los diez huecos, nunca por el color. Si se pinta de otro color, sigue siendo el nido.
- El pulso de acierto nace en el **borde del nido de ella**, no en la pieza: un anillo `#F4C56D` de 6 px que crece y se apaga en 1,2 s.

### Hueco

- Cuadrado redondeado, fondo crema, contorno. Nunca se preilumina.
- El hueco vacío y el hueco lleno se distinguen por la piedra dentro, no por el color del hueco.
- El andamio de 7 y 3 son **huecos vacíos**, no piedras marcadas. No se dibujan las dos cosas a la vez.

### Montón y celda

- Seis celdas de 96×96 en dos columnas de tres, sin dibujar la celda: solo la piedra de 72 dentro de un espacio de 96.
- La celda no lleva recuadro ni fondo distinto. Si se dibuja una bandeja, la bandeja no tiene borde de botón.

### Paño del ejemplo

- Rectángulo redondeado de 200×72, `#F1D5AB`, contorno 3 px.
- Dentro, la cuenta en cifras de 26 px y las piedras pequeñas en dos grupos.
- **No se toca.** No es un botón: no tiene relieve ni cambia al pasar el dedo. Al resetear se apaga en 0,4 s sin pulso ámbar, para que no parezca que se ha roto algo.

### Banda de frase

- 832×56, fondo crema, contorno 3 px, radio 14.
- Texto `#2C2416` de **32 px como mínimo**, alineado a la izquierda con 20 px de margen.
- Como mucho una frase de doce palabras y sin signos de interrogación.

### Campana, ventanas y puertas del patio

- Ventana de 160×160; cuando haya más salas, 96×96 con 24 px de aire, **cuatro por fila como máximo**.
- La ventana abierta se ve por dentro. La que no existe **no se dibuja**: ni candado, ni hueco gris, ni silueta.
- La campana es un arco de 96×96 en la esquina. No mide 48 px y no lleva asa que parezca un botón de menú.

### Collar, ganchos y arcón

- Cordón de 640×96, ganchos de 80×80 separados 120 px.
- El patrón se ve en **forma**, no en color: piedra, estrella, piedra, estrella, hueco.
- La estrella del patrón es de tela, `#F4C254`, como el broche. No brilla.
- El arcón mide 160×220 y está cerrado en el primer jugable: lo que hay dentro no se dibuja.

### Farol de la torre

- Se suelta en 160×160 y se ve entero ahí. Entre ámbar y terracota, los dos válidos.
- Un segundo adorno **no se dibuja** hasta el día en que se gana. No hay silueta de lo que falta, ni rejilla con huecos vacíos.

## 4. Estrella en pantalla

- **112×150**, de pie, sin fondo. La cara fijada se recorta y se le quita el fondo; no se redibuja.
- Tres caras: curiosa, contenta, pensando. **No existe celebrando.**
- Lo que no cambia nunca: corte de pelo, altura de la línea del flequillo, separación de los ojos, forma de la nariz, tamaño de la boca, sitio del broche.
- Un fallo **no cambia la cara**. La señal de fallo es la pieza que vuelve.
- Si a 112×150 las tres caras no se distinguen, no se usa la cara como señal: se queda en curiosa y la señal es la pieza y el pulso.

## 5. Fondos y escenas

- Dos planos como máximo: pared y suelo. Nada más compite con las piezas.
- El suelo empieza a la altura de los pies de Estrella (y = 430 en el nido).
- La pared es lisa, del color de la sala. No lleva estanterías, cuadros ni textura.
- La niebla es una cortina crema `#E7DCC8` sin ojos, sin voz y sin cuerpo. No se dibuja como humo negro.
- Nada de viñetas, desenfoques de fondo, ni luces dinámicas. La tableta no puede con ellas y no hacen falta.

## 6. Estados que se ven y estados que no

| Estado | Qué se dibuja | Qué no |
|---|---|---|
| Acierto | Anillo ámbar de 1,2 s en el borde del nido y la frase 4 s | Confeti, estrellas, destellos, la cara celebrando |
| Fallo | La pieza vuelve a su sitio en 0,4 s, en silencio | Cruces, rojo, temblor, sonido, cara de pena |
| Duda | Nada | Un cartel que nombre la duda |
| Corte | La frase de corte y el cierre | Pantalla de fin, resumen, nota |
| Sin audio | Lo mismo, sin esperar a la campanada | Un icono de altavoz tachado |
| Sin disco | Si cabe, la frase V08 | Un aviso técnico, un número de error |

## 7. Lo que nunca se dibuja

Brillos, degradados, sombras arrojadas, texturas, cristal, joyas, coronas, varitas, alas, ojos con destello, dientes, lágrimas, ceños, caras nuevas, números sobre las piedras, texto dentro de una pieza, botones con relieve, iconos de altavoz, barras de progreso, relojes, marcadores, candados y huecos grises de lo que no existe.

## 8. Producción

1. **Toda imagen de Estrella** se genera tomando `assets/personajes/estrella-cara.png` como referencia, con la instrucción de no redibujar pelo, ojos, boca ni piel. Solo cambia el gesto.
2. **Toda pieza** se genera con el mismo estilo y luego se **limpia**: fondo plano quitado, contorno cerrado, un solo tono de sombra.
3. Se exporta a PNG con transparencia para las piezas y a PNG opaco para las placas de pantalla.
4. La geometría (sitios, tamaños, zonas seguras) **no se genera con IA**: se dibuja con código, como en `tools/mockup_nido.py`. Un modelo de imagen no coloca un hueco a 92 px de otro.
5. Lo que la IA haga con texto saldrá mal escrito: las frases se componen en el juego, nunca dentro de la imagen.

## 9. Archivos que tiene que haber antes de programar

| Archivo | Qué |
|---|---|
| `assets/personajes/estrella-cara.png` | Hecho |
| `assets/pantallas/nido-1024x600.png` | Hecho |
| `assets/piezas/piedra.png` | Piedra de 96 px con transparencia |
| `assets/piezas/nido.png` | Nido de diez huecos |
| `assets/piezas/estrella-tela.png` | Estrella del patrón del collar |
| `assets/piezas/farol.png` | Farol de la torre, dos variantes |
| `assets/piezas/campana.png` | Campana del patio |
| `assets/fondos/piedras.png` | Pared y suelo de 1024×600 |

Mientras falten, el juego usa el sustituto de color plano con el contorno. Un sustituto no es un dibujo: se nota y se sustituye.

## 10. Criterios de rechazo

Un dibujo no entra si:

- Tiene más de dos tonos por forma.
- Tiene brillo, degradado o textura.
- La silueta no se reconoce a tamaño de juego.
- La línea se cierra mal o tiene grosor distinto al de su tamaño.
- Cambia el pelo, la piel, los ojos o la boca de Estrella.
- Pone un número, una letra o un texto dentro de una pieza.
- Dibuja lo que todavía no existe, aunque sea en gris.
- Necesita que alguien explique qué es.
