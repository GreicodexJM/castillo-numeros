# Programación — primer jugable

Este documento obedece `docs/GDD.md`. Si algo de aquí lo contradice, manda el GDD. Cierra lo que un programador tendría que decidir y que el GDD deja abierto; cuando una decisión no está en el GDD se dice, para que se pueda cambiar sin miedo.

Las coordenadas no se copian de aquí: se leen de las placas de `assets/pantallas/`, que se generan del GDD con `tools/mockup_pantallas.py`. Si una placa y el GDD no coinciden, el error está en la placa y se regenera.

Idioma de pantalla y de datos: español de España. No hay nombre, foto ni edad de una niña real. No hay identificador de aparato porque no se pide.

## 1. Qué se construye

Godot 4.7.2, solo 2D, GDScript. Sin C#, sin extensión nativa, sin plugin de red. El corte es jugable de principio a fin:

- Patio con tres ventanas y la campana.
- Nido: hacer el diez. Dos filas de cinco huecos. La décima enciende. Una oncena no.
- Collar: piedra, estrella, piedra, estrella. La siguiente se arrastra desde el arcón.
- Cierre: nueve puestas, ella pone la última.
- Farol: dos, los dos válidos, lo coloca ella.
- Pantalla del padre con PIN y como mucho dos frases.
- Registro de duda, fallo y corte.
- Hora e inclinación se anotan y no cambian nada.

Partida de referencia, si nada se tuerce: tres piedras; Estrella cierra un diez en el paño; ella repite 7 y 3; borde 8, 5 y 9; collar; cierre con su mano; farol.

No entra: llevada, préstamo, euros, céntimos, centenas, grupos, reparto, sobra, problemas con historia, las otras seis salas y los 81 micropasos como selector.

## 2. Aparato y proyecto

Amazon Fire 7 (2022), KFQUWI. Fire OS 8.3.3.8, Android 11, API 30. MT8168, Mali-G52, 2 GB de RAM; en reposo quedan unos 620 MB. Pantalla 1024×600, 60 Hz, unos 171 dpi. Acelerómetro sí. Giroscopio no. Multitáctil. Sin permiso de internet. El APK cabe por debajo de 40 MB y nunca pasa de 80.

Se prueba antes en el ordenador con el ratón como dedo. En el escritorio el acelerómetro devuelve cero: la inclinación queda `desconocida` y el juego sigue igual. No se simula una postura en la exportación.

| Ajuste | Valor |
|---|---|
| Renderer | `gl_compatibility`, también en móvil. Sin Vulkan, sin Forward+ |
| Viewport | 1024×600 |
| Estirado | `canvas_items`, aspecto `expand` |
| Orientación | landscape fijo, no sensor |
| Inmersivo | sí, en la exportación Android |
| Arquitectura | solo `arm64-v8a` |
| min SDK | 30 |
| target SDK | el de la plantilla de Godot 4.7.2, si arranca en API 30 |
| Permisos | ninguno. Internet apagado |
| Sensores en el manifiesto | acelerómetro `required=false`. El giroscopio no se lee |
| Main scene | `res://escenas/arranque.tscn` |

`user://` es el directorio privado de la app. No hay permiso de disco y no se escribe fuera.

Botón atrás: en una sala guarda y vuelve al patio; en el patio guarda y sale. Sin diálogo de «¿seguro?». `auto_accept_quit` en falso. Se vuelca en pausa, pérdida de foco, atrás y cierre.

Nada importante vive en los 48 px de abajo. Un toque mide al menos 80 px. Aire de 24 px. Frase de hasta doce palabras, cuerpo 32 px como mínimo. El texto se ve aunque no haya voz.

## 3. Presupuesto

Una sala en memoria. Al cambiar de escena se suelta el fondo y el atlas de la anterior. Los autoloads no cargan dibujos de sala.

| Tope | Cifra |
|---|---|
| Sprites en movimiento | 40 |
| Partículas al encender | 12, `CPUParticles2D`, discos del mismo ámbar, 1,2 s. No confeti |
| Capas de fondo | 2 |
| Fondo | 1024×600, ETC2 |
| Atlas de la sala | 512×512, se suelta al salir |
| Pieza | 128×128 en textura, 96 px en pantalla |
| APK | por debajo de 40 MB; nunca 80 |
| Dibujo comprimido | no pasa de 8 MB. Si no cabe, se quita dibujo, no el gesto |
| `user://` | kilobytes. `metricas.json` no pasa de 256 KB |

Si falta un dibujo, `ColorRect` del color de sala y del mismo tamaño. No hay color de fallo. Paleta cerrada en `assets/palette.json`.

Sin vídeo, sin malla, sin shader pesado, sin precarga de las otras salas. Una voz como mucho a la vez. Sin vibración.

Prohibido en el proyecto: `HTTPRequest`, sockets, `Input.get_gyroscope()`, nodos 3D, `VideoStreamPlayer`, anuncios, cuentas, y un `Label` de tiempo aunque sea invisible.

## 4. Escenas y archivos

```
res://escenas/arranque.tscn            Node. Carga el guardado y pasa al patio. Sin logotipo, sin «pulsa para empezar»
res://escenas/patio/patio.tscn         Control
res://escenas/nido/nido.tscn           Control. Hacer el diez
res://escenas/collar/collar.tscn       Control. El patrón
res://escenas/cierre/cierre.tscn       Control. Nueve y una
res://escenas/farol/farol.tscn         Control. Dos faroles
res://escenas/torre/torre.tscn         Control. El farol en la pared
res://escenas/padre/padre.tscn         Control. PIN y frases
res://escenas/ui/frase.tscn            Se instancia
res://escenas/ui/estrella.tscn         Se instancia. Cara según estado
res://escenas/piezas/piedra.tscn
res://escenas/piezas/cuenta.tscn       Piedra o estrella de tela
res://escenas/piezas/farol.tscn
res://escenas/ui/pulso.tscn            Anillo ámbar de 1,2 s
```

```
res://scripts/nucleo/reglas.gd         Constantes. Sin nodos
res://scripts/nucleo/sesion.gd         Máquina de sesión. Sin nodos
res://scripts/nucleo/adaptador.gd      Qué toca. Sin nodos
res://scripts/nucleo/guardado.gd       Serializa y valida. Sin nodos
res://scripts/nucleo/medida.gd         Distancias y radios. Sin nodos
res://scripts/autoload/progreso.gd     Autoload
res://scripts/autoload/metricas.gd     Autoload
res://scripts/autoload/adaptador_nodo.gd  Autoload, envuelve a nucleo/adaptador.gd
```

Todo lo de `scripts/nucleo/` es lógica pura, sin `Node`, para poder probarla en cabeza sin ventana. Es la única parte con pruebas automáticas en este corte.

Arte ya hecho, que se usa tal cual:

| Archivo | Uso |
|---|---|
| `assets/pantallas/<sala>-1024x600.png` | Referencia de la placa. No se carga en el juego si los nodos ya la reproducen |
| `assets/pantallas/<sala>-zonas-1024x600.png` | Las zonas numeradas, para comprobar el árbol de nodos |
| `assets/piezas/piedra-96.png`, `piedra-72.png`, `piedra-68.png` | Piedra del montón, del hueco y del cierre |
| `assets/piezas/nido.png` | Marco de diez huecos |
| `assets/piezas/estrella-tela.png` | Estrella del patrón |
| `assets/piezas/farol-ambar.png`, `farol-terracota.png` | Los dos faroles |
| `assets/piezas/campana.png` | Campana del patio |
| `assets/fondos/piedras.png` | Pared y suelo de la sala de Piedras |
| `assets/personajes/estrella-cara.png` | Cara fijada. Se recorta a 112×150 |

Navegación con `change_scene_to_file`. El estado no viaja en la escena: vive en los autoloads. El fundido de 200 ms es un `ColorRect` en un `CanvasLayer` del autoload, sin retener las dos salas.

## 5. Autoloads

Tres, en este orden: `Progreso`, `Metricas`, `AdaptadorNodo`. No hay un cuarto. Las constantes viven en `nucleo/reglas.gd`, precargado.

Las salas no deciden pedagogía. Emiten hechos. `Metricas` los anota. `AdaptadorNodo` responde. `Progreso` guarda. Ella no ve el nombre de ningún estado.

### Progreso

Único escritor de `user://progreso.json` y `user://sesion_abierta.json`.

- Carga al arrancar. Si no existe, partida nueva: sin luces, con la llama de casa encendida, sin aciertos inventados, sin cierre pendiente.
- Escritura atómica: `.tmp`, `flush`, cerrar, renombrar encima. Se conserva la generación anterior como `.bak`. Si el principal está corrupto y el `.bak` vale, se restaura. Si fallan los dos, se empieza de cero y **no** se fabrica un cierre.
- Guarda en cada suelta juzgada y en cada cambio de estado. Una ráfaga se aplaza 200 ms; pausa, atrás y cierre no esperan.
- Una pieza en el aire al matar la app se tira. No es fallo ni acierto. El nido vuelve al último estado asentado.

Una luz en `true` no vuelve a `false` por ningún camino de código. Aserto al guardar.

### Metricas

Único escritor de `user://metricas.json`. No dibuja, no elige micropaso y no habla con el padre.

Clasifica la suelta en crudo y emite el evento del GDD 10.1. Anillo de intentos: 200. Anillo de eventos de duda: 800. Al pasar, se olvidan los más viejos. Nunca se olvidan luces, adornos ni estados: eso no vive aquí.

### AdaptadorNodo

La máquina de sesión, sin nodos de interfaz. Lee a los otros dos.

Solo puede cambiar: el tramo, cuántas piedras hay en el nido al empezar, si el paño del ejemplo está, qué `error_id` se nombra, cuánto dura el corte y si hoy hay idea nueva. En este corte la idea de hoy es siempre hacer el diez y no hay otro micropaso en pantalla.

No puede: quitar luces, poner cronómetro, cerrar el collar, enseñar un marcador, enviar datos, quitar un adorno, ni dejar que la hora o la inclinación cambien el plan.

Señales que la sala escucha: `presentar`, `mostrar_ejemplo`, `ocultar_ejemplo`, `volver_pieza`, `encender`, `frase`, `ir_a`. Señales que la sala emite: `agarrar`, `mover`, `soltar`, `desdecirse`, `toque_vacio`, `salir`, `pausa_app`.

La sala no cuenta fallos ni compara números. Manda píxeles y tiempos en crudo.

## 6. Máquina de sesión

Estados, que ella no ve: `PATIO`, `ENTRADA`, `YA_SABE`, `IDEA_DEMO`, `IDEA_REPITE`, `BORDE`, `ACERTIJO`, `CIERRE`, `FAROL`, `TORRE`, `GUARDADO`.

```
PATIO → ENTRADA → YA_SABE → IDEA_DEMO → IDEA_REPITE → BORDE → ACERTIJO → CIERRE → FAROL → TORRE → GUARDADO → PATIO
                                                          |          |
                                                          |          +-- 2 fallos, o corte --> CIERRE
                                                          +-- el reloj interno no corta un arrastre
```

| Estado | Entra | Sale | Qué ve ella |
|---|---|---|---|
| `PATIO` | Al abrir o al guardar | Toca una ventana o la campana | Tres ventanas, la campana. Sin marcador |
| `ENTRADA` | Entra en el nido | 4 s, o ella toca una pieza | Estrella curiosa, una frase. Aún no cuenta |
| `YA_SABE` | Tras la entrada | Acierto. Se ayuda hasta lograrlo | Tres piedras. Los tropiezos de aquí no cortan |
| `IDEA_DEMO` | Tras el ya-sabe | 20 s, o ella empieza a arrastrar | Estrella cierra un diez en el paño |
| `IDEA_REPITE` | Al acabar el modelo | Ella suelta el gesto | Nido con siete. Ella añade tres. Con ejemplo: es ayuda |
| `BORDE` | Tras la repetición | 3 intentos, o 4, o 2 fallos, o corte | 8, luego 5, luego 9. Sin «1/3» |
| `ACERTIJO` | Borde sin corte | El collar resuelto, o corte | Collar. Un tropiezo aquí no toca la aritmética |
| `CIERRE` | Por orden, por corte o por reloj | Ella enciende la luz | Nueve y una. Estrella no la resuelve |
| `FAROL` | Tras el cierre | Ella elige uno | Dos faroles, los dos válidos |
| `TORRE` | Tras elegir | Lo coloca, o sale | El farol en la pared |
| `GUARDADO` | Al colocar o al salir | Patio, o la app se cierra | Nada nuevo. La luz sigue |

El reloj interno no se dibuja y no corta un arrastre. Actúa al soltar, entre turnos:

- 420 s: no se abre otro intento de borde.
- 480 s: al soltar la pieza que tiene en la mano, se entra en el cierre.
- 400 s y sigue en el collar con la pieza avanzando: se respeta la mano hasta la suelta.
- 20 s sin toque con la pieza presentada y no en la mano: abandono. En la misma sentada se va al cierre.
- Menos de 15 s dentro de una sala sin haber tocado una pieza: no abre sesión, no deja farol y se borra `sesion_abierta.json`.

Si el recorrido acaba antes, se acaba. No se rellena.

**Decidido aquí, no en el GDD:** el collar no tiene límite propio de tiempo. Lo cierra el acierto, el corte o el reloj interno. Un límite de 90 s se descartó porque el GDD ya corta a los 480 s y dos relojes distintos se contradicen.

## 7. Los cuatro finales

Un final es cómo termina la sesión, no una pantalla.

| Final | Cómo se llega | Qué queda |
|---|---|---|
| Completo | Borde sin dos fallos, collar, cierre y farol | Luz de Piedras, luz de Acertijos si se resolvió el collar, farol colocado |
| Dos fallos en el borde | Segundo fallo del borde | Frase de corte, cierre, farol. Sin collar. El segundo fallo no enciende nada |
| Corte por cansancio | Tres devoluciones en un intento, tres pausas de 4 s en un intento, o el segundo fallo | Igual que el anterior, con la misma frase |
| A medias | Cierra la tableta, botón atrás o 20 s sin toque | Se guarda lo hecho. El acierto no se inventa. Al volver, una que ya sabe |

El cierre y el farol existen en los cuatro. Lo que cambia es si hay collar y si el farol se coloca en esa sentada o en la siguiente.

Los fallos de `YA_SABE` no cuentan para el corte. Una devolución sola no corta. Una pausa sola no corta.

Al volver otro día, y solo entonces: V05, V06, V07, y luego una que ya sabe. Sin saludo si en quince segundos no toca una pieza.

## 8. Entrada y colocación

Un dedo. El segundo se ignora: no suelta la pieza del primero, no pulsa atrás y no abre una sala.

- Agarrar: contacto sobre una pieza del montón o de la bandeja.
- Mover: el centro se ha alejado 24 px o más del origen. Menos de eso es un toque quieto y no es intento.
- Soltar: levantar el dedo.
- Vale si el centro queda a **36 px o menos** del centro de un hueco vacío. Es el mismo radio para todos los huecos y ninguno se preilumina.
- Si no vale, la pieza vuelve al origen en 0,4 s, en silencio.
- Si vale, ocupa el hueco: imán al centro del hueco, sin física.

Sin doble toque. Sin pulsación larga salvo la campana, 1,5 s. Sin cuerpo rígido. `Control` y el dedo alcanzan.

**Decidido aquí:** el radio de 36 px es también el que decide que la pieza «entró» en un destino, para las reglas de duda. Un solo radio en todo el código.

## 9. El nido

Micropaso de pantalla: M11, la caja de diez. M01 a M10 no se juegan en este corte.

| Tramo | Nido al empezar | Montón | Acierto |
|---|---|---|---|
| Ya sabe | vacío | tres, ya encendidas, sin otras | las tres en el nido. Calor pequeño, no la luz del diez |
| Demo | el de Estrella, en el paño | Estrella añade hasta cerrar diez, 20 s | ella lo ve. Esa luz no es del castillo |
| Repite | siete | tres claras y otras apagadas | la décima enciende. Una oscura no entra y vuelve, y eso aún no es fallo del borde |
| Borde 1 | ocho | al menos seis, ninguna preelegida | parar en diez |
| Borde 2 | cinco | igual | igual |
| Borde 3 | nueve | igual | igual |
| Borde 4 | seis | igual | solo si van cero fallos, sin corte y reloj interno por debajo de 300 s |
| Cierre | nueve y una clara | lo justo para un gesto | la enciende su dedo |

No hay botón de listo. Quedarse corta no es fallo: el nido espera.

La oncena, con el nido lleno, vuelve sola en 0,4 s y en silencio. Estrella, pensando. La primera del intento no suma fallo. La segunda del mismo intento es `E_DIEZ`.

Un grupo que no cierra el diez y se deja 3 s sin desdecirse es fallo a la primera en el borde: es una respuesta, no un límite del material. Si se desdice dentro de los 3 s, no es fallo.

Adivinar no cuenta. Tocar el vacío o soltar sin haber movido no enciende nada y no es fallo.

El pulso ámbar de 1,2 s nace en el borde del nido de ella, en la suelta válida, y no convive con otro. El paño del ejemplo, al resetear, se apaga en 0,4 s **sin** pulso.

El andamio de 7 y 3 son huecos vacíos, no piedras marcadas. Nunca las dos cosas.

## 10. Collar

Solo si el borde no se cortó. No se anuncia como examen ni con número de pregunta. Pantalla propia, con fundido: no hay cordón de camino.

Tira puesta: piedra, estrella, piedra, estrella, y un hueco que pide piedra. La siguiente cuelga del arcón. Un solo sitio del que sale la pieza: no hay dos botones y no se dice en texto qué pide el hueco.

Si no sigue el ritmo, resbala en 0,4 s, en silencio, y vuelve al arcón. Eso no suma fallo del borde y no toca M11. Al segundo tropiezo, Estrella deja el ritmo en su lado y ella coloca en el suyo: eso es ayuda del acertijo, no una nota.

La victoria es el mismo pulso de 1,2 s sobre el cordón. No nace un adorno de torre por el collar.

Si entra al collar desde el patio sin haber hecho el borde, puede jugarlo y luego ir al nido. La sala no se cierra para obligarla.

## 11. Cierre

Una que puede hacer. Si el borde de nueve salió, se repite ese gesto con la piedra clara cerca de la mano. Si costó, son las tres del ya-sabe.

1. **C0.** Piezas a la vista. Unos 15 s para el primer movimiento.
2. **C1.** Si no enciende, o pasan 15 s sin un movimiento con destino: el ejemplo aparece en el lado de Estrella. La zona es amplia y no es un solo píxel el que brilla.
3. No hay C2. No hay botón de saltar.

Estrella no pone la última piedra. El acierto no sube de estado, no suma fallo del borde y no baja peldaño. Hasta que esa luz se enciende con su mano no se da el farol por ganado.

Si cierra la tableta antes, el cierre queda pendiente y el patio ofrece esa bandeja al volver, no el nido que falló.

## 12. Farol y torre

Dos faroles, ámbar y terracota, misma forma y mismo tamaño. Los dos son válidos: ninguno es el bueno y ninguno es gris. Se elige uno y se coloca. Torcido vale. Encima de otro vale. El juego no lo endereza.

El farol se gana por un solo hecho: ella ha encendido el cierre con su dedo en esa sentada. También si el borde se saltó. No se gana por no haberse equivocado.

En la torre no se dibujan ganchos vacíos: serían estrellas vacías. La pared está lisa y solo se ve lo colocado.

## 13. Duda, fallo y corte

Un intento escribe como máximo una etiqueta de juicio: duda, fallo o corte. No las tres.

### Duda

Se anota al soltar. Ella no lo ve y no se le dice que ha dudado. La duda no hereda frases de fallo.

| Tipo | Cuándo | No es |
|---|---|---|
| `origen` | El centro acaba a 24 px o menos del origen, tras tenerla 1 s o más | Ni acierto ni fallo |
| `destino` | Durante el agarre el centro estuvo 0,4 s o más en el radio de un destino, y se suelta en otro | No es fallo por sí solo |
| `quieta` | La pieza quieta, menos de 24 px, más de 8 s | No es además una pausa ni un lento |
| `desdice` | Antes de 3 s desde la suelta vuelve a cogerla y la saca del destino | No es devolución. No se quita el gesto |

Una suelta puede llevar más de un tipo.

### Devolución

Vuelve al origen después de 3 s, habiendo salido. Tres en el mismo intento cortan lo nuevo. Una no corta.

### Fallo

Suelta, habiendo movido, en un sitio que no enciende. La segunda pieza que el material rechaza en el mismo intento es el fallo. Un método equivocado dejado 3 s sin desdecirse es fallo a la primera.

### Corte

Entre turnos, nunca a mitad de un arrastre:

- tres devoluciones en el mismo intento, fuera de la ventana de 3 s;
- tres pausas de 4 s sin toque en el mismo intento;
- el segundo fallo del borde;
- el reloj interno.

Frase, literal y única: «Seguimos con una que ya sabes.» Luego silencio y el cierre. No se nombra cansancio ni fallo. El corte no quita luz, no quita farol y no es una bajada del castillo.

### Ayuda

Ayuda usada significa solo esto: el paño del ejemplo está en pantalla, el tramo es la repetición del modelo, o el cierre está en el peldaño C1. No hay detección de un segundo dedo de otra persona.

| Estado | Andamio, sin anunciarlo |
|---|---|
| Aprendiendo | ejemplo al lado |
| Frágil | piezas a la vista, ejemplo ausente |
| Firme | ejemplo ausente |
| Suelto | sin piezas de apoyo |

## 14. Algoritmos

Locales. Ella no los ve y no se le dice que ha subido ni que ha bajado. La edad no es una entrada y no hay campo de edad.

### 14.1 Observación

Las tres primeras sesiones completas solo observan: no se sube a frágil, ni a firme, ni a suelto, y no se baja. Sin ver pasa a aprendiendo si ella arrastra el modelo; esos aciertos no se aplican al terminar la tercera. Se empieza a contar en la sesión 4.

Desde la sesión 1 sí mandan el cierre en acierto, el corte a los dos fallos del borde y el corte por cansancio. Enseñar el gesto si duda y falla es ayuda, no un juicio, y también manda desde el día 1.

**Decidido aquí:** durante las tres primeras sesiones el micropaso es siempre M11 y el borde repite 8, 5, 9. No hay idea nueva porque no hay otro micropaso en este corte.

### 14.2 Estados

Sin ver, aprendiendo, frágil, firme, suelto. El estado vive en el id del micropaso, no en la sala: M12 firme no marca M13. Solo se sube uno. Solo se baja uno. El suelo, una vez vista la idea, es aprendiendo. Bajar no quita luces ni adornos.

Otro día es otra fecha local, no 24 horas.

Sube:

- A aprendiendo: arrastra el modelo.
- A frágil: acierta sola hoy, moviendo piezas, sin ayuda y sin duda. No vale el cierre ni la repetición del modelo.
- A firme: 3 ítems distintos del banco de ese id, ninguno igual al ejemplo, en al menos 2 fechas, como máximo 2 ítems por fecha, sin ayuda, sin duda y sin ser cierre. Si el banco tiene discriminador, uno de los 3 es ese. Un mismo ítem no es más de la mitad de los aciertos que alimentan la subida. Un acierto de hace más de 14 fechas no sirve. No baja el estado y no apaga luces.
- A suelto: ya firme, sin piezas de apoyo, en 2 fechas distintas de la fecha en que pasó a firme, sin adivinanza, y con tiempo de manipulación menor o igual que su mediana. Hacen falta 6 aciertos sola de ese id.

El primer acierto sola de ese id en esa fecha no sube a firme ni a suelto. El tramo `YA_SABE` no consume ese cupo. Lento no existe hasta esos 6 aciertos: lento es tiempo con la pieza en movimiento mayor que 1,5 veces la mediana de esos 6. Lento no impide frágil ni firme; impide suelto.

Baja:

- Como máximo una bajada por id y fecha.
- Si duda y falla: baja uno y se enseña el gesto. Si ya estaba en aprendiendo, se queda y vuelve el ejemplo.
- El segundo fallo con duda del borde corta, enseña el gesto y no baja otra vez.
- Suelto no llega a frágil en la misma fecha.
- Un fallo aislado sin duda no tira un cimiento firme.

El cierre, la repetición del modelo y el acertijo no cambian ningún estado de aritmética.

En este corte, M11 puede llegar a frágil. Firme pide 3 ítems distintos en 2 fechas, y el banco de este corte no los tiene: no se escribe firme a mano.

### 14.3 Error sistemático

Mismo `error_id` en 2 ítems distintos y 2 fechas, y solo si el discriminador de esa familia ya se ha visto. Hasta entonces no hay frase y no hay techo. El techo, si llega, baja como máximo un estado por fecha. Mientras esté puesto, el sucesor no se abre.

32−17 no separa errores. El discriminador es 32−15: bien 17, girar 23, olvidar el descuento 27. Sin el discriminador no se elige frase.

### 14.4 Qué toca

Cada sesión, desde la cuarta:

- **Ya sabe:** el id firme o frágil cuyo acierto sola es el más antiguo. Uno.
- **Borde:** el id en aprendiendo o frágil con predecesores firmes, el más antiguo. Si no hay, el siguiente sin ver cuyo predecesor está firme.
- **Repaso:** va dentro de ya sabe, no es un tramo extra.
- **Acertijo:** uno cuyo cimiento de compañía esté al menos en aprendiendo y que no esconda una cuenta por encima del borde.

Parecido, si acertó dudando: el mismo id, otro ítem. Cada tercer parecido es el discriminador, si existe. Un paso nuevo solo si cada predecesor está firme; los predecesores se declaran en el id, no son «el número anterior».

### 14.5 Qué puede cambiar y qué no

Puede cambiar: el id, el tamaño de los números dentro de ese id, si el ejemplo está, la frase de ayuda de ese `error_id`, si hoy hay idea nueva y la duración al cortar.

No puede: quitar luces, poner cronómetro, cerrar acertijos, enseñar un marcador, enviar datos fuera, ni usar la hora, la inclinación o la edad como argumento de ninguna función.

### 14.6 Sala evitada

Solo si era elegible y, en 3 de las últimas 5 sesiones abiertas, no se entró. Antes, silencio. La ventana no lleva marca. La frase del padre, si cabe en el cupo de dos, es «La sala sigue abierta.» No dice «no ha entrado».

## 15. Guardado y telemetría

Tres ficheros. JSON, UTF-8, sin identificador de aparato y sin nombre de niña. La hora es local, ISO-8601 con desplazamiento. El día es `YYYY-MM-DD` local.

### 15.1 `progreso.json`

```json
{
  "version": 1,
  "silencio": false,
  "pin": null,
  "techo": "ninguno",
  "observando": true,
  "sesiones_completas": 0,
  "llama_casa": true,
  "luces": { "piedras": false, "acertijos": false },
  "farol_ganado": false,
  "farol_colocado": null,
  "cierre_pendiente": false,
  "estados": {
    "M11": {
      "estado": "sin_ver",
      "ultimo_dia_sola": null,
      "aciertos_sola": 0,
      "items": [],
      "error_id": null
    }
  },
  "ultima_sesion": {
    "dia": "2026-11-06",
    "hora": "18:04",
    "duracion_juego_ms": 0,
    "salas_abiertas": ["piedras", "acertijos"],
    "sala_propuesta": "piedras",
    "salas_no_entradas": [],
    "cierre_pendiente": false,
    "farol_ganado": false,
    "techo": "ninguno"
  }
}
```

`pin` es `null` o `{ "sal": "<hex>", "hash": "<hex>" }`: SHA-256 de 16 bytes de sal más los cuatro dígitos. Nunca el PIN en claro. `techo` queda en `ninguno` en este corte; los valores futuros son `hasta_20`, `sin_llevada`, `sin_mercado`, `sin_centenas`, `sin_por`. `observando` pasa a `false` al terminar la tercera sesión completa. `farol_colocado` es `null` o `{ "color": "ambar|terracota", "x": 0, "y": 0 }`; no guarda huecos vacíos.

`items` guarda, por id, la lista de ítems ya acertados sola con su fecha, para la regla de los 3 distintos. Se recorta a los 12 más recientes.

### 15.2 `sesion_abierta.json`

Existe solo si hay sesión. Al terminar de verdad se vuelca lo duradero a `progreso.json` y se borra.

```json
{
  "version": 1,
  "inicio": "2026-11-06T18:04:00+01:00",
  "dia_local": "2026-11-06",
  "estado": "BORDE",
  "tramo": "borde",
  "sala": "nido",
  "toque_pieza": false,
  "fallos": 0,
  "cortada": false,
  "motivo_corte": null,
  "cierre_pendiente": false,
  "farol_pendiente": false,
  "inclinacion_inicio": "desconocida",
  "nido": [0, 1, 2, 3, 4, 5, 6, 7],
  "intento": 1,
  "ejemplo": false,
  "duracion_juego_ms": 0
}
```

`motivo_corte` es `null`, `dos_fallos`, `devoluciones`, `pausas`, `abandono` o `reloj`. No es una emoción. `nido` son los huecos ocupados, 0 a 9, dos filas de cinco: índice `r*5 + c`.

Al volver no se restaura el borde abandonado: si `cierre_pendiente`, el patio entra por el cierre; si no, la próxima apertura es una que ya sabe.

### 15.3 `metricas.json`

Un registro por intento, con la forma exacta del GDD 10.1:

```json
{
  "version": 1,
  "intentos": [
    {
      "id": "M11",
      "item": "8+2",
      "fecha": "2026-11-06",
      "t0": 0,
      "primer_toque_ms": 1200,
      "moviendo_ms": 4300,
      "pausas_4s": 0,
      "etiqueta": "acierto",
      "sola": false,
      "ejemplo": true,
      "cierre": false,
      "duda": ["destino"],
      "devoluciones": 1,
      "error_id": "",
      "tilt": "plana"
    }
  ]
}
```

`etiqueta` es `duda`, `fallo`, `corte`, `acierto` o `nada`. `t0` es el instante del primer toque del intento, en ms desde el inicio de la sesión. `item` es la cuenta de ese intento en texto corto (`8+2`, `7+3`, `collar-piedra`). `tilt` usa los cuatro cubos del apartado 16.

Tiempos separados, nunca sumados en un «lento»: hasta el primer toque, con desplazamiento de al menos 24 px, y pausas sin toque de al menos 4 s.

No se guarda una conclusión, ni una emoción, ni un porcentaje.

## 16. Inclinación

La tableta no sabe si ella está sentada o acostada; solo la inclinación del aparato. No hay giroscopio y no se echa de menos. Inclinar, agitar o tumbar la tableta no mueve piezas, no abre salas y no acorta la sesión.

`Input.get_accelerometer()` devuelve m/s², o `Vector3.ZERO` si no hay sensor. En el escritorio será cero.

Godot puede entregar el vector en ejes del aparato o ya girado con la pantalla. No se adivina: en el KFQUWI se mide una vez, con la tableta plana y la pantalla arriba, y el vector unitario queda fijado en `reglas.gd` con un comentario del eje medido. Hasta medirlo, el código usa `Vector3(0, 0, 1)` solo como candidato y una lectura fuera de rango no se clasifica.

```
g = Input.get_accelerometer()
si |g| < 7 o |g| > 12: muestra inestable; se conserva la última estable
d = normalizar(g) · normal_pantalla
plana        si d > cos(25°)      = 0,9063
encima       si d < -cos(35°)     = -0,8192
de_pie       en cualquier otro caso estable
desconocida  si no hay tres lecturas válidas
```

Una muestra por segundo, solo con sesión abierta. Se anota la mediana de cinco al empezar la sesión y en cada cambio de estado. No se guarda el chorro de 1 Hz.

Ninguno de esos valores elige nido, acorta la sesión, se muestra a ella ni sale en la pantalla del padre. No se llaman sentada, acostada, noche ni tumbada.

## 17. Padre

Pulsación de 1,5 s en la campana. Si no hay PIN, la primera entrada lo elige y lo repite. No hay PIN de fábrica. Si falla, las casillas se vacían y no se dice nada: sin contador de intentos y sin bloqueo. Bloquear dejaría a la niña fuera de su propio juego.

Con la cuarta cifra se cierra solo: no hay botón de confirmar. «C» borra una cifra.

Estrella no está en esa pantalla y no se la nombra. Él ve como máximo dos frases, en este orden, y solo si el hecho es de las sesiones ya contadas, no de la observación:

1. Si un sucesor no se abre por un error sistemático: «Seguimos con el gesto de antes.»
2. Si una sala se evita, según la regla: «La sala sigue abierta.»
3. Si no hay nada de eso: «Esto no es una nota.»

No aparecen: dudado, despacio, lento, siempre, frustrada, no ha entrado, retrasada, noche, tumbada, ni un número.

Techos, cinco, y solo estos. Ponerlos frena; quitarlos no salta cimientos.

| Techo | Qué esconde |
|---|---|
| Hasta 20 | Decenas, centenas, llevada, préstamo |
| Sin llevada | Llevada y préstamo |
| Sin mercado | Mercado, masa, capacidad, billetes |
| Sin centenas | Tres cifras y céntimos que exigen el cien |
| Sin signo de por | Los signos × y ÷. No esconde los grupos ni el reparto con piezas |

## 18. Texto y voz

Solo se graban ocho frases en este corte. Si falta el fichero, se ve el texto.

| Id | Cuándo | Frase |
|---|---|---|
| V01 | Primera llegada, si ha tocado una pieza | Hola. Soy Estrella. |
| V02 | Después, una vez | Mi magia no adivina. |
| V03 | Entrar al nido | Aquí las piedras se juntan y se separan. |
| V04 | Corte | Seguimos con una que ya sabes. |
| V05 | Volver otro día | Me alegro de verte. |
| V06 | Volver otro día | Tus luces siguen encendidas. |
| V07 | Volver otro día | No hay que recuperar nada. |
| V08 | Disco lleno, si cabe texto | Seguimos. Hoy no se ha guardado. |

Texto de pantalla que no se graba, el de las placas:

| Id | Dónde | Texto |
|---|---|---|
| T01 | Nido, si el tramo lo pide | Pon las que faltan. |
| T02 | Cierre | Pon la que falta. |
| T03 | Farol | Elige uno de los dos. |

Contrato de audio:

- `res://audio/voz/v01.ogg` … `v08.ogg`, OGG Vorbis, mono, 44,1 kHz, 96 kbps, sin silencio de cola, 4 s como máximo.
- `res://audio/campana.ogg`, 0,4 s, la misma con ayuda o sin ella.
- Normalizado a −3 dBFS de pico. Sin compresión que suba el ruido de fondo.
- Una voz a la vez. Tocar la frase la repite. Sin bucle, sin suspiro.
- Si el archivo no está, el juego funciona igual: la frase se ve y el acierto no espera sonido.

El texto permanece al menos 4 s. Ella puede seguir tocando antes de 0,8 s; el texto no bloquea.

## 19. Lo que no se escribe

Espejo, Círculo, Pergamino, Mercado, Jardín y Tesoro como escenas en las que se entra. Llevada, préstamo, centenas, euros, céntimos, grupos, reparto, sobra, signos × y ÷, problemas con historia. Los 81 micropasos como selector. Exportación. Vídeo. Red. Cuentas. Anuncios. Marcador. Vidas. Estrellas vacías. Sonido de error. Giroscopio. 3D. Un cronómetro, aunque sea invisible. Un icono de altavoz. Un botón de «listo». Dos botones en el collar. Una cara de Estrella en la pantalla del padre.

El esquema de `estados` y de `luces` admite claves nuevas sin borrar el historial: no hace falta migrar el fichero cuando entre otra sala.

## 20. Hecho, cuando

Se comprueba en el ordenador y luego en la tableta.

- [ ] La partida de referencia se juega entera con el ratón: tres piedras, demo, 7 y 3, borde 8-5-9, collar, cierre con su mano, farol en la pared.
- [ ] Dos sueltas que no encienden en el borde saltan al cierre, sin tercer fallo y sin collar. La ventana del collar sigue en el patio.
- [ ] Devolver tres veces, encadenar tres pausas o fallar dos veces cortan con la frase literal, y el último gesto es un acierto suyo.
- [ ] Cerrar a medias no inventa ese acierto. Al volver no reaparece el borde fallido y el patio ofrece el cierre pendiente.
- [ ] Menos de 15 s sin tocar una pieza no deja farol ni fichero de sesión.
- [ ] Una oncena no enciende. La segunda del mismo intento queda en `metricas.json` como `E_DIEZ`.
- [ ] `origen`, `destino`, `quieta` y `desdice` aparecen en `metricas.json` y en ningún nodo visible.
- [ ] La inclinación se anota en los cuatro cubos y el nido no cambia al tumbar la tableta.
- [ ] Un segundo dedo no suelta la pieza del primero ni abre una sala.
- [ ] Ningún hueco se preilumina en ningún tramo.
- [ ] `progreso.json` sobrevive a un corte de corriente: queda el `.bak` o el principal, y las luces no se apagan.
- [ ] Con el audio borrado, la partida se juega igual y la frase se ve.
- [ ] El APK es arm64, Compatibility, inmersivo, 1024×600, sin permiso de internet y no llama al giroscopio.
- [ ] No hay pose triste, ni corona, ni varita, ni reloj en pantalla, ni botón de listo, ni dos botones en el collar.
