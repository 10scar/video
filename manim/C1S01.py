import importlib.util
from pathlib import Path

from manim import *

_ruta = Path(__file__).with_name("0.plantilla.py")
_spec = importlib.util.spec_from_file_location("plantilla", _ruta)
p = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(p)


class C1S01(Scene):
    def construct(self):
        p.presentar(
            self,
            "El problema: decisión secuencial, política y utilidad",
            "El problema",
            inicio=True,
            segundos_seccion=2.58,
            segundos_titulo=0.54,
        )
        self.decision_que_se_repite()
        self.un_paso_y_la_secuencia()
        self.lista_fija_y_politica()

    def decision_que_se_repite(self):
        origen = p.estado(LEFT * 4.2)
        agente = Dot(origen.get_center(), radius=0.1, color=p.AGENT)
        alto = p.estado(LEFT * 1.1 + UP * 1.35)
        bajo = p.estado(LEFT * 1.1 + DOWN * 1.35)
        ida_alta = Arrow(origen.get_center(), alto.get_center(), buff=0.42, color=p.INK, stroke_width=3)
        ida_baja = Arrow(origen.get_center(), bajo.get_center(), buff=0.42, color=p.QUIET, stroke_width=2.5)
        self.play(Create(origen), FadeIn(agente), run_time=0.50)
        self.wait(2.63)
        self.play(Create(ida_alta), Create(ida_baja), Create(alto), Create(bajo), run_time=1.00)
        self.wait(1.85)
        self.play(agente.animate.move_to(alto.get_center()), run_time=0.70)
        siguiente_a = p.estado(RIGHT * 2.3 + UP * 2.0)
        siguiente_b = p.estado(RIGHT * 2.3 + UP * 0.55)
        otra_a = Arrow(alto.get_center(), siguiente_a.get_center(), buff=0.42, color=p.INK, stroke_width=3)
        otra_b = Arrow(alto.get_center(), siguiente_b.get_center(), buff=0.42, color=p.QUIET, stroke_width=2.5)
        self.play(Create(otra_a), Create(otra_b), Create(siguiente_a), Create(siguiente_b), run_time=1.20)
        self.wait(0.55)

    def un_paso_y_la_secuencia(self):
        salida = p.estado(LEFT * 3.2)
        llegada = p.estado(LEFT * 0.4)
        paso = Arrow(salida.get_center(), llegada.get_center(), buff=0.42, color=p.INK, stroke_width=3)
        marca = Square(side_length=0.28, color=p.AGENT, fill_color=p.AGENT, fill_opacity=1).next_to(
            llegada, UP, buff=0.15
        )
        p.limpiar(self, run_time=0.30)
        self.play(Create(salida), Create(paso), Create(llegada), FadeIn(marca), run_time=1.00)
        self.wait(3.05)
        anterior = llegada
        marcas = VGroup(marca)
        for x in (2.2, 4.6):
            nuevo = p.estado(RIGHT * x)
            union = Arrow(anterior.get_center(), nuevo.get_center(), buff=0.42, color=p.INK, stroke_width=3)
            otra = Square(side_length=0.22, color=p.AGENT, fill_color=p.AGENT, fill_opacity=1).next_to(
                nuevo, UP, buff=0.12
            )
            marcas.add(otra)
            anterior = nuevo
            self.play(Create(union), Create(nuevo), FadeIn(otra), run_time=0.55)
        self.play(marcas.animate.arrange(RIGHT, buff=0.08).next_to(anterior, DOWN, buff=0.45), run_time=0.55)
        self.wait(1.20)

    def lista_fija_y_politica(self):
        centros = [LEFT * 4.5 + RIGHT * i * 2.3 for i in range(4)]
        nodos = VGroup(*[p.estado(c) for c in centros])
        uniones = VGroup(
            *[
                Arrow(nodos[i].get_center(), nodos[i + 1].get_center(), buff=0.42, color=p.INK, stroke_width=3)
                for i in range(3)
            ]
        )
        agente = Dot(nodos[0].get_center(), radius=0.1, color=p.AGENT)
        desvio = p.estado(nodos[1].get_center() + DOWN * 1.7)
        caida = Arrow(nodos[1].get_center(), desvio.get_center(), buff=0.42, color=p.AGENT, stroke_width=3)
        p.limpiar(self, run_time=0.30)
        self.play(Create(nodos), Create(uniones), FadeIn(agente), run_time=0.70)
        self.play(agente.animate.move_to(nodos[1].get_center()), run_time=0.40)
        self.play(Create(caida), Create(desvio), agente.animate.move_to(desvio.get_center()), run_time=0.70)
        self.play(uniones[1].animate.set_opacity(0.15), uniones[2].animate.set_opacity(0.15), run_time=0.40)
        self.wait(1.31)
        self.play(FadeOut(uniones), FadeOut(caida), FadeOut(agente), FadeOut(desvio), run_time=0.35)
        direcciones = [UP, RIGHT, DOWN, LEFT]
        propias = VGroup()
        for nodo, direccion in zip(nodos, direcciones):
            punta = nodo.get_center() + direccion * 0.95
            propias.add(Arrow(nodo.get_center(), punta, buff=0.4, color=p.INK, stroke_width=3))
        self.play(LaggedStart(*[Create(f) for f in propias], lag_ratio=0.2), run_time=1.30)
        self.wait(3.79)
