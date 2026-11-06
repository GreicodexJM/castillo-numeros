# Encargo cerrado — Estrella y el Castillo de los Números

Este archivo es la fuente de restricciones. Los expertos amplían y especifican. No contradicen lo cerrado. No inventan datos de una niña real. No hay nombre, foto, edad exacta ni identificadores de dispositivo más allá del modelo de tableta.

Idioma de todo el material: español de España. Vocabulario de colegio: unidades, decenas, centenas, céntimos, «me llevo una», «pido prestada una decena».

## Jugadora

Niña de primer grado, entre 6 y 7 años, que ya lee frases cortas. Las matemáticas le parecen difíciles y se frustra con facilidad. El juego tiene que servir también a niñas y niños de 6 a 10 años sin cambiar de producto: el mismo castillo, techo de contenido más alto, misma regla de no humillar.

Objetivo del padre: que aprenda bien las bases de los números, la aritmética y problemas de lógica, en forma de juego, para que no queden huecos más adelante. El juego anima a seguir. No es un examen.

## Dispositivo

Amazon Fire 7 (2022), modelo KFQUWI, conectada y leída por USB.

- Fire OS 8.3.3.8, Android 11, API 30
- MediaTek MT8168, 4 núcleos, GPU Mali-G52 MC2
- 2 GB de RAM; en reposo quedan unos 620 MB
- Pantalla 7 pulgadas, 1024×600, 60 Hz, unos 171 dpi, densidad 160
- En horizontal, con la barra de sistema, el área útil baja a unos 1024×552
- OpenGL ES 3.2. Vulkan existe y no se usa
- Acelerómetro sí. Giroscopio no
- Multitáctil
- Disco de 10 GB, 91 % usado, unos 900 MB libres
- Sin permiso de internet en el juego
- Instalación futura: APK desde el perfil de padre, añadido a Amazon Kids

## Motor

Godot 4.7.2, solo 2D, renderer Compatibility (OpenGL ES 3). Export arm64-v8a, sin binario de 32 bits. Diseño 1024×600, horizontal, pantalla completa inmersiva. Botones de unos 96 px. APK objetivo por debajo de 80 MB, mejor si cabe en 40. Sin vídeos embebidos. Sustitutos de color si falta un dibujo. Progreso en `user://`.

## Fantasía

Estrella, aprendiz de magia, personaje original. Nada de Disney ni de princesas con copyright. La niebla ha apagado las luces del castillo. Cada sala se enciende entendiendo un método, no acertando un número a ciegas. Tema visual: princesas y magia, cálido, formas grandes, mucho aire, contraste alto, poco detalle. Estrella nunca parece decepcionada, enfadada ni triste por un fallo. Curiosa, contenta o pensando.

El castillo solo gana luz. Nunca se apaga por no jugar. No hay vidas, reloj en pantalla, estrellas vacías ni sonido de error. El premio es decorar la torre, y se gana por jugar, no por hacerlo perfecto.

## Sesión

Unos siete minutos. Siempre acaba en un acierto, aunque haya que acortar. Puede salir cuando quiera y se guarda lo hecho.

1. Una cuenta que ya sabe.
2. La idea de hoy, unos veinte segundos, y la repite ella arrastrando.
3. Tres o cuatro intentos del borde.
4. Un acertijo que no parece un examen.
5. Cierre con una que puede hacer.

Si en el paso 3 falla dos veces, se salta al cierre.

## Orden de aprendizaje

Nada de esto se elimina. Cambia el orden. Una idea nueva cada vez. El nombre difícil llega cuando el gesto ya se entiende. La conmutativa y la asociativa solo se enseñan en la suma. La resta no las cumple.

1. Sentir los números. Ver 1 a 5 sin contar. Contar de uno en uno. Más, menos e igual. Recta hasta 20. El 10 como grupo especial.
2. Hasta 10 y hasta 20. Sumar y restar de 1 y de 2. Amigos del 10. Pasar por el 10: 8+5 = 8+2+3. Conmutativa como truco, sin el nombre todavía.
3. Decenas. 23 = 2 decenas y 3 unidades = 20+3. Sumar decenas sueltas. Pergamino vertical sin llevada.
4. Llevada y préstamo. Solo cuando hacer dieces ya es fácil. Estrella que salta de columna. En la resta, una decena se rompe en 10 unidades.
5. Centenas. La misma idea, una columna más.
6. Mercado. Euros y céntimos. Es cambiar 10 por 1, no una mate nueva. Primero euros enteros. Monedas de 1, 2, 5, 10, 20 y 50 céntimos, y 1 y 2 euros.
7. Veces y reparto. Grupos y reparto justo. Tablas del 2, del 5 y del 10. Los signos × y ÷ después del gesto. Asociativa con tres números pequeños, cuando sumar ya no da miedo.

En paralelo desde el primer día, sala de acertijos: patrones, qué sobra, ordenar, igualdad en dos bandejas, caminos con una condición. Los problemas con historia llegan cuando la cuenta ya se hace con las manos. Primero un paso, con dibujo. Dos pasos, mucho más tarde.

Para 8–10 años el mismo castillo abre el techo: centenas con más soltura, problemas de dos pasos, tablas ya nombradas, repartos con sobra explicada sin castigo. No es otro juego.

## Salas

| Sala | Método |
|---|---|
| Piedras de luz | Descomposición y valor posicional |
| Espejo | Propiedad conmutativa de la suma |
| Círculo | Propiedad asociativa de la suma |
| Pergamino | Suma y resta vertical, alineando C, D y U, con llevada |
| Mercado | Euros y céntimos |
| Jardín | Multiplicación como grupos |
| Tesoro | División como reparto justo |
| Acertijos | Lógica, en paralelo |

Ella manipula. Escribir el número es solo la comprobación. No hay cuatro opciones para adivinar.

## Algoritmos

Locales, en el aparato, sin internet, sin cámara, sin micrófono. Ella no los ve. Los primeros días solo observan.

Se anota, por ejercicio: sola / con ayuda / no; tiempo al primer toque; tiempo manipulando; pausas largas aparte; duración de la sesión; hora de inicio; postura de la tableta (de pie, plana, encima de la cara); duda (suelta en el sitio, cambia de destino, sostiene mucho, se desdice).

La tableta no sabe si la niña está sentada o acostada. Solo la inclinación del aparato. Con pocas partidas, hora y postura no mandan.

1. Saber, por micropaso: sin ver, aprendiendo, frágil, firme, suelto. Pesa más acertar sola y en otro día. Lo firme se repasa. El castillo no se apaga.
2. Seguro no es suelto. Acertar despacio no sube de nivel. Adivinar rápido obliga a mover piezas.
3. Duda. Si acierta dudando, el siguiente es parecido. Si duda y falla, baja un peldaño y se enseña el gesto. Si falla sin dudar y el error es siempre el mismo, hay una frase para ese error.
4. Cansancio de la sesión. Si alarga tiempos, devuelve piezas, encadena fallos o abandona, se corta lo nuevo y viene un acierto fácil.
5. Qué toca. Cada sesión: una que ya sabe, un repaso, un paso del borde y un acertijo. Un paso nuevo solo si el anterior está firme. Si evita una sala, no se cierra; el padre lo ve.

Pueden cambiar: micropaso, tamaño de los números, si las piezas siguen a la vista, la frase de ayuda, la duración y si hoy hay idea nueva.

No pueden: quitar luces, poner cronómetro, cerrar acertijos, enseñar un marcador, enviar datos fuera.

El padre entra con PIN y lee frases, no notas. Puede poner un techo. Puede exportar un resumen a mano.

## Producción de arte y audio

Los generadores se usan en el ordenador de desarrollo, nunca desde el juego. Gemini y Grok Imagine para imagen, Tripo3D solo para sacar vistas fijas, Higgsfield como mucho un clip de 3 o 4 segundos que no va dentro del APK, ElevenLabs para un listado cerrado de frases en español de España, voz cálida y lenta. Hugging Face no corre en la tableta. No se suben fotos de la niña. Si falta un audio, se ve el texto.

## Primer jugable

No empieza por la llevada. Empieza por Estrella, la torre que se decora, la sala de hacer el 10, un acertijo de patrones, el cierre siempre en acierto, el registro de duda al soltar una pieza y el corte por cansancio. Hora y postura se anotan y no mandan hasta tener varias partidas.

## Qué no es este juego

No es una ficha. No es multijugador. No tiene anuncios, compras ni cuentas. No diagnostica. No compara con otros niños. «Lento» significa lento para ella en ese paso.
