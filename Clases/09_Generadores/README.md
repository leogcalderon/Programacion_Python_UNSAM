# 8. Generadores e iteradores

Programar es básicamente escribir condicionales, ciclos y asignaciones de variables. Aunque no de cualquier forma.

Los ciclos, ya sean ciclos while o iteraciones for son una de las estructuras más ubicuas en cualquier lenguaje. Los programas hacen muchas iteraciones para procesar listas, leer archivos, buscar en bases de datos y demás.

Una de las características más poderosas de Python es la capacidad de redefinir la iteración mediante las llamadas "funciones generadoras". En esta sección veremos de que se trata ésto. Hacia el final vas a escribir programas que procesan datos en tiempo real, a medida que son generados.

En esta clase aprendiste sobre generadores e iteradores, dos conceptos muy interesantes de Python. Viste que el mecanismo de iteración es una forma de dialogar con un objeto. Además, aprendiste los métodos que necesitás implementar para que un objeto que creaste sea iterable.

Discutimos también las ventajas de construír un programa con estos conceptos. Los programas resultan mas versátiles, modulares, y ligeros. Como con el concepto de comprensión de listas, podés usar la sintaxis de comprensión para construír un iterable: una expresión sobre la cual podés iterar sin necesidad de almacenar todos los elementos posibles en una lista ni escribir una función para calcularlos.

Por último, viste la ventaja de crear pipelines: estructuras de procesamiento de datos configurables en vuelo, altamente modulares.

### Ejercicios 9.2 (informe.py)

        1. En un nuevo archivo llamado camion.py, definí la clase Camion

        2. Modificá la función leer_camion() en informe.py de modo que cree una instancia de Camion.

### Ejercicio 9.3 (camion.py)

        1. Cuando hagas clases que sean recipientes ó contenedores de estructuras de datos vas a necesitar
         que hagan algo más que simplemente iterar. Probá modificar la clase Camion de modo que tenga algunos
         de los "métodos mágicos" que mencionamos en la Sección 8.3. (__len__ , __getitem__, __contains__, ...)

### Ejercicio 9.7 (vigilante.py)

        1. Modificá el código del Ejercicio 9.5 de modo que la lectura del archivo esté resuelta por una única
        función generadora vigilar() a la que se le pasa un nombre de archivo como parámetro.
        2. Modificá el programa vigilante.py para que sólo informe las líneas que tienen precios de lotes incluídos
        en un camión, e ignore el resto de los productos

### Ejercicio 9.12 (ticker.py)

        1. En el programa ticker.py (esta versión te vamos a pedir que la entregues) escribí una función
        ticker(camion_file, log_file, fmt) que cree un indicador en tiempo real para un camión, archivo log,
        y formato de tabla de salida particulares.
