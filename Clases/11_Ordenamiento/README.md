# 11. Ordenamiento

Ordenar una lista de números es una de las tareas fundamentales que realiza un ordenador (también llamado computadora). Los algoritmos conceptualmente más sencillos tienen una complejidad computacional (en el peor caso) que crece de forma cuadrática (n^2) con la longitud, n, de la lista a ordenar. Veremos en detalle dos algoritmos sencillos: el algoritmo de selección y el de inserción y luego divide and conquer que lleva a la idea de merge sort.

### Ejercicios 11.2 (burbujeo.py)

        1. El ordenamiento por burbujeo se basa en una idea bastante sencilla. El algoritmo
        compara dos elementos contiguos de la lista y, si el orden es adecuado, los deja como
        están, si no, los intercambia. La repetición de este paso elemental (una burbuja) a lo
        largo de la lista (recorriéndola desde el comienzo hasta el final) garantiza llevar el
        mayor elemento al final de la lista, pero no garantiza que el menor elemento haya quedado
        en el primer lugar. De hecho, el menor elemento solo se mueve un paso hacia la izquierda
        en una recorrida completa de la lista. Es por esto que estas recorridas se repiten sucesivas
        veces (¿cuántas hace falta?) de manera de garantizar que el lista quede completamente ordenada.

        Como en el primer paso tenemos la garantía de que el mayor elemento quedó al final de la lista,
        la segunda recorrida puede evitar llegar hasta esa última posición. Así, cada recorrida es más
        corta que la anterior. En cada recorrida se comparan todos los pares de elementos sucesivos
        (en el rango correspondiente) y se intercambian si no están ordenados.

        Programá una función ord_burbujeo(lista) que implemente este método de ordenamiento.
        ¿Cuántas comparaciones realiza esta función en una lista de largo n?

### Ejercicio 11.7 (comparaciones_ordenamiento.py)

        1. Vamos a tratar de comparar visualmente la cantidad de comparaciones que hacen estos algoritmos
        para diferentes largos de listas. Hacé un programa comparaciones_ordenamiento.py que para N entre
        1 y 256 genere una lista de largo N con números enteros del 1 al 1000, calcule la cantidad de comparaciones
        realizadas por cada método y guarde estos resultados en tres vectores de largo 256: comparaciones_seleccion,
        comparaciones_insercion y comparaciones_burbujeo.

        Graficá estos tres vectores. Si las curvas se superponen, graficá una de ellas con línea punteada para
        poder verlas bien. ¿Cómo dirías que crece la complejidad de estos métodos? ¿Para cuáles depende de la
        lista a ordenar y para cuáles solamente depende del largo de la lista?

        2. Modificá la función merge_sort para que también devuelva la cantidad de comparaciones hechas.
        Rehacé el último ejercicio de la sección anterior (Ejercicio 11.5) incorporando el merge sort a la comparación y al gráfico.

### Ejercicio 11.8 (time_ordenamiento.py)

        1. Juntá en el archivo time_ordenamiento.py los métodos de búsqueda del Ejercicio 11.7.
        Antes de empezar el experimento, eliminá de las funciones a medir todo código no esencial,
        en particular los prints para debug. Consumen tiempo y no son parte del algoritmo. También
        eliminá las cuentas de comparaciones, que ahora no son necesarias.
        Escribí un experimento que, tal como hiciste en el Ejercicio 11.5, para N entre 1 y 256
        genere una lista de largo N con números enteros del 1 al 1000, calcule el tiempo que tarda
        cada método en ordenar la lista y guarde estos resultados en vectores de largo 256.
        Asegurate de evaluar todos los métodos de ordenamiento con las mismas listas (siempre usá
        copias para no reordenar listas ya ordenadas) y guardar esta información para poder mostrarla
        o usarla.
        Graficá los datos de tiempos de ejecución en función de longitudes de la lista.
        ¿Coinciden las curvas con lo que habías predicho estimando el número de operaciones?


### Ejercicio 11.10 (iris_seaborn.py)

        1. Plotea con seaborn los datos del dataset de iris.
