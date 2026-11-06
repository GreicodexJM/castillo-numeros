# Cobertura de 1º

Cada fila es un saber del primer ciclo, recortado a 1º, y el gesto que lo cierra. Si no hay gesto, no está cubierto. Fuente de verdad: `docs/GDD.md`.

| Saber | Estado | Dónde |
|---|---|---|
| Conteo hasta 20 y hasta 99 | Cubierto | Nido y recta, M01–M10, M32 |
| Lectura hasta 999, sin operar millares | Cubierto | Centenas, M47–M51 |
| Estimar y comprobar | Cubierto | Acertijos, señalar y emparejar |
| Descomponer unidades, decenas, centenas | Cubierto | Nido, pergamino |
| Ordenar y comparar | Cubierto | Emparejar, recta |
| Recta numérica | Cubierto | M09, M10 |
| Suma y resta sin llevada | Cubierto | M12–M22, M38–M40 |
| Suma y resta con llevada y préstamo | Cubierto | M41–M46, con puertas |
| Familia suma-resta | Cubierto | M27. No se llama conmutativa |
| Conmutativa de la suma | Cubierto | Espejo. La resta no entra |
| Asociativa de la suma | Cubierto | Círculo. La resta no entra |
| Igual, no igual, dato tapado | Cubierto | Bandejas |
| Cálculo mental ±1, ±2, amigos del 10, puente | Cubierto | M12–M26 |
| Grupos del 2, del 5 y del 10 | Cubierto | Jardín. Otras tablas no entran |
| Reparto exacto y sobra | Cubierto | Tesoro. La sobra no es un fallo |
| Euros y céntimos | Cubierto | Mercado |
| Billetes de 5 y 10 | Techo | Papel de juego. 20, 50 y 100 no entran |
| Longitud | Cubierto | Dos cintas |
| Masa | Cubierto | Balanza de dibujo |
| Capacidad | Cubierto | Vasos |
| Hora en punto y y media | Cubierto | Dos piezas gordas. Sin cronómetro |
| Ayer, hoy, mañana | Cubierto | Tira de tres |
| Semana | Techo | Tira de siete. Meses no entran |
| Metro, kilo, litro | Nombre de después | Sin conversiones |
| Figuras planas | Cubierto | Apartar cuatro formas |
| Cuerpos sencillos | Cubierto | Empujar. Sin 3D |
| Posición | Cubierto | Soltar respecto a Estrella |
| Instrucciones de dos o tres pasos | Cubierto | Losas coge, pon, enciende |
| Recuento | Cubierto | Palitos. No es el nido |
| Pictograma | Cubierto | Pilas que no miden el saber |
| Problemas de un paso | Cubierto | Cuando el gesto ya está |
| Problemas de dos pasos | Techo | Dos momentos dibujados |
| Afecto | Cubierto | Reglas del castillo, no un test |

## Telemetría y control

| Señal | Se guarda | Cambia el juego |
|---|---|---|
| Sola, con ayuda, o no | Sí | Sí, el estado |
| Primer toque, tiempo moviendo, pausas de 4 s | Sí | La pausa triple corta lo nuevo. El lento solo impide suelto |
| Hora de inicio | Sí | No |
| Inclinación de la tableta | Sí | No |
| Duda al soltar o devolver | Sí | No sube. Tres devoluciones cortan lo nuevo |
| Error sistemático | Sí | Frena al sucesor |
| Abandono y sala evitada | Sí | El abandono va al cierre. La sala no se cierra |
| Edad | No | No |

Los umbrales están en los apartados 8, 9 y 10 del documento de diseño.
