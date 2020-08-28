# 4. Aleatoridad

En esta clase introducimos conceptos y técnicas relacionadas al azar. La aleatoriedad puede ser un gran aliado para realizar cálculos de fenómenos estocásticos pero también de fenómenos deterministas. Introducimos los números pseudoaleatorios, así como el módulo numpy y sus métodos más sencillos.

Presentamos una versión libre de un ejercicio lindísimo del curso Exactas Programa que te guía para que resuelvas la pregunta ¿cuántos paquetes de figuritas tengo que comprar para llenar un álbum? con un enfoque estadístico usando el método de Montecarlo.

Introducimos los arrays de la biblioteca numpy en una sección un poco técnica pero importante para el futuro.

A lo largo de la clase iremos haciendo nuestros primeros gráficos en Python. Cerramos introducuiendo los scatterplots que permiten visualizar dos variables en simultaneo y facilitan el análisis exploratorio de datos.

En esta cuarta clase trabajamos con la generación de números (pseudo)aleatorios, el uso de la biblioteca NumPy y algunos ejemplos de aplicación de estos conceptos. También aprendimos a hacer algunos gráficos elementales en Python.

### Ejercicio 4.7 (generala.py)

        1. Queremos estimar la probabilidad de obtener una generala servida en una tirada de dados. 
        Podemos hacer la cuenta usando un poco de teoría de probabilidades, o podemos simular que tiramos
        los dados muchas veces y ver cuántas de esas veces obtuvimos cinco dados iguales. En este ejercicio 
        vamos a usar el segundo camino. Escribí una función tirar() que devuelva una lista con cinco dados 
        generados aleatoriamente. Escribí otra función llamada es_generala(tirada) que devuelve True si y sólo
        si los cinco dados de la lista tirada son iguales.


        2. Si uno juega con las reglas originales (se puede volver a tirar algunos de los cinco dados hasta dos 
        veces, llegando hasta a tres tiradas en total) siguiendo una estrategia que intente obtener generala 
        (siempre guardar los dados que más se repiten y tirar nuevamente los demás) es más probable obtener 
        una generala que si sólo consideramos la generala servida. Escribí un programa que estime la probabilidad 
        de obtener una generala en las tres tiradas de una mano y guardalo en un archivo generala.py.

### Ejercicio 4.8 (envido.py)

        1. Teniendo en cuenta las reglas del Truco, estimá la probabilidad de obtener 31, 32 o 33 puntos de envido
        en una mano. ¿Son iguales estas tres probabilidades? ¿Por qué?
        *Observación: como corresponde, en esta materia jugamos al truco sin flor.*

### Ejercicio 4.13 (termometro.py)

        1. Supongamos que una persona se compra un termómetro que mide la temperatura con un error aleatorio normal 
        con media 0 y desvío estándar de 0.2 grados (error gaussiano). Si la temperatura real de la persona es de 37.5 
        grados, simulá usando normalvariate() (con mu y sigma adecuados) n = 99 valores medidos por el termómetro. 
        Imprimí los valores obtenidos en las mediciones de temperatura simuladas y luego, como resumen, cuatro líneas 
        indicando el valor máximo, el mínimo, el promedio y la mediana de estas n mediciones. Guardá tu programa en el 
        archivo termometro.py.

        2. Ampliá el código de termometro.py que escribiste para que guarde el vector con las temperaturas simuladas en el
        directorio Data de tu carpeta de ejercicios, en un archivo llamado Temperaturas.npy. Hacé que corra 999 veces en
        lugar de solo 99.

### Ejercicio 4.14 (plotear_temperaturas.py)

        1. Escribí un archivo plotear_temperaturas.py que lea el archivo de datos Temperaturas.npy con 999 mediciones simuladas 
        que creaste recién y hacé un histograma de las temperaturas simuladas.

### Ejercicio 4.4  (figuritas.py)


#### Solo con figuritas

        1. Datos:
            - Álbum con 670 figuritas.
            - Cada figurita se imprime en cantidades iguales y se distribuye aleatoriamente.
            - Cada paquete trae cinco figuritas.

          Vamos a representar un álbum de n figuritas utilizando un vector de NumPy con posiciones numeradas
          de 0 a n-1. Cada posición representa el estado de una figurita con dos valores: 0 para indicar que aún 
          no la conseguimos y 1 para indicar que si.

        2. Implementá la función crear_album(figus_total) que devuelve un álbum (vector) vacío con figus_total 
        espacios para pegar figuritas.

        3.  Implementá una función comprar_figu(figus_total) que reciba el número total de figuritas que tiene el
        álbum (dado por el parámetro figus_total) y devuelva un número entero aleatorio que representa la figurita
        que nos tocó.

        4. Implementá la función cuantas_figus(figus_total) que, dado el tamaño del álbum (figus_total), genere un 
        álbum nuevo, simule su llenado y devuelva la cantidad de figuritas que se debieron comprar para completarlo.

        5. Ejecutá n_repeticiones = 1000 veces la función anterior utilizando figus_total = 6 y guardá en una lista 
        los resultados obtenidos en cada repetición. Con los resultados obtenidos estimá cuántas figuritas hay que comprar, 
        en promedio, para completar el álbum de seis figuritas.

        6. Calculá n_repeticiones=100 veces la función cuantas_figus(figus_total=670) y guardá los resultados obtenidos 
        en cada repetición en una lista. Con los resultados obtenidos estimá cuántas figuritas hay que comprar, en promedio,
        para completar el álbum (de 670 figuritas).

#### Solo con paquetes

        1. Simulá la generación de un paquete con cinco figuritas, sabiendo que el álbum es de 670. Tené en cuenta que, 
        como en la vida real, puede haber figuritas repetidas en un paquete.

        2. Implementá una función comprar_paquete(figus_total, figus_paquete) que, dado el tamaño del álbum (figus_total) 
        y la cantidad de figuritas por paquete (figus_paquete), genere un paquete (vector) de figuritas al azar.

        3. Implementá una función cuantos_paquetes(figus_total, figus_paquete) que dado el tamaño del álbum y la cantidad 
        de figus por paquete, genere un álbum nuevo, simule su llenado y devuelva cuántos paquetes se debieron comprar para completarlo.

        4. Calculá n_repeticiones = 100 veces la función cuantos_paquetes, utilizando figus_total = 670, figus_paquete = 5. 
        Guarda los resultados obtenidos en una lista y calculá su promedio. Si te da la compu, hacelo con 1000 repeticiones.

### Ejercicio 4.31 (arboles.py)

        1. Usando tu trabajo en el Ejercicio 3.19, generá un histograma con las alturas de los Jacarandás en el dataset.

        2. Usando como base tu trabajo del Ejercicio 3.20, vas a generar un scatterplot para visualizar la relación 
        entre diámetro y alto de los Jacarandás del dataset.
