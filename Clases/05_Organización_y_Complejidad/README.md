# 5. Complejidad y Organización de programas

Hasta aquí aprendimos algunas cosas básicas de Python y escribimos nuestros primeros programa. A medida que escribas programas más grandes, vas a necesitar organizarlos un poco mejor. En esta clase trataremos con mayor detalle cómo escribir funciones y módulos propios.

En la segunda mitad retomamos nuestra discusión sobre algoritmos de búsqueda e introducimos la búsqueda binaria, un algoritmo mucho más eficiente para buscar un elemento en un vector. Discutimos algunos conceptos de la teoría de la complejidad y finalmente haremos unos gráficos para comparar visualmente la cantidad de operaciones que realizan dos métodos de búsqueda.

En esta quinta clase trabajamos con funciones y creamos módulos. También aprendimos algunas nociones de complejidad de algoritmos, estudiamos la búsqueda binaria y comparamos su performance con la de la búsqueda secuencial..


### Ejercicio 5.5 (fileparse.py)

        1. Vamos a empezar por el problema simple de leer un archivo CSV para guardar los datos que contiene
        en una lista de diccionarios.

        2. Modifiquemos la función parse_csv de modo que permita al usuario elegir (opcionalmente) algunas
        columnas del siguiente modo: ```select=['nombre','cajones']```

        3. Modificá la función parse_csv() de modo que permita, opcionalmente, convertir el tipo de los datos
        recuperados antes de devolverlos.

        4. Modificá la función parse_csv() de forma que (opcionalmente) pueda trabajar con este tipo de archivos, creando
        tuplas en lugar de diccionarios cuando no haya encabezados.

### Ejercicio 5.8 (informe_funciones.py)

        1. Retomá ese programa (informe_funciones.py) y modificalo de modo que todo el procesamiento de archivos de entrada de datos
         se haga usando funciones del módulo fileparse. Para lograr éso, importá fileparse como un módulo y cambiá las funciones leer_camion()
          y leer_precios() para que usen la función parse_csv().


### Ejercicio 5.9 (costo_camion.py)

        1. Modificá el archivo costo_camion.py para que use la función informe.leer_camion() del programa informe_funciones.py.

### Ejercicio 5.12 (bbin.py)

        1. Modificando la función busqueda_binaria(lista, x) adecuadamente, definí una función donde_insertar(lista, x) de forma que
         reciba una lista ordenada y un elemento y devuelva la posición de ese elemento en la lista (si se encuentra en la lista) o
         la posición donde se podría insertar el elemento para que la lista permanezca ordenada (si no está en la lista).

        Por ejemplo: el elemento 3 podría insertarse en la posición 2 en la lista [0,2,4,6] para mantenerla ordenada. Por lo tanto,
         el llamado donde_insertar([0,2,4,6], 3) deberá devolver 2, al igual que el llamado donde_insertar([0,2,4,6], 4).

### Ejercicio 5.17  (plot_bbin_vs_bsec.py)

        1. Usando experimento_secuencial_promedio(lista,m,k) como base, escribí una función experimento_binario_promedio(lista,m,k) 
        que cuente la cantidad de comparaciones que realiza en promedio (entre k experimentos elementales) la búsqueda binaria
        sobre la lista pasada como parámetro.

        2. Graficá los resultados de estos experimentos para listas de largo entre 1 y 256.

        3. Graficá ambas curvas en una misma figura, nombrando adecuadamente las curvas, los ejes y la figura completa.
