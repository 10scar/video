import importlib.util
from pathlib import Path

from manim import *

_ruta = Path(__file__).with_name("0.plantilla.py")
_spec = importlib.util.spec_from_file_location("plantilla", _ruta)
p = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(p)

AZUL = "#1A56C4"


class C1S04(Scene):
    def construct(self):
        p.presentar(
            self,
            "El problema: decisión secuencial, política y utilidad",
            "Modelo de transición",
            segundos_titulo=1.95,
        )
        self.escribir_formula()
        self.escribir_definicion()
        self.markov()
        self.efecto_pedido()
        self.angulo_recto()
        self.muro_o_borde()
        self.desde_uno_uno()

    def escribir_formula(self):
        self.formula = MathTex(r"P(s' \mid s,\, a)", color=p.INK).scale(1.7)
        self.formula.move_to(UP * 0.6)
        self.play(Write(self.formula), run_time=1.30)
        self.wait(1.30)

    def escribir_definicion(self):
        self.glosa = Text(
            "probabilidad de llegar a s′ desde s con la acción a",
            font="Liberation Sans",
            font_size=28,
            color=p.INK,
        )
        self.glosa.next_to(self.formula, DOWN, buff=0.45)
        self.play(Write(self.glosa), run_time=1.80)
        self.wait(3.89)

    def nodo(self, texto, punto, color):
        circulo = Circle(radius=0.42, color=color, stroke_width=2.5).move_to(punto)
        rotulo = Text(texto, font="Liberation Sans", font_size=28, color=color).move_to(punto)
        return VGroup(circulo, rotulo)

    def markov(self):
        self.play(FadeOut(self.glosa), run_time=0.35)
        puntos = [LEFT * 4.6 + DOWN * 1.7, LEFT * 2.5 + DOWN * 1.7, LEFT * 0.3 + DOWN * 1.7, RIGHT * 2.6 + DOWN * 1.7]
        self.antes = VGroup(
            self.nodo("s₁", puntos[0], p.QUIET),
            self.nodo("s₂", puntos[1], p.QUIET),
            Arrow(puntos[0], puntos[1], buff=0.5, color=p.QUIET, stroke_width=2.5),
        )
        self.actual = self.nodo("s", puntos[2], p.INK)
        self.llegada = self.nodo("s′", puntos[3], p.INK)
        paso = Arrow(puntos[2], puntos[3], buff=0.5, color=p.INK, stroke_width=3)
        accion = Text("a", font="Liberation Sans", font_size=28, weight=BOLD, color=p.AGENT)
        accion.next_to(paso, UP, buff=0.12)
        self.paso = VGroup(paso, accion)
        self.play(FadeIn(self.antes), FadeIn(self.actual), FadeIn(self.llegada), Create(paso), FadeIn(accion), run_time=1.30)
        anteriores = Text("anteriores", font="Liberation Sans", font_size=24, color=p.QUIET)
        anteriores.next_to(self.antes[0:2], DOWN, buff=0.35)
        actual = Text("actual", font="Liberation Sans", font_size=24, color=p.INK)
        actual.next_to(self.actual, DOWN, buff=0.35)
        self.play(self.antes.animate.set_opacity(0.25), FadeIn(anteriores), FadeIn(actual), run_time=0.75)
        self.notas = VGroup(anteriores, actual)
        self.wait(4.43)

    def flecha(self, origen, destino, color):
        return Arrow(
            self.celdas[origen].get_center(),
            self.celdas[destino].get_center(),
            buff=0.22,
            color=color,
            stroke_width=3.5,
        )

    def cifra(self, texto, punto, color=AZUL):
        rotulo = Text(texto, font="Liberation Sans", font_size=26, weight=BOLD, color=color)
        rotulo.move_to(punto)
        rotulo.set_z_index(8)
        return rotulo

    def reaparecer(self, xy):
        self.play(FadeOut(self.agente), run_time=0.15)
        self.agente.move_to(self.celdas[xy].get_center())
        self.play(FadeIn(self.agente), run_time=0.15)

    def efecto_pedido(self):
        p.limpiar(self, run_time=0.30)
        self.celdas = {}
        for x in range(1, 5):
            columna = []
            for y in range(1, 4):
                celda = p.casilla(x, y)
                self.celdas[(x, y)] = celda
                columna.append(celda)
            self.play(LaggedStart(*[Create(c) for c in columna], lag_ratio=0.15), run_time=0.32)
        self.play(self.celdas[(2, 2)].animate.set_fill(p.WALL, opacity=1), run_time=0.35)
        self.agente = Dot(self.celdas[(3, 1)].get_center(), radius=0.12, color=p.AGENT)
        self.agente.set_z_index(12)
        self.principal = self.flecha((3, 1), (3, 2), p.INK)
        self.ocho = self.cifra("0,8", self.celdas[(3, 1)].get_center() + UP * 0.58 + LEFT * 0.62)
        self.demo = VGroup(self.principal, self.ocho)
        self.play(FadeIn(self.agente), Create(self.principal), FadeIn(self.ocho), run_time=0.55)
        self.wait(2.73)

    def angulo_recto(self):
        self.dos = self.cifra("0,2", self.celdas[(3, 1)].get_center() + DOWN * 0.62)
        self.play(FadeIn(self.dos), run_time=0.40)
        self.wait(1.39)
        self.lado_izq = self.flecha((3, 1), (2, 1), p.QUIET)
        self.lado_der = self.flecha((3, 1), (4, 1), p.QUIET)
        self.play(Create(self.lado_izq), Create(self.lado_der), run_time=1.10)
        self.wait(2.80)
        medio_izq = (self.celdas[(3, 1)].get_center() + self.celdas[(2, 1)].get_center()) / 2
        medio_der = (self.celdas[(3, 1)].get_center() + self.celdas[(4, 1)].get_center()) / 2
        self.uno_izq = self.cifra("0,1", medio_izq + DOWN * 0.38)
        self.uno_der = self.cifra("0,1", medio_der + DOWN * 0.38)
        self.play(FadeOut(self.dos), FadeIn(self.uno_izq), FadeIn(self.uno_der), run_time=0.45)
        self.wait(1.34)

    def muro_o_borde(self):
        self.play(
            FadeOut(self.principal),
            FadeOut(self.ocho),
            FadeOut(self.lado_izq),
            FadeOut(self.lado_der),
            FadeOut(self.uno_izq),
            FadeOut(self.uno_der),
            run_time=0.30,
        )
        self.reaparecer((1, 2))
        self.play(self.agente.animate.shift(RIGHT * 0.32), run_time=0.55, rate_func=linear)
        self.play(self.agente.animate.move_to(self.celdas[(1, 2)].get_center()), run_time=0.45, rate_func=linear)
        self.permanece = Text("permanece", font="Liberation Sans", font_size=26, color=p.INK)
        self.permanece.next_to(self.celdas[(1, 2)], LEFT, buff=0.2)
        self.play(FadeIn(self.permanece), run_time=0.40)
        self.play(Indicate(self.celdas[(2, 2)], color=p.WALL), run_time=0.60)
        self.wait(2.61)

    def desde_uno_uno(self):
        self.play(FadeOut(self.permanece), FadeOut(self.agente), run_time=0.25)
        self.agente.move_to(self.celdas[(1, 1)].get_center())
        self.play(FadeIn(self.agente), run_time=0.25)
        self.wait(0.48)
        sube = self.flecha((1, 1), (1, 2), p.INK)
        ocho = self.cifra("0,8", self.celdas[(1, 1)].get_center() + UP * 0.58 + LEFT * 0.48)
        self.play(Create(sube), FadeIn(ocho), run_time=0.65)
        self.wait(3.26)
        lateral = self.flecha((1, 1), (2, 1), p.QUIET)
        medio = (self.celdas[(1, 1)].get_center() + self.celdas[(2, 1)].get_center()) / 2
        uno_lateral = self.cifra("0,1", medio + DOWN * 0.38)
        self.play(Create(lateral), FadeIn(uno_lateral), run_time=0.55)
        self.wait(2.06)
        self.play(self.agente.animate(rate_func=there_and_back).shift(LEFT * 0.28), run_time=0.80)
        uno_queda = self.cifra("0,1", self.celdas[(1, 1)].get_center() + DOWN * 0.58 + LEFT * 0.15)
        self.play(FadeIn(uno_queda), run_time=0.40)
        self.wait(2.38)
        borde = Line(
            self.celdas[(1, 1)].get_corner(DL),
            self.celdas[(1, 1)].get_corner(UL),
            color=p.MINUS,
            stroke_width=8,
        )
        borde.shift(LEFT * 0.06)
        self.play(Create(borde), run_time=0.45)
        self.wait(1.17)
