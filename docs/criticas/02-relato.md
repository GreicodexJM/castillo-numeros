# Crítica del relato

El relato no se puede producir. No hay una escena dibujada de principio a fin. Hay tres biblias que no dicen lo mismo, un guion que enseña mal el único acertijo del primer día, y un lote de voz grabado a partir del guion que el GDD ya no manda.

`docs/GDD.md` manda. `docs/expertos/02-relato.md` se presenta como la boca y cierra diciendo que el listado de audio es cada línea entre comillas angulares. En ese archivo hay 632, 530 distintas. Cuarenta y tres son las frases que no se dicen. `docs/specs/lore.md` dice que no reabre lo cerrado y reabre el collar, el adorno y la vuelta. `docs/specs/audio.md` fija 395 frases en `data/voces.json`. De esas, 36 llevan banco y 359 no. Hay 13 secuencias. Ninguna llega del patio al adorno con la pieza, el sitio y la mano en cada paso. `docs/specs/programacion.md` ya tuvo que escribir una tabla de choques para no implementar el guion. Un relato que otro documento tiene que desobedecer no es un guion.

Esto ya está cerrado y no se vota: Estrella es aprendiz de magia de las luces, original, sin corona, sin varita y sin Disney. La niebla no es un monstruo, no tiene ojos ni voz, y no crece si un día no se juega. No se humilla. No se elogia a la persona. Trata de tú. No dice «niña», «guapa» ni «lista». El castillo solo gana luz.

## 1. Personaje, pelo, edad, frases, tono

El relato no fija la cara. Dice que el tono de la piel y el peinado «los fija el dibujo» (`02-relato.md`). El dibujo no está fijo. Hay tres Estrellas.

- Pelo. El GDD y `docs/specs/personajes.md` cierran melena a la mandíbula, flequillo recto, sin trenza y sin coleta. El GDD añade: si un prompt dice trenza, no se usa. `docs/specs/concept-art.md` pide una trenza corta en su lado derecho y manda repetir la imagen si el generador cambia esa trenza de lado. `docs/specs/direccion-artistica.md` pide media melena hasta la clavícula, raya a su izquierda, «sin trenza que cambie de hombro». Tres cortes. Uno está prohibido por el documento que manda y aun así es el prompt de concept.
- Piel y ojos. `personajes.md` cierra piel `#E2A56B`, ojos `#3F2A22`, boca `#C46A52`. `concept-art.md` usa piel `#C4845A` y ojos `#3A2418`. `direccion-artistica.md` usa piel `#C6866A`, ojos `#5A3A2E` y boca `#A15A52`. El relato dice que siempre son los mismos. No lo son.
- Broche. `personajes.md` lo cose en el cuello. `direccion-artistica.md` lo pone en el pecho. Pensar es tocarlo. Si no se sabe dónde está, la pose no se dibuja.
- Edad. `personajes.md` dice «unos once años en el dibujo». `direccion-artistica.md` dice que se lee como aprendiz joven, no como una niña de 6 y no como una reina, y que la edad es la misma en todos los dibujos, pero no da la cifra. El relato solo dice «chica joven». Para una niña de 6, once años es una hermana mayor. Para una de 10, es una igual. La boca no elige. Habla a las dos como a un parvulario.
- Caras. El relato y el GDD cierran tres: curiosa, contenta, pensando. `personajes.md` abre una cuarta, «celebrando», y en el mismo archivo dice que ante un fallo solo valen las tres. `concept-art.md` vuelve a tres y, además, cierra la boca de curiosa. `personajes.md` la deja entreabierta. El guion del primer día tiene que escribir «Contentísima no: contenta» para no hacer la cara que el propio texto estaba a punto de hacer. Si hay que prohibirla dentro de la escena, la escena no está cerrada.
- La aprendiz que no sabe es mentira a los veinte segundos. El relato dice que no sabe la cuenta antes y que no la esconde para poner nota. Dice «Yo también estoy aprendiendo.» En el mismo guion, antes de que la niña mueva nada, Estrella dice «Ocho y dos son diez.» En la llevada dice «Cinco y cinco son diez» y «Me llevo una.» En el euro dice el precio y la moneda. Sabe. Lo anuncia. La frase de aprendiz es un disfraz de maestra. Una niña de 6 lo nota. Una de 10 lo nota antes.
- Tono. «No habla como un bebé» y «no habla como una maestra severa». La boca hace las dos cosas. De bebé: «despacito» (D07), «abrazamos» (Círculo), «algo bonito», «estrellita» dicha al lado de su nombre. De maestra: «El diez es un grupo especial», «El cero cabe. Significa que las diez ya saltaron», «Esto se llama llevada», «Este truco tiene un nombre largo. Conmutativa. Significa esto», «No hay otro castillo para los mayores.» Esa última frase le explica a la niña una decisión de diseño. No juega nada. A los 9 años, con el diez todavía frágil, «especial», «bonito» y «fácil» hablan hacia abajo. Hablar hacia abajo humilla sin decir «mal».

Se sienta al lado. El guion de llegada la pone en la puerta, de pie, soltando ocho frases. `docs/specs/ui-ux.md` la deja en un busto de 96 px en el borde, para no tapar el nido. El relato escribe un paseo. El juego no se camina. Hay una pantalla, el Patio. Esa Estrella no cabe en esa pantalla.

## 2. Escenas que no tienen guion literal

Un guion literal, para esta edad y este aparato, es una secuencia: qué hay en la mesa, qué mano se mueve, qué frase se dice, qué pasa si suelta mal, y cómo acaba. Un banco no es una escena. Un «por ejemplo» no es una escena. «Luego la sesión de siempre» no es una escena.

### Primera sesión completa

Hay un capítulo que se llama guion. No es la partida que el GDD manda, y no está dibujado hasta el final.

El GDD, si nada se tuerce: ver tres piedras; Estrella cierra un diez; ella repite 7 y 3; borde 8, luego 5, luego 9; collar piedra-estrella; cierre de una que puede; farol a la torre. El objeto es un nido de dos filas de cinco. La décima enciende. La siguiente del collar se cuelga desde un arcón.

El relato escribe otra partida: cuenco, no nido; Estrella enseña 8 y 2 y ella repite 8 y 2; borde 7, 9, 6 y, si cabe, 5 y 5; acierto del collar si pone la estrella; cierre con cinta. `lore.md` copia la partida del GDD y, en el mismo archivo, deja «Ponla con cuidado. Ahí, en el cuenco.» `programacion.md` ya archivó el guion del relato en la columna «no se implementa». `voces.json` grabó el guion descartado: `cuenta.arrastra_cuenco`, `idea.ocho_y_dos`, `cierre.elige_cinta`.

El collar está mal enseñado. En la mesa hay piedra, estrella, piedra, estrella, y un hueco. El hueco es el quinto. La siguiente es una piedra. Lo dicen `lore.md` y `docs/specs/puzzles.md`. El relato, si acierta, dice «Has puesto la estrella en el hueco.» Si suelta la piedra, dice «El hueco pide estrella.» F08 repite el error. Una niña que obedece a Estrella aprende el patrón al revés. En un juego de números, eso no es un matiz de tono. Es una mentira.

Lo que el capítulo no dibuja, y sin ello no hay sesión:

- El patio de una sola pantalla. La llegada es un cuento de puerta, torre y sala. No hay plano de qué se toca.
- La oncena. El GDD la define. El relato no tiene frase ni silencio escrito.
- El arcón. El relato habla de «piezas sueltas». El juguete es un arcón con piedras y estrellas de más, no dos botones y no un montón sin nombre.
- El fallo del borde. «Por ejemplo con un dos» no es el gesto de 8, de 5 ni de 9. No se sabe qué piezas hay en la mesa en la partida que manda.
- La ayuda «hasta lograrlo». No tiene último paso. Puede comerse los siete minutos.
- Cerrar la tableta a medias, y menos de quince segundos sin tocar una pieza. El GDD lo cierra. El relato no lo pone en escena. `lore.md` dice que entonces no se saluda. En el relato ese silencio no está escrito, así que alguien saludará.
- La ficha escrita del diez. El relato la añade y admite que puede no ser la del diez. `programacion.md` prohíbe una ficha que pueda fallar la sesión. El GDD dice que escribir, si aparece, es la comprobación, después de la luz. No es otro ejercicio.
- El final. `voces.json` tiene seis fragmentos (`bienvenida_primer_dia`, `torre_primer_dia`, `entrar_piedras`, `cuenta_que_ya_sabe`, `idea_de_hoy_hacer_el_diez`, `cierre_primer_dia`, `cierre_adorno`) y ninguno encadena borde, acertijo y cierre. La «sesión completa» son trozos.

La llegada sola son ocho frases en unos treinta segundos, antes de una piedra. El relato pide una frase y luego silencio. El audio encadena con 0,6 s. Una niña de 6 no guarda ocho ideas. A los siete minutos de sesión, más de un minuto y medio se va en tesis.

### Primera llevada

No es una escena. Es una lección con números de muestra. No hay secuencia en `voces.json`.

El día dice que no se nombra «llevada» y, en el mismo documento, deja «Esto se llama llevada» entre comillas de voz. El lote, por la regla final del relato, la grabaría. El cuarto intento, quince más seis, mete una segunda idea: la decena que salta se junta con una que ya está. El propio relato pide una idea cada vez. El acertijo es un párrafo. El corte son dos frases. El cero se explica («Significa que las diez ya saltaron») en vez de verse en la columna vacía. No se dice qué varilla arrastra ella, con qué mano, ni qué queda en el pergamino si falla la segunda vez. No se puede animar.

Además no entra en el primer jugable. Escribirla ahora solo hincha el lote.

### Primer euro

Tampoco hay secuencia. Solo `mercado_monedas`, el aviso legal. El resto es prosa.

El mismo día dice «No se compra de verdad» y «Has pagado un euro». El lazo «ya se puede ir a la torre» como si se hubiera comprado. El aviso y el verbo se pisan. «Cuenta las monedas de euro, despacio» pide una cuenta que la boca no puede oír: no hay micrófono y no se pide hablar en alto. Hay dos acertijos «si un día se cambia». Los céntimos se dicen «si se dice». Un «si» no es un guion. El cierre repite el lazo de un euro que ya fue la idea. No hay subida ni gesto nuevo: hay lista.

### Vuelta al día siguiente

Tres entradas, y las tres se cortan en el saludo.

- Firme, en el relato y en `vuelta_dia_siguiente_firme`: «La cinta sigue en la torre.» «Hoy hay una luz nueva, pequeña.»
- Sin firme: «La cinta sigue ahí.» «Volvemos al diez.»
- Varios días, y el GDD: «Me alegro de verte.» «Tus luces siguen encendidas.» «No hay que recuperar nada.»

`lore.md` prohíbe reciclar la cinta el día después del farol. El audio la grabó igual. Después del saludo, el relato dice «luego la sesión de siempre». No dice qué nido, qué números, si el ejemplo está, ni qué adorno se ofrece. Si el diez no está firme, no se sabe qué cuenta es «una que ya sabe»: las tres piedras, el 7 y 3, u otra. Sin eso, el día siguiente se improvisa. Improvisar está prohibido.

### Corte por cansancio

Una frase, `corte`: «Seguimos con una que ya sabes.» Eso es lo que manda el GDD. No es una escena.

No se dice qué piezas se apartan, qué nido queda, ni cuál es la cuenta que ya sabe. El relato, para el corte de dos fallos, escribe otras dos frases: «El diez de hoy ya ha trabajado.» «Vamos a una que puedes hacer.» El audio dice que no se encadenan con el puente, y que siguen en el lote porque el relato las escribió. Tres bocas para un corte. Los signos que el GDD llama cansancio (devuelve piezas, pausas largas, fallos encadenados, se va) no tienen beat. D12 («Parar un momento está bien») puede sonar justo antes del puente, o no. No está decidido. El cierre después del corte es el mismo 5 y 5 «fácil» que el camino largo. Si acaba de fallar el borde, esa cuenta puede no ser una que ya sabe. El relato no lo distingue.

### Padre

Cero frases en el relato. El GDD dice que lee frases, no notas. `audio.md` dice que ahí no habla nadie. `ui-ux.md` pide «una o dos frases, del tipo ya cerrado». Ese tipo no está cerrado en el relato. `docs/expertos/03-pedagogia.md` redacta ejemplos («Hoy ha hecho dieces sola…», «Ha acertado despacio para ella…»). No son el listado del relato, no están en `voces.json` y no están marcados como literales del padre. Un hueco de frases, en una pantalla de adulto, se llena con una nota. La nota es lo que el GDD prohíbe. O se listan, o el primer jugable no las muestra. «Del tipo ya cerrado» no es una lista.

La salida a medias son tres frases y ningún plano. Cabe en el mismo hueco: no es una escena, es un cartel.

## 3. Prohibidas que se cuelan, y bancos que ya no son un listado

El GDD prohíbe «mal», «incorrecto», «eres un genio», «casi», «date prisa», «esto es fácil», cualquier comparación y cualquier etiqueta de emoción o de inteligencia. El relato añade «otra vez», «no tengas miedo», y limita «no pasa nada» a volver o no recordar.

Se cuelan igual, en frases que el audio ya grabó o que el relato manda decir:

- «Cerramos con una fácil.» Tres veces en el relato. Id `cierre.facil`. El audio necesita un párrafo para explicar que no es «esto es fácil». Si hace falta el párrafo, la frase ya está sucia. Si el cierre se le atasca, «fácil» la deja por debajo. Eso humilla.
- «Otra vez: piedra, estrella.» El relato prohíbe «otra vez» y lo escribe en la ayuda. Id `ayuda.otra_vez_ritmo`. «Los juntamos otra vez» repite el hueco.
- «Ya sabes hacer el diez.» Etiqueta a la persona. No es el puente del GDD, que habla de la cuenta («una que ya sabes»), no de ella.
- «Has pagado un euro con una moneda.» Tres ids. Choca con «No se compra de verdad» en la misma sesión.
- «Si sobra una pieza, se queda en la mesa, y no pasa nada.» Primera visita del Tesoro, y encima es literal que el audio no deja partir. «No pasa nada» queda fuera del único sitio donde el relato decía que cabía. D03 lo usa otra vez: «Si la sueltas ahí, no pasa nada.»
- «El diez no se va. Lo miramos despacito.» Diminutivo de bebé, contra la propia ficha de voz.
- Preguntas que la boca no puede responder: «¿Qué sigue en el hueco?», «¿Qué sigue?», «¿Qué moneda sigue?», «¿Pesan igual?», «¿Cuántas hay?», «¿Probamos con la de dos?», «¿Te acuerdas del dos con el ocho?». El relato dice que no hace preguntas que exijan voz, y luego escribe la pregunta y una nota de que se responde con la mano. La niña oye la pregunta. La nota no se oye.
- «Tus manos ya lo saben» y «Lo has visto» nombran un don. El relato lo autoriza. La regla de no elogiar a la persona no deja ese resquicio: «tus» sigue siendo ella.
- La lista de «frases que no se dicen nunca» está entre comillas angulares. La última regla del relato dice que eso es el listado de audio. Grabaría «Mal.», «Eres un genio.», «Date prisa.» El audio, con buen criterio, se niega. La regla de cierre del relato es falsa.

Los bancos de doce no son el listado. F01–F12, D01–D12 y A01–A12 son 36 frases. El relato permite cambiar el número, cambiar «piedra» y «estrella», y, si ninguna nombra la mesa de hoy, usar «la frase del guion». Eso es un generador. El generador ya se ejecutó: 395 frases, 100 solo de «idea de hoy», 67 de acierto, 57 de fallo. Una variante que no está en el JSON se enseña como texto del relato, que a su vez dice que se pueden cambiar los números. El listado no está cerrado. Está abierto por dos sitios a la vez.

En una Fire 7, por debajo de 40 MB y nunca por encima de 80, con la voz entera por debajo de 8 MB, 395 tomas no son un primer jugable. Son el archivo de todo lo que aún no se ha decidido no decir.

## 4. Donde explica la regla en vez de hacerla jugar

Una niña de 6 no necesita la metafísica. Necesita una piedra que entra en un hueco y una luz que sube. Cada vez que Estrella explica por qué el juego es bueno, la mesa está parada.

- La llegada. Ocho frases para decir que la niebla es suave, que la luz se queda, que se puede ir y que el castillo guarda. La niebla se ve. Explicar que es suave es la manera de sugerir que podría no serlo. «No se dice no tengas miedo» y se hace el mismo trabajo en tres frases.
- «No está castigada. Espera su momento.» Si la puerta no es un botón prohibido, no hace falta el discurso. El discurso inventa el castigo para negarlo.
- «Si entendemos una, se queda encendida.» «No hace falta hacerlo perfecto.» «Jugar ya cuenta.» Tesis. La torre ya está bien: eso sí se puede ver. El resto se demuestra no apagando nada, no diciéndolo.
- «La lámpara quiere ver las manos.» «Si la pieza no viaja, no se acuerda.» La regla del gesto, dicha. El juguete, si no enciende sin arrastre, ya la ha dicho.
- «Cuando el diez se cierra, las piedras brillan.» Anuncia el efecto. El efecto tenía que ocurrir en silencio, o con una frase después, nombrando lo que ella ha soltado.
- La llevada. «Diez unidades no se quedan aquí. Se hacen una decena.» Luego el significado del cero. Luego, otro día, el nombre. Tres capas de explicación para un salto que se ve.
- El préstamo. Cinco frases antes de romper una decena con la mano.
- «Estas monedas son del juego.» «No se compra de verdad.» Hace falta. No hace falta dentro del gesto. Es frase de padre, y el padre no tiene frases. Puesta en la mesa, convierte el juguete en un aviso.
- «No hay otro castillo para los mayores.» «Los números son más largos.» «El gesto es el mismo.» Le cuenta el techo de edad. No hay pieza.
- «La pregunta se responde arrastrando. Estrella no espera una palabra.» La nota admite que la pregunta es falsa.
- «Cómo se elige una frase», los estados, y «eso ha sido una duda» prohibido en voz pero explicado al equipo dentro del capítulo de boca. Eso no es relato. Es un manual metido en la boca para que nadie lo encuentre.

Lo único que juega la regla sin decirla es la torre ya completa, sin ganchos vacíos, y un adorno que se pone por haber llegado. El relato lo escribe y luego lo tapa con cinta, con «fácil» y con un discurso de bienvenida.

## 5. Qué sobra

Sobra todo lo que no es el primer día, escrito como si ya hubiera que grabarlo.

- «Aportes al documento único», al final del relato. Es una tercera copia, y ya se ha desviado: cinta, 8 y 2, borde 7-9-6. Un resumen que miente es peor que no tener resumen.
- `lore.md` como segunda biblia de frases. Corrige el farol y la piedra, y no llega a la boca. Dos verdades.
- Las presentaciones de Espejo, Círculo, Pergamino, Mercado, Jardín, Tesoro y Acertijos, más la segunda tanda dentro del guion de Piedras («Hoy entramos…» repite lo que la presentación ya dijo). Dos frases de visita no son una sala. Hasta que la sala tenga escena, sobran.
- Céntimos, préstamo, centenas, jardín, tesoro, problemas con historia, «conmutativa», «asociativa», tablas del 2, del 5 y del 10. Apuntes. No escenas. En el lote pesan igual que una frase que sí se dice el primer día.
- El catálogo de adornos: farolillo, maceta, estrella de papel, cojín, guirnalda, baldosa, campanilla. El primer día necesita un farol, dos colores, los dos válidos. El resto es una lista de compra.
- Los bancos de doce más las 359 frases sin banco. Si el guion nombrara cada número, no haría falta el banco. Si el banco bastara, no haría falta el guion. Están los dos, y la escena no está en ninguno.
- La lista de prohibidas dentro del documento cuya regla de oro es «se dice lo que va entre comillas angulares». Las prohibidas viven en una página de no hacer. No en la boca.
- «Unos siete minutos», «unos veinte segundos», «unos treinta segundos». Son del diseño. En el capítulo de boca ocupan el sitio del plano. Estrella no los dice, y el montador tampoco puede usarlos: ocho frases no caben en treinta segundos si de verdad hay silencio después de cada una.

No sobra la regla de una frase y silencio. Sobra incumplirla en la primera página que la niña oye.

## Decisiones que el documento único debe cerrar

1. El pelo es melena a la mandíbula, flequillo recto, sin trenza y sin coleta. No se usa el prompt de `concept-art.md` que pide trenza, ni el de `direccion-artistica.md` que acaba el pelo en la clavícula.
2. Piel, ojos y boca tienen un solo hex, el de `personajes.md`. No conviven `#E2A56B`, `#C4845A` y `#C6866A`.
3. La edad del dibujo es una: unos once años. No se la dibuja de 6 ni adulta. En la boca no están «despacito» ni «abrazamos».
4. Las caras son tres: curiosa, contenta, pensando. No existe «celebrando». La boca de curiosa es una, no abierta y cerrada a la vez.
5. El broche va en el cuello. No en el pecho.
6. El primer día el objeto es el nido de dos filas de cinco. Ninguna frase de ese día dice «cuenco».
7. La partida de referencia es la del GDD, con esos números y en ese orden. El guion de 8 y 2, y el borde 7, 9, 6, 5 y 5, no es esa partida. No hay una ficha escrita que ella pueda colocar mal.
8. En el collar del primer día la siguiente es una piedra, colgada desde el arcón. No se dice que el hueco pide estrella.
9. El adorno del primer día es un farol, a elegir entre dos, y lo coloca ella. No se dice «Elige una cinta» ni «La cinta sigue en la torre» al día siguiente de ese farol.
10. El acierto del cierre lo hace ella soltando la pieza. No se escribe que las piezas acompañan la mano ni que el acierto es de las dos.
11. El corte por dos fallos y el corte por cansancio dicen solo «Seguimos con una que ya sabes.» No se añade «ya ha trabajado» ni «una que puedes hacer».
12. No se dice «Cerramos con una fácil», «Ya sabes hacer el diez», «Has pagado», «Otra vez» ni una frase con «¿». «No pasa nada» no está en el Tesoro ni en un fallo.
13. «Yo también estoy aprendiendo» no se dice en una escena en la que ella anuncia el resultado antes del gesto.
14. La bienvenida del primer día no define la niebla en tres frases. No se dice miedo, monstruo, oscuridad ni peligro.
15. El primer jugable tiene cuatro finales escritos, cada paso con pieza, sitio y mano: partida de referencia, corte a los dos fallos, corte por cansancio y salida a medias. Si no se toca una pieza en quince segundos, no hay saludo.
16. La vuelta al día siguiente tiene una sola entrada, la del GDD, y sigue con la cuenta que ya sabe, números escritos. No existe «la sesión de siempre».
17. El rincón del padre, en el primer jugable, o no muestra frases o las lista todas, literales, sin nota y sin Estrella. «Del tipo ya cerrado» no cuenta. Ninguna frase nombra padre, PIN ni aparato en la boca de ella.
18. El lote de voz del primer jugable es solo esas escenas. No entran llevada, euro, céntimos, préstamo, centenas, jardín, tesoro, nombres largos ni el catálogo de adornos. Las frases que no se dicen no van entre comillas de voz. 395 no es ese lote.
19. La oncena, la primera vez del intento, no tiene frase. Silencio, y cara curiosa.
