#!/usr/bin/env python3
"""Dibuja las placas de las pantallas del primer jugable a 1024x600.

Las coordenadas salen del apartado 5 del documento de diseno (docs/GDD.md).
Las piezas se pegan desde assets/piezas/, que son las definitivas.
Cada placa sale dos veces: limpia y con las zonas marcadas.
"""
import os
from PIL import Image, ImageDraw, ImageFont

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PIEZAS = os.path.join(RAIZ, "assets", "piezas")
FONDOS = os.path.join(RAIZ, "assets", "fondos")
SALIDA = os.path.join(RAIZ, "assets", "pantallas")
PERSONAJE = os.path.join(RAIZ, "assets", "personajes", "estrella-cara.png")

W, H = 1024, 600

CREMA = (245, 237, 226)
CONTORNO = (51, 22, 13)
TINTA = (44, 36, 22)
TELA = (241, 213, 171)
AMBAR = (244, 197, 109)
TERRACOTA = (191, 80, 47)
NOCHE = (30, 42, 74)
NOCHE_SUELO = (40, 54, 92)
PIEDRA_SUELO = (61, 79, 138)
PIEDRA_PARED = (245, 237, 226)
ACERTIJOS = (142, 124, 195)
TORRE_PARED = (243, 230, 200)
COSTURA = (196, 92, 40)
VERDE = (0, 130, 70)
AZUL = (0, 90, 200)
ROSA = (200, 0, 120)


def fuente(px, negrita=True):
    rutas = [
        "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf" if negrita else "/usr/share/fonts/TTF/DejaVuSans.ttf",
        "/usr/share/fonts/noto/NotoSans-Bold.ttf" if negrita else "/usr/share/fonts/noto/NotoSans-Regular.ttf",
    ]
    import os
    for ruta in rutas:
        if os.path.exists(ruta):
            return ImageFont.truetype(ruta, px)
    return ImageFont.load_default()

def pieza(nombre):
    return Image.open(os.path.join(PIEZAS, nombre)).convert("RGBA")


def pega(im, nombre, caja, ajuste="caber"):
    """Pega una pieza dentro de una caja x,y,w,h sin deformarla."""
    x, y, w, h = caja
    p = pieza(nombre)
    if ajuste == "caber":
        k = min(w / p.width, h / p.height)
    elif ajuste == "ancho":
        k = w / p.width
    else:
        k = 1.0
    p = p.resize((max(1, int(p.width * k)), max(1, int(p.height * k))), Image.LANCZOS)
    im.paste(p, (x + (w - p.width) // 2, y + (h - p.height) // 2), p)


def recorta_fondo(im, tolerancia=42):
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


def estrella(im, caja):
    x, y, w, h = caja
    cara = Image.open(PERSONAJE).convert("RGB")
    cw, ch = cara.size
    r = cara.crop((int(cw * 0.06), 0, int(cw * 0.94), int(cw * 0.88 * h / w)))
    r = recorta_fondo(r.resize((w, h), Image.LANCZOS))
    im.paste(r, (x, y), r)


def ventana(d, caja, relleno):
    """Ventana de castillo: arco arriba y lados rectos. Se reconoce sin texto."""
    x, y, w, h = caja
    d.pieslice([x, y, x + w - 1, y + w - 1], 180, 360, fill=relleno)
    d.rectangle([x, y + w // 2, x + w - 1, y + h - 1], fill=relleno)
    d.arc([x, y, x + w - 1, y + w - 1], 180, 360, fill=CONTORNO, width=5)
    d.line([(x, y + w // 2), (x, y + h - 1)], fill=CONTORNO, width=5)
    d.line([(x + w - 1, y + w // 2), (x + w - 1, y + h - 1)], fill=CONTORNO, width=5)
    d.line([(x, y + h - 1), (x + w - 1, y + h - 1)], fill=CONTORNO, width=5)
    # segundo trazo por dentro
    d.arc([x + 7, y + 7, x + w - 8, y + w - 8], 180, 360, fill=CONTORNO, width=2)
    d.line([(x + 7, y + w // 2), (x + 7, y + h - 8)], fill=CONTORNO, width=2)
    d.line([(x + w - 8, y + w // 2), (x + w - 8, y + h - 8)], fill=CONTORNO, width=2)


def banda(d, caja, texto, tam=32):
    x, y, w, h = caja
    d.rounded_rectangle([x, y, x + w - 1, y + h - 1], radius=14, fill=CREMA,
                        outline=CONTORNO, width=3)
    if texto:
        d.text((x + 20, y + (h - tam) // 2 - 4), texto, font=fuente(tam), fill=TINTA)


def zonas(im, lista, util=True):
    d = ImageDraw.Draw(im)
    f = fuente(18)
    for etiqueta, caja, color in lista:
        x, y, w, h = caja
        d.rectangle([x, y, x + w - 1, y + h - 1], outline=color, width=2)
        d.rectangle([x + 2, y + 2, x + 24, y + 24], fill=color)
        d.text((x + 8, y + 3), etiqueta, font=f, fill=(255, 255, 255))
    if util:
        d.rectangle([48, 24, 976, 552], outline=ROSA, width=2)
        d.text((56, 528), "area util x 48-976, y 24-552", font=fuente(14), fill=ROSA)
    return im


def guarda(nombre, im, lista=None):
    os.makedirs(SALIDA, exist_ok=True)
    im.save(os.path.join(SALIDA, nombre + ".png"))
    print("  ", nombre + ".png")
    if lista is not None:
        zonas(im.copy(), lista).save(os.path.join(SALIDA, nombre + "-zonas.png"))
        print("  ", nombre + "-zonas.png")


# ---------------------------------------------------------------- patio

def patio():
    im = Image.new("RGB", (W, H), NOCHE)
    d = ImageDraw.Draw(im)
    d.rectangle([0, 470, W, H], fill=NOCHE_SUELO)
    d.rectangle([0, 470, W, 476], fill=(54, 70, 112))

    cajas = [(160, 180, 160, 160), (432, 180, 160, 160), (704, 180, 160, 160)]
    for caja, relleno in zip(cajas, (PIEDRA_SUELO, ACERTIJOS, TORRE_PARED)):
        ventana(d, caja, relleno)

    # Lo que se ve dentro de cada ventana: el nido, el patron del collar, el farol.
    pega(im, "nido.png", (172, 218, 136, 90))
    d = ImageDraw.Draw(im)
    d.line([(448, 300), (578, 300)], fill=CONTORNO, width=6)
    mini = ["piedra-72.png", "estrella-tela.png", "piedra-72.png", "estrella-tela.png"]
    for i, cual in enumerate(mini):
        x = 448 + i * 32
        pega(im, cual, (x, 252, 30, 30))
    pega(im, "farol-ambar.png", (732, 236, 104, 104))
    pega(im, "campana.png", (880, 24, 96, 96))

    lista = [
        ("1", cajas[0], AZUL),
        ("2", cajas[1], AZUL),
        ("3", cajas[2], AZUL),
        ("4", (880, 24, 96, 96), VERDE),
    ]
    guarda("patio-1024x600", im, lista)


# ---------------------------------------------------------------- collar

def collar():
    im = Image.new("RGB", (W, H), CREMA)
    d = ImageDraw.Draw(im)
    d.rectangle([0, 430, W, H], fill=ACERTIJOS)
    d.rectangle([0, 430, W, 438], fill=(160, 142, 208))

    # Cordon: 96, 220, 640, 96. Es una cinta; las piezas cuelgan por delante.
    d.rounded_rectangle([96, 264, 736, 300], radius=18, fill=TELA, outline=CONTORNO, width=4)
    for i in range(6):
        d.line([(126 + i * 106, 282), (158 + i * 106, 282)], fill=COSTURA, width=3)

    # Ganchos: i = 0..4 en x = 120 + i*120, y = 228, 80x80.
    # Un aro pequeno arriba y la pieza colgada debajo. No hay cajas de boton.
    patron = ["piedra-72.png", "estrella-tela.png", "piedra-72.png", "estrella-tela.png", None]
    for i, cual in enumerate(patron):
        x = 120 + i * 120
        d.ellipse([x + 32, 230, x + 48, 246], fill=TELA, outline=CONTORNO, width=3)
        if cual:
            pega(im, cual, (x + 12, 250, 56, 56))
        else:
            d.line([(x + 40, 246), (x + 40, 258)], fill=CONTORNO, width=3)

    # Arcon: 800, 180, 160, 220. Cerrado. La siguiente pieza sale de su boca.
    d.rounded_rectangle([800, 180, 959, 399], radius=16, fill=(196, 146, 92), outline=CONTORNO, width=5)
    d.line([(800, 250), (959, 250)], fill=CONTORNO, width=4)
    d.rounded_rectangle([866, 244, 894, 274], radius=6, fill=AMBAR, outline=CONTORNO, width=3)
    d.line([(884, 274), (884, 300)], fill=COSTURA, width=3)
    pega(im, "piedra-72.png", (860, 300, 48, 48))

    lista = [
        ("1", (96, 220, 640, 96), VERDE),
        ("2", (120, 228, 80, 80), AZUL),
        ("3", (800, 180, 160, 220), AZUL),
    ]
    guarda("collar-1024x600", im, lista)


# ---------------------------------------------------------------- torre

def torre():
    im = Image.new("RGB", (W, H), TORRE_PARED)
    d = ImageDraw.Draw(im)
    d.rectangle([0, 470, W, H], fill=(214, 190, 150))
    d.rectangle([0, 470, W, 476], fill=(196, 170, 128))
    # Pared completa y lisa: nada de ganchos vacios, nada de siluetas, nada de textura.
    # Solo la mancha plana bajo lo que se apoya.
    d.ellipse([724, 330, 844, 348], fill=(196, 170, 128))
    pega(im, "farol-ambar.png", (704, 180, 160, 160))

    lista = [
        ("1", (704, 180, 160, 160), AZUL),
    ]
    guarda("torre-1024x600", im, lista)


# ---------------------------------------------------------------- padre

def padre():
    im = Image.new("RGB", (W, H), CREMA)
    d = ImageDraw.Draw(im)
    d.rectangle([0, 470, W, H], fill=(232, 220, 200))
    d.rectangle([0, 470, W, 476], fill=(214, 200, 178))

    texto = "Esto no es una nota."
    f = fuente(34)
    ancho = d.textlength(texto, font=f)
    d.text(((W - ancho) / 2, 48), texto, font=f, fill=TINTA)

    # Cuatro casillas del PIN
    for i in range(4):
        x = 376 + i * 76
        d.rounded_rectangle([x, 108, x + 60, 176], radius=10, fill=(255, 255, 255), outline=CONTORNO, width=3)

    # Teclado: 3 columnas x 4 filas de 76, aire 12. Cabe entero en el area util.
    teclas = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "C", "0", "<"]
    for i, t in enumerate(teclas):
        c, r = i % 3, i // 3
        x = 386 + c * 88
        y = 200 + r * 88
        d.rounded_rectangle([x, y, x + 76, y + 76], radius=18, fill=(255, 255, 255), outline=CONTORNO, width=3)
        ft = fuente(38)
        ancho = d.textlength(t, font=ft)
        d.text((x + (76 - ancho) / 2, y + 16), t, font=ft, fill=TINTA)

    lista = [
        ("1", (376, 108, 292, 68), AZUL),
        ("2", (386, 200, 252, 340), AZUL),
    ]
    guarda("padre-1024x600", im, lista)


# ---------------------------------------------------------------- cierre

def cierre():
    im = Image.new("RGB", (W, H), PIEDRA_PARED)
    d = ImageDraw.Draw(im)
    d.rectangle([0, 430, W, H], fill=PIEDRA_SUELO)
    d.rectangle([0, 430, W, 438], fill=(78, 98, 158))

    pega(im, "nido.png", (80, 108, 500, 220))
    # Nueve puestas, una hueca: la que pone ella.
    d = ImageDraw.Draw(im)
    puestas = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1), (1, 1), (2, 1), (3, 1)]
    for (c, r) in puestas:
        cx, cy = 100 + c * 92 + 40, 128 + r * 92 + 40
        pega(im, "piedra-68.png", (cx - 34, cy - 34, 68, 68))
    # El hueco que falta no se marca: ningun hueco se preilumina.

    pega(im, "piedra-72.png", (700, 300, 72, 72))
    estrella(im, (848, 280, 112, 150))
    banda(d, (96, 468, 832, 56), "Pon la que falta.")

    lista = [
        ("1", (80, 108, 500, 220), AZUL),
        ("2", (100 + 4 * 92, 220, 80, 80), VERDE),
        ("3", (700, 300, 72, 72), AZUL),
        ("4", (848, 280, 112, 150), AZUL),
        ("5", (96, 468, 832, 56), VERDE),
    ]
    guarda("cierre-1024x600", im, lista)


# ---------------------------------------------------------------- farol

def farol_eleccion():
    im = Image.new("RGB", (W, H), TORRE_PARED)
    d = ImageDraw.Draw(im)
    d.rectangle([0, 470, W, H], fill=(214, 190, 150))
    d.rectangle([0, 470, W, 476], fill=(196, 170, 128))
    pega(im, "farol-ambar.png", (336, 200, 160, 160))
    pega(im, "farol-terracota.png", (528, 200, 160, 160))
    banda(d, (96, 468, 832, 56), "Elige uno de los dos.")

    lista = [
        ("1", (336, 200, 160, 160), AZUL),
        ("2", (528, 200, 160, 160), AZUL),
        ("3", (96, 468, 832, 56), VERDE),
    ]
    guarda("farol-1024x600", im, lista)


def main():
    print("placas")
    patio()
    collar()
    torre()
    padre()
    cierre()
    farol_eleccion()


if __name__ == "__main__":
    main()
