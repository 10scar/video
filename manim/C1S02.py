import importlib.util
from pathlib import Path

from manim import *

_ruta = Path(__file__).with_name("0.plantilla.py")
_spec = importlib.util.spec_from_file_location("plantilla", _ruta)
p = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(p)


class C1S02(Scene):
    def construct(self):
        p.presentar(
            self,
            "El problema: decisión secuencial, política y utilidad",
            "Ejemplo del Problema",
            segundos_titulo=1.08,
        )
        self.celdas = {}
        self.total = None
        self.wait(1.24)
        self.armar_rejilla()
        self.colocar_agente()
        self.marcar_salidas()
        self.diez_pasos()
        self.motivo()
        self.cuatro_acciones()
        self.conoce_la_casilla()

    def armar_rejilla(self):
        for x in range(1, 5):
            columna = []
            for y in range(1, 4):
                celda = p.casilla(x, y)
                self.celdas[(x, y)] = celda
                columna.append(celda)
            self.play(LaggedStart(*[Create(c) for c in columna], lag_ratio=0.2), run_time=0.40)
        self.play(self.celdas[(2, 2)].animate.set_fill(p.WALL, opacity=1), run_time=0.45)
        self.wait(1.19)

    def colocar_agente(self):
        self.agente = Dot(self.celdas[(1, 1)].get_center(), radius=0.12, color=p.AGENT)
        self.agente.set_z_index(12)
        self.play(FadeIn(self.agente, scale=0.4), run_time=0.40)
        self.wait(2.07)

    def caminar(self, casillas, paso):
        for xy in casillas:
            self.play(
                self.agente.animate.move_to(self.celdas[xy].get_center()),
                run_time=paso,
                rate_func=linear,
            )

    def reaparecer_en(self, xy, salida, entrada):
        self.play(FadeOut(self.agente), run_time=salida)
        self.agente.move_to(self.celdas[xy].get_center())
        self.play(FadeIn(self.agente, scale=0.4), run_time=entrada)

    def marcar_salidas(self):
        self.caminar([(1, 2), (1, 3), (2, 3), (3, 3), (4, 3)], 0.42)
        self.mas = Text("+1", font="Liberation Sans", font_size=28, weight=BOLD, color=p.PAPER)
        self.mas.move_to(self.celdas[(4, 3)])
        self.mas.set_z_index(9)
        self.play(
            self.celdas[(4, 3)].animate.set_fill(p.PLUS, opacity=1),
            FadeIn(self.mas, scale=0.5),
            run_time=0.40,
        )
        self.wait(0.90)
        self.reaparecer_en((1, 1), 0.10, 0.10)
        self.caminar([(2, 1), (3, 1), (4, 1), (4, 2)], 0.32)
        self.menos = Text("−1", font="Liberation Sans", font_size=28, weight=BOLD, color=p.PAPER)
        self.menos.move_to(self.celdas[(4, 2)])
        self.menos.set_z_index(9)
        self.play(
            self.celdas[(4, 2)].animate.set_fill(p.MINUS, opacity=1),
            FadeIn(self.menos, scale=0.5),
            run_time=0.28,
        )
        self.wait(0.40)

    def acumular(self, texto, color, animacion, run_time):
        nuevo = Text(texto, font="Liberation Sans", font_size=36, weight=BOLD, color=color)
        nuevo.next_to(self.celdas[(2, 1)], DOWN, buff=0.42)
        nuevo.set_x(0)
        nuevo.set_z_index(10)
        cambio = FadeIn(nuevo, shift=DOWN * 0.15) if self.total is None else ReplacementTransform(self.total, nuevo)
        self.play(animacion, cambio, run_time=run_time)
        self.total = nuevo

    def diez_pasos(self):
        self.reaparecer_en((1, 1), 0.12, 0.12)
        montos = ["−0,04", "−0,08", "−0,12", "−0,16", "−0,20", "−0,24", "−0,28", "−0,32", "−0,36"]
        ruta = [(1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1)]
        self.acumular(
            montos[0],
            p.INK,
            self.agente.animate(rate_func=linear).move_to(self.celdas[ruta[0]].get_center()),
            run_time=1.20,
        )
        for xy, monto in zip(ruta[1:], montos[1:6]):
            self.acumular(
                monto,
                p.INK,
                self.agente.animate(rate_func=linear).move_to(self.celdas[xy].get_center()),
                run_time=1.20,
            )
        self.acumular(
            montos[6],
            p.INK,
            self.agente.animate(rate_func=there_and_back).shift(DOWN * 0.28),
            run_time=1.20,
        )
        for xy, monto in zip([(3, 2), (3, 3)], montos[7:]):
            self.acumular(
                monto,
                p.INK,
                self.agente.animate(rate_func=linear).move_to(self.celdas[xy].get_center()),
                run_time=1.20,
            )
        esquina = self.celdas[(4, 3)].get_corner(UL) + RIGHT * 0.22 + DOWN * 0.22
        self.acumular(
            "0,64",
            p.PLUS,
            AnimationGroup(
                self.agente.animate(rate_func=linear).move_to(self.celdas[(4, 3)].get_center()),
                self.mas.animate.move_to(esquina).scale(0.72),
            ),
            run_time=1.20,
        )
        self.wait(0.89)

    def motivo(self):
        self.wait(3.24)

    def cuatro_acciones(self):
        self.play(FadeOut(self.total), run_time=0.25)
        self.play(self.agente.animate.move_to(self.celdas[(1, 1)].get_center()), run_time=0.40)
        self.wait(1.67)
        centro = self.celdas[(1, 1)].get_center()
        esperas = (0.11, 0.11, 0.11, 0.27)
        for direccion, espera in zip((UP, DOWN, LEFT, RIGHT), esperas):
            flecha = Arrow(centro, centro + direccion * 0.72, buff=0.16, color=p.INK, stroke_width=3)
            flecha.set_z_index(5)
            self.play(Create(flecha), run_time=0.35)
            self.wait(espera)

    def conoce_la_casilla(self):
        anillo = Circle(radius=0.42, color=p.AGENT, stroke_width=5).move_to(self.agente.get_center())
        anillo.set_z_index(6)
        self.play(Create(anillo), run_time=0.40)
        self.wait(4.99)
