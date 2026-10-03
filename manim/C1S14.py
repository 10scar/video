import importlib.util
from pathlib import Path

import numpy as np
from manim import *

_ruta = Path(__file__).with_name("0.plantilla.py")
_spec = importlib.util.spec_from_file_location("plantilla", _ruta)
p = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(p)

SECCION = "El problema: decisión secuencial, política y utilidad"
TITULO = "Escala de recompensas y representación"
TOTAL = 47.0

# El título dura 2,00 s. Los 45 s restantes se reparten en proporción a las
# 150 palabras de las oraciones (45 s × palabras / 150 = 0,30 s por palabra).
DUR = {
    "titulo": 2.00,  # título
    "s1": 1.50,      # 5 palabras
    "s2": 1.80,      # 6
    "s3": 8.40,      # 28
    "s4": 7.20,      # 24
    "s5": 2.10,      # 7
    "s6": 3.90,      # 13
    "s7": 4.80,      # 16
    "s8": 9.90,      # 33
    "s9": 5.40,      # 18
}
assert abs(sum(DUR.values()) - TOTAL) < 1e-6


class C1S14(Scene):
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
        self.hasta(TOTAL)
        assert abs(self.reloj - TOTAL) < 1e-6
        print(f"C1S14: suma de run_time y wait = {self.reloj:.2f} s")

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
            raise ValueError(f"C1S14: la animación se pasa {-falta:.2f} s del tiempo asignado")
        self.esperar(falta)

    # ---------- objetos de la escena ----------
    def preparar(self):
        # ----- Primera idea: teorema de shaping -----
        self.etiqueta = Text(
            "Teorema de shaping", font="Liberation Sans", font_size=34, weight=BOLD, color=p.INK
        )
        self.etiqueta.move_to(UP * 2.35)

        # R'(s,a,s') = R(s,a,s') + γ Φ(s') − Φ(s)
        self.shaping = MathTex(
            r"R'(s,a,s')=R(s,a,s')+",
            r"\gamma",
            r"\Phi(s')",
            r"-\Phi(s)",
            color=p.INK,
        ).scale(1.1)
        if self.shaping.width > 11:
            self.shaping.scale_to_fit_width(11)
        self.shaping.move_to(UP * 1.1)
        self.shaping[1].set_color(p.AGENT)

        self.conclusion = Text(
            "La política óptima no cambia.", font="Liberation Sans", font_size=30, color=p.INK
        )
        self.conclusion.move_to(DOWN * 0.05)

        # Camino de entrenamiento: un paso, una golosina
        self.centros = [np.array([x, -1.9, 0.0]) for x in (-4.4, -2.2, 0.0, 2.2, 4.4)]
        self.estados = VGroup(*[p.estado(c) for c in self.centros])
        self.flechas = VGroup(
            *[
                Arrow(self.centros[i], self.centros[i + 1], buff=0.42, color=p.INK, stroke_width=3)
                for i in range(4)
            ]
        )
        self.agente = Dot(self.centros[0], radius=0.1, color=p.AGENT)
        self.agente.set_z_index(12)
        self.golosinas = [
            Square(
                side_length=0.22, color=p.AGENT, fill_color=p.AGENT, fill_opacity=1
            ).next_to(self.estados[i + 1], UP, buff=0.12)
            for i in range(4)
        ]

        # ----- Segunda idea: representar un problema grande -----
        # Rejilla 4×3 en pequeño, a la izquierda
        celdas = {}
        for x in range(1, 5):
            for y in range(1, 4):
                celdas[(x, y)] = p.casilla(x, y)
        celdas[(2, 2)].set_fill(p.WALL, opacity=1)
        celdas[(4, 3)].set_fill(p.PLUS, opacity=1)
        celdas[(4, 2)].set_fill(p.MINUS, opacity=1)
        self.mini = VGroup(*celdas.values()).scale(0.6)
        self.mini.move_to(LEFT * 4.6 + UP * 0.6)
        self.entradas = Text("484 entradas", font="Liberation Sans", font_size=28, color=p.INK)
        self.entradas.next_to(self.mini, DOWN, buff=0.35)

        # Rótulo del centro
        self.red = Text(
            "Red de decisión dinámica", font="Liberation Sans", font_size=26, color=p.INK
        )
        self.red.move_to(LEFT * 0.3 + UP * 0.6)

        # Tablero de Tetris de 10 × 20, a la derecha
        columnas, filas, lado = 10, 20, 0.17
        cx, cy = 3.4, 0.0
        izq, abajo = cx - columnas * lado / 2, cy - filas * lado / 2
        marco = Rectangle(width=columnas * lado, height=filas * lado, color=p.INK, stroke_width=2.5)
        marco.move_to(np.array([cx, cy, 0.0]))
        rejilla = []
        for i in range(1, columnas):
            x = izq + i * lado
            rejilla.append(
                Line(np.array([x, abajo, 0.0]), np.array([x, abajo + filas * lado, 0.0]),
                     color=p.QUIET, stroke_width=1.2)
            )
        for j in range(1, filas):
            y = abajo + j * lado
            rejilla.append(
                Line(np.array([izq, y, 0.0]), np.array([izq + columnas * lado, y, 0.0]),
                     color=p.QUIET, stroke_width=1.2)
            )
        self.tablero = VGroup(marco, *rejilla)

        # Tetris: del orden de 10^62 estados
        self.conteo = VGroup(
            Text("Tetris: del orden de", font="Liberation Sans", font_size=28, color=p.INK),
            MathTex(r"10^{62}", color=p.INK),
            Text("estados", font="Liberation Sans", font_size=28, color=p.INK),
        ).arrange(RIGHT, buff=0.25)
        self.conteo.move_to(RIGHT * 2.6 + DOWN * 2.7)

    # ---------- una función por oración ----------
    def oracion_1(self):
        """Dos ideas más, sin demostración."""
        t0 = self.reloj
        self.hasta(t0 + DUR["s1"])

    def oracion_2(self):
        """La primera: el teorema de shaping."""
        t0 = self.reloj
        self.esperar(0.45)
        self.jugar(Write(self.etiqueta), run_time=1.25)
        self.hasta(t0 + DUR["s2"])

    def oracion_3(self):
        """Si a la recompensa le sumamos gamma por fi de s prima, menos fi de s, donde fi es cualquier función del estado, la política óptima no cambia."""
        t0 = self.reloj
        f = self.shaping
        tramos = [
            (0.45, VGroup(f[0]), 1.35),         # a la recompensa le sumamos
            (1.80, VGroup(f[1], f[2]), 1.60),   # gamma por fi de s prima
            (3.60, VGroup(f[3]), 1.10),         # menos fi de s
        ]
        for inicio, parte, marcha in tramos:
            self.hasta(t0 + inicio)
            self.jugar(Write(parte), run_time=marcha)
        self.hasta(t0 + 6.90)
        self.jugar(Write(self.conclusion), run_time=1.20)  # la política óptima no cambia
        self.hasta(t0 + DUR["s3"])

    def oracion_4(self):
        """Es el entrenador que da una golosina por cada paso hacia el truco: la recompensa inmediata informa más y el comportamiento óptimo sigue igual."""
        t0 = self.reloj
        self.hasta(t0 + 0.30)
        self.jugar(
            Create(self.estados), Create(self.flechas), FadeIn(self.agente), run_time=0.90
        )
        for i in range(4):
            self.jugar(
                self.agente.animate(rate_func=linear).move_to(self.centros[i + 1]),
                FadeIn(self.golosinas[i], scale=0.5),
                run_time=0.65,
            )
        self.hasta(t0 + DUR["s4"])

    def oracion_5(self):
        """La segunda: cómo representar un problema grande."""
        t0 = self.reloj
        p.limpiar(self, run_time=0.60)
        self.reloj += 0.60
        self.hasta(t0 + DUR["s5"])

    def oracion_6(self):
        """En el cuatro por tres bastan tablas de cuatrocientas ochenta y cuatro entradas."""
        t0 = self.reloj
        self.hasta(t0 + 0.10)
        self.jugar(
            LaggedStart(*[Create(c) for c in self.mini], lag_ratio=0.08),
            run_time=1.50,
        )
        self.hasta(t0 + 2.40)
        self.jugar(Write(self.entradas), run_time=1.30)
        self.hasta(t0 + DUR["s6"])

    def oracion_7(self):
        """Pero en uno grande se factoriza el estado en variables, con una red de decisión dinámica."""
        t0 = self.reloj
        self.hasta(t0 + 2.90)
        self.jugar(Write(self.red), run_time=1.60)
        self.hasta(t0 + DUR["s7"])

    def oracion_8(self):
        """En Tetris, el estado es la pieza actual, la siguiente y un bit por cada celda de un tablero de diez por veinte: del orden de diez elevado a sesenta y dos estados."""
        t0 = self.reloj
        self.hasta(t0 + 0.30)
        self.jugar(
            LaggedStart(*[Create(m) for m in self.tablero], lag_ratio=0.03),
            run_time=5.50,
        )
        self.hasta(t0 + 6.90)
        self.jugar(Write(self.conteo), run_time=2.70)
        self.hasta(t0 + DUR["s8"])

    def oracion_9(self):
        """Ninguna tabla guarda eso, y por eso no todo se resuelve calculando una tabla completa antes de actuar."""
        t0 = self.reloj
        self.hasta(t0 + 0.20)
        self.jugar(Indicate(self.conteo, color=p.AGENT, scale_factor=1.1), run_time=1.40)
        self.hasta(t0 + DUR["s9"])