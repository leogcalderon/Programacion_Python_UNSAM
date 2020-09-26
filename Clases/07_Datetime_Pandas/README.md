# 6. Fechas, carpetas y Pandas

En esta clase introducimos el módulo datetime para manejar datos relacionados con el tiempo (Sección 1) y un par de funciones del módulo os para leer directorios, procesar archivos y realizar algunas tareas relacionadas con el sistema operativo (Sección 2). Luego te proponemos integrar esto para hacer un script que corra desde línea de comandos y te permita ordenar los archivos de cierto tipo (Sección 3).

En la segunda mitad introducimos el módulo Pandas y el tipo DataFrame así como algunos de sus métodos elementales. Usamos pandas para analizar dos datasets de Arbolado Porteño graficando algunos de sus datos. En esta parte tenés que comparar caracterísiticas de árboles que crecen en los parques con otros que crecen en las veredas (Sección 4 y ejercicio de revisión por pares).

En la parte, Sección 5, te proponemos análizar ondas de mareas en el Río de la Plata como excusa para introducir el procesamiento de series temporales. Nos metemos un poco en temas específicos con una última parte optativa que incluye un breve análsis de la transformada de Fourier para medir el tiempo que tarda esta onda de marea en trasladarse de un puerto a otro.


### Ejercicios 7.1 (vida.py)

        1. Escribí una función a la que le pasás tu fecha de nacimiento como cadena en formato 'dd/mm/AAAA'
        (día, mes, año con 2, 2 y 4 dígitos, separados con barras normales) y te devuelve la cantidad de segundos
        que viviste (asumiendo que naciste a las 00:00hs de tu fecha de nacimiento).

### Ejercicio 7.5 (listar_imgs.py)

        1. Escribí un programa que dado un directorio, imprima en pantalla los nombres de todos los archivos .png que se
        encuentren en algún subdirectorio del él. Observación: Al final, tu script debería poder ejecutarse desde la línea
        de comandos recibiendo como parámetro el directorio a leer original. En la Sección 6.2 dimos un modelo de script que
        te puede servir.


### Ejercicio 7.9 (arbolado_parques_veredas.py)

        1. Al comienzo de la materia estuvimos trabajando con el dataset de árboles en parques. Ahora estuvimos analizando otro dataset:
         el de árboles en veredas. Ahora queremos estudiar si hay diferencias entre los ejemplares de una misma especie según si crecen en un sitio o en otro.
         Queremos hacer un boxplot del diámetro a la altura del pecho para las Tipas (su nombre científico es tipuana tipu),
         que crecen en ambos tipos de ambiente. Para eso tendremos que juntar datos de dos bases de datos diferentes.

        Nos vamos en meter en un lío. El GCBA usa en un dataset 'altura_tot', 'diametro' y 'nombre_cie' para las alturas, diámetros
        y nombres científicos de los ejemplares, y en el otro dataset usa 'altura_arbol', 'diametro_altura_pecho' y 'nombre_cientifico'
         para los mismos datos.

        Es más, los nombres científicos varían de un dataset al otro. 'Tipuana Tipu' se transforma en 'Tipuana tipu' y 'Jacarandá mimosifolia'
         en 'Jacaranda mimosifolia'. Obviamente son cambios menores pero suficientes para desalentar al usuarie desprevenide.

        - Abrí ambos datasets a los que llamaremos df_parques y df_veredas.

        - Para cada dataset armate otro seleccionando solamente las filas correspondientes
        a las tipas (llamalos df_tipas_parques y df_tipas_veredas, respectivamente) y las
        columnas correspondientes al diametro a la altura del pecho y alturas. Hacelo como copias
        (usando .copy() como hicimos más arriba) para poder trabajar en estos nuevos dataframes
        sin modificar los dataframes grandes originales.
        Renombrá las columnas que muestran la altura y el diámetro a la altura del pecho para
        que se llamen igual en ambos dataframes, para ello explorá el comando rename.

        - Agregale a cada dataframe (df_tipas_parques y df_tipas_veredas) una columna llamada
        'ambiente' que en un caso valga siempre 'parque' y en el otro caso 'vereda'.

        - Juntá ambos datasets con el comando df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques]).
        De esta forma tenemos en un mismo dataframe la información de las tipas distinguidas por ambiente.

        - Creá un boxplot para los diámetros a la altura del pecho de la tipas distinguiendo los ambientes
        (boxplot('diametro_altura_pecho',by = 'ambiente')).

        - Repetí para alturas.

        - ¿Qué tendrías que cambiar para repetir el análisis para otras especies? ¿Convendría definir una función?
