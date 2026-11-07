#!/usr/bin/env python3
"""Dibuja la pantalla del nido a 1024x600 con las zonas exactas del documento de diseño.

No inventa coordenadas: todas salen del apartado 5.2 de docs/GDD.md.
Genera dos archivos:
  assets/pantallas/nido-1024x600.png        arte limpio
  assets/pantallas/nido-zonas-1024x600.png  con las zonas marcadas para programar
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 600
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "pantallas")

# Colores medidos sobre assets/personajes/estrella-cara.png
CREMA = (245, 237, 225)
CONTORNO = (58, 36, 28)
PIEDRA = (242, 226, 160)
PIEDRA_SOMBRA = (216, 193, 115)
NIDO = (196, 146, 92)
NIDO_SOMBRA = (170, 120, 70)
SUELO = (61, 79, 138)
SUELO_CLARO = (78, 98, 158)
TINTA = (44, 36, 22)
AMBAR = (244, 197, 109)
TELA = (232, 214, 186)


def fuente(px):
    for ruta in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ):
        if os.path.exists(ruta):
            return ImageFont.truetype(ruta, px)
    return ImageFont.load_default()


def piedra(d, cx, cy, r, relleno=PIEDRA, borde=4):
    """Un canto rodado irregular, no un círculo ni un cuadrado. La misma forma siempre."""
    import math
    puntos = []
    n = 13
    for i in range(n):
        a = 2 * math.pi * i / n
        k = 1.0 + 0.10 * math.sin(3 * a + 0.7) + 0.05 * math.cos(5 * a + 1.9)
        puntos.append((cx + math.cos(a) * r * k, cy + math.sin(a) * r * k))
    d.polygon(puntos, fill=relleno)
    if borde:
        d.line(puntos + [puntos[0]], fill=CONTORNO, width=borde, joint="curve")
    # faceta de abajo, un solo tono más oscuro, dentro del contorno
    faceta = []
    for i in range(n):
        a = 2 * math.pi * i / n
        k = (1.0 + 0.10 * math.sin(3 * a + 0.7) + 0.05 * math.cos(5 * a + 1.9)) * 0.62
        if math.sin(a) > 0.05:
            faceta.append((cx + math.cos(a) * r * k, cy + math.sin(a) * r * k))
    if len(faceta) > 2:
        d.polygon(faceta, fill=PIEDRA_SOMBRA)


def recorta_fondo(im, tolerancia=42):
    """Quita el fondo liso de la ficha sin tocar los blancos de dentro de la cara."""
    im = im.convert("RGB")
    marca = (255, 0, 255)
    for esquina in ((0, 0), (im.width - 1, 0), (0, im.height - 1), (im.width - 1, im.height - 1)):
        ImageDraw.floodfill(im, esquina, marca, thresh=tolerancia)
    rgba = im.convert("RGBA")
    px = rgba.load()
    for y in range(rgba.height):
        for x in range(rgba.width):
            if px[x, y][:3] == marca:
                px[x, y] = (0, 0, 0, 0)
    return rgba


def rect_zona(d, caja, color=(255, 0, 0), ancho=2):
    x, y, w, h = caja
    d.rectangle([x, y, x + w - 1, y + h - 1], outline=color, width=ancho)


def dibuja_arte(marcar=False):
    im = Image.new("RGB", (W, H), CREMA)
    d = ImageDraw.Draw(im)

    # Pared y suelo. El suelo empieza a la altura de los pies de Estrella.
    d.rectangle([0, 430, W, H], fill=SUELO)
    d.rectangle([0, 430, W, 438], fill=SUELO_CLARO)

    # Paño del ejemplo (80, 24, 200, 72). No se toca.
    x, y, w, h = 80, 24, 200, 72
    d.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=TELA, outline=CONTORNO, width=3)
    d.text((x + 12, y + 8), "7 + 3", font=fuente(26), fill=TINTA)
    for i in range(7):
        piedra(d, x + 86 + (i % 4) * 17, y + 26 + (i // 4) * 17, 8, borde=2)
    for i in range(3):
        piedra(d, x + 86 + i * 17, y + 60, 8, borde=2)

    # Marco del nido (80, 108, 500, 220)
    mx, my, mw, mh = 80, 108, 500, 220
    d.rounded_rectangle([mx, my, mx + mw, my + mh], radius=48, fill=NIDO, outline=CONTORNO, width=6)
    d.rounded_rectangle([mx + 10, my + 10, mx + mw - 10, my + mh - 10], radius=40,
                        outline=NIDO_SOMBRA, width=6)

    # Diez huecos: x = 100 + c*92, y = 128 + r*92, 80x80. Dos filas de cinco.
    for r in range(2):
        for c in range(5):
            hx = 100 + c * 92
            hy = 128 + r * 92
            d.rounded_rectangle([hx, hy, hx + 79, hy + 79], radius=22, fill=CREMA, outline=CONTORNO, width=4)
    # Siete puestas, tres huecas: es el turno del 7 y 3.
    puestas = [(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (1, 1), (2, 1)]
    for (c, r) in puestas:
        piedra(d, 100 + c * 92 + 40, 128 + r * 92 + 40, 34)

    # Celda del montón: x = 640 + c*96, y = 120 + r*96, 96x96, seis piedras de 72.
    for c in range(2):
        for r in range(3):
            cx = 640 + c * 96 + 48
            cy = 120 + r * 96 + 48
            piedra(d, cx, cy, 36)

    # Estrella: 848, 280, 112, 150. Se recorta el fondo de la ficha para que esté de pie en el suelo.
    cara = Image.open(os.path.join(os.path.dirname(OUT), "personajes", "estrella-cara.png")).convert("RGB")
    cw, ch = cara.size
    recorte = cara.crop((int(cw * 0.06), 0, int(cw * 0.94), int(cw * 0.88 * 150 / 112)))
    recorte = recorta_fondo(recorte.resize((112, 150), Image.LANCZOS))
    im.paste(recorte, (848, 280), recorte)

    # Banda de frase: 96, 468, 832, 56
    fx, fy, fw, fh = 96, 468, 832, 56
    d.rounded_rectangle([fx, fy, fx + fw, fy + fh], radius=14, fill=CREMA, outline=CONTORNO, width=3)
    d.text((fx + 20, fy + 12), "Pon las que faltan.", font=fuente(32), fill=TINTA)

    # Pulso ámbar del acierto, en el borde del nido de ella: 1,2 s y se va.
    d.ellipse([mx + mw - 26, my + mh // 2 - 18, mx + mw + 10, my + mh // 2 + 18],
              outline=AMBAR, width=6)

    if marcar:
        azul = (0, 90, 200)
        verde = (0, 130, 70)
        rosa = (200, 0, 120)
        f = fuente(18)
        zonas = [
            ("1", (80, 24, 200, 72), azul),
            ("2", (mx, my, mw, mh), azul),
            ("3", (640, 120, 192, 288), azul),
            ("4", (848, 280, 112, 150), azul),
            ("5", (fx, fy, fw, fh), verde),
            ("6", (100, 128, 80, 80), verde),
        ]
        for etiqueta, caja, color in zonas:
            rect_zona(d, caja, color, 2)
            tx, ty = caja[0] + 2, caja[1] + 2
            d.rectangle([tx, ty, tx + 22, ty + 22], fill=color)
            d.text((tx + 6, ty + 1), etiqueta, font=f, fill=(255, 255, 255))
        d.rectangle([48, 24, 976, 552], outline=rosa, width=2)
        d.rectangle([44, 24, 52, 552], fill=rosa)
        d.rectangle([972, 24, 980, 552], fill=rosa)
        d.text((56, 528), "area util x 48-976, y 24-552", font=fuente(14), fill=rosa)

    return im


def main():
    os.makedirs(OUT, exist_ok=True)
    dibuja_arte(False).save(os.path.join(OUT, "nido-1024x600.png"))
    dibuja_arte(True).save(os.path.join(OUT, "nido-zonas-1024x600.png"))
    print("ok")


if __name__ == "__main__":
    main()
