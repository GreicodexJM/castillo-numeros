# Audio — Estrella y el Castillo de los Números

Este texto obedece `Documento-de-diseno` y el encargo cerrado del repositorio. Si choca con ellos, mandan ellos. El relato de `Relato` fija la boca: no se improvisa, no se alarga, no se canta. El lote que se graba está en `data/voces.json`. Si una línea del relato no está en ese archivo, se ve el texto del relato, tal cual. No se sustituye por otra frase grabada que no nombre el gesto.

Idioma: español de España. Estrella trata de tú. No dice «niña», «guapa» ni «lista». No adivina cómo se llama. No hay micrófono: ninguna pregunta espera una palabra. La respuesta son las manos.

Los generadores corren en el ordenador de desarrollo, nunca en el juego y nunca en la tableta. El APK no lleva clave de ningún servicio. No tiene permiso de internet. Si falta un archivo de audio, manda el texto.

## Qué se oye

Solo habla Estrella. No hay narrador. La niebla no tiene voz, ni gruñido, ni respiración de monstruo. En el mercado no habla un tendero. En el rincón del padre no habla nadie: ahí se leen frases, no notas, y Estrella no nombra el PIN, el padre ni el aparato.

Una frase, luego silencio. El silencio no es un fallo. No se encadenan dos frases de fallo sin una ayuda visual en medio. No se acumulan tres halagos. No se mezcla un acierto con un pero.

El texto se ve aunque haya voz. Es el campo `texto` del JSON, letra de al menos 28 px. No se resume y no se traduce. Una frase de hasta doce palabras, salvo cuatro literales del relato que ya pasan de doce y no se reescriben (abajo).

## Voz

ElevenLabs, en el ordenador de desarrollo. Una toma por id. El archivo no añade palabras, suspiros, risas ni jadeos.

| Dato | Valor |
|---|---|
| Personaje | Estrella, aprendiz, chica joven |
| Idioma | español de España |
| Tono | cálido, claro, lento |
| Cara que se oye | curiosa, contenta o pensando |
| Lo que no se oye | decepción, enfado, tristeza, prisa, examen |

No habla como un bebé. No habla como una maestra severa. Se sienta al lado. También está aprendiendo: no esconde la cuenta para poner nota.

La entonación de una pregunta es suave y se queda esperando las manos. No se repite la pregunta. Un acierto no sube a tono de concurso. Un fallo no baja a tono de pena. La pieza, si vuelve, vuelve despacio. La voz no la empuja.

Dentro de la frase, la pausa es solo la que ya marca el punto. No se añade un «eh» ni un «venga».

### Entrega por situación

| Situación | Cómo suena | Qué no hace |
|---|---|---|
| bienvenida | Sonrisa pequeña. Lenta. Presenta y calla. | No pide que contesten. No nombra miedo. |
| idea de hoy | Enseña con las manos. Unos veinte segundos de boca, luego ella arrastra. | No dice «a ver si puedes». No anuncia un reto. |
| duda | Espera. Habla de la mano y de la pieza, no de lo que ella siente. | No hereda una frase de fallo. No dice «venga». |
| fallo concreto | Curiosa. Nombra las piezas y el número. | No nombra a la persona. No hay sonido de error. |
| acierto concreto | Contenta, una frase, el gesto. | No dice genio, ni lista, ni perfecto, ni campeona. |
| cierre | Calma. El adorno importa más que la palmada. | No cuenta aciertos. No dice que ha sido perfecto. |
| vuelta al día siguiente | Contenta de ver. La luz sigue. | No dice «te echaba de menos», ni «por fin», ni «se ha apagado». |
| cansancio | El mismo tono de siempre. Una frase puente. | No dice cansancio, ni fallo, ni prisa, ni minutos. |

El JSON usa también `sala`, `cuenta que ya sabe`, `borde`, `acertijo`, `ayuda` y `salida`. Son el mismo personaje y la misma toma. No son bancos distintos de emoción.

## El archivo `data/voces.json`

Listado cerrado. 395 frases. Una frase por id. No hay dos id con el mismo texto: si el relato repite una línea, se graba una vez y se reutiliza el id.

Cada entrada tiene:

| Campo | Uso |
|---|---|
| `id` | Nombre del archivo: `audio/voz/{id}.ogg` |
| `situacion` | Para elegir, no para leer en voz alta |
| `texto` | Lo que se dice y lo que se escribe |
| `palabras` | Control del tope de doce |
| `banco` | Solo en F01–F12, D01–D12 y A01–A12 |
| `literal_gdd` | Si está, el texto no se toca |

`secuencias` ordena ids ya existentes. No añade frases. Entre frase y frase de una secuencia se espera a que acabe el audio y un silencio de unos 0,6 s. Si ella está arrastrando, no se habla encima. El reloj de la sesión no corta un arrastre a medias y no se dibuja.

### Literales que no se tocan

Del GDD, copiados tal cual:

- «Seguimos con una que ya sabes.» → `cansancio.seguimos`
- «Me alegro de verte.» → `vuelta.alegro`
- «Tus luces siguen encendidas.» → `vuelta.luces`
- «No hay que recuperar nada.» → `vuelta.nada`
- «Estas monedas son del juego.» → `sala.monedas_juego`

También quedan cerrados, y no se parafrasean: «No se compra de verdad.», «Me llevo una.», «Pido prestada una decena.», «Son nueve. Falta una.»

Cuatro líneas del relato pasan de doce palabras. Son literales de primera visita o del banco de acierto. No se parten y no se acortan: el audio y el subtítulo dicen lo mismo.

| Id | Palabras |
|---|---|
| `sala.tesoro_1` | 13 |
| `sala.tesoro_2` | 13 |
| `sala.acertijos_1` | 13 |
| `acierto.a07` | 13 |

En pantalla pueden ocupar dos líneas. Siguen siendo una frase.

### Qué no se graba

No se graba la sección «Frases que no se dicen nunca» del relato. Esos ejemplos no entran en ElevenLabs ni en el JSON. Tampoco se graba una frase nueva inventada en el aparato, ni una variante de número armada a trozos.

Si el número de hoy no tiene frase propia en el JSON, se ve el texto del guion, con el número en palabra: uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve, diez, once, doce, trece, catorce, quince, dieciséis, diecisiete, dieciocho, diecinueve, veinte. No se pega una cifra grabada a otra frase. F08 y F12 cambian la pieza o el número solo si la frase resultante ya está en el archivo. Si no, manda el texto.

«Sobran tres.» es `idea.sobran_tres`. Sirve al enseñar ocho y cinco, y también al nombrar el resto en la llevada. No se graba dos veces.

## Cómo se elige

1. Si es duda, solo `duda.d01`–`duda.d12`. Aunque luego falle. Mientras la pieza no se ha soltado en un sitio que no toca, no hay fallo.
2. Si es fallo, la frase del banco que nombra ese gesto. Si el error de hoy es el de otros días, esa misma, sin decir que se repite.
3. Si el banco no nombra las piezas de hoy, la frase concreta del guion que sí esté en el JSON. Si tampoco está, se ve el texto del relato. No se inventa.
4. No se dicen dos frases de fallo seguidas sin una ayuda visual en medio.
5. A la segunda vez del borde, no hay tercera frase de fallo. Se dice `cansancio.seguimos` y se va al cierre. No se anuncia el corte. No se dice que el acertijo se pierde. La sala de acertijos sigue abierta.
6. El acierto usa el banco o la frase concreta del guion. Una sola. `cierre.a10` solo al poner el adorno del cierre, nunca en cada intento.
7. No se mezcla un acierto con un pero.
8. Si falta el audio, se ve el texto. No se sustituye por un pitido, ni por un sonido de error, ni por otra frase «parecida».
9. Estrella no explica estas reglas. No dice «eso ha sido una duda».

La duda, según lo que se ve:

| Se ve | Id |
|---|---|
| La sostiene en la mano | `duda.d01` |
| Conviene recordar que no hay prisa, una sola vez | `duda.d02` |
| La suelta cerca del origen | `duda.d03` |
| Cambia de destino | `duda.d04` |
| La mira un rato | `duda.d05` |
| Puede devolverla | `duda.d06` |
| El diez de hoy aún se está mirando | `duda.d07` |
| La sostiene mucho | `duda.d08` |
| Se le puede ofrecer la de dos; ella elige | `duda.d09` |
| Se desdice | `duda.d10` |
| La columna espera | `duda.d11` |
| Para un momento | `duda.d12` |

No se repite la misma en el mismo intento. Si `duda.d02` ya se dijo y el sistema corta lo nuevo, no se dice otra vez: se pasa a `cansancio.seguimos`. `duda.d09` se responde con la mano. Si no quiere esa pieza, no se insiste.

`ayuda.*` no es el banco de duda. Es el ejemplo al lado, cuando el guion ya ha decidido ayudar. «Otra vez: piedra, estrella.» (`ayuda.otra_vez_ritmo`) solo muestra el ritmo del acertijo, una vez. No es un reproche. «Los juntamos otra vez.» (`vuelta.juntamos`) solo cabe al no recordar, junto a `vuelta.no_pasa_nada` y `vuelta.siguen_aqui`. «No pasa nada» no tapa un fallo de cuenta. En un fallo de cuenta, manda el banco o «Son nueve. Falta una.»

`borde.*` es la consigna, antes de soltar. No es un fallo ni un acierto. No se dice cuántos intentos quedan. No se dice «último».

## Corte y cansancio

El corte de dos fallos y el corte por cansancio de la sesión usan la misma boca. No nombran el cuerpo ni el fallo. No hablan de minutos. Los siete minutos no se dicen.

Por defecto se dice solo `cansancio.seguimos`: «Seguimos con una que ya sabes.» Luego el cierre, con una que puede hacer. No se encadena con `cansancio.diez_trabajado`, `cansancio.una_que_puedes`, `cansancio.salto_trabajado` ni `cansancio.mercado_trabajado`. Esas cuatro quedan en el lote porque el relato las escribe. Si algún día una sala usa una de ellas en lugar del puente, es una sola frase, y no se suma al literal del GDD.

El camino corto no pasa por el acertijo. Salir a medias no es un corte: se dice la secuencia `salida` y se guarda. No se retiene a nadie hasta que acierte. No se dice «¿seguro?», ni «una más», ni «ya casi».

## Vuelta

No hay deuda ni racha. No se cuentan cintas en voz alta. No se dice «lento».

| Cuándo | Secuencia |
|---|---|
| Primer día | `bienvenida_primer_dia`, luego `torre_primer_dia` |
| Al día siguiente, si el diez está firme | `vuelta_dia_siguiente_firme` |
| Al día siguiente, si aún no está firme | `vuelta_dia_siguiente_sin_firme` |
| Después de varios días | `vuelta_varios_dias` |

`vuelta_varios_dias` dice, en este orden: «Hola.» «Me alegro de verte.» «Tus luces siguen encendidas.» «No hay que recuperar nada.» «Empezamos por una que ya sabes.» Si además hay que acortar, el puente es otra vez `cansancio.seguimos`, no una frase nueva.

Una sala no visitada no se nombra como evitada. Si toca decirlo: `vuelta.puerta` y `vuelta.cuando_toque`. No se dice «cuando te atrevas».

## Primer jugable

Sala: Piedras de luz, hacer el diez. No hay llevada, ni euro, ni problema con historia en esta boca, aunque esas frases ya estén en el lote para más adelante.

Orden, si no hay corte:

1. `bienvenida_primer_dia`
2. `torre_primer_dia`
3. `entrar_piedras`
4. `cuenta_que_ya_sabe` — los tropiezos de aquí no cuentan para el corte; se ayuda hasta el acierto
5. `idea_de_hoy_hacer_el_diez` — ella repite ocho y dos; el ejemplo se queda al lado
6. Borde, sin anunciar la cifra: siete, nueve, seis, y cinco y cinco solo si aún no van dos fallos
7. Acertijo piedra, estrella, piedra, estrella, solo si no hubo corte
8. `cierre_primer_dia`, luego la ficha del diez como comprobación guiada, luego `cierre_adorno`

El acierto del cierre es suyo, con ayuda si hace falta. Estrella no coloca la última pieza por ella. Si la ficha escrita no es la del diez, se cambia con calma (`cierre.ficha_diez`, `cierre.la_tuya_aqui`). No cuenta como fallo.

Al abrir el mercado, antes de jugar con monedas: `mercado_monedas`. «Estas monedas son del juego.» «No se compra de verdad.»

## Música

Bucle suave, original, sin letra. Se compone en el ordenador de desarrollo. No hay música con prisa: no acelera, no tiene un tic de reloj, no sube de tono para empujar, no cuenta los segundos. El pulso, si lo hay, es el de un paseo lento. Cabe un compás de silencio dentro del bucle.

No se parece a una canción de película ni a un castillo con marca. No hay fanfarria de victoria ni redoble de fallo. El cierre puede ser un poco más cálido. No es un premio de marcador.

| Archivo | Dónde | Duración |
|---|---|---|
| `audio/musica/patio.ogg` | Patio | 32–48 s, bucle |
| `audio/musica/sala.ogg` | Cualquier sala | 32–48 s, bucle |
| `audio/musica/cierre.ogg` | Torre, al elegir adorno | 24–36 s, bucle o una sola vez |

Una sola música a la vez. Al entrar en una sala, el cambio es un fundido de unos 0,8 s, no un corte seco. Mientras habla Estrella, la música baja a un susurro o se calla, y no vuelve hasta unos 0,8 s después de la frase. Nunca tapa la voz.

Si falta el archivo, hay silencio. El silencio vale. No se sustituye por un zumbido.

## Efectos

Mínimos. Generados en el ordenador, no en la tableta. El mismo gesto suena igual haya acertado o no.

| Archivo | Qué es | Qué no es |
|---|---|---|
| `audio/sfx/piedra.ogg` | Posar o devolver una pieza. Corto, suave. | No baja de tono si vuelve a la mesa. |
| `audio/sfx/luz.ogg` | La lámpara sube un poco. Menos de 0,8 s. | No es un aplauso ni una fanfarria. |
| `audio/sfx/adorno.ogg` | Cinta, farol u otro adorno, una vez. | No es un marcador que suma. |
| `audio/sfx/campanilla.ogg` | Campanilla del patio, suave, o no se usa. | No es alarma ni aviso de error. |

No existe `audio/sfx/error.ogg`. No se crea. No hay timbre de fallo, ni buzz, ni nota que desciende, ni vibración de castigo. Si una pieza vuelve, suena `piedra.ogg` o no suena. El relato lo deja en esas dos opciones. Se elige una y se mantiene: en el primer jugable, suena como cualquier piedra.

No hay aplauso grabado. La palmada, si se anima, es una y no lleva pista de público. No hay confeti sonoro. No hay tic de cronómetro. El botón, si suena, usa un toque más bajo que la piedra, el mismo para todos. No hay un clic de «prohibido».

La niebla, si se quiere aire, es un soplo casi inaudible, estable, sin forma de voz. Puede no existir. No crece si no se juega.

## Archivos y peso

| Tipo | Formato | Tope orientativo |
|---|---|---|
| Voz | Ogg Vorbis, mono, 22050 Hz, unos 32 kb/s | El lote entero, por debajo de 8 MB |
| Música | Ogg Vorbis, estéreo, bucle limpio, unos 64 kb/s | Por debajo de 1 MB las tres |
| Efecto | Ogg Vorbis, mono, corto | Unos pocos cientos de KB |

Normalizar la voz cerca de −16 LUFS, pico por debajo de −1 dB. Cabeza de silencio de unos 80 ms y cola de unos 200 ms. Sin música horneada dentro del archivo de voz.

El juego cabe holgado por debajo de 40 MB y nunca pasa de 80. Si el audio aprieta, no se recorta el gesto ni se inventa una frase más corta. Se dejan sin archivo las frases que no usa el primer jugable: se verá el texto. Orden de grabación, si hay que escalonar:

1. Literales del GDD y secuencias del primer día, del corte, de la vuelta y de la salida.
2. Bancos `duda.d01`–`duda.d12`, `fallo.f01`–`fallo.f12`, `acierto.a01`–`acierto.a09`, `acierto.a11`, `acierto.a12` y `cierre.a10`.
3. Primera visita de cada sala.
4. El resto del JSON.

En Godot el reproductor lee `data/voces.json`, busca `res://audio/voz/{id}.ogg` y, si no está, muestra `texto`. No llama a la red. No sintetiza en el aparato. No registra un error visible para ella.

## Prohibido en la boca y en la pista

No se dice, ni como consuelo ni como animación: «mal», «incorrecto», «eres un genio», «casi», «date prisa», «esto es fácil». Tampoco «error», «has fallado», «por poco», «rápido», «se acaba el tiempo», «último intento», «te echaba de menos», «se ha apagado», «qué lista», «qué listo», «perfecto» a solas, «campeona», «campeón», ni una comparación con otros niños o con el ayer en forma de nota.

«No hace falta hacerlo perfecto.» sí se dice: es `bienvenida.no_perfecto`, y niega que haga falta la perfección. No es un elogio. «No hay prisa. La piedra espera.» es `duda.d02`, no es «date prisa». «Cerramos con una fácil.» es `cierre.facil`, la invitación al cierre que ya escribe el relato. No es «esto es fácil» dicho para quitar importancia a un fallo, y no se usa fuera del cierre.

No hay sonido de error. No hay música con prisa. No hay vidas, cronómetro en pantalla, estrellas vacías ni marcador, ni en la voz ni en el efecto.
