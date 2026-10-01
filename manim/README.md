# Escenas en Manim

Cada diapositiva del guion es un archivo de Manim. El identificador del guion, el nombre del archivo, la clase y el video coinciden: `C1S02` está en `manim/C1S02.py`, clase `C1S02`, y el video queda en `manim/escenas/C1S02.mp4`.

El texto que se lee está en `guion.md`, en la raíz del proyecto. No se reescribe el **Hablado**. La duración es la que figura en **Duración**, o la que se mida leyendo en voz alta.

## Estructura

```
video/
├── guion.md                 texto de cada diapositiva
├── bin/manim                comando para renderizar
└── manim/
    ├── README.md
    ├── 0.plantilla.py       fondo, títulos, colores y casillas
    ├── img/logo_unal.png    logo de la portada
    ├── C0S01.py             una escena por archivo
    ├── C1S02.py
    ├── escenas/             videos finales: escenas/C1S02.mp4
    └── media/               caché de Manim; no es el video que se usa
```

Los comandos se ejecutan desde la raíz del proyecto (`video/`).

## Orden de las diapositivas

El número `Cn` es el bloque. `SNN` es la diapositiva dentro de ese bloque. Van en este orden.

Dentro de C1, C3 y C4 hay diapositivas marcadas **Gente**. Esas son entrevistas: se inserta el video grabado y el narrador calla. No se animan como cuadrícula salvo que se pida.

La primera diapositiva de un bloque con narración (`C1S01`, `C2S01`, …) muestra primero el título del bloque y después el título de la diapositiva. La portada no muestra un cartel grande: usa el logo. En la tabla de contenido, la etiqueta de arriba a la izquierda dice «Tabla de contenido».

## Cómo pedir una escena

Un prompt sirve para una diapositiva. Se nombra el identificador, se dice que la animación sigue el guion frase por frase, se da la duración medida y, si hace falta, se añade una indicación visual.

```
Anima C1S02.

Toma del guion esa diapositiva, con su título y su Hablado. No cambies el texto hablado.
Anima oración por oración, en el orden de la lectura: primero el título de la diapositiva y después cada frase. En cada frase cambia una sola cosa en pantalla y mantenla hasta la frase siguiente.
La duración total es 1:14, contando el título y el tema. Reparte ese tiempo entre el título y cada oración.
Si la frase dice que el agente llega a un estado, camina o se acumula una suma, muéstralo con el movimiento del agente, no con una fila de símbolos suelta.
Exporta la escena y deja el mp4 en manim/escenas/.
```

Qué se cambia según la diapositiva:

- El identificador (`C1S02`, `C2S01`, …).
- La duración medida (`28 seg`, `1:14`, …). Si todavía no se midió, se deja el campo del guion en `[calcular duración leyendo]` y no se inventa un tiempo.
- La última indicación, la que empieza por «Si la frase…». Ahí se dice qué debe verse: el recorrido hasta el +1, la cuenta que termina en 0,64, las cuatro flechas, u otra cosa concreta de esa diapositiva.

La portada y las referencias no llevan narración. En esas se pide la permanencia en pantalla, no un reparto por oraciones.

## Generar una escena

Desde la raíz del proyecto:

```sh
./bin/manim -ql manim/C1S02.py C1S02
```

`-ql` renderiza a 480p y 15 fps, que es la calidad de trabajo. El video queda en:

```
manim/escenas/C1S02.mp4
```

Para otra diapositiva se cambian el archivo y la clase, que llevan el mismo identificador:

```sh
./bin/manim -ql manim/C1S01.py C1S01
```

Ese archivo queda en `manim/escenas/C1S01.mp4`.