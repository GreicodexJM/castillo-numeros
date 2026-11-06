# Plan — Estrella y el Castillo de los Números

Juego de matemáticas para una Amazon Fire 7 (2022), modelo KFQUWI. Godot 4.7.2, solo 2D, sin internet. El diseño completo es `GDD.md` más los cinco capítulos de `docs/expertos/`. Este plan dice en qué orden se construye.

## Qué queda cerrado

- Una niña de 6 a 7 años que se frustra, con techo hasta 10 en el mismo castillo. Sin datos de una niña real.
- El castillo solo gana luz. No hay vidas, reloj en pantalla, marcador, estrellas vacías ni sonido de error.
- Cada sesión que ella termina acaba en un acierto hecho con sus manos.
- Un paso nuevo solo si el anterior está firme: sola, en otro día, sin duda.
- Primer jugable: hacer el 10, un acertijo de patrón y la torre. No la llevada.
- Métricas locales. La tableta no diagnostica ni sabe si ella está sentada o acostada.

## Fases

1. **Diseño.** Hecho en los capítulos de expertos y en el documento único. Los especialistas escriben specs y assets de cada área.
2. **Primer jugable, en el ordenador.** Escena de Piedras de luz (hacer el 10), un patrón piedra-estrella, cierre en acierto, torre con un adorno, registro de duda al soltar y corte a los dos fallos. Sustitutos de color si falta el dibujo.
3. **Prueba en la Fire.** Export arm64, Compatibility, sin permiso de red, pantalla completa. Antes hay que liberar espacio: el disco estaba al 91 %. No instalar con la batería baja.
4. **Resto de salas**, solo cuando el cimiento anterior esté especificado y el anterior jugable se sienta bien en el dedo: hasta 20, espejo, pergamino sin llevada, llevada, préstamo, centenas, mercado, jardín, círculo, tesoro, techo.
5. **Voz.** Listado cerrado, generado en el PC. Si falta un audio, se lee el texto.

## Qué no entra en el primer jugable

Llevada, préstamo, euros, centenas, signos × y ÷, problemas de historia, vídeo, 3D en la tableta, red, cuentas, anuncios.

## Dónde está cada cosa

| Pieza | Archivo |
|---|---|
| Restricciones | `BRIEF.md` |
| Documento único | `docs/GDD.md` |
| Juego | `docs/expertos/01-videojuegos.md` |
| Relato | `docs/expertos/02-relato.md` |
| Pedagogía | `docs/expertos/03-pedagogia.md` |
| Matemáticas, 81 micropasos | `docs/expertos/04-matematicas.md` |
| Edutenimiento | `docs/expertos/05-edutenimiento.md` |
| Encargos de especialistas | `agentes/10-` a `agentes/18-` |
