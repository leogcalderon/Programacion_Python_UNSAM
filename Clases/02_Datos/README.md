# 2. Trabajando con datos

Para escribir programas útiles, necesitamos aprender a trabajar con datos. En esta clase vas a escribir un programa que lee un archivo de datos en formato csv y realiza un cálculo simple. Vas a aprender a estructurar tu código creando funciones. También introducimos las estructuras de datos elementales de Python que nos faltan: tuplas, conjuntos y diccionarios y profundizamos un poco más en las listas y sus usos.

Discutimos el problema de la búsqueda de un elemento en un vector e introducimos la búsqueda lineal.

### Ejercicio 2.8 (camion_commandline.py)

        1. Escribí un programa llamado costo_camion.py que abra el archivo, lea las líneas, y calcule el precio pagado por los cajones cargados en el camión.

        2. Transformá el programa costo_camion.py en una función costo_camion(nombre_archivo). Esta función recibe un nombre de archivo como entrada, lee la información sobre los cajones que cargó el camión y devuelve el costo de la carga de frutas como una variable de punto flotante.

        3. ¿Qué pasa si intentás usar la función costo_camion() con un archivo que tiene datos faltantes? Modificá el programa costo_camion.py para que atrape la excepción, imprima un mensaje de aviso (warning) y continúe procesando el resto del archivo.

        4. Modificá tu programa costo_camion.py para que use el módulo csv para leer los archivos CSV.

        5. Copiá el contenido de costo_camion.py a un nuevo archivo llamado camion_commandline.py que incorpore la lectura de parámetros por línea de comando.

### Ejercicio 2.15 (informe.py)

        1. Creá un nuevo archivo informe.py. En este archivo, definí una función leer_camion(nombre_archivo) que abre un archivo con el contenido de un camión, lo lee y devuelve la información como una lista de tuplas.

        2. Tomá la función que escribiste en el ejercicio anterior y modificala para representar cada cajón del camión con un diccionario en vez de una tupla. En este diccionario usá los campos "nombre", "cajones" y "precio" para representar las diferentes columnas del archivo de entrada.

        3. Escribí una función leer_precios(nombre_archivo) que a partir de un conjunto de precios como éste arme un diccionario donde las claves sean los nombres de frutas y verduras, y los valores sean los precios por cajón.

        4. Juntá todo el trabajo que hiciste recién en tu programa informe.py (usando las funciones leer_camion() y leer_precios()) y completa el programa para que con los precios del camión y los de venta en el negocio calcule lo que costó el camión, lo que se recaudo con la venta, y la diferencia. ¿Hubo ganancia o pérdida? El programa debe imprimir por pantalla un balance con estos datos.

### Ejercicio 2.22 (arboles.py)

        1. Definí una función leer_parque(nombre_archivo, parque) que abra el archivo indicado y devuelva una lista de diccionarios con la información del parque especificado. La función debe devolver, en una lista un diccionario con todos los datos por cada árbol del parque elegido (recordá que cada fila del csv es un árbol).

        2. Escribí una función especies(lista_arboles) que tome una lista de árboles como la generada en el ejercicio anterior y devuelva el conjunto de especies (la columna 'nombre_com' del archivo) que figuran en la lista.

        3. Escribí una función contar_ejemplares(lista_arboles) que, dada una lista como la que generada con leer_parque(), devuelva un diccionario en el que las especies (recordá, es la columna 'nombre_com' del archivo) sean las claves y tengan como valores asociados la cantidad de ejemplares en esa especie en la lista dada.

        4. Escribí una función obtener_alturas(lista_arboles, especie) que, dada una lista de árboles como la anterior y una especie de árbol (un valor de la columna 'nombre_com' del archivo), devuelva una lista con las alturas (columna 'altura_tot') de los ejemplares de esa especie en la lista.

        5. Escribí una función obtener_inclinaciones(lista_arboles, especie) que, dada una especie de árbol y una lista de árboles como la anterior, devuelva una lista con las inclinaciones (columna 'inclinacio') de los ejemplares de esa especie.

        6. Combinando la función especies() con obtener_inclinaciones() escribí una función especimen_mas_inclinado(lista_arboles) que, dada una lista de árboles devuelva la especie que tiene el ejemplar más inclinado y su inclinación.

        7. Volvé a combinar las funciones anteriores para escribir la función especie_promedio_mas_inclinada(lista_arboles) que, dada una lista de árboles devuelva la especie que en promedio tiene la mayor inclinación y el promedio calculado.

### Ejercicio 2.33 (tabla_informe.py)

### Ejercicio 2.34 (tablamult.py)
