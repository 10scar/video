from pathlib import Path

from manim import *

config.video_dir = str(Path(__file__).resolve().parent / "escenas")

PAPER = "#F4F0E6"
INK = "#1C1915"
AGENT = "#C9842A"
QUIET = "#8A8175"
WALL = "#2A2824"
PLUS = "#1F7A4D"
MINUS = "#9C2F2F"


def fondo(escena):
    escena.camera.background_color = PAPER


def presentar(escena, seccion, titulo, inicio=False, segundos_seccion=2.3, segundos_titulo=0.8):
    fondo(escena)
    if inicio:
        cartel = Text(seccion, font="Liberation Serif", font_size=48, color=INK)
        if cartel.width > 12:
            cartel.scale_to_fit_width(12)
        entrada, salida = 0.45, 0.40
        espera = max(0.2, segundos_seccion - entrada - salida)
        escena.play(FadeIn(cartel), run_time=entrada)
        escena.wait(espera)
        escena.play(FadeOut(cartel), run_time=salida)
    encabezado = Text(titulo, font="Liberation Sans", font_size=28, weight=BOLD, color=INK)
    encabezado.to_corner(UL, buff=0.35)
    encabezado.set_z_index(20)
    letras = [m for m in encabezado if isinstance(m, VMobject)]
    if not letras:
        letras = [encabezado]
    escena.play(
        LaggedStart(
            *[FadeIn(letra, shift=RIGHT * 0.15) for letra in letras],
            lag_ratio=0.06,
        ),
        run_time=segundos_titulo,
    )
    escena.encabezado = encabezado


def limpiar(escena, run_time=0.3):
    restos = [m for m in list(escena.mobjects) if m is not getattr(escena, "encabezado", None)]
    if restos:
        escena.play(*[FadeOut(m) for m in restos], run_time=run_time)


def estado(punto):
    return Circle(radius=0.36, color=INK, stroke_width=2.5).move_to(punto)


def casilla(x, y):
    return Square(side_length=0.95, color=INK, stroke_width=2).move_to(
        RIGHT * (x - 2.5) * 1.15 + UP * (y - 2) * 1.15
    )
