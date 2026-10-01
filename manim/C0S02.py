import importlib.util
from pathlib import Path

from manim import *

_ruta = Path(__file__).with_name("0.plantilla.py")
_spec = importlib.util.spec_from_file_location("plantilla", _ruta)
p = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(p)


class C0S02(Scene):
    def construct(self):
        p.presentar(self, "Tabla de contenido", "Tabla de contenido")
        lineas = [
            "1   El problema: decisión secuencial, política y utilidad",
            "2   Los algoritmos: iteración de valores e iteración de políticas",
            "3   Los bandidos: explotar o explorar",
            "4   La observación parcial: decidir sin conocer la casilla",
            "5   Aplicación en computación y comunicaciones",
            "6   Conclusiones y recomendaciones",
        ]
        textos = VGroup(
            *[
                Text(linea, font="Liberation Sans", font_size=28, color=p.QUIET)
                for linea in lineas
            ]
        ).arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        textos.move_to(ORIGIN)
        for texto in textos:
            texto.set_opacity(0.25)
            self.add(texto)
        for texto in textos:
            self.play(texto.animate.set_opacity(1).set_color(p.INK), run_time=0.6)
            self.wait(0.8)
