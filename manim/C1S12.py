import importlib.util
from pathlib import Path

import numpy as np
from manim import *

_ruta = Path(__file__).with_name("0.plantilla.py")
_spec = importlib.util.spec_from_file_location("plantilla", _ruta)
p = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(p)

SECCION = "El problema: decisión secuencial, política y utilidad"
TITULO = "Utilidad de un estado"
TOTAL = 49.0

# El título dura 2,00 s. Los 47 s restantes se reparten en proporción a las
# 160 palabras de las oraciones (47 s × palabras / 160), redondeados a 0,01 s.
DUR = {
    "titulo": 2.00,  # título
    "s1": 7.05,      # 24 palabras
    "s2": 11.16,     # 38
    "s3": 4.41,      # 15
    "s4": 8.22,      # 28
    "s5": 7.05,      # 24
    "s6": 1.47,      # 5
    "s7": 7.64,      # 26
}
assert abs(sum(DUR.values()) - TOTAL) < 1e-6


class C1S12(Scene):
    def construct(self):
        self.reloj = 0.0
        self.preparar()
        p.presentar(self, SECCION, TITULO, segundos_titulo=DUR["titulo"])
        self.reloj += DUR["titulo"]
        self.oracion_1()
        self.oracion_2()
        self.oracion_3()
        self.oracion_4()
        self.oracion_5()
        self.oracion_6()
        self.oracion_7()
        self.hasta(TOTAL)
        assert abs(self.reloj - TOTAL) < 1e-6
        print(f"C1S12: suma de run_time y wait = {self.reloj:.2f} s")

    # ---------- reloj: lleva la cuenta de cada run_time y cada wait ----------
    def jugar(self, *animaciones, run_time):
        self.play(*animaciones, run_time=run_time)
        self.reloj += run_time

    def esperar(self, segundos):
        if segundos > 1e-9:
            self.wait(segundos)
            self.reloj += segundos

    def hasta(self, instante):
        falta = instante - self.reloj
        if falta < -1e-6:
            raise ValueError(f"C1S12: la animación se pasa {-falta:.2f} s del tiempo asignado")
        self.esperar(falta)

    def caminar(self, casillas, paso):
        for xy in casillas:
            self.jugar(
                self.agente.animate(rate_func=linear).move_to(self.celdas[xy].get_center()),
                run_time=paso,
            )

    # ---------- objetos de la escena ----------
    def preparar(self):
        # Entorno 4×3, igual que en C1S02
        self.celdas = {}
        for x in range(1, 5):
            for y in range(1, 4):
                self.celdas[(x, y)] = p.casilla(x, y)
        self.celdas[(2, 2)].set_fill(p.WALL, opacity=1)
        self.celdas[(4, 3)].set_fill(p.PLUS, opacity=1)
        self.celdas[(4, 2)].set_fill(p.MINUS, opacity=1)
        self.mas = Text("+1", font="Liberation Sans", font_size=28, weight=BOLD, color=p.PAPER)
        self.mas.move_to(self.celdas[(4, 3)])
        self.mas.set_z_index(9)
        self.menos = Text("−1", font="Liberation Sans", font_size=28, weight=BOLD, color=p.PAPER)
        self.menos.move_to(self.celdas[(4, 2)])
        self.menos.set_z_index(9)
        self.agente = Dot(self.celdas[(1, 1)].get_center(), radius=0.12, color=p.AGENT)
        self.agente.set_z_index(12)

        # Parámetros: γ = 1 y r = −0,04
        gamma_uno = MathTex(r"\gamma", r"=1", color=p.INK)
        gamma_uno[0].set_color(p.AGENT)
        conector = Text("y", font="Liberation Sans", font_size=28, color=p.INK)
        r_valor = MathTex(r"r", r"=-0{,}04", color=p.INK)
        self.parametros = VGroup(gamma_uno, conector, r_valor).arrange(RIGHT, buff=0.3)
        self.parametros.move_to(DOWN * 2.5)

        # Panel de valores, en el orden en que se dicen
        self.v33 = MathTex(r"U(3,3) = 0{,}9578", color=p.INK)
        self.v11 = MathTex(r"U(1,1) = 0{,}7453", color=p.INK)
        self.v41 = MathTex(r"U(4,1) = 0{,}4279", color=p.INK)
        panel = VGroup(self.v33, self.v11, self.v41).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        panel.scale(0.9)
        panel.move_to(RIGHT * 4.85)

        # Dos planes que llegan al mismo estado (3,1)
        self.planes = VGroup(
            Arrow(
                self.celdas[(2, 1)].get_center(), self.celdas[(3, 1)].get_center(),
                buff=0.2, color=p.INK, stroke_width=3.5,
            ),
            Arrow(
                self.celdas[(4, 1)].get_center(), self.celdas[(3, 1)].get_center(),
                buff=0.2, color=p.INK, stroke_width=3.5,
            ),
        )

        # π*(s) = argmax_a Σ P(s'|s,a) [R(s,a,s') + γ U(s')]
        self.politica = MathTex(
            r"\pi^{*}",
            r"(s)=\arg\max_{a}\sum_{s'}P(s'\mid s,a)[R(s,a,s')+",
            r"\gamma",
            r"\,U(s')]",
            color=p.INK,
        ).scale(0.95)
        if self.politica.width > 11:
            self.politica.scale_to_fit_width(11)
        self.politica.move_to(UP * 2.45)
        self.politica[2].set_color(p.AGENT)
        self.resto_politica = VGroup(self.politica[1], self.politica[2], self.politica[3])

    # ---------- una función por oración ----------
    def oracion_1(self):
        """La utilidad de un estado, U de s, es lo que el agente espera acumular si parte de s y sigue una política óptima."""
        t0 = self.reloj
        self.jugar(
            LaggedStart(*[Create(c) for c in self.celdas.values()], lag_ratio=0.08),
            FadeIn(self.mas),
            FadeIn(self.menos),
            FadeIn(self.agente),
            Write(self.parametros),
            run_time=2.20,
        )
        self.hasta(t0 + DUR["s1"])

    def oracion_2(self):
        """Con menos cero coma cero cuatro por paso y gamma igual a uno, posible porque siempre se llega a una salida, en tres tres, junto al más uno, U vale cero coma nueve mil quinientos setenta y ocho."""
        t0 = self.reloj
        self.hasta(t0 + 3.80)
        self.caminar([(1, 2), (1, 3), (2, 3), (3, 3)], 0.55)
        self.hasta(t0 + 8.20)
        self.jugar(Write(self.v33), run_time=2.40)
        self.hasta(t0 + DUR["s2"])

    def oracion_3(self):
        """En el estado inicial, uno uno, vale cero coma siete mil cuatrocientos cincuenta y tres."""
        t0 = self.reloj
        self.caminar([(2, 3), (1, 3), (1, 2), (1, 1)], 0.40)
        self.hasta(t0 + 1.75)
        self.jugar(Write(self.v11), run_time=2.40)
        self.hasta(t0 + DUR["s3"])

    def oracion_4(self):
        """Y en cuatro uno, solo cero coma cuatro mil doscientos setenta y nueve: está lejos del más uno y pegado al menos uno, con riesgo de caer ahí."""
        t0 = self.reloj
        self.caminar([(2, 1), (3, 1), (4, 1)], 0.40)
        self.jugar(Write(self.v41), run_time=2.70)
        self.hasta(t0 + DUR["s4"])

    def oracion_5(self):
        """Con horizonte infinito, la política óptima no depende del estado inicial: si dos planes llegan al mismo estado, desde ahí el futuro es igual."""
        t0 = self.reloj
        self.hasta(t0 + 3.23)
        self.jugar(Create(self.planes), run_time=1.20)
        self.hasta(t0 + DUR["s5"])

    def oracion_6(self):
        """Por eso escribimos pi asterisco."""
        t0 = self.reloj
        self.esperar(0.50)
        self.jugar(Write(self.politica[0]), run_time=0.80)
        self.hasta(t0 + DUR["s6"])

    def oracion_7(self):
        """Y con U a la mano, decidir es fácil: se elige la acción que maximiza la recompensa inmediata esperada más el valor descontado del estado siguiente."""
        t0 = self.reloj
        self.hasta(t0 + 2.64)
        self.jugar(Write(self.resto_politica), run_time=4.60)
        self.hasta(t0 + DUR["s7"])