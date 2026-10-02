# Guion hablado · Capítulo 16. Decisiones complejas

Texto para grabar en audio. Lo que está bajo **Hablado** se lee tal cual. Lo que está bajo **Producción** o **Indicación** no se pronuncia.

Capítulo: Russell y Norvig, *Making Complex Decisions*, secciones 16.1 a 16.5, archivo [tema.pdf](tema.pdf).

El orden del audio es el de una exposición: portada en silencio, tabla de contenido, explicación, análisis en computación y comunicaciones, conclusiones y referencias en silencio. En lo que se dice en voz alta no se nombra el libro ni el número de sección: se define y se explica. Los cuatro insertos de entrevista se mantienen. Su función es recoger una respuesta previa al apartado que viene, no sustituir la explicación.

La presentación en [presentacion.html](presentacion.html) todavía no está ajustada a esta versión del texto.

## Cómo se leen los números

En el audio se pronuncian como están escritos en **Hablado**. Las fórmulas de pantalla pueden llevar símbolos. La voz no improvisa el nombre del símbolo.

- γ se dice «gamma».
- π se dice «pi».
- ε se dice «épsilon».
- λ se dice «lambda».
- La casilla (1,1) se dice «uno uno». La casilla (4,3) se dice «cuatro tres».



## Protocolo de las cuatro entrevistas

Se graban antes que la narración. El procedimiento es el mismo en las cuatro.

1. Lugar en silencio, plano medio, micrófono cerca de la persona. Se evita música y se evita un fondo que compita con la voz.
2. El entrevistador lee la pregunta una sola vez, con el enunciado de este guion, y no añade ejemplos ni la definición que vendrá después.
3. Cada persona dispone de quince a veinte segundos. No se la interrumpe y no se le corrige.
4. Se graban al menos cuatro personas por pregunta.
5. En la edición se conservan dos respuestas que no coincidan. Si alguien condiciona la respuesta a un dato, por ejemplo el costo, el tiempo restante o la información disponible, esa toma se conserva: ese dato es el parámetro que el bloque siguiente va a definir.
6. El inserto final dura entre veinte y treinta segundos. El narrador no habla encima.
7. Antes del inserto, el narrador anuncia la pregunta. Después del inserto, el narrador dice qué se va a definir con esas dos respuestas.

Preguntas, en el orden del video:

1. Antes del modelo de transición. Si cada paso acierta en la dirección pedida solo ocho de cada diez veces, y el resto del tiempo el agente se desplaza de lado, ¿conviene la ruta corta, junto al estado de recompensa menos uno, o la ruta larga, que se aleja de ese estado?
2. Antes del apartado de recompensas. Cada transición entre estados no terminales recibe una recompensa r. ¿A partir de qué valor de r elegirían ustedes entrar de inmediato al estado de recompensa menos uno, en lugar de continuar hacia el estado de recompensa más uno?
3. Antes de los bandidos. Hay dos opciones. Una ya entregó recompensa en ensayos anteriores. La otra no se ha ensayado. En el siguiente ensayo, ¿repiten la opción conocida o prueban la desconocida?
4. Antes de los procesos parcialmente observables. El agente está en el mismo entorno de cuatro por tres, pero no observa la casilla. Solo recibe una señal con error sobre si hay muro en cada dirección. La siguiente acción, ¿debe ser un desplazamiento o una acción destinada a reducir la incertidumbre?

---



## C0 · Portada

**Duración del bloque:** [calcular duración leyendo]

Sin narración. Permanencia en pantalla: unos ocho segundos.

### C0S01 · Portada

**Duración:** [calcular duración leyendo]

**En pantalla:**

- Asignatura: Modelos estocásticos.
- Título: Decisiones complejas.
- Expositores: [nombres].
- Profesor de la asignatura: [nombre].
- Logo de la Universidad Nacional de Colombia.

**Hablado:** ninguno.

---



## C0 · Tabla de contenido



### C0S02 · Tema · Orden de la exposición

**Duración:** [calcular duración leyendo]

**En pantalla:**

1. El problema: decisión secuencial, política y utilidad.
2. Los algoritmos: iteración de valores e iteración de políticas.
3. Los bandidos: explotar o explorar.
4. La observación parcial: decidir sin conocer la casilla.
5. Aplicación en computación y comunicaciones.
6. Conclusiones y recomendaciones.
7. Bibliografia

**Hablado:** se lee las secciones 

---



## C1 · El problema: decisión secuencial, política y utilidad.

**Duración del bloque:** [calcular duración leyendo]

### C1S01 · Yo · El problema

**Duración:** 28 seg

**En pantalla:** Sin frases. Un estado, una flecha que se abre en dos llegadas, y una segunda decisión al llegar. Luego un solo paso con la marca del resultado; después la marca repartida a lo largo de varios pasos. La sucesión fija se rompe cuando el agente se desvía. Al final, cada estado tiene su propia flecha.

**Hablado:**

Se trata de determinar qué acción corresponde en el instante presente cuando el estado siguiente no queda fijado por esa acción y, una vez alcanzado, exige una decisión nueva.

Si la decisión fuera de un solo paso, bastaría con la utilidad del resultado inmediato. En este caso la utilidad depende de la secuencia completa. La solución no consiste, por tanto, en fijar de antemano una sucesión de acciones. Consiste en una política, esto es, en asignar una acción a cada estado en el que el agente pueda encontrarse.

---



### C1S02 · Tema · Ejemplo del Problema.

**Duración:** 40 seg

**En pantalla:** La cuadrícula se dibuja y el muro ocupa dos dos. El agente aparece en uno uno, camina hasta cuatro tres y después hasta cuatro dos. Luego da diez pasos hasta el más uno: debajo, la suma baja de cuatro en cuatro centésimas y, al entrar, queda en cero punto seis cuatro. Desde uno uno salen las cuatro direcciones, y la casilla queda señalada.

**Hablado: 40 seg**

Definamos el entorno.

Hay cuatro columnas y tres filas, con un muro en la casilla dos dos. El agente comienza en la casilla uno uno. El proceso termina al entrar en cuatro tres, con recompensa más uno, o en cuatro dos, con recompensa menos uno.

En las transiciones que no entran a un estado terminal, la recompensa es menos cero punto cero cuatro es decir si el agente llega al estado más uno en diez pasos, se le resta por cada casilla que haya pasado y el resultado es cero punto seis cuatro. la recompensa negativa da un motivo para terminar pronto.

Las acciones en cada estado no terminal son arriba, abajo, izquierda y derecha. En esta primera parte el entorno es totalmente observable: el agente conoce la casilla en la que está.

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

### C1S04 · Tema · Modelo de transición

**Duración:** 48 segundos

**Hablado:**

Definamos el modelo de transición. Se escribe P de s prima dado s y a. Es la probabilidad de llegar al estado s prima si en el estado s se ejecuta la acción a. Suponemos que esa probabilidad es markoviana: depende del estado actual y de la acción, no de los estados anteriores.

En el ejemplo, cada acción producira el efecto pedido con probabilidad cero punto ocho. Con probabilidad cero punto dos el agente se mueve en ángulo recto respecto de la dirección pedida, cero punto uno a cada lado. Si el destino es un muro o el borde del entorno, el agente permanece en la misma casilla.

Desde uno uno, la acción arriba llega a uno dos con probabilidad cero punto ocho, a dos uno con probabilidad cero punto uno, y permanece en uno uno con probabilidad cero punto uno, porque el lado izquierdo es el borde.

### C1S05 · Tema · Estados alcanzables.

**Duración:** [calcular duración leyendo]

**En pantalla:** Secuencia arriba, arriba, derecha, derecha, derecha. Probabilidad de la trayectoria intencional: cero punto ocho a la quinta, igual a cero punto tres dos siete seis ocho. Probabilidad total de llegar a más uno: cero punto tres dos siete siete seis.

**Indicación:** lanzar la simulación de doscientos ensayos. Si la frecuencia se aparta de treinta y tres por ciento, se dice que la muestra es finita y que el valor exacto es cero punto tres dos siete siete seis.

**Hablado:**

Si el entorno fuera determinista, una solución sería la secuencia arriba, arriba, derecha, derecha, derecha. Con el modelo anterior, esa secuencia solo es una trayectoria posible.

La probabilidad de que las cinco acciones produzcan el efecto pedido es cero punto ocho elevado a cinco, es decir cero punto tres dos siete seis ocho. Existe además una probabilidad pequeña de llegar al estado más uno por el otro lado del muro. Si se suman ambas contribuciones, el resultado es cero punto tres dos siete siete seis.

Ese valor es aproximadamente un tercio. La secuencia no indica qué hacer si el agente termina en otra casilla. Por eso la solución tiene que asignar una acción a cada estado alcanzable, no solo a los estados de una trayectoria prevista.

### C1S06 · Tema · Definición de proceso de decisión de Markov

**Duración:** [calcular duración leyendo]

**En pantalla:** Estados, estado inicial, acciones A(s), transición P(s prima | s, a), recompensa R(s, a, s prima).

**Hablado:**

Con estos elementos definamos un proceso de decisión de Markov. Consta de un conjunto de estados, con un estado inicial; un conjunto de acciones en cada estado; un modelo de transición markoviano; y una función de recompensa R de s, a y s prima. Las recompensas están acotadas por una constante R máxima.

En este entorno las acciones disponibles son las mismas en todos los estados no terminales. En otros problemas el conjunto de acciones puede depender del estado. Lo que se mantiene es la propiedad de Markov y la forma aditiva de la recompensa a lo largo de la historia.

Para resolverlo usaremos programación dinámica: se divide el problema en subproblemas, se conserva la solución de cada subproblema y se reutiliza. Ese cálculo lo hacemos cuando hablemos de los algoritmos.

### C1S07 · Tema · Política y política óptima

**Duración:** [calcular duración leyendo]

**En pantalla:** π(s) es la acción que la política asigna al estado s. π asterisco es una política óptima.

**Hablado:**

Una política, denotada por pi, es una función que asigna una acción a cada estado. Pi de s es la acción recomendada en s. Después de ejecutarla, el estado resultante también tiene una acción asignada. La política queda definida aunque la transición no sea la que se intentó.

Como la transición es aleatoria, la misma política puede generar historias distintas. Su calidad es la utilidad esperada de esas historias. Una política óptima, pi asterisco, es una política cuya utilidad esperada es máxima.

Una política, una vez calculada, se ejecuta así: se observa el estado y se aplica la acción correspondiente. El cálculo previo usa las utilidades. La ejecución solo consulta la acción ya asignada.

### C1S08 · Tema · Políticas óptimas según la recompensa r

**Duración:** [calcular duración leyendo]

**En pantalla:** Para r igual a menos cero punto cero cuatro, en (3,1) son óptimas izquierda y arriba. Debajo, los intervalos de r.

**Indicación:** mover el control de r y detenerse en cada intervalo que se enuncia.

**Hablado:**

Para r igual a menos cero punto cero cuatro hay dos políticas óptimas. Difieren solo en la casilla tres uno, donde izquierda y arriba tienen el mismo valor. Izquierda alarga el recorrido y reduce la probabilidad de entrar en cuatro dos. Arriba lo acorta y aumenta esa probabilidad.

Al cambiar r, la recompensa de las transiciones no terminales, cambia la política.

Si r es menor que menos uno punto seis cuatro nueve siete, la política se dirige a la salida más cercana, incluido el terminal de recompensa menos uno.

Si r está entre menos cero punto siete tres uno uno y menos cero punto cuatro cinco dos seis, desde dos uno, tres uno y tres dos se toma la ruta más corta hacia más uno. Desde cuatro uno se prefiere entrar en menos uno.

Entre menos cero punto cero ocho cinco cero y menos cero punto cero dos siete tres reaparece el empate en tres uno.

Entre menos cero punto cero dos siete cuatro y cero, en cuatro uno y en tres dos la acción se aleja del terminal menos uno, aunque la transición deje al agente contra el muro.

Si r es positivo, se evitan los dos terminales. Una política que no garantiza llegar a un terminal se llama impropia. Con r positivo y sin descuento, su recompensa total es infinita, y toda política de ese tipo es óptima.

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

### C1S10 · Tema · Horizonte y política estacionaria

**Duración:** [calcular duración leyendo]

**En pantalla:** Con horizonte N igual a tres, desde (3,1) la acción óptima es arriba. Con N igual a cien, es izquierda. Sin horizonte fijo, la política óptima es estacionaria.

**Hablado:**

Definamos ahora la utilidad de una historia.

La primera decisión es si el horizonte es finito o infinito. Horizonte finito significa que existe un tiempo N después del cual la historia ya no modifica la utilidad. En la casilla tres uno, si N es igual a tres, la acción que puede alcanzar el estado más uno es arriba. Si N es igual a cien, hay tiempo para la ruta izquierda. La acción óptima en el mismo estado depende del tiempo restante. Esa política se llama no estacionaria.

Si no hay un plazo fijo, no hay motivo para elegir acciones distintas en el mismo estado en dos instantes distintos. La política óptima es estacionaria: la acción depende solo del estado. De aquí en adelante trabajamos con horizonte infinito.

Horizonte infinito no significa que toda historia sea infinita. Significa que no hay un plazo establecido de antemano. Si hay estados terminales y la política es propia, la historia termina.

### C1S11 · Tema · Recompensa descontada

**Duración:** [calcular duración leyendo]

**En pantalla:** U de la historia es igual a R cero, más gamma R uno, más gamma al cuadrado R dos, y así sucesivamente. Gamma igual a cero punto nueve equivale a una tasa de interés de once punto uno por ciento.

**Hablado:**

Definamos la utilidad como la suma de recompensas descontadas. La primera recompensa entra completa, la siguiente multiplicada por gamma, y la posterior por gamma al cuadrado. Gamma está entre cero y uno. Cerca de cero, las recompensas lejanas casi no contribuyen. Cerca de uno, conservan peso. Si gamma es uno, la expresión es la suma sin descuento.

Hay tres razones para usar esta forma. En personas y en animales, la recompensa próxima suele valorarse más que la lejana. Si la recompensa es monetaria, recibirla antes permite invertirla: gamma igual a cero punto nueve equivale a una tasa de once punto uno por ciento. Y si el orden de preferencia entre dos continuaciones es uno, ese orden debe mantenerse cuando esas continuaciones empiezan hoy. Esa condición se llama estacionariedad de las preferencias, y la utilidad que la cumple es la suma descontada.

Sin descuento, dos historias infinitas pueden valer ambas infinito y no compararse. Si gamma es menor que uno y cada recompensa está acotada por R máxima, la suma no supera a R máxima partida por uno menos gamma.

### C1S12 · Tema · Utilidad de un estado

**Duración:** [calcular duración leyendo]

**En pantalla:** Gamma igual a uno y r igual a menos cero punto cero cuatro. U(1,1) es igual a cero punto siete cuatro cinco tres. U(3,3) es igual a cero punto nueve cinco siete ocho. U(4,1) es igual a cero punto cuatro dos siete nueve.

**Hablado:**

Definida la utilidad de una historia, la utilidad de un estado es el valor esperado de esa suma si, desde ese estado, se ejecuta una política óptima. Se denota U de s.

Calculemos esos valores con gamma igual a uno y r igual a menos cero punto cero cuatro. En tres tres, junto al terminal más uno, U vale cero punto nueve cinco siete ocho. En el estado inicial uno uno, U vale cero punto siete cuatro cinco tres. En cuatro uno, U vale cero punto cuatro dos siete nueve. El valor es menor porque desde esa casilla hay probabilidad de entrar en el terminal menos uno.

Con utilidades descontadas y horizonte infinito, la política óptima no depende del estado inicial. Por eso puede escribirse pi asterisco, sin indicar desde qué estado se empezó. La secuencia de acciones sí depende del estado inicial, porque la política se consulta en el estado que efectivamente se alcanza.

Con U conocida, la acción óptima en s maximiza la recompensa inmediata esperada más el valor descontado del estado siguiente. Esa regla es la que escribimos a continuación como ecuación de Bellman.

### C1S13 · Tema · Ecuación de Bellman y función Q

**Duración:** [calcular duración leyendo]

**En pantalla:** U(s) es el máximo, sobre las acciones, de la suma sobre s prima de P(s prima | s, a) por corchete R más gamma U(s prima). En (1,1): arriba cero punto siete cuatro cinco, izquierda cero punto siete uno uno, abajo cero punto siete cero cero, derecha cero punto seis siete uno.

**Hablado:**

La ecuación de Bellman, de mil novecientos cincuenta y siete, escribe U de s como el máximo, sobre las acciones, de la suma sobre los estados siguientes. Cada término es la probabilidad de la transición, multiplicada por la recompensa de esa transición más gamma por la utilidad del estado de llegada.

En uno uno, con gamma igual a uno, los cuatro valores son estos. Arriba, cero punto siete cuatro cinco. Izquierda, cero punto siete uno uno. Abajo, cero punto siete cero cero. Derecha, cero punto seis siete uno. El máximo es arriba y coincide con U de uno uno.

La solución del sistema es única. No hacemos aquí la demostración. El uso es este: unos valores que cumplen Bellman en todos los estados son las utilidades, y la política se lee en el máximo de cada estado.

Q de s y a es la utilidad esperada de ejecutar la acción a en s y continuar después con una política óptima. U de s es el máximo de Q, y la política óptima elige la acción de ese máximo.

### C1S14 · Tema · Escala de recompensas y representación

**Duración:** [calcular duración leyendo]

**En pantalla:** Teorema de shaping: R prima igual a R más gamma por fi de s prima menos fi de s. La política óptima no cambia. Tetris: del orden de diez elevado a sesenta y dos estados.

**Hablado:**

Antes de pasar a los algoritmos, enunciemos dos resultados. No los demostramos.

El primero es el teorema de shaping. Si a la recompensa se le suma gamma por fi de s prima menos fi de s, donde fi es una función del estado, la política óptima permanece igual. La transformación puede hacer más informativa la recompensa inmediata. No modifica cuál es la política óptima.

El segundo es la representación. Para un entorno pequeño, la transición y la recompensa caben en tablas. Para un entorno grande, el estado se factoriza en variables, mediante una red de decisión dinámica. En Tetris, el estado incluye la pieza actual, la pieza siguiente y un bit por cada celda de un tablero de diez por veinte. El número de estados es del orden de diez elevado a sesenta y dos. Esa cifra explica, cuando hablemos de algoritmos, por qué no todo proceso se resuelve calculando una tabla completa antes de actuar.

---



## C2 · Los algoritmos

**Duración del bloque:** [calcular duración leyendo]

### C2S01 · Tema · Iteración de valores

**Duración:** [calcular duración leyendo]

**En pantalla:** Actualización de Bellman. Gamma igual a cero punto nueve y r igual a menos cero punto cero cuatro. En la iteración cinco la política ya es óptima y el error máximo de las utilidades es cero punto cinco uno.

**Indicación:** reiniciar la simulación y reproducirla. Indicar la casilla tres tres cuando su valor aumente. Pausar cuando las acciones dejen de cambiar y el error siga siendo visible. Si el contador de la simulación marca la iteración cuatro con error cero punto cinco uno, se dice ese número y se dice el número de la simulación y se añade que, en el cálculo de referencia, la política ya es óptima en la iteración cinco, con error cero punto cinco uno.

**Hablado:**

Hablemos de cómo calcular la política. El primer algoritmo es la iteración de valores. Hay una ecuación de Bellman por estado. El máximo impide resolver el sistema como un sistema lineal. El algoritmo parte de utilidades iniciales, aquí iguales a cero, y en cada iteración sustituye la utilidad de cada estado por el máximo de sus Q, calculadas con los valores de la iteración anterior. La sustitución es simultánea en todos los estados.

Los estados lejanos al terminal más uno reciben primero la recompensa negativa. El estado tres tres, adyacente a cuatro tres, incorpora antes la recompensa más uno. En las iteraciones siguientes ese cambio pasa a los vecinos.

Si gamma es menor que uno, cada iteración reduce el error al menos en el factor gamma. Hay una sola solución y el procedimiento converge a ella. Con gamma igual a cero punto nueve la convergencia es rápida. Cuando gamma se acerca a uno, el número de iteraciones aumenta. Se puede parar antes: si ningún estado cambia más que épsilon por uno menos gamma, partido por gamma, el error ya es menor que épsilon.

Conviene separar la convergencia de los números y la de las acciones. Con gamma igual a cero punto nueve, en la iteración cinco la política ya es óptima y el error máximo de las utilidades sigue en cero punto cinco uno. La simulación muestra el mismo hecho: las acciones se fijan mientras los valores siguen moviéndose.

### C2S02 · Tema · Pérdida de política

**Duración:** [calcular duración leyendo]

**En pantalla:** Si el error de U es menor que épsilon, la pérdida de política es menor que dos épsilon.

**Hablado:**

La pérdida de política es la diferencia entre la utilidad de la política óptima y la utilidad de la política que se obtiene con la estimación actual. Si el error máximo de las utilidades es menor que épsilon, esa pérdida es menor que dos épsilon.

En el ejemplo, la pérdida llega a cero antes de que el error de las utilidades sea pequeño. Para decidir cuántas iteraciones ejecutar, el criterio relevante es el momento en que la acción recomendada en cada estado deja de cambiar.

### C2S03 · Tema · Iteración de políticas y programación lineal

**Duración:** [calcular duración leyendo]

**En pantalla:** Evaluación: con la acción fija, el sistema es lineal. Mejora: sustituir la acción por la de mayor Q. Parada: cuando la política no cambia.

**Hablado:**

La iteración de políticas alterna dos pasos. En la evaluación, la acción de cada estado está fija, el máximo desaparece y queda un sistema lineal: n ecuaciones y n utilidades. En la mejora, cada estado adopta la acción de mayor Q si esa acción aumenta el valor.

El algoritmo termina cuando la política ya no cambia. Esas utilidades cumplen Bellman y la política es óptima. Termina en un número finito de pasos porque hay finitas políticas y cada mejora estricta aumenta el valor.

Con muchos estados no hace falta resolver el sistema hasta el último decimal, ni actualizar todos los estados en cada vuelta. Esas variantes se llaman iteración modificada e iteración asíncrona. El problema también puede escribirse como un programa lineal. En la práctica, ese método no supera a la programación dinámica en estos procesos.

### C2S04 · Tema · Métodos en línea

**Duración:** [calcular duración leyendo]

**En pantalla:** Tetris, del orden de diez elevado a sesenta y dos estados. Con gamma cero punto cinco, un horizonte de profundidad cinco puede bastar. Con gamma cero punto nueve, el cálculo análogo pide profundidad del orden de cuarenta y cuatro.

**Hablado:**

Esos dos algoritmos calculan la política completa antes de actuar. En el entorno de cuatro por tres el cálculo es viable. En Tetris, con del orden de diez elevado a sesenta y dos estados, no lo es.

Entonces el cálculo se hace en el momento de la decisión. En cada nodo de decisión se toma el máximo, y en cada nodo de azar el promedio. Con gamma igual a cero punto cinco, una profundidad de cinco puede dejar el error por debajo de una cota fijada. Con gamma igual a cero punto nueve, la profundidad análoga es del orden de cuarenta y cuatro. Si hay demasiados sucesores, el promedio se estima con muestras. El algoritmo UCT se formuló para este problema. En el cuatro por tres las trayectorias se alargan por los ciclos. En Tetris, la simulación distingue una colocación estable de una que llena el tablero.

Con esto cerramos los algoritmos del caso en que el modelo se conoce. Ahora cambia el problema: la recompensa de cada opción deja de ser conocida.

---



## C3 · Los bandidos

**Duración del bloque:** [calcular duración leyendo]

### C3S01 · Tema · Definición

**Duración:** [calcular duración leyendo]

**En pantalla:** n brazos. Cada brazo es un proceso de recompensa de Markov. Solo se puede accionar un brazo en cada instante. Gamma es común.

**Hablado:**

Definamos un bandido de n brazos. Cada brazo es un proceso de recompensa de Markov, esto es, un proceso con una sola acción. Solo evoluciona el brazo seleccionado. El agente elige un brazo por instante, recibe su recompensa y usa un mismo gamma.

En cada instante hay dos alternativas. Explotar es seleccionar el brazo de mayor recompensa esperada con la información actual. Explorar es seleccionar un brazo menos observado, porque el resultado puede mejorar las elecciones posteriores. El mismo modelo describe la elección entre tratamientos, inversiones, proyectos o anuncios: cada ensayo cuesta y su resultado informa el ensayo siguiente.

Dos datos ayudan a situar el problema. Durante la Segunda Guerra Mundial el problema se consideró tan difícil que se propuso, como broma, enviarlo al adversario en calidad de sabotaje intelectual. Y una política óptima no tiene que terminar en el mejor brazo: hay una probabilidad positiva de que se fije en un brazo inferior, porque seguir explorando tiene costo.

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

### C3S03 · Tema · Ejemplo con gamma igual a cero punto cinco

**Duración:** [calcular duración leyendo]

**En pantalla:** Brazo M: cero, dos, cero, siete punto dos, y después ceros. Brazo M uno: uno en todos los instantes. Utilidades: uno punto nueve, dos, y dos punto cero dos cinco.

**Hablado:**

Tomemos un caso determinista, con gamma igual a cero punto cinco. El brazo M entrega la secuencia cero, dos, cero, siete punto dos, y después ceros. El brazo M uno entrega uno en cada instante.

Si hay que elegir un solo brazo y mantenerlo, la utilidad de M es uno punto nueve. Se obtiene sumando cero, más cero punto cinco por dos, más cero punto uno dos cinco por siete punto dos. La utilidad de M uno es la suma de la serie geométrica de razón cero punto cinco, igual a dos. Con esa restricción, M uno es mejor.

Si se permite cambiar, la política que acciona M durante los cuatro primeros instantes y después pasa a M uno obtiene dos punto cero dos cinco. Es mayor que uno punto nueve y mayor que dos. Cambiar antes deja sin cobrar el siete punto dos. Cambiar después dedica instantes descontados a recompensas cero, cuando el uno seguro todavía tiene peso.

El ejemplo muestra lo que importa: la política óptima usa el brazo de recompensa variable mientras esa recompensa llega en instantes cuyo descuento aún es significativo, y después pasa al brazo de recompensa constante.

### C3S04 · Tema · Índice de Gittins

**Duración:** [calcular duración leyendo]

**En pantalla:** Lambda es la recompensa constante que deja indiferente entre seguir con el brazo M y recibir lambda en todos los instantes. La política óptima selecciona el brazo de mayor índice.

**Hablado:**

Generalicemos el ejemplo. Un brazo entrega una secuencia de recompensas. El otro entrega una constante lambda, conocida, en todos los instantes. Equivale a decidir si se continúa con el primer brazo o se detiene y se recibe lo seguro.

Existe un valor de lambda que deja indiferente entre esas dos alternativas. Ese valor es el índice de Gittins del brazo. En la fórmula, el numerador es la utilidad esperada de continuar hasta el mejor momento de parada, y el denominador es el tiempo descontado consumido por esa continuación. El índice mide la mayor utilidad por unidad de tiempo descontado que el brazo puede entregar.

Para varios brazos independientes, la política óptima calcula el índice de cada brazo por separado y selecciona el de índice mayor. No se necesita una planificación conjunta. No derivamos aquí la fórmula. Usamos el resultado: el índice resume cada brazo en un número comparable con una recompensa segura.

### C3S05 · Tema · Superproceso y costo de oportunidad

**Duración:** [calcular duración leyendo]

**En pantalla:** Cuatro proyectos y un solo recurso. Calendario óptimo de un proyecto aislado: primera entrega en la semana quince. Calendario que adelanta la entrega a la semana cinco. Con cuatro proyectos, las entregas quedan en las semanas cinco, diez, quince y veinte, en lugar de quince, treinta, cuarenta y cinco y sesenta.

**Hablado:**

Hablemos, para cerrar este bloque, del superproceso. Cada brazo es ahora un proceso de decisión completo, y solo se puede atender uno en cada instante.

Resolver cada proceso por separado y después elegir cuál atender no da, en general, la política del conjunto. Dentro de un proceso, la solución global puede usar una acción que no es óptima para ese proceso aislado. La causa es el costo de oportunidad: el tiempo dado a una tarea se resta a las otras, y el descuento penaliza la espera.

Veamos un caso. El calendario óptimo de un solo proyecto entrega la primera unidad en la semana quince. Otro calendario, de mayor costo para ese proyecto, la entrega en la semana cinco. Con cuatro proyectos y un solo equipo, las entregas quedan en las semanas cinco, diez, quince y veinte, en lugar de quince, treinta, cuarenta y cinco y sesenta. Las soluciones local y global coinciden solo si gamma es igual a uno, porque entonces esperar no tiene costo de descuento.

---



## C4 · Observación parcial

**Duración del bloque:** [calcular duración leyendo]

### C4S01 · Tema · Qué cambia al retirar la observación completa

**Duración:** [calcular duración leyendo]

**En pantalla:** POMDP igual a MDP más un modelo de sensor P(e | s).

**Hablado:**

Hasta aquí el agente conocía el estado, y la política óptima dependía de ese estado. Retiremos esa hipótesis.

Si la observación es parcial, el agente no puede ejecutar pi de s, porque no sabe si el estado actual es s. Además, la utilidad y la acción óptima dependen de la información disponible, no solo del estado físico. Definamos este problema como un proceso de decisión de Markov parcialmente observable. El entorno real es de este tipo, así que no es un caso que se pueda dejar fuera por ser más difícil.

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

### C4S03 · Tema · Sensor, creencia y actualización

**Duración:** [calcular duración leyendo]

**En pantalla:** Creencia inicial uniforme, un noveno en cada uno de los nueve estados no terminales. Actualización: la acción aplica el modelo de transición; la evidencia repondera los estados compatibles con el sensor.

**Indicación:** iniciar con la creencia uniforme. Pulsar percibir dos veces. Después ejecutar un desplazamiento. Activar la casilla real solo al final, para mostrar que la creencia es una distribución y no la casilla.

**Hablado:**

El proceso parcialmente observable conserva transición, acciones y recompensa, y añade el sensor. P de e dado s es la probabilidad de observar la evidencia e en el estado s.

En este entorno la evidencia tiene cuatro bits: muro o no muro al norte, al sur, al este y al oeste. Cada bit es correcto con probabilidad uno menos épsilon.

La información del agente es una creencia b, una probabilidad por estado. Sin información inicial, b vale un noveno en cada estado no terminal y cero en los terminales.

La actualización tiene dos pasos. La acción reparte la probabilidad de cada estado según la transición, incluido el desplazamiento lateral. La evidencia aumenta la probabilidad de los estados compatibles con lo observado y disminuye la de los demás. Es el filtrado de un estado oculto, con la acción incluida.

En la simulación la distribución inicial es uniforme. Cada observación la concentra. Cada desplazamiento la dispersa según la transición. La casilla real puede ser, o no, la de mayor probabilidad. La creencia es la distribución condicionada a las acciones y a las evidencias, no la casilla.

### C4S04 · Tema · Consecuencia para la acción y para el cálculo

**Duración:** [calcular duración leyendo]

**En pantalla:** La acción óptima depende de la creencia. El conjunto de creencias es continuo.

**Hablado:**

En el proceso totalmente observable, el estado tres dos determina la acción. En el proceso parcialmente observable, el agente puede estar en tres dos y no saberlo. Dos creencias distintas, incluso si el estado físico es el mismo, pueden hacer óptimas acciones distintas. Una acción puede alejar al agente del terminal menos uno. Otra puede elegirse porque reduce la incertidumbre, aunque no sea la acción que correspondería si el estado se conociera.

Por eso el estado del problema pasa a ser la creencia. El conjunto de creencias es continuo: hay infinitas distribuciones sobre el mismo conjunto finito de casillas. La utilidad, como función de la creencia, se puede representar por fragmentos lineales, y sobre ese espacio también hay iteración de valores y métodos en línea. Esa construcción no la desarrollamos aquí.

La consecuencia que se retiene es la siguiente. El cálculo exacto es de otro orden que el del proceso observable, y la pregunta de la acción actual sigue definida: se elige la acción que maximiza el valor esperado a partir de la creencia presente. Esa acción puede obtener recompensa o puede obtener información que mejore la creencia usada en la decisión siguiente.

---



## C5 · Análisis y aplicación en computación y comunicaciones

**Duración del bloque:** [calcular duración leyendo]

### C5S01 · Tema · Dónde aparece el cálculo

**Duración:** [calcular duración leyendo]

**En pantalla:** Política como regla de la siguiente acción. Tabla completa si el modelo cabe. Cálculo en el momento si el estado no cabe. Bandidos: anuncios, configuraciones, caché. Comunicaciones: ruta, potencia, banda. Medir también es una acción.

**Hablado:**

Hablemos de dónde aparece este cálculo en computación y en comunicaciones.

En computación, una política es la regla con la que un programa elige la siguiente acción cuando el resultado no está garantizado. La iteración de valores y la de políticas calculan esa regla si el modelo cabe en una tabla. Cuando el estado es demasiado grande, como en el tablero de diez por veinte, la decisión se calcula en el momento, mirando hacia adelante.

Los bandidos aparecen cuando hay que repartir ensayos entre opciones: qué anuncio mostrar, qué configuración probar, qué elemento conservar en una caché. Explotar repite lo que ya rindió. Explorar gasta un ensayo para saber más.

En comunicaciones, el canal no se comporta igual en cada instante. Elegir una ruta, una potencia o una banda es una acción. La recompensa puede ser el paquete que llega o el retardo que se evita. Si el nodo no observa el estado completo del enlace, solo una medida con error, el problema es el de la creencia. La acción puede enviar el paquete o puede medir de nuevo para reducir la incertidumbre. Gamma pesa el retardo: un paquete que llega tarde vale menos. La recompensa por paso castiga el intento que no termina.

---



## C6 · Conclusiones y recomendaciones

**Duración del bloque:** [calcular duración leyendo]

### C6S01 · Yo · Recapitulación

**Duración:** [calcular duración leyendo]

**En pantalla:** Los bloques de la tabla inicial, la política del entorno con r igual a menos cero punto cero cuatro, y tres recomendaciones.

**Hablado:**

Recorramos la tabla con la que abrimos.

Primero, en un entorno aleatorio la solución es una política. La recompensa por paso y gamma determinan cuál es óptima. Bellman da la utilidad de cada estado y Q da la utilidad de cada acción.

Después, la iteración de valores calcula esas utilidades y la iteración de políticas alterna evaluación y mejora. Si el número de estados impide la tabla completa, la acción se calcula desde el estado actual, mirando hacia adelante.

Luego, el índice de Gittins compara seguir en un brazo con recibir una recompensa segura. Con varias tareas y un solo recurso, la solución de cada tarea por separado no es la solución del conjunto.

Por último, si el estado no se observa, la política se define sobre la creencia.

La acción de hoy es la que esa política asigna al estado actual o, si el estado no se observa, a la creencia actual. El cálculo ya incluye la transición aleatoria y las decisiones posteriores.

La recomendación es esta. Conviene calcular la tabla completa cuando el entorno es pequeño y el modelo se conoce. Conviene calcular en el momento de la decisión cuando el número de estados no cabe. Y conviene tratar la medición como una acción, no como un dato gratis, cuando el canal o el sistema solo se observan en parte.

---



## C7 · Referencias bibliográficas

**Duración del bloque:** [calcular duración leyendo]

Sin narración. Permanencia en pantalla: unos doce segundos.

### C7S01 · Referencias

**Duración:** [calcular duración leyendo]

**En pantalla:**

- Russell, Stuart y Norvig, Peter. Artificial Intelligence: A Modern Approach. 4.ª ed. Pearson, 2020. Capítulo 16, Making Complex Decisions.
- Bellman, Richard. Dynamic Programming. Princeton University Press, 1957.
- Gittins, John C. «Bandit Processes and Dynamic Allocation Indices». Journal of the Royal Statistical Society, Series B, vol. 41, n.º 2, 1979, pp. 148-177.
- Ng, Andrew Y.; Harada, Daishi y Russell, Stuart. «Policy Invariance under Reward Transformations: Theory and Application to Reward Shaping». Proceedings of the 16th International Conference on Machine Learning, 1999.
- Whittle, Peter. Discusión de «Bandit Processes and Dynamic Allocation Indices». Journal of the Royal Statistical Society, Series B, vol. 41, n.º 2, 1979.

**Hablado:** ninguno.