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
            segundos_titulo=1.89,
        )
        self.celdas = {}
        self.wait(2.16)
        self.armar_rejilla()
        self.marcar_muro()
        self.colocar_agente()
        self.marcar_mas_uno()
        self.marcar_menos_uno()
        self.un_paso_cuesta()
        self.nueve_pasos_y_el_premio()
        self.el_resultado()
        self.un_paso_mas_reduce()
        self.cuatro_acciones()
        self.conoce_la_casilla()

    def armar_rejilla(self):
        for x in range(1, 5):
            columna = []
            for y in range(1, 4):
                celda = p.casilla(x, y)
                self.celdas[(x, y)] = celda
                columna.append(celda)
            self.play(LaggedStart(*[Create(c) for c in columna], lag_ratio=0.2), run_time=0.62)
        self.wait(0.49)

    def marcar_muro(self):
        self.play(self.celdas[(2, 2)].animate.set_fill(p.WALL, opacity=1), run_time=0.55)
        self.wait(2.42)

    def colocar_agente(self):
        self.agente = Dot(self.celdas[(1, 1)].get_center(), radius=0.12, color=p.AGENT)
        self.agente.set_z_index(8)
        self.play(FadeIn(self.agente, scale=0.4), run_time=0.45)
        self.wait(3.87)

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

    def marcar_mas_uno(self):
        self.caminar([(1, 2), (1, 3), (2, 3), (3, 3), (4, 3)], 0.40)
        self.mas = Text("+1", font="Liberation Sans", font_size=28, weight=BOLD, color=p.PAPER)
        self.mas.move_to(self.celdas[(4, 3)])
        self.mas.set_z_index(9)
        self.play(
            self.celdas[(4, 3)].animate.set_fill(p.PLUS, opacity=1),
            FadeIn(self.mas, scale=0.5),
            run_time=0.50,
        )
        self.wait(3.44)

    def marcar_menos_uno(self):
        self.reaparecer_en((1, 1), 0.12, 0.12)
        self.caminar([(2, 1), (3, 1), (4, 1), (4, 2)], 0.35)
        self.menos = Text("−1", font="Liberation Sans", font_size=28, weight=BOLD, color=p.PAPER)
        self.menos.move_to(self.celdas[(4, 2)])
        self.menos.set_z_index(9)
        self.play(
            self.celdas[(4, 2)].animate.set_fill(p.MINUS, opacity=1),
            FadeIn(self.menos, scale=0.5),
            run_time=0.40,
        )
        self.wait(1.74)

    def un_paso_cuesta(self):
        self.reaparecer_en((1, 1), 0.15, 0.15)
        destino = self.celdas[(1, 2)].get_center()
        self.play(self.agente.animate.move_to(destino), run_time=0.70, rate_func=linear)
        self.costo = Text("−0,04", font="Liberation Sans", font_size=28, color=p.INK)
        self.costo.next_to(self.celdas[(1, 2)], RIGHT, buff=0.15)
        self.play(FadeIn(self.costo), run_time=0.40)
        self.wait(7.78)

    def cobrar(self, texto, animacion, run_time):
        nuevo = Text(texto, font="Liberation Sans", font_size=40, weight=BOLD, color=p.INK)
        nuevo.move_to(self.ancla_total)
        nuevo.set_z_index(10)
        cambio = FadeIn(nuevo) if self.total is None else ReplacementTransform(self.total, nuevo)
        self.play(animacion, cambio, run_time=run_time)
        self.total = nuevo

    def nueve_pasos_y_el_premio(self):
        self.play(FadeOut(self.costo), run_time=0.20)
        self.reaparecer_en((1, 1), 0.12, 0.12)
        self.total = None
        self.ancla_total = self.celdas[(4, 2)].get_right() + RIGHT * 1.15
        montos = [
            "−0,04",
            "−0,08",
            "−0,12",
            "−0,16",
            "−0,20",
            "−0,24",
            "−0,28",
            "−0,32",
            "−0,36",
        ]
        self.cobrar(
            montos[0],
            self.agente.animate(rate_func=there_and_back).shift(DOWN * 0.28),
            run_time=0.85,
        )
        ruta = [(1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (3, 2), (3, 3)]
        for xy, monto in zip(ruta, montos[1:]):
            self.cobrar(
                monto,
                self.agente.animate(rate_func=linear).move_to(self.celdas[xy].get_center()),
                run_time=0.85,
            )
        esquina = self.celdas[(4, 3)].get_corner(UL) + RIGHT * 0.22 + DOWN * 0.22
        self.play(
            self.agente.animate(rate_func=linear).move_to(self.celdas[(4, 3)].get_center()),
            self.mas.animate.move_to(esquina).scale(0.72),
            run_time=0.85,
        )
        self.wait(1.05)

    def el_resultado(self):
        suma = Text("0,64", font="Liberation Sans", font_size=48, weight=BOLD, color=p.PLUS)
        suma.move_to(self.ancla_total)
        suma.set_z_index(10)
        premio = self.mas.copy()
        self.add(premio)
        self.play(ReplacementTransform(VGroup(self.total, premio), suma), run_time=1.10)
        self.resultado = suma
        self.wait(2.41)

    def un_paso_mas_reduce(self):
        reducido = Text("0,60", font="Liberation Sans", font_size=48, weight=BOLD, color=p.MINUS)
        reducido.move_to(self.ancla_total)
        reducido.set_z_index(10)
        self.play(ReplacementTransform(self.resultado, reducido), run_time=0.55)
        self.resultado = reducido
        self.wait(8.90)

    def cuatro_acciones(self):
        self.play(FadeOut(self.resultado), run_time=0.35)
        self.play(self.agente.animate.move_to(self.celdas[(1, 1)].get_center()), run_time=0.45)
        self.wait(3.26)
        centro = self.celdas[(1, 1)].get_center()
        tiempos = (0.80, 0.45, 0.50, 0.50)
        esperas = (0.00, 0.36, 0.58, 0.58)
        for direccion, duracion, espera in zip((UP, DOWN, LEFT, RIGHT), tiempos, esperas):
            flecha = Arrow(centro, centro + direccion * 0.72, buff=0.16, color=p.INK, stroke_width=3)
            flecha.set_z_index(5)
            self.play(Create(flecha), run_time=duracion)
            if espera:
                self.wait(espera)

    def conoce_la_casilla(self):
        anillo = Circle(radius=0.42, color=p.AGENT, stroke_width=5).move_to(self.agente.get_center())
        anillo.set_z_index(6)
        self.play(Create(anillo), run_time=0.50)
        self.wait(9.11)
