# 3. Algoritmos sobre listas y comprensión de listas

En esta clase discutimos los tipos de errores que pueden aparecer en un programa y les proponemos una serie de ejercicios donde tienen que escribir algoritmos que operen sobre listas. Luego introducimos la comprensión de listas, un concepto muy hermoso y pythonesco. Cerramos la clase con una discusión sobre el concepto de objeto que subyace al lenguaje.

En esta tercera clase vimos algo más sobre errores, el manejo de lista y la creación de listas por comprensión.

### Ejercicio 3.1 y siguientes (solucion_de_errores.py)

        1. Determiná los errores de los siguientes códigos y corregilos en un archivo 
        solucion_de_errores.py comentando brevemente los errores. ¿Qué tipo de errores tiene cada uno?
        
        
### Ejercicio 3.6 y el Ejercicio 3.7 (busqueda_en_listas.py)

        1. El algoritmo de búsqueda lineal tiene un comportamiento proporcional a la longitud de 
        la lista involucrada, o que es un algoritmo lineal. En este primer ejercicio tenés que 
        escribir una función buscar_u_elemento() que reciba una lista y un elemento y devuelva 
        la posición de la última aparición de ese elemento en la lista (o -1 si el elemento no pertenece a la lista).
        
        2. Agregale a tu programa busqueda_en_listas.py una función buscar_n_elemento() que 
        reciba una lista y un elemento y devuelva la cantidad de veces que aparece el elemento 
        en la lista. Probá también esta función con algunos ejemplos.
        
        3. Agregale a tu archivo busqueda_en_listas.py una función maximo() que busque el valor máximo 
        de una lista de números positivos. Si te dan ganas, agregá una función minimo() al archivo.  ( NO USAR max() )
        

### Ejercicio 3.8 (invlista.py)

        1. Escribí una función invertir_lista(lista) que dada una lista devuelva otra que tenga los 
        mismos elementos pero en el orden inverso. Es decir, el que era el primer elemento de la lista 
        de entrada deberá ser el último de la lista de salida y análogamente con los demás elementos.


### Ejercicio 3.9 (propaga.py)
        
        1. Imaginate una fila con varios fósforos uno al lado del otro. Los fósforos pueden estar en 
        tres estados: nuevos, prendidos fuego o ya gastados (carbonizados). Representaremos esta 
        situación con una lista L con un elemento por fósforo, que en cada posición tiene un 0 (nuevo), 
        un 1 (encendido) o un -1 (carbonizado). El fuego se propaga inmediatamente de un fósforo encendido 
        a cualquier fósoforo nuevo que tenga a su lado. Los fósforos carbonizados no se encienden nuevamente.

        Escribí una función llamada propagar que reciba un vector con 0's, 1's y -1's y devuelva un 
        vector en el que los 1's se propagaron a sus vecinos con 0. Guardalo en un archivo propaga.py.


### Ejercicio 3.20 (arboles2.py)