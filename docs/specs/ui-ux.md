# Interfaz

Las pantallas del primer jugable, con sus zonas en píxeles y lo que pasa al tocarlas. Las coordenadas salen del apartado 5 de `docs/GDD.md`; lo que este documento añade son los estados, el texto y los casos raros.

Las placas están dibujadas a tamaño real en `assets/pantallas/`, cada una con su versión `-zonas`:

| Placa | Pantalla |
|---|---|
| `patio-1024x600.png` | Patio |
| `nido-1024x600.png` | Nido |
| `collar-1024x600.png` | Collar |
| `torre-1024x600.png` | Torre |
| `padre-1024x600.png` | Padre |
| `cierre-1024x600.png` | Cierre del día |
| `farol-1024x600.png` | Elegir farol |

Se regeneran con `tools/mockup_pantallas.py` y `tools/mockup_nido.py`. Si cambia una coordenada en el GDD, se cambia ahí y se vuelven a dibujar: la placa no es una ilustración, es la medida.

## 1. Lienzo

- 1024×600. Área útil x 48–976, y 24–552. Los 48 px de abajo no llevan nada que se toque.
- Horizontal bloqueado. Si el sistema pide vertical, la escena no gira: letterbox y las piezas sin rotar.
- Un dedo. El segundo dedo no suelta la pieza del primero, no pulsa atrás y no abre una sala.
- Nada de hover, nada de doble toque, nada de pulsación larga salvo la campana (1,5 s).
- Ningún hueco se preilumina y no hay botón de «listo».

## 2. Transiciones

```
Arranque ──▶ Patio
Patio ──▶ Nido ──▶ Cierre ──▶ Farol ──▶ Patio
Patio ──▶ Collar ──▶ Patio
Patio ──▶ Torre
Patio ──▶ Padre (solo desde la campana)
```

- Fundido corto, 200 ms, entre pantallas. Nada de diapositivas ni rebotes.
- El collar y el nido son pantallas propias: no hay cordón de camino, ni pasillo.
- Con un cierre pendiente el patio muestra la bandeja de ese cierre **o** las ventanas, no las dos.

## 3. Patio

Fondo noche `#1E2A4A`, suelo `#28365C`. Nada más: ni textura, ni estanterías, ni ventanas cerradas, ni candados.

| Zona | Rectángulo | Qué hace |
|---|---|---|
| Nido (Piedras) | 160, 180, 160, 160 | Abre el nido |
| Collar (Acertijos) | 432, 180, 160, 160 | Abre el collar |
| Torre | 704, 180, 160, 160 | Abre la torre |
| Campana | 880, 24, 96, 96 | Pulsación de 1,5 s: pantalla del padre |

- Las ventanas son arcos de castillo con el borde grueso. Lo que hay dentro se ve desde fuera: el nido, el patrón del collar, el farol.
- Cuando haya más salas, 96×96 con 24 px de aire y **cuatro por fila como máximo**.
- Lo que no está abierto no se dibuja. No hay hueco gris.
- Menos de 15 s sin tocar una pieza no abre sesión y no cuenta como sala evitada.

## 4. Nido

| Zona | Rectángulo |
|---|---|
| Marco del nido | 80, 108, 500, 220 |
| Hueco c, r | x = 100 + c×92, y = 128 + r×92, 80×80 |
| Celda del montón c, r | x = 640 + c×96, y = 120 + r×96, 96×96, piedra de 72 |
| Estrella | 848, 280, 112, 150 |
| Banda de frase | 96, 468, 832, 56 |
| Paño del ejemplo | 80, 24, 200, 72 (solo si toca) |

- Soltar vale si el centro de la pieza queda a **36 px o menos** del centro del hueco.
- Un toque quieto, sin mover 24 px, no es intento. La piedra no parece un botón; el botón es un arco.
- Acierto: anillo ámbar en el **borde del nido de ella**, 1,2 s, y la frase 4 s. Un solo pulso a la vez.
- Pieza rechazada: vuelve en 0,4 s, en silencio.
- El paño del ejemplo, al resetear, se apaga en 0,4 s **sin** pulso ámbar.
- El andamio de 7 y 3 son huecos vacíos, no piedras marcadas.

## 5. Collar

| Zona | Rectángulo |
|---|---|
| Cordón | 96, 220, 640, 96 |
| Gancho i | x = 120 + i×120, y = 228, 80×80 |
| Arcón | 800, 180, 160, 220 |

- En el cordón: piedra, estrella, piedra, estrella, hueco. Un solo gancho vacío.
- La pieza que toca sale del arcón colgada de un hilo. No hay dos botones y no se dice en texto qué pide el hueco.
- El arcón está cerrado en el primer jugable: no se dibuja lo que hay dentro.

## 6. Torre

| Zona | Rectángulo |
|---|---|
| Farol | 704, 180, 160, 160 |

- Pared completa y lisa con su mancha plana bajo el farol. Sin ganchos vacíos, sin siluetas de lo que falta, sin rejilla.
- El farol se gana por un solo hecho: ella encendió el cierre con su dedo en esa sentada. No se gana por no haberse equivocado.

## 7. Cierre del día

- El nido con nueve puestas y un hueco, la piedra que le toca a un lado, Estrella a la derecha.
- **Ningún hueco se marca.** La señal de cuál falta es que los otros nueve están puestos.
- Frase: «Pon la que falta.» Texto sin voz: no está en las ocho grabadas.
- Ese acierto no sube de estado y lo hace ella. Estrella no coloca la última pieza.

## 8. Elegir farol

| Zona | Rectángulo |
|---|---|
| Farol ámbar | 336, 200, 160, 160 |
| Farol terracota | 528, 200, 160, 160 |
| Banda de frase | 96, 468, 832, 56 |

- Los dos son válidos. No hay uno bueno y uno malo.
- Al soltar, el elegido se queda en la torre y la frase desaparece.
- Frase: «Elige uno de los dos.»

## 9. Padre

- Misma campana. Estrella no está en esta pantalla y no se la nombra.
- PIN de cuatro cifras que él elige la primera vez. No hay PIN de fábrica. No hay cambio de PIN.
- Teclado de 3×4: teclas de 76×76 con 12 px de aire, empezando en 386, 200. Cuatro casillas de 60×68 encima.
- Con la cuarta cifra se cierra solo: no hay botón de confirmar. «C» borra una cifra.
- Si el PIN no es, las casillas se vacían y no se dice nada. Sin contador de intentos y sin bloqueo: bloquear dejaría a la niña fuera de su propio juego.
- Si se olvida, no se borra nada: luces, estados y techos siguen. La pantalla se queda cerrada y ella sigue jugando.
- Lo que ve el padre: como máximo dos frases de la lista del GDD, y solo si el hecho es de las sesiones contadas. Si no hay nada: «Esto no es una nota.»

## 10. Texto

- Cuerpo mínimo 32 px. Una frase de hasta doce palabras, o silencio.
- Sin signos de interrogación, sin exclamaciones, sin mayúsculas sostenidas.
- No se escribe nada dentro de una pieza: ni números en las piedras, ni letras en el nido.
- Solo las ocho frases del GDD llevan voz. El resto se ve como texto. Si falta el fichero de una voz, se ve su texto.

## 11. Casos raros, con dueño

| Caso | Qué pasa |
|---|---|
| Cierra la tableta a media pieza | Se guarda en cada suelta. No se inventa el acierto. Al volver no está el borde a medias |
| Giro accidental | La escena no gira. No se pierde nada |
| Segundo dedo | Se ignora. No suelta la pieza del primero |
| Sin audio | El acierto no espera a la campanada: pulso y texto |
| Disco lleno | No se inventa el acierto. Si cabe texto, «Seguimos. Hoy no se ha guardado.» |
| Vuelve al día siguiente | Tres frases de la lista y una que ya sabe. No se dice «te echaba de menos» |
| 20 s sin toque con la pieza presentada | Abandono: se va al cierre en la misma sentada |
| Menos de 15 s en una sala | No abre sesión y no cuenta como evitada |
| PIN olvidado | Nada se borra. La pantalla del padre queda cerrada |

## 12. Lo que queda por decidir

Dos cosas que las placas dejan a la vista y el GDD no fija. No las resuelve el dibujo:

1. **Estrella en el collar.** El GDD solo pone cordón, ganchos y arcón. La placa la deja fuera. Si se quiere dentro, hay que añadir su rectángulo al GDD antes de programar.
2. **Fondo de la torre.** Se ha dibujado pared lisa, que es lo que dice el GDD. Si una pared vacía parece una pantalla rota, la solución no es añadir adornos: es que la torre no sea una pantalla a la que se entra sin nada que hacer.
