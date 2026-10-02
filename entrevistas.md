# Entrevistas

Cuatro diapositivas de entrevista. Cada una está dentro de una sección del guion.


| Sección                                                    | Diapositivas de la sección | Entrevistas  |
| ---------------------------------------------------------- | -------------------------- | ------------ |
| C0 · Portada y tabla de contenido                          | 2                          | ninguna      |
| C1 · El problema: decisión secuencial, política y utilidad | 14                         | C1S03, C1S09 |
| C2 · Los algoritmos                                        | 4                          | ninguna      |
| C3 · Los bandidos                                          | 5                          | C3S02        |
| C4 · Observación parcial                                   | 4                          | C4S02        |
| C5 · Análisis y aplicación en computación y comunicaciones | 1                          | ninguna      |
| C6 · Conclusiones y recomendaciones                        | 1                          | ninguna      |
| C7 · Referencias bibliográficas                            | 1                          | ninguna      |


### C1S03 · Gente · Ruta corta o ruta larga

**Duración:** [calcular duración leyendo]

**Producción:** Pregunta uno del protocolo. Se inserta aquí, antes de calcular la probabilidad de la secuencia fija. Duración del inserto: veinte a treinta segundos. Silencio del narrador durante el inserto.

**Pregunta, leída igual en la entrevista y en este audio:** Si cada paso acierta en la dirección pedida solo ocho de cada diez veces, y el resto del tiempo el agente se desplaza de lado, ¿conviene la ruta corta, junto al estado de recompensa menos uno, o la ruta larga, que se aleja de ese estado?

**En pantalla:** la pregunta y el video.

**Hablado, antes del inserto:**

Antes de escribir el modelo, escuchemos esa decisión sin el cálculo. La pregunta formulada a las personas entrevistadas fue esta. Si cada paso acierta en la dirección pedida solo ocho de cada diez veces, y el resto del tiempo el agente se desplaza de lado, ¿conviene la ruta corta, junto al estado de recompensa menos uno, o la ruta larga, que se aleja de ese estado?

**Indicación:** silencio mientras se reproduce el video.

**Hablado, después del inserto:**

Las dos respuestas quedan registradas. A continuación definimos el modelo de transición y vemos por qué una secuencia fija no resuelve el problema. Más adelante, el valor de la recompensa por paso decide cuál de esas dos rutas es óptima.

### C1S09 · Gente · Umbral de la recompensa r

**Duración:** [calcular duración leyendo]

**Producción:** Pregunta dos del protocolo. Se inserta después de mostrar los intervalos de r y antes de separarlos del descuento. Silencio durante el inserto.

**Pregunta:** Cada transición entre estados no terminales recibe una recompensa r. ¿A partir de qué valor de r elegirían ustedes entrar de inmediato al estado de recompensa menos uno, en lugar de continuar hacia el estado de recompensa más uno?

**En pantalla:** la pregunta y el video.

**Hablado, antes del inserto:**

Acabamos de ver que la política cambia con r. Antes de hablar del tiempo, escuchemos cómo se responde esa pregunta sin esos umbrales. La formulación fue esta. Cada transición entre estados no terminales recibe una recompensa r. ¿A partir de qué valor de r elegirían ustedes entrar de inmediato al estado de recompensa menos uno, en lugar de continuar hacia el estado de recompensa más uno?

**Indicación:** silencio durante el video.

**Hablado, después del inserto:**

El valor a partir del cual cambia la respuesta es, en el modelo, uno de los umbrales de r que se acaban de enunciar. La recompensa por paso y el peso del futuro son parámetros distintos. El siguiente apartado fija el segundo.

### C3S02 · Gente · Opción conocida u opción nueva

**Duración:** [calcular duración leyendo]

**Producción:** Pregunta tres del protocolo. Se inserta después de definir explotación y exploración, y antes del ejemplo numérico. Silencio durante el inserto.

**Pregunta:** Hay dos opciones. Una ya entregó recompensa en ensayos anteriores. La otra no se ha ensayado. En el siguiente ensayo, ¿repiten la opción conocida o prueban la desconocida?

**En pantalla:** la pregunta y el video.

**Hablado, antes del inserto:**

La definición ya distingue explotación y exploración. La entrevista recoge la misma alternativa sin el cálculo. La pregunta fue esta. Hay dos opciones. Una ya entregó recompensa en ensayos anteriores. La otra no se ha ensayado. En el siguiente ensayo, ¿repiten la opción conocida o prueban la desconocida?

**Indicación:** silencio durante el video.

**Hablado, después del inserto:**

El ejemplo que sigue muestra que ni repetir siempre la opción conocida ni permanecer siempre en la desconocida es, en general, la política de mayor utilidad. El resultado depende de la secuencia de recompensas y del descuento.

### C4S02 · Gente · Desplazamiento u observación

**Duración:** [calcular duración leyendo]

**Producción:** Pregunta cuatro del protocolo. Se inserta después de enunciar que el estado ya no se observa, y antes de definir la creencia. Silencio durante el inserto.

**Pregunta:** El agente está en el mismo entorno de cuatro por tres, pero no observa la casilla. Solo recibe una señal con error sobre si hay muro en cada dirección. La siguiente acción, ¿debe ser un desplazamiento o una acción destinada a reducir la incertidumbre?

**En pantalla:** la pregunta y el video.

**Hablado, antes del inserto:**

Antes de definir el estado de creencia, se registra cómo se responde sin esa definición. La pregunta fue esta. El agente está en el mismo entorno de cuatro por tres, pero no observa la casilla. Solo recibe una señal con error sobre si hay muro en cada dirección. La siguiente acción, ¿debe ser un desplazamiento o una acción destinada a reducir la incertidumbre?

**Indicación:** silencio durante el video.

**Hablado, después del inserto:**

Definamos las dos posibilidades. Un desplazamiento cambia la distribución sobre las casillas. Una observación, aunque no entregue la recompensa del terminal, puede reducir esa distribución y modificar la decisión siguiente.