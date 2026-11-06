# Acertijos — banco de lógica

Este texto especifica la sala de Acertijos. Obedece `docs/GDD.md`. Si un capítulo dice otra cosa, manda el GDD. No reabre lo cerrado en `BRIEF.md`. No nombra a ninguna niña real. No diagnostica. No compara.

El banco que carga el juego es `data/puzzles.json`. Si esta prosa y el JSON discrepan en una pieza, un gancho o una solución, manda el JSON en el dato y el GDD en la regla. Hoy no discrepan: hay 30 puzles, y el primero del primer jugable es P01.

Idioma: español de España. Una frase de hasta 12 palabras. El texto se ve aunque haya voz. Sin atribución a nadie que no sea el juego.

## Qué manda el primer jugable

P01, y solo P01, entra en el primer jugable.

En el cordón ya hay cuatro piezas: piedra, estrella, piedra, estrella. El quinto gancho está vacío. Ella cuelga la siguiente desde el arcón de piezas. La siguiente es una piedra. No elige entre dos botones.

El capítulo de juego describe ese hueco como círculo, estrella, círculo, estrella. El GDD dice piedra, estrella, piedra, estrella. Manda el GDD. El arcón lleva cuatro piedras y cuatro estrellas, no una pareja de botones y no dos círculos enfrentados a dos estrellas en forma de test.

El capítulo de relato, si el hueco fuera el cuarto, dice que ha puesto la estrella. Aquí el hueco es el quinto: cuatro piezas ya colgadas, y ella cuelga la que sigue. La frase de acierto usa la forma del relato y cambia la pieza: «Has puesto la piedra en el hueco.» La forma de F08 se conserva y se ajusta a la pieza de hoy, como ese banco ya permite: «El hueco pide piedra. El ritmo es piedra, estrella.»

No entra la llevada, ni el euro, ni un problema con historia. No se pregunta cuántas faltan.

## Qué es la sala

Verbo de la sala: ensartar. El primer día se ensarta colgando desde el arcón al cordón. Los otros gestos no sustituyen a ensartar. Se suman, en el mismo patio, cuando el juguete ya está construido. La sala está abierta desde el día 1. No se cierra por fallar, por un techo del padre, por no jugar ni por saltarse el acertijo de una tarde.

Familias, las cinco del encargo:

| Familia | Gesto | Objeto | Victoria | Qué no hace |
|---|---|---|---|---|
| patrón | ensartar | cordón, ganchos, arcón de piezas | la pieza se queda, el collar se alza y se cuelga de un clavo de la torre | no es un test de serie escrita ni dos botones |
| qué sobra | apartar | paño y tapete | la que no pega sale del paño; el paño se asienta y brilla | no hay cuatro botones con la rara ya enmarcada |
| ordenar | ordenar | fila de ganchos | la fila encaja y se hace camino de luz | no es un dictado de cifras; no se pide la distancia |
| bandejas | equilibrar | dos bandejas, o tres en el techo | quedan a la misma altura y la puerta se queda abierta | no es una resta; no se pregunta cuánto falta |
| camino | trazar | losas y una vela | el dedo recorre solo las losas de una condición y llega a la vela | una sola condición; no una cuenta disfrazada |

Ella manipula. Un toque sin arrastre no cuenta. Adivinar no enciende. Escribir un número, si algún día aparece, es la comprobación, después de la luz, y en este banco no hace falta.

## Qué no es un acertijo de este banco

Se tira, y no está en el JSON, cualquier pieza cuya vía corta sea una resta, una llevada o un préstamo.

No se construye:

- «¿Cuántas más hay en la figura 5 que en la figura 2?»
- «Sobra el número que es el resultado de 15 − 8.»
- «Pisa la losa si el número es 15 − 8.»
- «Pisa si es mayor que 12 − 7.»
- 23 en una bandeja y 17 en la otra para preguntar cuánto falta.
- La serie 3, 6, 9, o cualquier tabla del 3, del 4, del 6, del 7, del 8 o del 9.
- Dos condiciones encadenadas («azul y además par») en el primer mes. En el techo, solo si cada condición por separado ya es visible, y aun así no es una resta. Este banco no mete esa pieza: los caminos de aquí tienen una sola condición.
- Un problema con historia. Eso llega cuando la cuenta ya se hace con las manos, en la sala de ese gesto, primero un paso y con dibujo. No vive en este JSON.
- Una resta difícil disfrazada de dragón, de niebla o de precio.

La edad no sube de banda. Una niña de 9 años con el diez todavía frágil ve P01 si el patrón de dos se le cae. Una de 6 años no recibe P26 porque haya cumplido años: lo recibe si el círculo de la suma está firme.

## Bandas

El JSON agrupa por `banda`. La banda crece el juguete. No crece la cuenta por encima de un gesto que ya está firme.

| Banda | Cuándo se ofrece | Qué crece | Qué no entra | Ids |
|---|---|---|---|---|
| 1 | Día 1. También el primer jugable, que solo carga P01 | Cualidad que se ve: ritmo de dos, forma, luz, altura, igual ya visto, un color | Cualquier cuenta; patrón de tres; dos condiciones; «cuántas más» | P01–P08 |
| 2 | El cimiento que pide ese puzle está firme | Cantidad que ya ve o cuenta; recta; emparejar hasta 5 | Distancia entre números; 2, 4, 6, 8; 14 frente a 40 | P09–P16 |
| 3 | El patrón de dos ya no se cae, y el cimiento nombrado está firme | Ritmo de tres; amigos del 10 como dos cajas ya llenas; 2, 4, 6, 8; 10, 20, 30; cuatro piezas si caben | Tabla del 3; resta de dos cifras; «cuántas faltan» | P17–P24 |
| 4 | Techo del mismo castillo. El cimiento de debajo está firme. No es otro juego | Cadena de tres más larga; tres bandejas si el círculo está firme; un camino de grupos de 2; orden de cuatro cantidades ya vistas | Resta difícil; dos condiciones; tablas que este producto no enseña | P25–P30 |

`requiere_firme` es una puerta de no humillar: no se le pone delante un gesto que aún no tiene. No es una aduana para abrir la sala. Si el cimiento no está firme, ese puzle no sale hoy y la sala sigue abierta con otro de banda más baja.

`requiere_alguno`, si viene, basta con uno de la lista. P17 sale si sumar 2 está firme o si los grupos de 2 están firmes. No espera a los dos.

`no_ofrecer_si` aparta un puzle cuando el error de ese nombre sigue activo. P20 no se ofrece si catorce y cuarenta, o quince y cincuenta, se confunden: eso es el micropaso, no un acertijo.

## Cómo se elige

Una sesión, si no hubo corte, ofrece un acertijo. No un menú de 30. No un «1 de 4».

1. El primer jugable ignora el resto y carga P01.
2. Fuera del corte, se miran los puzles cuyo `requiere_firme` está firme, cuyo `requiere_alguno` cumple al menos uno, y a los que no alcanza `no_ofrecer_si`.
3. Se prefiere la banda más baja que aún se le cae. Dentro de ella, se rota la familia, para que no sean todo collares.
4. Cuando en el patio ya hay más de un juguete, ella puede elegir el gesto que ya conoce: ensartar, apartar, ordenar, equilibrar o trazar. No elige un puzle concreto de una lista numerada. No elige uno que esconda un cimiento cerrado: esos no están en la mesa.
5. Acertarlo no salta un cimiento de cuentas. Fallarlo no baja la aritmética y no cierra la sala.
6. Dos fallos en el borde, o cansancio fuerte, saltan al cierre. El acertijo de esa tarde puede esperar. Si al llegar al patio, con el adorno en la mano, se acerca al cordón, puede ensartar. No se la arrastra fuera.

En las dos primeras sesiones del corte se repite hacer el 10. El acertijo, si el camino es el largo, sigue siendo P01. No se adelanta el ritmo de tres.

## Manos, fallo y ayuda

Piezas de unos 96 px. Aire de 24 px. El gancho vacío se ve vacío. No parpadea. La pieza buena, dentro del arcón, no brilla. No hay un único sitio que brille para adivinar, ni cuatro opciones, ni un botón de listo.

El arcón de piezas es del claustro. No es el arcón de la torre, que guarda adornos que no caben en los ganchos. Del arcón de piezas no se tira nada: la pieza que no sigue vuelve a él.

Si la suelta no enciende, la pieza vuelve en silencio. Estrella está curiosa, contenta o pensando. Nunca decepcionada, enfadada ni triste. No hay sonido de error, ni aspa, ni vida, ni estrella vacía.

Un tropiezo aquí no es un golpe del borde. A la segunda suelta que no enciende, Estrella hace el gesto en su lado. Ella coloca la pieza real en el suyo. Estrella no coloca la última pieza por ella. Una sola ayuda, y se sigue. Un acertijo no se queda a medias si ella sigue en la sesión.

La duda al soltar se anota y ella no la ve: suelta a menos de 24 px del origen tras tenerla 1 s; cambia de destino; sostiene más de 8 s; se desdice antes de 3 s. La duda no hereda frases de fallo de mates. Si acierta dudando, el siguiente acertijo es del mismo tipo. No sube un micropaso de cuenta, que este gesto tampoco subía.

Si se va, el collar a medias no se castiga. Las luces ya encendidas siguen. No se inventa el acierto.

El reloj no se dibuja. El tamaño de diseño de este tramo, ya cerrado en el capítulo de juego, es de unos 70 s, con tope de 90 s, y entonces se va al cierre.

## Frases

Una frase, luego silencio. No se dice «mal», «incorrecto», «eres un genio», «casi», «date prisa», «esto es fácil», «examen», ni ninguna comparación, ni una etiqueta de emoción o de inteligencia.

Las de patrón usan la forma de F08, cambiando solo las piezas de hoy. Las de bandejas pueden usar «Las dos bandejas pesan igual.» El resto de las líneas de este banco están listadas en el JSON, en `frase` y `frase_ayuda`. No se improvisan en la partida. Si falta el audio, se ve el texto.

La pregunta, cuando la hay, se responde arrastrando. Estrella no espera una palabra.

## Aparato

Fire 7, horizontal, área útil de unos 1024×552. Una idea en pantalla: el juguete, una frase, la vuelta al patio.

El sendero de los caminos cabe: cuatro losas de 96 px con aire de 24 px ocupan 456 px de ancho. Cuatro torres en fila ocupan lo mismo. El arcón va abajo, ancho, con varias piezas de cada tipo sueltas, no alineadas como un control de dos opciones. El cordón cuelga a la altura de la mano, no en el borde.

Si falta el dibujo, vale una forma de color del mismo tamaño. Piedra: círculo `#F2E2A0`. Estrella: `#F4C56D`. Oscura: `#3D4F8A`. El patio de Acertijos, si hace falta un plano, es `#8E7CC3`. El juguete se entiende igual.

Como mucho, en este juguete, las piezas del cordón, las del arcón que se ven a la vez (ocho en P01) y Estrella. No hay vídeo. No hay red.

## Catálogo

Treinta puzles. Cada ficha dice presentación, gesto, solución, error típico y cimiento al que acompaña. El dato de piezas está en el JSON.

### Banda 1 — día 1

#### P01. Piedra, estrella, piedra, estrella

Primer jugable. Único acertijo de ese corte.

Presentación. Cordón con cuatro piezas ya colgadas: piedra, estrella, piedra, estrella. Quinto gancho vacío, sin brillo. Arcón de piezas con cuatro piedras y cuatro estrellas, revueltas, no enfrentadas como botones.

Gesto. Ensartar. Coge una pieza del arcón y la cuelga en el gancho vacío.

Solución. Una piedra.

Error típico. Cuelga una estrella porque es la última que ha visto. O busca dos números y los resta.

Cimiento. Ninguno. Acompaña el mirar, en paralelo a hacer el 10, sin usarlo. No exige M11 ni lo enseña.

Frase. «¿Qué sigue en el hueco?» Ayuda. «El hueco pide piedra. El ritmo es piedra, estrella.» Acierto. «Has puesto la piedra en el hueco.»

#### P02. Luz, oscura, luz, oscura

Presentación. Cuatro cuentas: luz, oscura, luz, oscura. Quinto gancho vacío. Arcón con cuatro luces y cuatro oscuras.

Gesto. Ensartar desde el arcón.

Solución. Una luz.

Error típico. Cuelga otra oscura. O cuenta las cuentas para restar.

Cimiento. Ninguno.

Frase. «Sigue el collar.» Ayuda. «El hueco pide luz. El ritmo es luz, oscura.»

#### P03. Círculo, cuadrado, círculo, cuadrado

Presentación. Cuatro cuentas de forma: círculo, cuadrado, círculo, cuadrado. Arcón con cuatro de cada. No es el primer jugable: el primero es piedra y estrella, no círculo y estrella.

Gesto. Ensartar desde el arcón.

Solución. Un círculo.

Error típico. Cuelga un cuadrado. O trata las formas como cifras.

Cimiento. Ninguno.

Frase. «Mira lo que se repite.» Ayuda. «El hueco pide círculo. El ritmo es círculo, cuadrado.»

#### P04. Tres redondas y una cuadrada

Presentación. Paño con tres piedras redondas y una cuadrada. Tapete vacío al lado. No hay marco de «elige una de cuatro».

Gesto. Apartar. Arrastra la que no pega al tapete.

Solución. La cuadrada.

Error típico. Aparta una redonda. O hace 4 − 3.

Cimiento. Ninguno. Acompaña el mirar la forma, en paralelo a ver de un vistazo, sin exigir el número.

Frase. «¿Cuál no pega?» Ayuda. «Las redondas van juntas. La cuadrada sale.»

#### P05. Tres encendidas y una apagada

Presentación. Paño con tres luces cálidas encendidas y una apagada. Se puede señalar con el dedo porque la razón se ve. El acierto es apartarla, no decirla.

Gesto. Apartar la apagada al tapete.

Solución. La apagada.

Error típico. Aparta una encendida. O cuenta las luces.

Cimiento. Ninguno.

Frase. «¿Cuál no pega?» Ayuda. «Tres están encendidas. La apagada sale.»

#### P06. Tres torres, de baja a alta

Presentación. Tres torres sueltas, de altura clara: baja, media, alta. Sin números pintados. Sin ladrillos que inviten a restar. Fila de tres ganchos.

Gesto. Ordenar. Arrastra cada torre a la fila, de la más baja a la más alta.

Solución. Baja, media, alta.

Error típico. Las pone de alta a baja. O cuenta ladrillos para hallar la diferencia. No se le pide cuántos ladrillos hay de más.

Cimiento. Acompaña el más y el menos que se ven (M06), sin exigirlo y sin medirlo. `requiere_firme` vacío: la altura se ve el día 1.

Frase. «De la baja a la alta.» Ayuda. «La más baja va primero.»

#### P07. Dos y dos, en otro sitio

Presentación. Bandeja A: dos piedras en fila. Bandeja B: dos piedras en triángulo. Ya pesan igual. Un hilo en la mesa. El arcón no ofrece una tercera piedra como solución.

Gesto. Equilibrar. Pasa el hilo de cada piedra de A a su pareja en B, o baja las dos bandejas a los ganchos. No añade. No quita.

Solución. Dejarlas iguales. Emparejar basta. Si añade una, la pieza vuelve y las bandejas no se asientan.

Error típico. Añade una para que «se vea más». O resta. O cree que igual exige la misma forma.

Cimiento. Acompaña el igual (M06) y ver dos (M01). No los exige. No hay que escribir nada.

Frase. «¿Pesan igual?» Ayuda. «Las mismas piedras, aunque cambien de sitio.»

#### P08. Solo las losas azules

Presentación. Sendero de la plantilla `sendero_a`. Unas losas azules llegan a la vela. Unas cálidas están al lado y no llegan. Una muestra azul, grande, junto a la frase. Una sola condición.

Gesto. Trazar. El dedo recorre solo las azules hasta la vela.

Solución. El camino marcado en la plantilla: inicio, y las azules que lo siguen, hasta la vela. Pisar una cálida apaga el trazo en silencio. No es un fallo del borde.

Error típico. Pisa la cálida porque está más cerca. O busca un número en la losa. No lo hay.

Cimiento. Ninguno.

Frase. «Solo las losas azules.» Ayuda. «El dedo sigue el azul hasta la vela.»

### Banda 2 — cuando ese mirar ya está firme

#### P09. Uno, dos, tres, cuatro

Presentación. Cordón con fichas de puntos: 1, 2, 3, 4, en constelación, no en cifra suelta. Quinto gancho vacío. Arcón con fichas del 1 al 6, varias de cada, no dos botones.

Gesto. Ensartar la ficha que sigue.

Solución. La ficha de 5 puntos.

Error típico. Cuelga la de 6. O resta 4 − 1. O la trata como una suma nueva.

Cimiento. Acompaña contar hasta 5 y hasta 10 (M03, M04). Exige los dos firmes. Es el contar, no una suma nueva. No se pide cuántas más hay que en la primera ficha.

Frase. «¿Qué ficha sigue?» Ayuda. «Después del cuatro va el cinco.»

#### P10. Tres figuras del dos y una del cinco

Presentación. Paño con tres fichas en la constelación del 2 y una en la del 5. La del 5 no es la misma figura. No se ofrece mientras ver 2 y ver 5 no estén firmes.

Gesto. Apartar la del 5 al tapete.

Solución. La ficha del 5.

Error típico. Aparta un 2. O calcula 5 − 2 = 3 y cree que esa es la pregunta.

Cimiento. Acompaña ver 1, 2 y 3 y ver 4 y 5 (M01, M02). Exige los dos. Sobra por la figura, no por la resta.

Frase. «¿Cuál no es la misma figura?» Ayuda. «Esa no es la figura del dos.»

#### P11. Tres, ocho y cinco en la recta

Presentación. Recta del 0 al 10, con marcas. Tres fichas sueltas: 3, 8 y 5. No hay cinta de medir. No se pregunta cuánto hay de 3 a 8.

Gesto. Ordenar. Coloca cada ficha en su marca, de menor a mayor. El orden queda 3, 5, 8.

Solución. 3, luego 5, luego 8, cada una en su sitio de la recta.

Error típico. Las pone al revés. Junta el 8 con el 3 por el tamaño del dibujo. Resta 8 − 3.

Cimiento. Acompaña la recta del 0 al 10 (M09). La exige firme. Es orden, no resta.

Frase. «Del pequeño al grande.» Ayuda. «Cada ficha va a su marca.»

#### P12. Tres y dos frente a cuatro y uno

Presentación. Bandeja A: 3 rojas y 2 amarillas. Bandeja B: 4 rojas y 1 amarilla. Las dos tienen 5. Se puede emparejar piedra con piedra. No hace falta escribir 3 + 2 = 4 + 1. No se pide cuánto le falta a una.

Gesto. Equilibrar. Pasa el hilo de cada piedra a su pareja. Las bandejas ya están iguales: bajarlas también vale. Mover piezas hasta cambiar el 5 no enciende.

Solución. Ver que ya son iguales, emparejando. Dejarlas.

Error típico. Pasa piedras de una a otra hasta deshacer el 5. Encadena igualdades. Resta.

Cimiento. Acompaña el igual hasta 5 y hasta 10 (M06, M07). Exige contar hasta 5 firme (M03), para que emparejar no sea un lío. No exige la suma.

Frase. «Empareja piedra con piedra.» Ayuda. «Las dos bandejas tienen las mismas.»

#### P13. Losas con dos puntos

Presentación. La misma plantilla `sendero_a`. La condición es la ficha de dos puntos, visible, como la muestra. Las otras losas tienen un punto o tres. Una sola condición. No dice «par».

Gesto. Trazar solo las losas de dos puntos hasta la vela.

Solución. El camino de la plantilla, cuyas losas buenas llevan dos puntos.

Error típico. Pisa la de un punto o la de tres. O resta 3 − 2.

Cimiento. Acompaña ver el 2 (M01). Lo exige firme. Si no lo está, la condición de ese día es el color, que es P08.

Frase. «Solo las losas con dos puntos.» Ayuda. «Dos puntos, como la muestra.»

#### P14. Dos, uno, dos, uno

Presentación. Cordón con fichas de puntos: 2, 1, 2, 1. Arcón con varias fichas de 1, de 2 y de 3. No es una suma.

Gesto. Ensartar la que sigue.

Solución. La ficha de 2.

Error típico. Cuelga la de 1, repitiendo la última. O suma 2 + 1.

Cimiento. Acompaña ver el 2 y el 1 (M01). Lo exige firme.

Frase. «Mira lo que se repite.» Ayuda. «El hueco pide dos. El ritmo es dos, uno.»

#### P15. Tres grupos de dos y uno de tres

Presentación. Paño con tres fichas de dos puntos y una de tres puntos. La de tres no es la misma figura.

Gesto. Apartar la de tres.

Solución. La ficha de 3 puntos.

Error típico. Aparta una de dos. O calcula 3 − 2.

Cimiento. Acompaña ver 2 y 3 (M01). Lo exige firme. No es una resta de uno.

Frase. «¿Cuál no es la misma figura?» Ayuda. «Esos son dos. Este es tres.»

#### P16. Faroles de uno, tres y cinco

Presentación. Tres faroles con puntos que se ven: 1, 3 y 5, en constelación. El marco de los tres es del mismo tamaño, para que el marco no mande. Fila de tres ganchos.

Gesto. Ordenar de menos puntos a más.

Solución. 1, 3, 5.

Error típico. Ordena por un brillo o por el marco. Pregunta cuántos puntos más tiene el de 5. No se le contesta con una resta: se le vuelve a la fila.

Cimiento. Acompaña ver hasta 5 (M01, M02) y el más y el menos (M06). Exige M01 y M02. No pide la distancia.

Frase. «De menos puntos a más.» Ayuda. «Mira los puntos, no el marco.»

### Banda 3 — el ritmo de dos ya no se cae

#### P17. Dos, cuatro, seis, ocho

Presentación. Cordón con fichas que se ven como grupos de dos: 2, 4, 6, 8. Arcón con varias fichas de 2, 4, 6, 8 y 10. No hay ficha de 9 ni de 7. Diez se ve como cinco pares o como la caja, no como una suma nueva escrita.

Gesto. Ensartar la que sigue.

Solución. La ficha de 10.

Error típico. Cuelga otra de 8. Busca el 9. Resta. Canta una tabla.

Cimiento. Acompaña sumar 2 dentro del 10 (M16) o los grupos de 2 (M68). Exige uno de los dos, firme. No aparece si ninguno lo está. No es la tabla del 3: 3, 6, 9 no existe en este banco.

Frase. «¿Qué grupo sigue?» Ayuda. «Otro grupo de dos. Ya son diez.»

#### P18. Diez, veinte, treinta

Presentación. Cordón con cajas cerradas: una, dos, tres. No se abren en este acertijo. Arcón con manojos de una, dos, tres, cuatro y cinco cajas. El quinto gancho espera un manojo, no una cifra.

Gesto. Ensartar el manojo que sigue.

Solución. Cuatro cajas cerradas.

Error típico. Cuelga tres otra vez. Dice treinta y uno. Abre las cajas y se pierde en las sueltas.

Cimiento. Acompaña contar de 10 en 10 (M32). Lo exige firme. No es una resta de decenas.

Frase. «¿Qué sigue en la fila?» Ayuda. «Después de tres cajas van cuatro.»

#### P19. Siete con tres, y seis con cuatro

Presentación. Dos cajas de diez huecos, ya llenas. Una tiene 7 y 3. La otra, 6 y 4. Las dos se ven cerradas. No hay hueco que completar. No se pregunta cuánto falta: no falta nada.

Gesto. Equilibrar. Empareja o baja las dos cajas a los ganchos. La puerta se queda abierta porque ya pesan igual.

Solución. Dejarlas. Las dos llenan una caja.

Error típico. Resta 7 − 6. Quita piedras para «hacer la cuenta». Trata el equilibrio como una llevada.

Cimiento. Acompaña los amigos del 10 (M23) y la caja de diez (M11). Exige los dos firmes. Es lógica de equilibrio, no una llevada.

Frase. «Las dos cajas se llenan.» Ayuda. «Siete con tres. Seis con cuatro.»

#### P20. Catorce, cuarenta y quince

Presentación. Tres manojos, no un dictado. Catorce: una caja y cuatro sueltas. Quince: una caja y cinco sueltas. Cuarenta: cuatro cajas cerradas. La recta hasta 40 tiene el 10 marcado. No se pide la distancia entre 15 y 40.

Gesto. Ordenar los manojos de menor a mayor: 14, 15, 40.

Solución. Catorce, quince, cuarenta, cada manojo en su tramo.

Error típico. Junta catorce y cuarenta porque suenan cerca. Resta 40 − 15. Lee quince como cincuenta.

Cimiento. Acompaña contar hasta 20 (M08) y del 11 al 19 (M31). Exige los dos firmes. No se ofrece si el error catorce/cuarenta o quince/cincuenta sigue activo: entonces no es un acertijo, es el micropaso, y se vuelve a las cajas. No enseña el nombre. No lo salta.

Frase. «Del pequeño al grande.» Ayuda. «Catorce es una caja. Cuarenta son cuatro.»

#### P21. Losas con caja cerrada

Presentación. Plantilla `sendero_a`. Las losas del camino llevan una caja cerrada. Las otras llevan piedras sueltas. Una sola condición. La muestra es una caja cerrada.

Gesto. Trazar solo las losas de caja cerrada hasta la vela.

Solución. El camino de la plantilla.

Error típico. Pisa las sueltas. Cuenta 10 − algo. Abre la caja para mirar dentro: no hace falta, y la losa no se abre en este juguete.

Cimiento. Acompaña la caja de diez (M11). La exige firme. Si la caja aún no se reconoce, ese día el camino es el color (P08) o los dos puntos (P13), no este.

Frase. «Solo las losas con caja cerrada.» Ayuda. «La caja cerrada es el camino.»

#### P22. Rojo, rojo, azul

Presentación. Cordón: rojo, rojo, azul, rojo, rojo, azul. Séptimo gancho vacío. Arcón con cuatro rojas y cuatro azules. Ritmo de tres. Solo cuando el de dos ya no se cae.

Gesto. Ensartar la que sigue.

Solución. Una roja.

Error típico. Lo lee como rojo, azul, rojo, azul, y cuelga una azul.

Cimiento. Ninguno de cuenta. Acompaña el patrón de dos, que ya no se cae. No sube la aritmética.

Frase. «Mira el grupo de tres.» Ayuda. «Rojo, rojo, azul. Otra vez rojo.»

#### P23. Tres macetas de dos y una de cinco

Presentación. Paño con cuatro macetas. Tres tienen dos flores. Una tiene cinco, en la figura del dado. La de cinco no es la misma figura. No se pregunta cuántas flores sobran.

Gesto. Apartar la maceta de cinco al tapete.

Solución. La maceta de cinco flores.

Error típico. Aparta una de dos. Calcula 5 − 2. Cuenta todas las flores del paño para restar.

Cimiento. Acompaña ver 2 y ver 5 (M01, M02). Exige los dos. Si los grupos de 2 ya se han visto, acompaña también ese mirar (M67), sin exigirlo.

Frase. «¿Cuál no es la misma figura?» Ayuda. «Esas tienen dos. Esta tiene cinco.»

#### P24. Cuatro torres

Presentación. Cuatro torres de altura clara, sin números: muy baja, baja, media, alta. Caben en la fila: cuatro piezas de 96 px y tres aires de 24 px. Solo cuando ordenar tres por altura ya no se cae.

Gesto. Ordenar de la más baja a la más alta.

Solución. Muy baja, baja, media, alta.

Error típico. Las pone al revés. Mide la diferencia de altura. No se le pide.

Cimiento. Acompaña el más y el menos que se ven (M06). No lo exige por el número: lo exige el puzle de tres torres ya firme en sus manos. Sin cifras.

Frase. «De la baja a la alta.» Ayuda. «La más baja va primero.»

### Banda 4 — techo, el mismo castillo

No hay reloj nuevo, ni otro tono, ni una resta más difícil por ser mayor.

#### P25. Piedra, estrella, luz

Presentación. Cordón más largo, todavía visible: piedra, estrella, luz, piedra, estrella, luz. Séptimo gancho vacío. Arcón con cuatro de cada una de las tres. No dos botones.

Gesto. Ensartar la que sigue.

Solución. Una piedra.

Error típico. Repite solo estrella y luz. Resta las tres formas. Se pierde porque la tira es larga: la ayuda vuelve a decir el grupo de tres, una vez.

Cimiento. Ninguno de cuenta. Acompaña el ritmo de tres (P22), que ya no se cae.

Frase. «Mira el grupo de tres.» Ayuda. «Piedra, estrella, luz. Otra vez piedra.»

#### P26. Tres bandejas con cinco

Presentación. Tres bandejas, ya iguales. Una: 2 y 3. Otra: 4 y 1. Otra: 5 sueltas. Las tres tienen 5. No se escribe 3 + 2 = 5 = 4 + 1. Si aparece esa cadena, se rehace en bandejas. No es un examen de álgebra.

Gesto. Equilibrar. Empareja las tres, o las baja a la misma altura. No pasa piedras para cambiar el 5.

Solución. Dejarlas. Las tres pesan igual.

Error típico. Encadena igualdades. Resta una bandeja de otra. Cree que solo hay una pareja buena.

Cimiento. Acompaña el círculo de la suma (M65) y juntar dentro del 10 (M19). Exige M65 firme. Es lógica de igual, no una suma nueva. No se abre el día 1.

Frase. «Las tres tienen las mismas.» Ayuda. «Empareja las tres. Ya están iguales.»

#### P27. Losas con un grupo de dos

Presentación. Plantilla `sendero_a`. Cada losa del camino muestra dos puntos juntos, un grupo que se ve. Las otras muestran un punto suelto o cinco. Una sola condición. No es «azul y además par». No se usa la palabra par si estorba: se ve el grupo.

Gesto. Trazar solo esas losas hasta la vela.

Solución. El camino de la plantilla.

Error típico. Pisa la de cinco. Resta. Espera una segunda condición que no está.

Cimiento. Acompaña los grupos de 2 (M68). Los exige firmes. Si no lo están, la condición es el color.

Frase. «Solo las losas con un grupo de dos.» Ayuda. «Dos juntos. Las otras no.»

#### P28. Dos, cuatro, cinco y diez

Presentación. Cuatro fichas con puntos que se ven: 2, 4, 5 y 10. El 10 es dos filas de cinco, no una cifra sola. Marcos iguales. No se pregunta cuántos más tiene el 10 que el 2.

Gesto. Ordenar de menos puntos a más.

Solución. 2, 4, 5, 10.

Error típico. Ordena por el marco. Calcula diferencias. Pone el 10 la primera porque la ficha «pesa».

Cimiento. Acompaña contar hasta 10 (M04) y más, menos e igual hasta 10 (M07). Exige los dos. Es orden, no resta.

Frase. «De menos puntos a más.» Ayuda. «Mira los puntos, no el marco.»

#### P29. Rojo, rojo, azul, y una que no

Presentación. Paño con seis cuentas en fila: rojo, rojo, azul, rojo, rojo, amarilla. La amarilla rompe el ritmo de tres. No es la «respuesta de una resta».

Gesto. Apartar la amarilla al tapete. Las otras se quedan y el paño se asienta.

Solución. La cuenta amarilla.

Error típico. Aparta un rojo. Cuenta las rojas y resta. Lee la fila como rojo, azul, rojo, azul.

Cimiento. Ninguno de cuenta. Acompaña el ritmo de tres (P22), que ya no se cae.

Frase. «¿Cuál no sigue el ritmo?» Ayuda. «El ritmo es rojo, rojo, azul.»

#### P30. La caja cerrada y las diez sueltas

Presentación. Bandeja A: una caja cerrada. Bandeja B: diez piedras sueltas. Ya son las mismas. No se abre la caja para restar. No se pregunta cuántas faltan.

Gesto. Equilibrar. Empareja, o baja las dos bandejas. Añadir o quitar no enciende: la pieza vuelve.

Solución. Dejarlas. La caja cerrada y las diez sueltas pesan igual.

Error típico. Abre la caja y cree que el número ha cambiado porque la forma cambió. Inventa una resta. Añade piedras a la caja cerrada.

Cimiento. Acompaña la caja de diez (M11) y el igual (M06). Exige M11 firme. No enseña el 10: lo usa cuando ya está firme. Por eso vive en el techo del banco, no en el primer jugable.

Frase. «¿Pesan igual?» Ayuda. «La caja cerrada vale las diez sueltas.»

## Plantilla del sendero

La usan P08, P13, P21 y P27. Cambia la marca. No cambia el camino. Así el juguete es el mismo y la idea nueva, si la hay, es solo la condición.

Losas, en una cuadrícula de 4 por 3. La vela está en la última del camino.

| Id | Casilla | En el camino | Qué lleva en P08 |
|---|---|---|---|
| s | columna 0, fila 1 | sí, inicio | azul |
| a | columna 1, fila 1 | sí | azul |
| c | columna 1, fila 0 | sí | azul |
| d | columna 2, fila 0 | sí | azul |
| v | columna 3, fila 0 | sí, vela | azul |
| t1 | columna 2, fila 1 | no | cálida |
| t2 | columna 0, fila 0 | no | cálida |
| t3 | columna 2, fila 2 | no | cálida |

Camino: s, a, c, d, v. En P13 las del camino llevan dos puntos y las otras, uno o tres. En P21, caja cerrada frente a sueltas. En P27, un grupo de dos frente a un punto o cinco.

Pisar una losa que no es del camino apaga el trazo. Silencio. Puede seguir. No suma un fallo de mates.

## Qué ve el padre

Una frase, no una nota. Si evita la sala, la sala sigue abierta. Ejemplo de frase, ya en el tono del castillo: los acertijos siguen abiertos. No se le dice a ella. El techo del padre no cierra esta sala y no apaga su luz.

## Qué no puede el juego, tampoco aquí

Quitar luces. Poner un cronómetro en pantalla. Cerrar acertijos. Enseñar un marcador. Enviar datos fuera. Decirle que ha subido o que ha bajado. Usar este banco para colar una llevada, un préstamo o una resta que aún no está firme.
