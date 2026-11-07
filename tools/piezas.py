#!/usr/bin/env python3
"""Dibuja las piezas del primer jugable con las reglas de docs/specs/direccion-artistica.md.

Salida en assets/piezas/ y assets/fondos/. Todas con transparencia salvo los fondos.
Se dibuja a 4x y se reduce, para que la línea quede limpia en la tableta.
"""
import math
import os
from PIL import Image, ImageDraw

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PIEZAS = os.path.join(RAIZ, "assets", "piezas")
FONDOS = os.path.join(RAIZ, "assets", "fondos")

CONTORNO = (51, 22, 13)
CREMA = (245, 237, 226)
PIEDRA = (242, 226, 160)
PIEDRA_SOMBRA = (216, 193, 115)
NIDO = (196, 146, 92)
NIDO_SOMBRA = (170, 120, 70)
TELA = (244, 194, 84)
TELA_SOMBRA = (216, 160, 60)
COSTURA = (196, 92, 40)
CAPA = (191, 80, 47)
SUELO = (61, 79, 138)
SUELO_CLARO = (78, 98, 158)
AMBAR = (244, 197, 109)
TERRACOTA = (191, 80, 47)
S = 4  # supermuestreo


def lienzo(w, h):
    im = Image.new("RGBA", (w * S, h * S), (0, 0, 0, 0))
    return im, ImageDraw.Draw(im)


def guardar(im, w, h, nombre, carpeta=PIEZAS):
    os.makedirs(carpeta, exist_ok=True)
    im.resize((w, h), Image.LANCZOS).save(os.path.join(carpeta, nombre))
    print("  ", nombre, w, "x", h)


def forma_piedra(cx, cy, r, n=13):
    puntos = []
    for i in range(n):
        a = 2 * math.pi * i / n
        k = 1.0 + 0.10 * math.sin(3 * a + 0.7) + 0.05 * math.cos(5 * a + 1.9)
        puntos.append((cx + math.cos(a) * r * k, cy + math.sin(a) * r * k))
    return puntos


def dibuja_piedra(d, cx, cy, r, linea=3):
    pts = forma_piedra(cx, cy, r)
    d.polygon(pts, fill=PIEDRA)
    faceta = []
    for i, (x, y) in enumerate(pts):
        if y > cy + r * 0.05:
            faceta.append((cx + (x - cx) * 0.62, cy + (y - cy) * 0.62))
    if len(faceta) > 2:
        d.polygon(faceta, fill=PIEDRA_SOMBRA)
    d.line(pts + [pts[0]], fill=CONTORNO, width=linea * S, joint="curve")


def piedra(tam):
    im, d = lienzo(tam, tam)
    dibuja_piedra(d, tam * S / 2, tam * S / 2, tam * S * 0.44, linea=3)
    guardar(im, tam, tam, "piedra-%d.png" % tam)


def nido():
    w, h = 500, 220
    im, d = lienzo(w, h)
    d.rounded_rectangle([0, 0, w * S - 1, h * S - 1], radius=48 * S, fill=NIDO, outline=CONTORNO, width=6 * S)
    d.rounded_rectangle([10 * S, 10 * S, (w - 10) * S - 1, (h - 10) * S - 1], radius=40 * S,
                        outline=NIDO_SOMBRA, width=6 * S)
    for r in range(2):
        for c in range(5):
            hx, hy = (20 + c * 92) * S, (20 + r * 92) * S
            d.rounded_rectangle([hx, hy, hx + 80 * S, hy + 80 * S], radius=22 * S,
                                fill=CREMA, outline=CONTORNO, width=4 * S)
    guardar(im, w, h, "nido.png")


def estrella_tela(tam=64):
    im, d = lienzo(tam, tam)
    cx = cy = tam * S / 2
    r = tam * S * 0.46
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.46
        pts.append((cx + math.cos(a) * rr, cy + math.sin(a) * rr))
    d.polygon(pts, fill=TELA)
    d.line(pts + [pts[0]], fill=CONTORNO, width=3 * S, joint="curve")
    # puntadas: trazos cortos por dentro del borde
    n = len(pts)
    for i in range(n):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % n]
        t0, t1 = 0.25, 0.6
        d.line([(x1 + (x2 - x1) * t0 + (cx - x1) * 0.16, y1 + (y2 - y1) * t0 + (cy - y1) * 0.16),
                (x1 + (x2 - x1) * t1 + (cx - x1) * 0.16, y1 + (y2 - y1) * t1 + (cy - y1) * 0.16)],
               fill=COSTURA, width=max(1, S))
    guardar(im, tam, tam, "estrella-tela.png")


def campana():
    tam = 96
    im, d = lienzo(tam, tam)
    cx = tam * S / 2
    # cuerpo: arco con falda plana
    d.pieslice([cx - 34 * S, 14 * S, cx + 34 * S, 82 * S], 180, 360, fill=PIEDRA, outline=CONTORNO, width=4 * S)
    d.rectangle([cx - 34 * S, 48 * S, cx + 34 * S, 74 * S], fill=PIEDRA)
    d.line([(cx - 34 * S, 74 * S), (cx + 34 * S, 74 * S)], fill=CONTORNO, width=4 * S)
    d.line([(cx - 34 * S, 48 * S), (cx - 34 * S, 74 * S)], fill=CONTORNO, width=4 * S)
    d.line([(cx + 34 * S, 48 * S), (cx + 34 * S, 74 * S)], fill=CONTORNO, width=4 * S)
    d.ellipse([cx - 7 * S, 74 * S, cx + 7 * S, 88 * S], fill=PIEDRA_SOMBRA, outline=CONTORNO, width=3 * S)
    d.ellipse([cx - 6 * S, 8 * S, cx + 6 * S, 20 * S], fill=PIEDRA_SOMBRA, outline=CONTORNO, width=3 * S)
    guardar(im, tam, tam, "campana.png")


def farol(color, nombre):
    w, h = 160, 160
    im, d = lienzo(w, h)
    # asa
    d.arc([56 * S, 8 * S, 104 * S, 56 * S], 180, 360, fill=CONTORNO, width=5 * S)
    # cuerpo
    d.rounded_rectangle([36 * S, 40 * S, 124 * S, 128 * S], radius=14 * S, fill=color, outline=CONTORNO, width=5 * S)
    # cristal
    d.rounded_rectangle([54 * S, 58 * S, 106 * S, 110 * S], radius=8 * S, fill=CREMA, outline=CONTORNO, width=4 * S)
    # llama: una gota, sin brillos
    d.polygon([(80 * S, 68 * S), (94 * S, 92 * S), (80 * S, 104 * S), (66 * S, 92 * S)],
              fill=AMBAR, outline=COSTURA)
    d.line([(80 * S, 68 * S), (94 * S, 92 * S), (80 * S, 104 * S), (66 * S, 92 * S), (80 * S, 68 * S)],
           fill=CONTORNO, width=3 * S, joint="curve")
    # base
    d.rectangle([30 * S, 128 * S, 130 * S, 142 * S], fill=color, outline=CONTORNO, width=5 * S)
    guardar(im, w, h, nombre)


def fondo_piedras():
    os.makedirs(FONDOS, exist_ok=True)
    w, h = 1024, 600
    im = Image.new("RGB", (w, h), CREMA)
    d = ImageDraw.Draw(im)
    d.rectangle([0, 430, w, h], fill=SUELO)
    d.rectangle([0, 430, w, 438], fill=SUELO_CLARO)
    im.save(os.path.join(FONDOS, "piedras.png"))
    print("   piedras.png 1024 x 600")


def main():
    print("piezas")
    for t in (96, 72, 68):
        piedra(t)
    nido()
    estrella_tela()
    campana()
    farol(AMBAR, "farol-ambar.png")
    farol(TERRACOTA, "farol-terracota.png")
    print("fondos")
    fondo_piedras()


if __name__ == "__main__":
    main()
