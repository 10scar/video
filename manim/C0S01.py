import importlib.util
from pathlib import Path

from manim import *

_ruta = Path(__file__).with_name("0.plantilla.py")
_spec = importlib.util.spec_from_file_location("plantilla", _ruta)
p = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(p)


class C0S01(Scene):
    def construct(self):
        p.fondo(self)
        asignatura = Text("Modelos estocásticos", font="Liberation Sans", font_size=28, color=p.QUIET)
        titulo = Text("Decisiones complejas", font="Liberation Serif", font_size=64, color=p.INK)
        expositores = Text("Expositores: [nombres]", font="Liberation Sans", font_size=28, color=p.INK)
        profesor = Text("Profesor: [nombre]", font="Liberation Sans", font_size=28, color=p.INK)
        logo = ImageMobject(str(Path(__file__).parent / "img" / "logo_unal.png"))
        logo.scale(1.35 / logo.height)
        datos = VGroup(expositores, profesor).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        bloque = VGroup(asignatura, titulo, datos).arrange(DOWN, buff=0.45)
        bloque.move_to(ORIGIN)
        logo.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(asignatura), FadeIn(titulo), run_time=1.2)
        self.play(FadeIn(datos), FadeIn(logo), run_time=1.0)
        self.wait(8)
