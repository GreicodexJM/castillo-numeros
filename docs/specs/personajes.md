# Personajes — Estrella

Este texto obedece a `docs/GDD.md`. Si algo choca, manda el GDD. Los hex de aquí son el cierre de Estrella. Otro capítulo puede nombrar colores del castillo; no le cambia la piel, el pelo ni la ropa.

No hay fotos. No hay nombre de una niña real. No hay parecido con una princesa de película. Nada de Disney.

## Quién hay

Solo Estrella. Aprendiz de magia de las luces. Personaje original. No es reina, no es hada, no espera un baile ni un príncipe. Estudia cómo se enciende una lámpara. También está aprendiendo. No examina.

La niebla no es un personaje. No tiene ojos, ni boca, ni cuerpo, ni voz. No crece si un día no se juega.

No hay tendero, rival, mascota ni narrador. Estrella es la única que habla.

La estrellita que salta en el pergamino, el día de la llevada, no es ella. No se le pone cara, capa ni broche. En el primer jugable esa estrellita no sale.

## Qué no cambia nunca

De un dibujo a otro, esto es el mismo dibujo:

1. La cara: mismas medidas, mismo pelo, misma piel, mismos ojos, misma boca pequeña, mismas mejillas.
2. El pelo: castaño oscuro, melena a la mandíbula, flequillo recto que no tapa los ojos, orejas redondas a la vista. Sin coleta, sin trenza, sin moño, sin diadema, sin horquilla.
3. La ropa: capa corta ámbar, abierta, hasta la cadera; túnica de lino; cinturón; bolsa en su cadera izquierda; botas blandas. Las piernas se ven. La capa no tapa las botas.
4. El broche: estrella de tela de cinco puntas, cosida en el cuello, no de metal y no de joya. Cuando piensa, lo toca.
5. Las manos: grandes, redondas, pulgar claro. En el juego, cuatro dedos juntos más pulgar. Siempre así.
6. La silueta: cabeza redonda, cuello corto, sin cintura de avispa, sin vestido de baile, sin cola de tela en el suelo.

Nunca lleva corona, tiara, velo, varita, cetro, orbe, joyas, guantes largos ni tacón. Su magia no sale de un palo. Enciende lo que las manos entienden.

## Cuerpo

Parece una chica joven, de unos once años en el dibujo. No es un bebé. No es una mujer adulta. No habla como un bebé y el dibujo tampoco la trata como tal.

Se sienta al lado, no enfrente como en un examen. En el patio del primer día puede estar sentada en un escalón, con un farol apagado en el regazo. Eso es la pose quieta, no otra persona.

| Parte | Cierre |
|---|---|
| Cabeza | Redonda, un poco más alta que ancha. Frente amplia. |
| Cuello | Corto. |
| Hombros | Estrechos, no de muñeca. |
| Manos | Grandes, para que el gesto se lea. |
| Pies | Botas blandas, punta redonda, sin tacón. |
| Bolsa | En su cadera izquierda. En vista de frente, a la derecha de la imagen. Tres piedras de luz asoman. Siempre el mismo lado. |

## Colores

Un color de la ropa no es una nota. El ámbar de la capa no significa acierto. El amarillo de la piedra no es una estrella de premio. No hay estrella vacía.

| Uso | Hex | No es |
|---|---|---|
| Piel | `#E2A56B` | porcelana de princesa |
| Sombra de piel | `#C4844E` | suciedad ni morado de susto |
| Mejilla | `#E58B6A` | rubor de vergüenza; va siempre, igual |
| Pelo y cejas | `#4A2E24` | rubio de cuento, negro azabache |
| Ojo | `#3F2A22` | azul, verde o violeta de joya |
| Blanco del ojo | `#F7F1E6` | blanco puro de muñeca |
| Boca | `#C46A52` | rojo de labios, rojo de fallo |
| Capa | `#C85A32` | alarma, error, vestido de baile |
| Forro y broche | `#F2C14E` | oro de corona, metal |
| Costura del broche | `#C45C28` | filigrana |
| Túnica | `#F4E2C0` | blanco de novia |
| Cinturón | `#6E432C` | hebilla de joya |
| Bolsa | `#8A5A3C` | cuero de armadura |
| Piedra de luz | `#F6E27A` | chispa de hada, nota |
| Bota | `#5C3D30` | charol, tacón |
| Contorno | `#3A241C` | negro puro |
| Fondo de la ficha de cara | `#F7F1E6` | escenario |

La luz más clara del personaje es la piedra `#F6E27A`. La capa es cálida y más oscura, para que no compita con la lámpara.

## Proporciones

Unidad: una cabeza. Altura de pie, del nacimiento del pelo a la suela: 4,2 cabezas. No 7 de figura de moda. No 2,5 de bebé.

| Tramo | Cabezas |
|---|---|
| Cabeza | 1,0 |
| Cuello | 0,2 |
| Torso, hasta la cadera | 1,3 |
| Piernas, cadera a suela | 1,7 |

La cabeza es 0,92 de ancha por 1 de alta. Los ojos ocupan 0,18 del alto de la cara, no más. Van separados el ancho de un ojo. La boca mide 0,22 del ancho de la cara.

En 1024×600, horizontal:

| Uso | Tamaño |
|---|---|
| De pie en el patio | 280 px de alto |
| Busto en una sala | 200 px de alto |
| Cabeza, mínimo para leer la cara | 72 px |
| Ficha de referencia, solo producción | 512×512, no va tal cual al APK |

Si falta el dibujo, vale `assets/personajes/estrella-silueta.svg` al mismo alto. Es la pose quieta, cara contenta, formas de estos colores. No se estira. No se le añade corona para «llenar».

## Caras

Solo cuatro. Ninguna triste, enfadada, decepcionada, asustada ni burlona. Un fallo no le cambia la cara a pena. Ante un fallo solo valen curiosa, contenta o pensando. Celebrando no se usa en un fallo.

Lo que no se mueve: forma del ojo, distancia entre ojos, color del iris, grosor de la ceja, ancho de la boca, sitio de las mejillas, nacimiento del pelo.

| Cara | Qué cambia | Qué no hace |
|---|---|---|
| Curiosa | Cejas un poco más altas por fuera. Ojos abiertos del todo. Boca pequeña entreabierta, sin dientes. Mirada al frente o a la pieza. | No es susto. No es un «oh» grande. |
| Contenta | Cejas en arco bajo, simétricas. Comisuras un pelo arriba. Ojos casi igual de abiertos. | No enseña dientes. No es carcajada. |
| Pensando | Una ceja un poco más alta que la otra, las dos suaves. Boca cerrada, comisuras planas. Mirada al broche o a la pieza. | La comisura no baja. La cabeza no cae. No hay suspiro. |
| Celebrando | La misma contenta, comisuras un grado más, mejillas un pelo más redondas, ojos abiertos. | No cierra los ojos. No llora de alegría. No es «contentísima». |

En una cara de 200 px de alto, las comisuras suben unos 2 px en contenta y unos 4 px en celebrando. Nunca más. La boca de curiosa se abre como mucho un 6 % del alto de la cara.

Cejas: nunca en pico, nunca juntas, nunca con el interior caído. Eso se lee como ceño.

Prohibido en cualquier cara: lágrima, ceño, boca hacia abajo, dientes, cabeza gacha, ojos cerrados de pena, dedo que niegue.

## Poses

Cuatro. La cara de cada una es la de la tabla. No se inventa una quinta pose de pena.

### Quieta

Cara contenta. De pie, peso igual, brazos caídos, manos a la vista, sin brazos en jarra. La jarra se lee como enfado.

También vale sentada en un escalón, la misma cara o la curiosa, farol apagado en el regazo. Mismas medidas. No es otro personaje.

Se usa al saludar, al esperar y en el patio. No tapa las piezas.

### Señalando

Cara curiosa. Un brazo hacia las piezas, palma abierta, índice (el dedo largo de la mano simplificada) hacia el objeto. El otro brazo bajo. Señala el nido, la piedra, la varilla o el hueco. Nunca a quien juega. Nunca a cámara como quien regaña. No hay varita que señale por ella.

### Pensando

Cara pensando. Una mano toca el broche. La otra baja. La cabeza puede ladearse hasta 8 grados. La barbilla no baja. Los ojos siguen abiertos. No se lleva la mano a la barbilla de pena. No mira al suelo.

Se usa si una pieza vuelve, si hay duda o si el gesto aún no cierra. Silencio. No suspira.

### Celebrando

Cara celebrando. Una palmada suave, a medias o justo al juntar las manos. Los pies siguen en el suelo. No salta: un salto taparía las piezas. No hay confeti, ni brazos en V, ni corona de luz, ni segunda palmada.

Solo en un acierto. En el cierre, mejor la cinta de la torre que la palmada. Contentísima, no: contenta.

## Ficha de cara

Primero se fija la cara. Todo lo demás usa esa referencia. Tripo, si hace falta, solo para vistas fijas y solo después de esta ficha. Sin vídeo. Sin 3D en la tableta.

La ficha es un retrato de frente, de hombros para arriba, fondo `#F7F1E6`, cara curiosa. El cuerpo entero no entra en esa imagen. El prompt cerrado está debajo y, igual, en `assets/personajes/estrella.json`.

Prompt de referencia, en español:

> Retrato de frente, de los hombros para arriba, fondo liso #F7F1E6, sin escenario. Estrella, personaje original, aprendiz de magia de las luces. Parece una chica joven, de unos once años en el dibujo: no es un bebé, no es una mujer adulta, no es una reina, no es un hada. Cara redonda, un poco más alta que ancha. Piel #E2A56B, sombra #C4844E, mejillas #E58B6A siempre en el mismo sitio. Pelo #4A2E24, melena a la mandíbula, flequillo recto que no tapa los ojos, orejas redondas a la vista, sin coleta, sin trenza, sin moño, sin diadema, sin horquilla. Ojos #3F2A22, blanco #F7F1E6, tamaño medio, separados el ancho de un ojo, sin pestañas largas, sin brillo de cristal. Cejas cortas y suaves, #4A2E24, nunca en pico. Nariz: una curva corta. Boca pequeña #C46A52, sin dientes. Esta ficha es la cara curiosa: cejas un poco más altas por fuera, ojos abiertos, boca pequeña entreabierta sin dientes, mirada al frente, cabeza alta. En el cuello, broche de tela en estrella de cinco puntas, #F2C14E, costura #C45C28, cosido, no de metal y no de joya. Asoma una capa corta #C85A32, sin vestido de baile. Dibujo plano, formas grandes, poco detalle, contorno #3A241C, contraste alto. Esta imagen fija la cara. No generes el cuerpo entero. No cambies el pelo ni la piel en imágenes posteriores. Prohibido: corona, varita, tiara, velo, joyas, maquillaje, lágrima, ceño, tristeza, enfado, decepción, cabeza gacha, sonrisa enorme, dientes, estilo de princesa de película, estilo Disney, foto real, texto, partículas, confeti.

El mismo texto en inglés, para el generador, vive en el JSON. Si el generador ignora el hex, se dicen los colores con estas palabras y no se cambian: piel albaricoque cálida, pelo castaño oscuro, ojos marrón cálido, boca coral suave, broche amarillo de tela, capa terracota.

Cada pose posterior lleva una línea fija: «Misma cara que la ficha de Estrella. No redibujes el pelo, los ojos ni la boca. Solo cambia el gesto indicado.»

## Qué no generar

- Corona, varita, tiara, velo, joyas, vestido de baile, tacón, guantes largos.
- Pelo largo, rubio de cuento, ojos de joya, pestañas de anuncio.
- Lágrima, ceño, boca caída, cabeza gacha, dedo que niegue, dedo hacia quien juega.
- Confeti, salto, brazos en V, aura de hada, partículas, brillo de cristal.
- Texto en el dibujo. Otra cara. Otra edad. Otra piel. Una niña real.
- Un segundo personaje, aunque sea de espaldas.
- La niebla con ojos. La estrellita de la llevada vestida de Estrella.
