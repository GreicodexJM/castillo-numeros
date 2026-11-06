# Documento de diseño — Estrella y el Castillo de los Números

Este documento manda. Si un capítulo de experto dice otra cosa, manda lo de aquí. Los capítulos amplían; no reabren lo cerrado.

Capítulos, que forman parte del diseño:

- Juego: `Juego`
- Relato y bancos de frases: `Relato`
- Pedagogía y regla de subida: `Pedagogia`
- Matemáticas, tabla M01–M81: `Matematicas`
- Salas como juguete: `Edutenimiento`

Restricciones de aparato y de producción: el encargo cerrado del repositorio.

## Promesa

Estrella es aprendiz de magia de las luces. No lleva corona ni varita. No se parece a una princesa de película. Su magia no adivina el número: enciende lo que las manos entienden. La niebla ha apagado las luces del castillo. No es un monstruo, no tiene ojos ni voz, y no crece si un día no se juega.

Cada sala es un juguete. La cuenta va dentro del gesto. Escribir el número, si aparece, es la comprobación, después de la luz. No hay cuatro opciones ni un único sitio que brille.

Público: 6 a 7 años, con techo hasta 10 en el mismo castillo. La edad no sube de nivel. Una niña de 9 años con el diez todavía frágil ve las piezas.

## Ocho reglas

1. El castillo solo gana luz. Una sala encendida no se apaga por fallar, por salir ni por no volver.
2. No hay vidas, cronómetro en pantalla, estrellas vacías, sonido de error ni marcador.
3. Toda sesión que ella termina acaba en un acierto que hace con las manos. Estrella no coloca la última pieza por ella.
4. Se enciende un método moviendo piezas. Adivinar no cuenta.
5. Dos fallos en el borde saltan al cierre. No hay un tercero. El acertijo de esa sesión puede esperar. La sala de acertijos no se cierra nunca.
6. La torre se decora por llegar al cierre jugando, no por hacerlo perfecto. Lo colocado no se quita.
7. Ante un fallo, Estrella está curiosa, contenta o pensando. Nunca decepcionada, enfadada ni triste.
8. Un paso nuevo solo si el anterior está firme. Firme es acertar sola, en otro día, sin ejemplo al lado y sin duda.

## Aparato

Fire 7 (2022), KFQUWI. Fire OS 8.3.3.8, Android 11, API 30. MT8168, Mali-G52, 2 GB de RAM. Pantalla 1024×600; en horizontal, con la barra, unos 1024×552. 60 Hz. Acelerómetro sí, giroscopio no. Disco justo: el juego cabe holgado por debajo de 40 MB si puede, y nunca pasa de 80. Sin permiso de internet. Godot 4.7.2, renderer Compatibility, solo arm64, pantalla completa. Botones y piezas de unos 96 px, aire de 24 px. Una frase de hasta 12 palabras. El texto se ve aunque haya voz.

## Salas

Una sola pantalla de mapa, el Patio. No se camina. No se dibujan huecos vacíos de salas cerradas. Lo que no se puede elegir no aparece como botón prohibido.

| Sala | Verbo | Objeto | Qué enseña | Qué no hace |
|---|---|---|---|---|
| Piedras de luz | anidar | nido de diez huecos y piedras | descomposición, valor de posición, hacer el 10 | el algoritmo en columnas |
| Espejo | voltear | espejo y dos montones | conmutativa de la suma | una resta |
| Círculo | enlazar | tres montones y una cinta | asociativa de la suma, tres números pequeños | una resta; no se abre junto al Espejo |
| Pergamino | deslizar | varillas de unidades, decenas y centenas | alinear, llevada, préstamo | la llevada antes de que hacer dieces sea fácil |
| Mercado | cambiar | monedas y un precio | euros y céntimos como cambio de 10 por 1 | billetes; comprar de verdad |
| Jardín | plantar | macetas iguales | grupos del 2, del 5 y del 10 | otras tablas |
| Tesoro | repartir | cofre y cuencos, nunca niños rivales | reparto justo | llamar fallo a la sobra |
| Acertijos | ensartar | cordón, cuentas, bandejas | lógica, desde el día 1 | esconder una resta difícil |
| Torre | colocar | adornos | ninguna cuenta | medir el saber |

Frases de primera visita, literales, en el capítulo de relato. No se improvisan.

## Sesión

Unos siete minutos. El reloj no se dibuja y no corta un arrastre a medias. Se acorta entre turnos.

1. Una cuenta que ya sabe. Los tropiezos de aquí no cuentan para el corte. Se ayuda hasta el acierto.
2. La idea de hoy, unos veinte segundos, en manos de Estrella. Ella la repite arrastrando. Sin vídeo.
3. Tres intentos del borde, o cuatro solo si van sin fallos y sin cansancio. Al segundo fallo se salta al cierre.
4. Un acertijo, si no hubo corte. Un tropiezo aquí no baja la aritmética.
5. Cierre con una que puede hacer. Luego un adorno, a elegir entre dos, los dos válidos.

Si cierra la tableta a medias, se guarda y no se inventa el acierto. Al volver no se reanuda el fallo: se entra por una cuenta que ya sabe. Menos de quince segundos sin tocar una pieza no abre sesión.

Frase del corte, sin nombrar cansancio ni fallo: «Seguimos con una que ya sabes.»

## Primer jugable

Solo esto:

- Estrella, curiosa o pensando, sin corona ni varita.
- Torre con un farol que ella coloca.
- Piedras de luz: hacer el 10. Caja de dos filas de cinco. La décima enciende. Una oncena de más, si el gesto era llenar diez, no enciende.
- Acertijo: piedra, estrella, piedra, estrella. Ella cuelga la siguiente desde un arcón, no elige entre dos botones.
- Cierre siempre en un acierto suyo.
- Registro de duda al soltar: suelta en el sitio, cambia de destino, sostiene mucho, se desdice.
- Corte a los dos fallos y corte si devuelve piezas, encadena fallos o se va.
- Hora y postura de la tableta se anotan y no cambian el juego todavía.

No entra la llevada, ni el euro, ni un problema con historia.

Partida de referencia del primer día, si nada se tuerce: ver tres piedras; Estrella cierra un diez; ella repite 7 y 3; borde 8, luego 5, luego 9; collar piedra-estrella; cierre de una que puede; farol a la torre.

## Orden de apertura

El camino de 6 a 7 años no salta puertas. El de 8 a 10 abre el techo del mismo castillo, no otro juego.

1. Sentir los números y hacer el 10. M01 a M11 viven en la entrada de Piedras. No son una aduana que impida jugar, pero si fallan el borde baja ahí. El primer jugable es M11 y los amigos del 10 cuando toque, no la llevada.
2. Hasta 20, amigos del 10, pasar por el 10. Espejo sin el nombre.
3. Decenas. Pergamino sin llevada.
4. Llevada, solo si amigos del 10 y pasar por el 10 al sumar están firmes. Frase: «Me llevo una.» No se dice «me llevo dos» con dos sumandos.
5. Préstamo, además con el puente de resta firme. «Pido prestada una decena.» La decena se rompe en diez unidades y no se devuelve. No se dice «robamos». No se dice «siempre se resta la cifra pequeña de la grande».
6. Centenas. La misma idea, una columna más.
7. Mercado. Primero euros enteros, cuando el cambio de diez por uno ya se entiende y la resta pequeña está firme. Céntimos después, cuando cien se entiende como diez dieces. Monedas: 1, 2, 5, 10, 20 y 50 céntimos, y 1 y 2 euros. Sin billetes. Se escribe 1,30 €. Frase fija: «Estas monedas son del juego.» «No se compra de verdad.»
8. Jardín, luego el signo ×. Tesoro, luego el signo ÷. Círculo cuando sumar ya no da miedo, no antes del mercado en el camino canónico. Sobra al final, sin castigo y sin fracción.

Tablas solo del 2, del 5 y del 10. No hay tablas del 3, 4, 6, 7, 8 ni 9. No hay negativos, ni millares, ni problemas de más de dos pasos.

Los 81 micropasos, con ejemplo, error, ayuda y puerta, están en el capítulo de matemáticas. Esa tabla es normativa. Los nombres («conmutativa», «asociativa») no bloquean el paso siguiente.

## Algoritmos

Locales. Ella no los ve. No se le dice que ha subido ni que ha bajado. Los primeros días el registro observa y no manda la subida ni la bajada. Desde el primer día sí mandan el cierre en acierto, el corte a los dos fallos, el corte por cansancio y enseñar el gesto si duda y falla.

Estados, de menor a mayor: sin ver, aprendiendo, frágil, firme, suelto. Solo se sube uno. Solo se baja uno. El suelo, una vez vista la idea, es aprendiendo. Bajar no quita luces ni adornos.

Sube a frágil si acierta sola hoy, moviendo piezas. Sube a firme si lo repite sola en otro día, sin ejemplo y sin duda. Sube a suelto si además el gesto ya va sin piezas de apoyo, a su ritmo, sin adivinanza. Lento y bien puede ser firme. Lento es lento para ella, no comparado con nadie. Acertar con ayuda, el acierto de cierre y el primer acierto del día no suben a firme.

Duda: suelta a menos de 24 px del origen tras haberla tenido 1 s; cambia de destino; sostiene más de 8 s; se desdice antes de 3 s. Si acierta dudando, el siguiente es parecido y no sube. Si duda y falla, baja un estado y se enseña el gesto. Si ya estaba aprendiendo, se queda y vuelve el ejemplo. Un fallo aislado sin duda no tira un cimiento firme. Si el error es siempre el mismo, no baja por el primer caso: hay una frase para ese error. Si sigue en otro día, no pasa de frágil.

Cansancio de esta sesión, visible: devuelve piezas, pausas largas que no son un arrastre que avanza, fallos encadenados, se va. Se corta lo nuevo. No se infiere emoción. La hora y la inclinación de la tableta se anotan. No mandan con pocas partidas, ni solas más adelante. No hay giroscopio. No hay cámara ni micrófono.

Qué puede cambiar: el micropaso, el tamaño de los números, si las piezas siguen a la vista, la frase de ayuda, la duración y si hoy hay idea nueva.

Qué no puede: quitar luces, poner cronómetro, cerrar acertijos, enseñar un marcador, enviar datos fuera.

## Padre

Entra con una pulsación larga en la campana del patio y un PIN local. Lee frases, no notas. Puede poner un techo en frontera de bloque: hasta 20, sin llevada, sin mercado, sin centenas, sin el signo de por. El techo solo frena. No apaga luces, no cierra acertijos, no quita adornos. Puede exportar un resumen a mano.

## Voz y fallo

Una frase, luego silencio. La duda no hereda frases de fallo. El acierto no elogia a la persona. Prohibido: «mal», «incorrecto», «eres un genio», «casi», «date prisa», «esto es fácil», cualquier comparación, cualquier etiqueta de emoción o de inteligencia.

Al volver: «Me alegro de verte.» «Tus luces siguen encendidas.» «No hay que recuperar nada.» No se dice «te echaba de menos» ni «se ha apagado».

El listado cerrado de frases está en el capítulo de relato. Si falta un audio, se ve el texto.

## Producción

Los generadores corren en el ordenador de desarrollo, nunca en el juego. La cara la fija `assets/personajes/estrella.json`: melena a la mandíbula, flequillo recto, sin trenza, sin coleta. Si un prompt dice trenza, no se usa. Todo lo demás usa esa referencia. Tripo solo para vistas fijas. Sin vídeo dentro del APK. Sin fotos de una niña real. Si falta un dibujo, vale una forma de color del mismo tamaño.

## Fuera de producto

Multijugador, anuncios, compras, cuentas, diagnóstico, comparación con otros niños, red, 3D en la tableta, Vulkan, vídeo embebido.
