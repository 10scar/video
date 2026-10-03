import importlib.util
from pathlib import Path

import numpy as np
from manim import *

_ruta = Path(__file__).with_name("0.plantilla.py")
_spec = importlib.util.spec_from_file_location("plantilla", _ruta)
p = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(p)

SECCION = "El problema: decisión secuencial, política y utilidad"
TITULO = "Recompensa descontada"
TOTAL = 61.0

# El título dura 2,00 s. Los 59 s restantes se reparten en proporción a las
# 189 palabras de las oraciones (59 s × palabras / 189), redondeados a 0,01 s.
DUR = {
    "titulo": 2.00,  # título
    "s1": 6.87,      # 22 palabras
    "s2": 4.37,      # 14
    "s3": 6.24,      # 20
    "s4": 6.87,      # 22
    "s5": 1.56,      # 5
    "s6": 4.37,      # 14
    "s7": 1.56,      # 5
    "s8": 7.81,      # 25
    "s9": 5.31,      # 17
    "s10": 3.43,     # 11
    "s11": 10.61,    # 34
}
assert abs(sum(DUR.values()) - TOTAL) < 1e-6


class C1S11(Scene):
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
        self.oracion_8()
        self.oracion_9()
        self.oracion_10()
        self.oracion_11()
        self.hasta(TOTAL)
        assert abs(self.reloj - TOTAL) < 1e-6
        print(f"C1S11: suma de run_time y wait = {self.reloj:.2f} s")

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
            raise ValueError(f"C1S11: la animación se pasa {-falta:.2f} s del tiempo asignado")
        self.esperar(falta)

    def brillo(self, g):
        # El brillo de cada término lejano es 0,15 + 0,85·g^k, con k la potencia de gamma.
        for k, termino in enumerate((self.tm1, self.tm2, self.tm3), start=1):
            termino.set_opacity(0.15 + 0.85 * g**k)

    # ---------- objetos de la escena ----------
    def preparar(self):
        self.formula = MathTex(
            r"U_h", r"=", r"R_0", r"+", r"\gamma", r"R_1", r"+", r"\gamma^{2}", r"R_2", r"+", r"\cdots",
            color=p.INK,
        ).scale(1.4)
        self.formula.move_to(UP * 1.3)
        f = self.formula
        self.cab = VGroup(f[0], f[1])
        self.tm0 = VGroup(f[2])
        self.tm1 = VGroup(f[3], f[4], f[5])
        self.tm2 = VGroup(f[6], f[7], f[8])
        self.tm3 = VGroup(f[9], f[10])
        self.gammas = VGroup(f[4], f[7])
        self.futuro = VGroup(self.tm1, self.tm2, self.tm3)
        for parte in (self.cab, self.tm0, self.tm1, self.tm2, self.tm3):
            parte.set_opacity(0.25)
        self.gammas.set_color(p.AGENT)
        self.gammas.set_opacity(1)

        self.centros = [np.array([x, -1.0, 0.0]) for x in (-4.4, -2.2, 0.0, 2.2)]
        self.estados = VGroup(*[p.estado(c) for c in self.centros])
        self.flechas = VGroup(
            *[
                Arrow(self.centros[i], self.centros[i + 1], buff=0.42, color=p.INK, stroke_width=3)
                for i in range(3)
            ]
        )
        self.sigue = Arrow(
            self.centros[3], self.centros[3] + RIGHT * 2.2, buff=0.42, color=p.QUIET, stroke_width=2.5
        )
        self.sigue.set_opacity(0.6)
        self.pista = VGroup(self.estados, self.flechas, self.sigue)
        self.punta = self.centros[3] + RIGHT * 1.6
        self.agente = Dot(self.centros[0], radius=0.1, color=p.AGENT)
        self.agente.set_z_index(12)

        gamma_09 = MathTex(r"\gamma", r"=0{,}9", color=p.INK)
        gamma_09[0].set_color(p.AGENT)
        equivale = Text(
            "equivale a una tasa de interés de 11,1 %",
            font="Liberation Sans",
            font_size=28,
            color=p.INK,
        )
        self.interes = VGroup(gamma_09, equivale).arrange(RIGHT, buff=0.3)
        self.interes.move_to(DOWN * 1.0)

        # Cota de la suma: U_h ≤ R_máx / (1 − γ)
        num = MathTex(r"R_{\max}", color=p.INK)
        den = MathTex(r"1-", r"\gamma", color=p.INK)
        den[1].set_color(p.AGENT)
        ancho = max(num.width, den.width) + 0.3
        barra = Line(LEFT * ancho / 2, RIGHT * ancho / 2, color=p.INK, stroke_width=3)
        fraccion = VGroup(num, barra, den).arrange(DOWN, buff=0.12)
        izquierda = MathTex(r"U_h", r"\le", color=p.INK)
        self.cota = VGroup(izquierda, fraccion).arrange(RIGHT, buff=0.3).scale(1.2)
        self.cota.move_to(DOWN * 2.55)

    # ---------- una función por oración ----------
    def oracion_1(self):
        """Cada paso da una recompensa, y hay que decidir cómo sumarlas: ¿vale lo mismo una recompensa hoy que dentro de un año?"""
        t0 = self.reloj
        self.jugar(
            Create(self.estados),
            Create(self.flechas),
            Create(self.sigue),
            FadeIn(self.agente),
            run_time=1.20,
        )
        self.hasta(t0 + DUR["s1"])

    def oracion_2(self):
        """El modelo dice que no, y usa un número entre cero y uno: gamma."""
        t0 = self.reloj
        self.hasta(t0 + 2.81)
        self.jugar(FadeIn(self.formula), run_time=1.20)
        self.hasta(t0 + DUR["s2"])

    def oracion_3(self):
        """La primera recompensa cuenta completa, la siguiente se multiplica por gamma, la otra por gamma al cuadrado, y así sucesivamente."""
        t0 = self.reloj
        pasos = [
            (self.centros[1], VGroup(self.cab, self.tm0), 0.90, 1.56),
            (self.centros[2], self.tm1, 0.90, 3.43),
            (self.centros[3], self.tm2, 0.90, 5.31),
            (self.punta, self.tm3, 0.70, DUR["s3"]),
        ]
        for destino, termino, marcha, fin in pasos:
            self.jugar(
                self.agente.animate(rate_func=linear).move_to(destino),
                termino.animate.set_opacity(1),
                run_time=marcha,
            )
            self.hasta(t0 + fin)

    def oracion_4(self):
        """Cerca de cero, importa solo lo inmediato; cerca de uno, el agente es paciente; con gamma igual a uno no hay descuento."""
        t0 = self.reloj

        def peso(a):
            return float(
                np.interp(
                    a,
                    [0, 0.07, 0.318, 0.40, 0.636, 0.72, 1.0],
                    [1.0, 0.03, 0.03, 0.92, 0.92, 1.0, 1.0],
                )
            )

        self.jugar(
            UpdateFromAlphaFunc(self.formula, lambda m, a: self.brillo(peso(a)), rate_func=linear),
            run_time=DUR["s4"],
        )
        self.hasta(t0 + DUR["s4"])

    def oracion_5(self):
        """Ojo: gamma no es r."""
        t0 = self.reloj
        self.esperar(0.30)
        self.jugar(Indicate(self.gammas, color=p.AGENT, scale_factor=1.6), run_time=1.00)
        self.hasta(t0 + DUR["s5"])

    def oracion_6(self):
        """La r es el costo de cada paso; gamma es cuánto pesa el futuro."""
        t0 = self.reloj
        self.hasta(t0 + 2.50)
        self.jugar(Indicate(self.futuro, color=p.AGENT, scale_factor=1.12), run_time=1.20)
        self.hasta(t0 + DUR["s6"])

    def oracion_7(self):
        """Hay tres razones para descontar."""
        t0 = self.reloj
        self.jugar(FadeOut(self.pista), FadeOut(self.agente), run_time=0.80)
        self.hasta(t0 + DUR["s7"])

    def oracion_8(self):
        """Primera, preferimos lo cercano: cobrar antes permite invertir, y gamma igual a cero coma nueve equivale a un interés de once coma uno por ciento."""
        t0 = self.reloj
        self.hasta(t0 + 2.81)
        self.jugar(Write(self.interes), run_time=4.60)
        self.hasta(t0 + DUR["s8"])

    def oracion_9(self):
        """Segunda, coherencia: si preferimos un futuro a otro cuando empiezan mañana, debemos preferirlo igual si empiezan hoy."""
        t0 = self.reloj

        def atenuar(_, a):
            self.tm0.set_opacity(
                float(np.interp(a, [0, 0.30, 0.62, 0.72, 1.0], [1.0, 0.15, 0.15, 1.0, 1.0]))
            )

        self.jugar(UpdateFromAlphaFunc(self.formula, atenuar, rate_func=linear), run_time=DUR["s9"])
        self.hasta(t0 + DUR["s9"])

    def oracion_10(self):
        """Eso es la estacionariedad, y solo la suma descontada la cumple."""
        t0 = self.reloj
        self.hasta(t0 + 1.25)
        self.jugar(Indicate(self.formula, color=p.AGENT, scale_factor=1.08), run_time=1.20)
        self.hasta(t0 + DUR["s10"])

    def oracion_11(self):
        """Tercera, sin descuento dos historias infinitas valen infinito y no se comparan; con gamma menor que uno y recompensas acotadas por R máxima, la suma no supera R máxima dividido entre uno menos gamma."""
        t0 = self.reloj
        self.hasta(t0 + 7.18)
        self.jugar(Write(self.cota), run_time=3.00)
        self.hasta(t0 + DUR["s11"])