# Programación — primer jugable

Este texto obedece `Documento-de-diseno` y el encargo cerrado del repositorio. Si un capítulo de experto dice otra cosa, manda el GDD. Aquí se cierra lo que un programador tendría que decidir. No es el juego. No abre la llevada, ni el euro, ni un problema con historia.

Idioma del material y de las cadenas: español de España. No hay nombre, foto ni edad de una niña real. No hay identificador de aparato más allá de no pedirlo.

## Qué se construye

Godot 4.7.2, solo 2D, GDScript. Sin C#, sin extensión nativa, sin plugin de red. El primer jugable, en el ordenador y luego en la tableta, es esto:

- Patio, Estrella, torre con un farol que ella coloca.
- Piedras de luz: hacer el 10. Caja de dos filas de cinco. La décima enciende. Una oncena de más no enciende.
- Acertijo: piedra, estrella, piedra, estrella. Ella cuelga la siguiente desde un arcón. No elige entre dos botones.
- Cierre siempre en un acierto suyo. Estrella no coloca la última pieza.
- Registro de duda al soltar.
- Corte a los dos fallos del borde, y corte si devuelve piezas, encadena fallos o se va.
- Hora y postura se anotan y no cambian el juego.

Partida de referencia, si nada se tuerce: ver tres piedras; Estrella cierra un diez; ella repite 7 y 3; borde 8, luego 5, luego 9; collar piedra-estrella; cierre de una que puede; farol a la torre.

## Aparato

Amazon Fire 7 (2022), KFQUWI. Fire OS 8.3.3.8, Android 11, API 30. MT8168, Mali-G52, 2 GB de RAM; en reposo quedan unos 620 MB. Pantalla 1024×600, 60 Hz, unos 171 dpi. En horizontal, con la barra, el área útil baja a unos 1024×552. Acelerómetro sí. Giroscopio no. Multitáctil. Sin permiso de internet. Disco justo: el APK cabe holgado por debajo de 40 MB y nunca pasa de 80.

El primer jugable se prueba antes en el ordenador. El ratón emula el dedo. En el escritorio el acelerómetro devuelve cero: la postura queda `desconocida` y el juego sigue igual. No se simula una postura en la exportación.

### Proyecto

| Ajuste | Valor |
|---|---|
| Renderer | `gl_compatibility`, también en móvil. Sin Vulkan, sin Forward+ |
| Viewport | 1024×600 |
| Estirado | `canvas_items`, aspecto `expand` |
| Orientación | landscape fijo, no sensor. El margen de abajo no puede rotar |
| Inmersivo | sí, en la exportación Android |
| Arquitectura | solo `arm64-v8a`. Sin armeabi-v7a, sin x86 |
| min SDK | 30 |
| target SDK | el de la plantilla de Godot 4.7.2, si el APK arranca en API 30 |
| Permisos | ninguno. Internet apagado. Sin red, cámara, micrófono ni almacenamiento externo |
| Sensores en el manifiesto | acelerómetro y giroscopio `required=false`. El giroscopio no se lee |
| Main scene | `res://escenas/arranque.tscn` |

`user://` es el directorio privado de la app. No hace falta permiso de disco. No se escribe fuera.

Botón atrás: en una sala, guarda y vuelve al patio. En el patio, guarda y sale. No hay diálogo de «¿seguro?». `auto_accept_quit` en falso. Se vacía el fichero en pausa, pérdida de foco, atrás y cierre.

Nada importante vive en los 48 px de abajo. Botones y piezas de unos 96 px. Aire de 24 px. Una frase de hasta 12 palabras, cuerpo 32 px. El texto se ve aunque no haya voz.

### Presupuesto

Una sala en memoria. Al cambiar de escena se suelta el fondo y el atlas de la anterior. Los autoloads no cargan dibujos de sala.

| Tope | Cifra |
|---|---|
| Sprites en movimiento | 40 |
| Partículas al encender | 12, `CPUParticles2D`, discos del mismo ámbar, 1,2 s. No confeti |
| Capas de fondo | 2 |
| Fondo | 1024×512, ETC2, sin mipmaps |
| Atlas de la sala | 512×512, se suelta al salir |
| Pieza | 128×128 en textura, 96 px en pantalla |
| APK del corte | por debajo de 40 MB; nunca 80 |
| Dibujo comprimido | no pasa de 8 MB. Si no cabe, se quita dibujo, no el gesto |
| Ficheros de `user://` | kilobytes. `metricas.json` no pasa de 256 KB |

Si falta un dibujo, `ColorRect` del color de sala, mismo tamaño. Colores: patio `#1E2A4A`, luz `#F4C56D`, Piedras `#3D4F8A`, piedra `#F2E2A0`, Acertijos `#8E7CC3`, texto crema `#F7F1E4` sobre oscuro, tinta `#2C2416` sobre claro. No hay color de fallo. El detalle de texturas está en `docs/specs/direccion-artistica.md`.

Sin vídeo, sin malla, sin shader pesado, sin precarga de las ocho salas. Una voz como mucho, y en el primer jugable no hace falta ningún ogg: si no hay audio, se ve el texto. La campanada suave, si entra, es un wav de unos pocos KB, 0,4 s, la misma con ayuda o sin ella. No hay zumbido de error. No hay vibración.

Prohibido en el proyecto: `HTTPRequest`, sockets, `Input.get_gyroscope()`, nodos 3D, `VideoStreamPlayer`, anuncios, cuentas, un `Label` de tiempo aunque sea invisible.

## Árbol de escenas

Tres autoloads, en este orden: `Progreso`, `Metricas`, `Adaptador`. No hay un cuarto. Las constantes viven en `res://scripts/reglas.gd`, precargado, no autoload.

```
res://escenas/arranque.tscn          Node. Carga el guardado y pasa al patio. Sin logotipo. Sin «pulsa para empezar».
res://escenas/patio/patio.tscn       Control. Mapa único.
res://escenas/piedras/piedras.tscn   Control. Hacer el 10.
res://escenas/acertijos/collar.tscn  Control. Patrón.
res://escenas/torre/torre.tscn       Control. Colocar el farol.
res://escenas/padre/padre.tscn       Control. PIN y frases. Ella no la ve en el flujo.
res://escenas/ui/frase.tscn          Se instancia. No es una sala.
res://escenas/ui/estrella.tscn       Se instancia. Tres poses.
res://escenas/piezas/piedra.tscn
res://escenas/piezas/cuenta.tscn     Cuenta del collar: piedra o estrella.
res://escenas/piezas/farol.tscn
```

Navegación con `change_scene_to_file`. El estado no viaja en la escena: vive en los autoloads. Un fundido de 0,4 s puede ser un `ColorRect` en un `CanvasLayer` del autoload de progreso visual, sin retener las dos salas.

### Patio

Fondo. Estrella a la izquierda, unos 200 px, curiosa o contenta. Torre a la derecha con la llama de casa ya encendida: no es un premio y no se apaga. Dos ventanas de 96 px, con 24 px entre ellas: Piedras de luz y Acertijos. Disponibles el primer día, no encendidas. Se encienden al primer cierre que ella completa allí. El resto de salas es un solo bulto de niebla, no seis candados y no un botón prohibido. Tocarlo no abre lección. Estrella, curiosa. Frase ya escrita, si cabe: «Las otras esperan, dormidas.» Si no se dice, silencio. No se inventa «esta sala espera» ni «esa luz viene después».

Campana de 96 px, sin rótulo «padres». Pulsación de 1,5 s abre el PIN. Altavoz de 96 px: calla el sonido y deja el texto. El silencio se guarda. Nada de esto es una cuenta.

### Piedras de luz

Una pantalla. Nido de dos filas de cinco huecos, 96 px, aire 24 px. Montón al centro, por encima del margen de 48 px. Estrella a un lado, con su nido de ejemplo, que no es el de ella. Frase arriba. Luz del nido, apagada hasta la décima. Sin teclado, sin botón de listo, sin «1/4», sin reloj.

### Collar

Cordón a la altura de la mano, no en el borde. Cuatro cuentas ya puestas: piedra, estrella, piedra, estrella. Un hueco. Arcón con al menos tres piedras y tres estrellas sueltas, de más, sin rótulo y sin pareja de botones. Un toque sin arrastrar no ensarta.

### Torre

Dos faroles del mismo tamaño y la misma forma. Dos colores cálidos, los dos válidos: `#F2E2A0` y `#F4C56D`. Ninguno es el de hacerlo perfecto. Ninguno es gris. Ella arrastra uno a la pared y lo suelta donde quiere. Torcido vale. Encima de otro vale. El juego no lo endereza. No se dibujan ganchos vacíos: serían estrellas vacías. En datos caben los puestos más adelante; en pantalla solo se ve lo colocado.

### Estrella

Tres poses y ninguna más: `curiosa`, `contenta`, `pensando`. Pensando es la cabeza un poco ladeada, la boca serena. No existe fotograma de decepción, enfado ni tristeza, ni en el proyecto. Sin corona. Sin varita. Si falta el dibujo, una forma de color del mismo tamaño, piel `#C6866A`, capa `#C45C4A`.

### Padre

Fuera del flujo de ella. Teclado de diez teclas de 96 px, que no son las piedras del juego. Una o dos frases. Sin gráfica, sin porcentaje, sin hora, sin postura, sin la palabra nivel. La exportación del resumen no entra.

## Autoloads

Las salas no deciden pedagogía. Emiten hechos. `Metricas` los anota. `Adaptador` responde. `Progreso` guarda. Ella no ve el nombre de ningún estado.

### Progreso

Único escritor de `user://progreso.json` y `user://sesion_abierta.json`.

- Carga al arrancar. Si el fichero no existe, partida nueva, sin luces de sala, con la llama de casa encendida, sin aciertos inventados.
- Escritura atómica: `fichero.json.tmp`, `flush`, cerrar, renombrar encima. Se conserva la generación anterior como `.bak`. Al arrancar, si el principal está corrupto y el `.bak` vale, se restaura. Si los dos fallan, se empieza de cero y no se fabrica un cierre.
- Guarda en cada cambio de estado de sesión y en cada suelta juzgada. Una ráfaga se aplaza 200 ms. Pausa, atrás y cierre no esperan.
- Una pieza en el aire al matar la app se tira. No es fallo ni acierto. El nido vuelve al último estado asentado.

No abre sockets. No lee el acelerómetro.

### Metricas

Único escritor de `user://metricas.json`. No dibuja. No elige micropaso. No habla con el padre.

Clasifica la suelta en crudo y emite el evento de duda, si lo hay. El anillo de ejercicios no pasa de 200. El de eventos no pasa de 800. Al pasar, se olvidan los más viejos. Nunca se olvidan luces, adornos ni estados: eso no vive aquí.

### Adaptador

La máquina de la sesión. Lee a los otros dos. No tiene nodos de interfaz.

Decide, y solo esto puede cambiar: el tramo, el tamaño del nido de hoy, si el ejemplo está al lado, el identificador de frase, la duración y si hoy hay idea nueva. En el primer jugable la idea de hoy es siempre hacer el 10. No hay otro micropaso en pantalla.

No puede: quitar luces, poner un cronómetro visible, cerrar Acertijos, enseñar un marcador, enviar datos, quitar un adorno, hacer que la hora o la postura cambien el plan.

Señales que la sala escucha: `presentar`, `mostrar_ejemplo`, `ocultar_ejemplo`, `volver_pieza`, `encender`, `frase`, `ir_a`. Señales que la sala emite: agarrar, mover, soltar, desdecirse, toque vacío, salir, pausa de la app. La sala no cuenta fallos.

## Máquina de sesión

Estados, que ella no ve: `PATIO`, `ENTRADA`, `YA_SABE`, `IDEA_DEMO`, `IDEA_REPITE`, `BORDE`, `ACERTIJO`, `CIERRE`, `TORRE`, `GUARDADO`.

```
PATIO → ENTRADA → YA_SABE → IDEA_DEMO → IDEA_REPITE → BORDE → ACERTIJO → CIERRE → TORRE → GUARDADO → PATIO
                                                     |            |
                                                     |            +-- 2 fallos, o cansancio --> CIERRE
                                                     +-- el reloj interno no abre otro intento a mitad de un arrastre
```

| Estado | Entra | Sale | Qué ve ella |
|---|---|---|---|
| `PATIO` | Al abrir, o al guardar | Toca una ventana disponible o encendida | Castillo, torre, niebla. Sin marcador |
| `ENTRADA` | Entra en una sala | 4 s, o ella toca | Estrella curiosa. Una frase. Aún no la cuenta |
| `YA_SABE` | Tras la entrada | Acierto. Se ayuda hasta lograrlo | Tres piedras. Los tropiezos de aquí no suman corte |
| `IDEA_DEMO` | Tras el ya-sabe | 20 s, o ella empieza a arrastrar | Estrella cierra un diez en su lado. Sin vídeo |
| `IDEA_REPITE` | Acaba el modelo | Ella suelta el gesto, o 40 s | Nido con 7. Ella añade 3. Ejemplo al lado: es con ayuda |
| `BORDE` | Tras la repetición | 3 intentos, o 4 si cabe, o 2 fallos, o cansancio | 8, luego 5, luego 9. Sin «1/3» |
| `ACERTIJO` | Borde sin corte | Acierto con sus manos, o 90 s, o cansancio | Collar. Un tropiezo aquí no baja la aritmética |
| `CIERRE` | Por orden, por corte o por reloj | Ella enciende la luz | Una que puede. Estrella no la resuelve |
| `TORRE` | Tras el cierre, si hay farol pendiente | Lo coloca, o sale | Dos faroles, los dos válidos |
| `GUARDADO` | Al colocar, o al salir habiendo guardado | Patio, o la app se cierra | Nada nuevo. La luz sigue |

El reloj interno no se dibuja. No corta un arrastre: actúa al soltar, entre turnos. A los 420 s no se abre otro intento de borde. Si van menos de dos fallos y no hay cansancio, el acertijo de ese corte dura 40 s; si no, al cierre. A los 480 s, tras la suelta en curso, al cierre. Si el recorrido acaba antes, se acaba. No se rellena.

Menos de 15 s dentro de una sala, sin haber tocado una pieza, no abre sesión. No queda farol, no queda reproche, se borra `sesion_abierta.json`. Tocar una pieza sí abre sesión, aunque luego salga. Mirar el patio no abre sesión.

### Choques cerrados

| Tema | Manda | No se implementa |
|---|---|---|
| Números del primer día | GDD: tres; Estrella cierra un diez; ella repite 7 y 3; borde 8, 5 y 9 | El guion de relato con 8+2 y borde 7, 9, 6, 5+5. Esas frases se reutilizan cambiando solo el número |
| Frase del corte | «Seguimos con una que ya sabes.» Una frase, luego silencio | Nombrar cansancio o fallo. Encadenar otras frases de puente |
| Acertijo | Piedra, estrella, piedra, estrella. La siguiente es piedra. Desde un arcón | Dos botones. Faroles círculo/estrella. Un collar que se cuelga solo en la torre |
| Comprobación | La décima enciende la losa. El 10, si se dibuja en la luz, no se traza y no se teclea | Teclado. Ficha que pueda fallar la sesión |
| Torre | Un farol, a elegir entre dos, los dos válidos. Lo coloca ella | Cinta del guion. Huecos vacíos. Un adorno mejor por no fallar |
| Ya-sabe | Los tropiezos no cuentan para el corte. Se ayuda hasta el acierto | Dos fallos de la apertura que manden al cierre |
| Oncena | No enciende. La primera del intento es el juguete. La segunda del mismo intento es fallo `E_DIEZ` | Un aspa, un zumbido, o contar la primera como fallo |
| Primeros días | El registro observa. No sube a firme ni a suelto. No baja un cimiento que aún no estaba establecido. Hora y postura no mandan | Un selector de los 81 micropasos. Dejar que la inclinación acorte la sesión |

Las dos primeras sesiones completas repiten hacer el 10. No hay idea nueva. Firme, si algún día llega, pide otro día, y aun así este corte no abre el Pergamino.

## Hacer el 10

Micropaso de pantalla: M11, la caja de diez. M01 a M10 no son una aduana y no se juegan en este corte. Si más adelante el borde tuviera que bajar a contar, sería dentro de Piedras, no otra sala. Aquí el borde no baja de estos nidos.

| Tramo | Nido al empezar | Montón | Acierto |
|---|---|---|---|
| Ya sabe | vacío | exactamente 3, ya encendidas, sin otras | las tres reposan en el nido. Calor pequeño, no la luz del diez |
| Demo | el de Estrella, en su lado | ella añade hasta cerrar un diez, en 20 s | ella lo ve. La luz del ejemplo se apaga al resetear y no es una luz del castillo |
| Repite | 7 | 3 claras y otras apagadas, para que no sea un botón con un 3 | la décima enciende. Una oscura no entra y vuelve. Eso no es fallo del borde: aún es la idea |
| Borde 1 | 8 | al menos 6, ninguna preelegida | parar en 10. Vaciar el montón no es el método |
| Borde 2 | 5 | igual | igual |
| Borde 3 | 9 | igual | igual |
| Borde 4 | 6 | igual | solo si van 0 fallos, no hay cansancio y el reloj interno va por debajo de 300 s |
| Cierre | 9 y una clara, o las 3 si el borde costó | lo justo para un gesto, no un imán de un píxel | la enciende su dedo |

No hay botón de listo. Quedarse corta no es fallo: el nido espera. A los 8 s sin toque, después de haber movido algo, el ejemplo aparece al lado. No se le dice que se dé prisa.

La oncena, con el nido lleno, vuelve sola en 0,4 s, en silencio. Estrella, pensando. La primera vez en ese intento no suma `fail_count`. La segunda en el mismo intento es `E_DIEZ` y sí suma, si el tramo es el borde.

Un grupo que no cierra el diez y se deja 3 s, sin desdecirse, es fallo a la primera en el borde: no es un límite del material, es una respuesta. Si se desdice dentro de los 3 s, no es fallo.

Adivinar no cuenta. Tocar el vacío, o soltar sin haber movido la pieza, no enciende nada y no es fallo. Estrella, pensando. Se sigue esperando el arrastre. Manipular menos de 0,8 s sin un gesto que llene huecos no cuenta y obliga a mover, sin sonido de error.

### Intentos

`PRESENTA` → `TOCA` al primer toque → `MUEVE` cuando la pieza cambia de sitio → `SUELTA` al levantar el dedo → 3 s para desdecirse → `JUICIO` si no se desdice.

- 20 s sin toque en `PRESENTA`: abandono. Se guarda. No es un fallo de carácter. Al volver, una cuenta que ya sabe, no este nido.
- Sostener 8 s o más: duda `sostiene_mucho`. Una frase de duda, si hace falta, y no se repite en el mismo intento. No hay reloj.
- Soltar sin haber movido: vuelve a `TOCA`. No es acierto.
- Devolver al origen se puede. No suena a error. Tres devoluciones en el mismo intento, o una en dos intentos seguidos: cansancio.
- El juicio de acierto enciende porque el nido tiene diez y ella ha movido piezas. Pulso de 1,2 s. Campanada 0,4 s si existe el wav. Estrella contenta, 1 s. La misma luz con ayuda o sin ella.

Resultado de cada ejercicio, una sola palabra guardada: `sola`, `con_ayuda` o `no`. Con ayuda es el ejemplo al lado, la repetición del modelo, o el cierre con ejemplo. Sola exige gesto, sin ejemplo haciendo el trabajo, sin duda y sin ir despacio para ella en ese paso. En este corte, `sola` se anota y no sube a firme ni a suelto. El acierto de cierre no sube. El primer acierto del día no sube a firme.

Estados de M11, de menor a mayor: `sin_ver`, `aprendiendo`, `fragil`, `firme`, `suelto`. Ella no los ve. Solo se sube uno. Solo se baja uno. El suelo, una vez vista la idea, es `aprendiendo`. Este corte puede pasar de `sin_ver` a `aprendiendo` cuando ella arrastra la repetición, y puede anotar `fragil` si acierta sola hoy. No escribe `firme` ni `suelto`. No baja un estado que aún no estaba establecido. Si duda y falla, se enseña el gesto igual: el ejemplo vuelve al lado de Estrella. Eso es ayuda, no un juicio, y no espera a tener muchas partidas.

## Acertijo

Solo si el borde no se cortó. No se anuncia como examen, ni como problema, ni con un número de pregunta.

Tira ya puesta: piedra, estrella, piedra, estrella. El hueco pide piedra, que es la que sigue. Ella la arrastra desde el arcón. Si no sigue el ritmo, resbala en 0,4 s, en silencio, y vuelve al arcón. Eso no suma `fail_count` del borde y no baja M11. Al segundo tropiezo, Estrella deja el ritmo en su lado y ella coloca en el suyo. Eso es con ayuda del acertijo, no una nota. A los 90 s, al cierre. Un acertijo no se queda imposible: la ayuda llega, y la última pieza la mueve ella.

La victoria es el cordón que da el mismo pulso de 1,2 s. No nace un adorno de torre por el collar. El farol llega después del cierre de la partida, no aquí.

Si ella entra en Acertijos desde el patio, sin haber hecho el borde, juega el collar y puede ir luego a Piedras. Si se queda y sale tras completarlo con las manos, ese acierto vale como visita, el farol espera si ya se ganó por haber jugado, y la idea de mates no se pierde. No se cierra la sala para obligarla. En este corte, con una sola sesión de referencia, entrar primero al collar no apaga Piedras.

## Cierre y torre

El cierre es una que puede hacer. Si el borde de 9 salió, se puede repetir ese gesto, con la piedra clara ya cerca de la mano. Si costó, son las tres del ya-sabe. Escalera, sin nombrarla:

1. **C0.** Piezas a la vista. Unos 15 s para el primer movimiento.
2. **C1.** Si no enciende, o pasan 15 s sin un movimiento con destino: el ejemplo aparece en el lado de Estrella. La zona es amplia, unos 120 px, y no es el único píxel que brilla. El brillo, si hace falta, es de toda la losa.
3. No hay C2. No hay botón de saltar. Estrella no pone la última piedra en el nido de ella. No suma fallo de borde. No baja peldaño.

Hasta que esa luz se enciende con su mano, no se da el farol por ganado y no se inventa el acierto. Si cierra la tableta antes, el cierre queda pendiente. Al volver, el patio ofrece esa bandeja, que es una que ya sabe, no el nido que falló. No se reanuda el `fail_count` como deuda visible. Lo ya escrito, incluidas las bajadas que de verdad ocurrieron, se queda, para no bajarla dos veces por lo mismo.

El farol se gana por llegar al cierre habiendo tocado una pieza, aunque el borde se saltara, aunque hubiera ayuda. Uno, no dos. Si sale antes de colocarlo, queda en el umbral, ya suyo. Colocarlo al volver no exige repetir la cuenta y no regala otro.

La luz de Piedras se enciende la primera vez que ella completa allí un cierre moviendo piezas, con ayuda o sin ella, y no se apaga. La de Acertijos, igual, la primera vez que completa el collar con las manos. Bajar un peldaño no quita luz ni farol. No jugar tampoco.

## Eventos de duda

Se anotan al soltar. Ella no los ve. No se le dice que ha dudado. La duda no hereda frases de fallo.

Una suelta puede llevar más de un tipo. Cualquiera de los cuatro marca el intento.

| Tipo | Cuándo | Qué no es |
|---|---|---|
| `suelta_en_el_sitio` | El centro acaba a 24 px o menos del origen del agarre, tras tenerla 1 s o más | Ni acierto ni fallo. Si no llegó a entrar en un destino, tampoco es devolución |
| `cambia_de_destino` | Durante ese agarre, el centro estuvo 0,4 s o más en el radio de un destino, y se suelta en otro destino distinto | No es fallo por sí solo |
| `sostiene_mucho` | El agarre dura 8 s o más | No dispara un fallo. No aparece un reloj |
| `se_desdice` | Antes de 3 s desde la suelta, vuelve a cogerla y la saca del destino | No es error. Deshacer no se quita. Se vuelve a `MUEVE` |

Radio de destino: 72 px desde el centro del hueco, en píxeles del viewport 1024×600. El imán de colocación usa ese mismo radio. Todos los huecos vacíos del nido valen. Ninguno se preilumina como la respuesta.

Distancia de origen: 24 px de viewport, no milímetros.

Respuesta, en el borde:

- Si luego acierta: no sube, el siguiente intento es del mismo tipo de nido, y hoy no se retira más ayuda.
- Si luego falla: se enseña el gesto. No se baja un cimiento que aún no estaba establecido. Si ya estaba establecido, bajar uno queda anotado para el producto, pero este corte no tiene un cimiento firme que tirar.
- Soltar en el sitio, por sí solo, no es el fallo.

Pausa larga: 4 s o más entre toques, guardada aparte, no sumada al tiempo manipulando. Una pausa no es un fallo. Tres pausas largas en el mismo intento no cortan solas mientras haya pocas partidas: se anotan. El cansancio que sí manda en este corte no necesita mediana.

Devolución, distinta de la duda: la pieza entró en un destino, o salió del montón hacia él, y vuelve al origen. Tres en el mismo intento, o en dos intentos seguidos, cortan lo nuevo.

### Hecho en crudo que emite la sala

La sala no clasifica. En cada suelta manda:

- identificador de pieza
- posición de origen y de suelta, en píxeles de viewport
- instante de agarrar y de soltar, `Time.get_ticks_msec()`
- lista de destinos cuyo radio ocupó el centro, con el tiempo acumulado en cada uno
- si la pieza había salido del origen más de 24 px

`Metricas` aplica la tabla y guarda el evento. `Adaptador` no vuelve a medir píxeles.

## Cansancio y corte

El juego no ve emoción. No escribe «frustrada» en ningún sitio. No se lo dice a ella ni al padre.

Se corta lo nuevo, entre turnos, no a mitad de un arrastre, si ocurre cualquiera de estos:

- devuelve piezas: 3 en un intento, o en dos seguidos
- encadena fallos: el segundo del borde
- se va: 20 s sin toque en `PRESENTA`, sale de la sala, o cierra la tableta
- el reloj interno pasa de unos 7 minutos, al soltar

No se corta solo porque manipule un buen rato si las piezas avanzan. No se corta por un primer toque lento. No se corta por la postura ni por la hora. Con pocas partidas, la mediana de tiempos no manda: no hay mediana que usar.

Frase del corte, literal, sin nombrar cansancio ni fallo: «Seguimos con una que ya sabes.» Luego silencio, y el cierre. El acertijo de esa sesión puede no caber. La sala de Acertijos no se cierra.

El corte no quita luz, no quita farol y no es una bajada de castillo.

## Muestreo de inclinación

La tableta no sabe si ella está sentada o acostada. Solo la inclinación del aparato. No hay giroscopio y no se echa de menos. El acelerómetro no es un mando: inclinar, agitar o tumbar la tableta no mueve piezas, no abre salas y no acorta la sesión.

No se llama a `Input.get_gyroscope()`. No se enciende ese sensor. No se pide permiso. Si el manifiesto de exportación marca el giroscopio como obligatorio, se quita o se deja `required=false`. Igual el acelerómetro: si falla, se juega igual.

### Lectura

`Input.get_accelerometer()` devuelve m/s², o `Vector3.ZERO` si no hay sensor. En el escritorio será cero.

Godot puede entregar el vector en ejes del aparato o ya girado con la pantalla. No se adivina. En la Fire, con la tableta plana y la pantalla hacia arriba, el eje dominante y su signo son la normal de la pantalla, hacia fuera. Ese vector unitario queda fijado en `reglas.gd` después de esa comprobación, con un comentario del eje medido. Hasta medirla en el KFQUWI, el código usa `Vector3(0, 0, 1)` solo como candidato, y una lectura fuera de rango no se clasifica.

```
g = Input.get_accelerometer()
si |g| < 7 o |g| > 12: muestra inestable; se conserva la última estable
d = normalizar(g) · normal_pantalla
plana              si d > cos(25°)
encima_de_la_cara  si d < -cos(35°)
de_pie             en cualquier otro caso estable
desconocida        si no hay tres lecturas válidas
```

`cos(25°)` es 0,9063. `cos(35°)` es 0,8192. Plana: la gravedad cae cerca de la normal, pantalla hacia arriba, a menos de 25°. Encima de la cara: la normal mira hacia abajo, a menos de 35° de la vertical invertida. Eso no significa que ella esté acostada. De pie: el resto, sujeta en vertical o inclinada.

### Cuándo se toma

No cada fotograma. Un temporizador de 1 s, solo con sesión abierta, refresca la última muestra estable. Se anota esa muestra al empezar la sesión y en cada cambio de estado. No se guarda el chorro de 1 Hz.

Esos tres valores no eligen nido, no acortan, no se muestran a ella y no salen en la pantalla del padre. Ni en este corte ni como orden más adelante. Si algún día un resumen exportado los lleva, irán en crudo, sin conclusión. La exportación no entra aquí.

## Formato de `user://`

Tres ficheros. JSON, UTF-8, sin identificador de aparato, sin nombre de niña. La hora es local, ISO-8601 con desplazamiento. El día es `YYYY-MM-DD` local. Otro día significa otra fecha local, no 24 horas exactas.

### `progreso.json`

```json
{
  "version": 1,
  "silencio": false,
  "pin": null,
  "techo": "ninguno",
  "observando": true,
  "llama_casa": true,
  "luces": { "piedras": false, "acertijos": false },
  "umbral": [],
  "colocados": [],
  "micropasos": {
    "M11": {
      "estado": "sin_ver",
      "ultimo_dia_sola": null,
      "error_id": null
    }
  },
  "sesiones_completas": 0
}
```

`pin` es `null` o `{ "sal": "<hex>", "hash": "<hex>" }`. SHA-256 de la sal de 16 bytes más los cuatro dígitos. Nunca el PIN en claro. `techo` queda en `ninguno` en este corte; los valores futuros son `hasta_20`, `sin_llevada`, `sin_mercado`, `sin_centenas`, `sin_por`. El techo solo frena. `observando` permanece `true`: este corte no lo apaga. `colocados` guarda `{ "id": "farol", "color": "luz", "x": 0, "y": 0 }`. No guarda huecos vacíos. `umbral` es el farol ganado y aún no colocado.

Una luz en `true` no vuelve a `false` por ningún camino de código. Conviene un aserto al guardar.

### `sesion_abierta.json`

Existe solo si hay sesión. Al terminar de verdad se vuelca lo duradero a `progreso.json` y se borra.

```json
{
  "version": 1,
  "id": "s-local",
  "inicio": "2026-11-05T18:04:00+01:00",
  "dia_local": "2026-11-05",
  "estado": "BORDE",
  "sala": "piedras",
  "toque_pieza": false,
  "fail_count": 0,
  "cortada": false,
  "motivo_corte": null,
  "cierre_pendiente": false,
  "farol_pendiente": false,
  "postura_inicio": "desconocida",
  "nido": [0, 1, 2, 3, 4, 5, 6, 7],
  "intento": 1,
  "ejemplo": false
}
```

`motivo_corte` es `null`, `dos_fallos`, `devoluciones`, `abandono` o `reloj`. No es una emoción. `nido` son los huecos ocupados, 0 a 9, dos filas de cinco. Al volver no se restaura el borde abandonado: si `cierre_pendiente`, el patio entra por el cierre; si no hubo cierre, la próxima apertura es una que ya sabe.

### `metricas.json`

```json
{
  "version": 1,
  "ejercicios": [
    {
      "sesion": "s-local",
      "tramo": "borde",
      "micropaso": "M11",
      "nido_inicial": 8,
      "resultado": "con_ayuda",
      "dudas": ["sostiene_mucho"],
      "t_primer_toque_ms": 1200,
      "t_manipulando_ms": 4300,
      "pausas_largas_ms": [4100],
      "hora_inicio": "18:04",
      "postura": "plana",
      "error": null
    }
  ],
  "dudas": [
    {
      "t": "2026-11-05T18:06:12+01:00",
      "sesion": "s-local",
      "intento": 1,
      "pieza": "piedra-3",
      "tipo": "cambia_de_destino",
      "dx_px": 180,
      "agarre_ms": 2400,
      "destino_previo": "hueco-8",
      "destino_suelta": "hueco-2"
    }
  ],
  "posturas": [
    { "t": "2026-11-05T18:04:00+01:00", "sesion": "s-local", "estado": "ENTRADA", "postura": "de_pie" }
  ]
}
```

`resultado` es `sola`, `con_ayuda` o `no`. `error` es `null` o `E_DIEZ` o `E_PATRON`. `postura` es `de_pie`, `plana`, `encima_de_la_cara` o `desconocida`. No se guarda aceleración en crudo de más: basta el cubo. No se guarda una conclusión.

## Padre

Pulsación de 1,5 s en la campana. Si no hay PIN, la primera entrada lo elige y lo repite. No hay PIN de fábrica. Si falla, silencio y patio. A la tercera vez seguida, patio también. No hay espera de castigo.

Él lee una o dos frases de esta lista, las que los hechos permitan. No se redactan otras.

| Hecho | Frase |
|---|---|
| Acertó sola un diez hoy | «Hoy ha hecho dieces sola. Mañana se mira si sigue. La llevada no se abre todavía.» |
| Dudó y falló, y volvió el ejemplo | «Ha dudado y ha fallado. Se ha vuelto al gesto. La torre no ha perdido luz.» |
| La sesión se cortó y hubo cierre | «La sesión se ha cortado y ha acabado en una cuenta que ya sabe.» |
| Salió cuando quiso | «Ha salido cuando ha querido. Lo hecho está guardado. El castillo sigue encendido.» |
| Siempre, si no cabe otra | «Esto no es una nota. No la compares con otros niños.» |

No se le dice que iba retrasada, ni que estaba tumbada, ni un porcentaje, ni un nivel, ni una emoción.

## Frases de ella

El listado cerrado está en `Relato`. No se improvisa. Se cambian los números, dichos con palabra, y en F08 se cambian «piedra» y «estrella» si el hueco pide la otra. El resto de la frase se queda.

En este corte se usan, con los números del GDD:

- Llegada y torre: las frases del guion de la primera sesión, literales.
- Ya sabe: «Mira estas tres.» «Se ven de un golpe.» «Arrástralas al cuenco.» Al lograrlo: «Has juntado las tres.» «Se ven claras.»
- Demo y repetición: el bloque de ocho y dos, cambiado a siete y tres. «Siete piedras en el cuenco.» «Añado tres.» «Siete y tres son diez.» «Ahora tú.»
- Borde: «Ahora lo miramos con otras.» «Aquí hay ocho.» «Aquí hay cinco.» «Aquí hay nueve.» «Busca las que faltan para diez.» En el de nueve: «Busca la que falta para diez.»
- Acertijo: «Ahora un juego de mirar.» «No hay que sumar.» «Piedra, estrella, piedra, estrella.» La respuesta se arrastra. Si el hueco pide piedra, la frase de acierto cambia la pieza, no la forma: «Has puesto la piedra en el hueco.» «El ritmo sigue.»
- Corte: «Seguimos con una que ya sabes.»
- Cierre, al encender ella: «Has hecho un diez.» «Hoy se queda encendido.»
- Torre: «Elige una.» no se inventa si el guion dice «Elige una cinta.» Se usan las dos frases que sí valen para el farol sin nombrar una cinta: se calla el nombre que no es, y se dice «Las dos sirven.» «La torre la guarda.» «Mañana sigue aquí.» «Cuando quieras, paramos.»
- Al volver tras días: «Me alegro de verte.» «Tus luces siguen encendidas.» «No hay que recuperar nada.»

Duda: solo D01–D12. Una por intento. D11 no entra: habla de columnas. Fallo del diez: F01, F02 o F11, con el número de la mesa. F04 y F05 no entran: son de llevada. Fallo del collar: F08, con la pieza que el hueco pide. Acierto, si se habla: A01–A12, nunca un elogio de persona. Prohibido en boca de Estrella: «mal», «incorrecto», «eres un genio», «casi», «date prisa», «esto es fácil», cualquier comparación, cualquier etiqueta de emoción o de inteligencia.

Una frase, luego silencio. Permanece al menos 4 s. Ella puede seguir al tocar, nunca antes de 0,8 s. Tocar la frase la repite, si hay audio. Sin bucle. Sin suspiro.

## Entrada

Un dedo basta. El segundo dedo se ignora. Sin doble toque. Sin pulsación larga en las piezas: la pulsación larga es solo la campana.

El arrastre sigue el dedo dentro del área segura. Al soltar, si el centro está en el radio de un hueco vacío, ocupa ese hueco. Si el nido ya tiene diez, vuelve en 0,4 s. No hay cuerpo rígido ni física. `Control` y el dedo alcanzan.

El botón atrás y matar la app son el mismo guardado.

## Qué no se escribe

Espejo, Círculo, Pergamino, Mercado, Jardín y Tesoro como escenas en las que se entra. Llevada, préstamo, centenas, euros, céntimos, grupos, reparto, sobra, signos × y ÷, problemas con historia, nombres difíciles. Los 81 micropasos como selector. Exportación. Vídeo. Red. Cuentas. Anuncios. Marcador. Vidas. Estrellas vacías. Sonido de error. Giroscopio. 3D. Un cronómetro, aunque sea invisible.

El esquema de `micropasos` y de `luces` admite claves nuevas sin borrar el historial. No hace falta migrar este fichero cuando entre otra sala.

## Hecho, cuando

- En el ordenador, la partida de referencia se puede jugar con el ratón: tres; demo; 7 y 3; borde 8, 5 y 9; collar; cierre con su mano; farol en la pared.
- Dos sueltas que no encienden en el borde saltan al cierre, sin tercer fallo y sin collar en el armazón. La ventana de Acertijos sigue en el patio.
- Devolver piezas, irse o encadenar fallos cortan con la frase literal, y el último gesto, si ella se queda, es un acierto suyo.
- Cerrar a medias no inventa ese acierto. Al volver no reaparece el borde fallido.
- Menos de 15 s sin tocar una pieza no deja farol ni fichero de sesión.
- Una oncena no enciende. La segunda del mismo intento queda en métricas como `E_DIEZ`.
- Soltar en el sitio, cambiar de destino, sostener 8 s y desdecirse antes de 3 s aparecen en `metricas.json` y en ningún nodo visible.
- La postura se anota en los tres cubos, o `desconocida`, y el nido no cambia al tumbar la tableta.
- El APK de prueba es arm64, Compatibility, inmersivo, 1024×600, sin permiso de internet, y no llama al giroscopio.
- No hay pose triste, ni corona, ni varita, ni reloj en pantalla, ni botón de listo, ni dos botones en el collar.
