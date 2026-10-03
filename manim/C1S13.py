import importlib.util
from pathlib import Path

import numpy as np
from manim import *

_ruta = Path(__file__).with_name("0.plantilla.py")
_spec = importlib.util.spec_from_file_location("plantilla", _ruta)
p = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(p)

SECCION = "El problema: decisión secuencial, política y utilidad"
TITULO = "Ecuación de Bellman y función Q"
TOTAL = 49.0

# El título dura 2,00 s. Los 47 s restantes se reparten en proporción a las
# 155 palabras de las oraciones (47 s × palabras / 155), redondeados a 0,01 s.
DUR = {
    "titulo": 2.00,  # título
    "s1": 10.92,     # 36 palabras
    "s2": 10.61,     # 35
    "s3": 9.70,      # 32
    "s4": 3.34,      # 11
    "s5": 6.37,      # 21
    "s6": 4.85,      # 16
    "s7": 1.21,      # 4
}
assert abs(sum(DUR.values()) - TOTAL) < 1e-6


class C1S13(Scene):
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
        print(f"C1S13: suma de run_time y wait = {self.reloj:.2f} s")

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
            raise ValueError(f"C1S13: la animación se pasa {-falta:.2f} s del tiempo asignado")
        self.esperar(falta)

    # ---------- objetos de la escena ----------
    def preparar(self):
        # Entorno 4×3, igual que en C1S02 y C1S12
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

        # Ecuación de Bellman: U(s) = max_a Σ P(s'|s,a) [R(s,a,s') + γ U(s')]
        self.ecuacion = MathTex(
            r"U(s)=",
            r"\max_{a\in A(s)}",
            r"\sum_{s'}",
            r"P(s'\mid s,a)",
            r"[R(s,a,s')+",
            r"\gamma",
            r"\,U(s')]",
            color=p.INK,
        ).scale(0.95)
        if self.ecuacion.width > 11.5:
            self.ecuacion.scale_to_fit_width(11.5)
        self.ecuacion.move_to(UP * 2.45)
        self.ecuacion[5].set_color(p.AGENT)

        # Las cuatro acciones desde (1,1), con su valor
        centro = self.celdas[(1, 1)].get_center()
        direcciones = {"arriba": UP, "izquierda": LEFT, "abajo": DOWN, "derecha": RIGHT}
        valores = {"arriba": "0,745", "izquierda": "0,711", "abajo": "0,700", "derecha": "0,671"}
        self.acciones = {}
        for nombre, direccion in direcciones.items():
            flecha = Arrow(centro, centro + direccion * 0.72, buff=0.16, color=p.INK, stroke_width=3)
            flecha.set_z_index(5)
            rotulo = Text(valores[nombre], font="Liberation Sans", font_size=26, weight=BOLD, color=p.INK)
            rotulo.move_to(centro + direccion * 1.12)
            rotulo.set_z_index(8)
            self.acciones[nombre] = VGroup(flecha, rotulo)

        # Panel de la derecha: Q(s,a), U(s) = max_a Q(s,a) y π*(s) = argmax_a Q(s,a)
        self.q = MathTex(r"Q(s,a)", color=p.INK).scale(1.2)
        u_max = MathTex(r"U(s)=\max_{a}Q(s,a)", color=p.INK).scale(0.85)
        pi_max = MathTex(r"\pi^{*}(s)=\arg\max_{a}Q(s,a)", color=p.INK).scale(0.85)
        panel = VGroup(self.q, u_max, pi_max).arrange(DOWN, aligned_edge=LEFT, buff=0.55)
        panel.move_to(RIGHT * 4.75 + DOWN * 0.3)
        self.lineas = VGroup(u_max, pi_max)

    # ---------- una función por oración ----------
    def oracion_1(self):
        """La ecuación de Bellman dice que lo que vale un estado es la recompensa del siguiente paso más el valor descontado del estado al que se llega, con la mejor acción y promediando los resultados posibles."""
        t0 = self.reloj
        self.jugar(
            LaggedStart(*[Create(c) for c in self.celdas.values()], lag_ratio=0.08),
            FadeIn(self.mas),
            FadeIn(self.menos),
            FadeIn(self.agente),
            run_time=3.50,
        )
        self.hasta(t0 + DUR["s1"])

    def oracion_2(self):
        """En símbolos: U de s es el máximo, sobre las acciones, de la suma, sobre los estados siguientes, de la probabilidad de la transición por la recompensa más gamma por U del estado de llegada."""
        t0 = self.reloj
        f = self.ecuacion
        tramos = [
            (0.55, VGroup(f[0]), 1.15),                 # U de s es
            (1.82, VGroup(f[1]), 1.30),                 # el máximo, sobre las acciones
            (3.34, VGroup(f[2]), 1.00),                 # de la suma, sobre los estados siguientes
            (5.46, VGroup(f[3]), 1.40),                 # de la probabilidad de la transición
            (7.28, VGroup(f[4], f[5], f[6]), 3.00),     # por la recompensa más gamma por U
        ]
        for inicio, parte, marcha in tramos:
            self.hasta(t0 + inicio)
            self.jugar(Write(parte), run_time=marcha)
        self.hasta(t0 + DUR["s2"])

    def oracion_3(self):
        """En uno uno, con gamma igual a uno: arriba vale cero coma setecientos cuarenta y cinco; izquierda, cero coma setecientos once; abajo, cero coma setecientos; derecha, cero coma seiscientos setenta y uno."""
        t0 = self.reloj
        for nombre, inicio in (("arriba", 2.45), ("izquierda", 4.90), ("abajo", 6.40), ("derecha", 7.60)):
            self.hasta(t0 + inicio)
            flecha, rotulo = self.acciones[nombre]
            self.jugar(Create(flecha), Write(rotulo), run_time=1.00)
        self.hasta(t0 + DUR["s3"])

    def oracion_4(self):
        """El máximo es arriba, y coincide con U de uno uno."""
        t0 = self.reloj
        self.hasta(t0 + 0.60)
        otras = VGroup(
            self.acciones["izquierda"], self.acciones["abajo"], self.acciones["derecha"]
        )
        self.jugar(
            self.acciones["arriba"].animate.set_color(p.AGENT),
            otras.animate.set_opacity(0.25),
            run_time=0.90,
        )
        self.hasta(t0 + DUR["s4"])

    def oracion_5(self):
        """Estos cuatro números son la función Q: la utilidad esperada de ejecutar esa acción y seguir después con una política óptima."""
        t0 = self.reloj
        self.hasta(t0 + 1.45)
        self.jugar(Write(self.q), run_time=1.00)
        self.hasta(t0 + DUR["s5"])

    def oracion_6(self):
        """U es el máximo de Q, y la política óptima elige la acción de ese máximo."""
        t0 = self.reloj
        self.hasta(t0 + 0.15)
        self.jugar(Write(self.lineas), run_time=4.30)
        self.hasta(t0 + DUR["s6"])

    def oracion_7(self):
        """La solución es única."""
        t0 = self.reloj
        self.esperar(0.10)
        self.jugar(Indicate(self.ecuacion, color=p.AGENT, scale_factor=1.05), run_time=1.00)
        self.hasta(t0 + DUR["s7"])