import importlib.util
from pathlib import Path

from manim import *

_ruta = Path(__file__).with_name("0.plantilla.py")
_spec = importlib.util.spec_from_file_location("plantilla", _ruta)
p = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(p)

SECCION = "Observación parcial"
TITULO = "Qué cambia al retirar la observación completa"
TOTAL = 29.0

# Tarjeta de sección 2,30 s y título 2,00 s. Los 24,70 s restantes se reparten en
# proporción a las 92 palabras de las oraciones (24,70 s × palabras / 92),
# redondeados a 0,01 s.
DUR = {
    "tarjeta": 2.30,  # tarjeta de sección
    "titulo": 2.00,   # título
    "s1": 2.68,       # 10 palabras
    "s2": 0.81,       # 3
    "s3": 5.10,       # 19
    "s4": 7.25,       # 27
    "s5": 5.91,       # 22
    "s6": 2.95,       # 11
}
assert abs(sum(DUR.values()) - TOTAL) < 1e-6


class C4S01(Scene):
    def construct(self):
        self.reloj = 0.0
        self.preparar()
        p.presentar(
            self,
            SECCION,
            TITULO,
            inicio=True,
            segundos_seccion=DUR["tarjeta"],
            segundos_titulo=DUR["titulo"],
        )
        self.reloj += DUR["tarjeta"] + DUR["titulo"]
        self.oracion_1()
        self.oracion_2()
        self.oracion_3()
        self.oracion_4()
        self.oracion_5()
        self.oracion_6()
        self.hasta(TOTAL)
        assert abs(self.reloj - TOTAL) < 1e-6
        print(f"C4S01: suma de run_time y wait = {self.reloj:.2f} s")

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
            raise ValueError(f"C4S01: la animación se pasa {-falta:.2f} s del tiempo asignado")
        self.esperar(falta)

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

        # Anillo: el agente conoce su casilla (como al final de C1S02)
        self.anillo = Circle(radius=0.42, color=p.AGENT, stroke_width=5)
        self.anillo.move_to(self.agente.get_center())
        self.anillo.set_z_index(6)

        # π(s) tachada: ya no se puede aplicar
        self.pi = MathTex(r"\pi(s)", color=p.INK).scale(1.8)
        self.pi.move_to(RIGHT * 4.8)
        self.cruz = Cross(self.pi, stroke_color=p.MINUS, stroke_width=6)

        # POMDP = MDP + modelo de sensor P(e | s)
        self.formula = MathTex(
            r"\mathrm{POMDP}=",
            r"\mathrm{MDP}",
            r"+P(e\mid s)",
            color=p.INK,
        ).scale(1.2)
        self.formula.move_to(UP * 2.55)
        self.etiqueta = Text("modelo de sensor", font="Liberation Sans", font_size=24, color=p.QUIET)
        self.etiqueta.next_to(self.formula[2], DOWN, buff=0.15)

    # ---------- una función por oración ----------
    def oracion_1(self):
        """Hasta aquí el agente siempre sabía en qué casilla estaba."""
        t0 = self.reloj
        self.jugar(
            LaggedStart(*[Create(c) for c in self.celdas.values()], lag_ratio=0.08),
            FadeIn(self.mas),
            FadeIn(self.menos),
            FadeIn(self.agente),
            Create(self.anillo),
            run_time=1.60,
        )
        self.hasta(t0 + DUR["s1"])

    def oracion_2(self):
        """Quitemos esa ayuda."""
        t0 = self.reloj
        self.esperar(0.10)
        self.jugar(FadeOut(self.anillo), run_time=0.50)
        self.hasta(t0 + DUR["s2"])

    def oracion_3(self):
        """Pensemos en un robot que no ve su casilla: solo recibe la señal de un sensor, que puede fallar."""
        t0 = self.reloj
        self.hasta(t0 + 2.90)
        self.jugar(
            Flash(
                self.agente,
                color=p.AGENT,
                line_length=0.3,
                num_lines=12,
                flash_radius=0.55,
                line_stroke_width=4,
            ),
            run_time=1.00,
        )
        self.hasta(t0 + DUR["s3"])

    def oracion_4(self):
        """Ya no puede aplicar pi de s, porque no sabe cuál es s, y la mejor acción depende de lo que sabe, no solo de dónde está."""
        t0 = self.reloj
        self.hasta(t0 + 1.00)
        self.jugar(Write(self.pi), run_time=0.90)
        self.hasta(t0 + 2.00)
        self.jugar(Create(self.cruz), run_time=0.80)
        self.hasta(t0 + DUR["s4"])

    def oracion_5(self):
        """A esto se le llama proceso de decisión de Markov parcialmente observable: el mismo proceso de antes más un modelo de sensor."""
        t0 = self.reloj
        f = self.formula
        tramos = [
            (1.30, VGroup(f[0]), 1.60),                  # proceso de decisión de Markov parcialmente observable
            (3.30, VGroup(f[1]), 0.90),                  # el mismo proceso de antes
            (4.60, VGroup(f[2], self.etiqueta), 1.20),   # más un modelo de sensor
        ]
        for inicio, parte, marcha in tramos:
            self.hasta(t0 + inicio)
            self.jugar(Write(parte), run_time=marcha)
        self.hasta(t0 + DUR["s5"])

    def oracion_6(self):
        """Y no es un caso raro: el mundo real es así."""
        t0 = self.reloj
        self.hasta(t0 + 1.00)
        self.jugar(Indicate(self.formula[0], color=p.AGENT, scale_factor=1.15), run_time=1.20)
        self.hasta(t0 + DUR["s6"])