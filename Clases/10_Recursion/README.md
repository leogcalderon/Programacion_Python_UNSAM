# 8. Recursión y regresión

En esta clase discutimos el concepto de recursión, proponemos algunas bases para el diseño de algoritmos recursivos y elaboramos algunos ejemplos con ellos, algunos un tanto esotéricos.

En otro orden de cosas, en la última sección damos un acercamiento práctico a las técnicas de regresión lineal y dejamos la posibilidad de profundizar más en el tema con referencias y ejercicios optativos.

En esta clase vimos el concepto de recursión y lo ejercitaste. También estudiamos un poquito (o no tan poco) sobre el ajuste y uso de regresiones lineales en Python.

### Ejercicios 10.9 (larenga.py)

        1. El triángulo de Pascal es un arreglo triangular de números que se define de la siguiente manera:
        Las filas se enumeran desde n = 0, de arriba hacia abajo. Los valores de cada fila se enumeran desde k = 0
        (de izquierda a derecha). Los valores que se encuentran en los bordes del triángulo son todos unos.
        Cualquier otro valor se calcula sumando los dos valores contiguos de la fila de arriba.
        Escribí la función recursiva pascal(n, k) que calcula el valor que se encuentra en la fila n y la columna k.

### Ejercicio 10.11 (bbin_rec.py)

        1. Escribí una función recursiva que implemente la búsqueda binaria de un elemento e en una lista ordenada lista.
        La función debe devolver simplemente True o False indicando si el elemento está o no en a lista.

### Ejercicio 10.13 (hojas_ISO.py)

        1. La norma ISO 216 especifica tamaños de papel. Es el estándar que define el popular tamaño de papel A4
        (210mm de ancho y 297mm de largo). Las hojas A0 miden 841mm de ancho y 1189mm de largo. A partir de la A0
        las siguientes medidas, digamos la A(N+1), se definen doblando al medio la hoja A(N). Siempre se miden en
        milímetros con números enteros: entonces la hoja A1 mide 594mm de ancho (y no 594.5) por 841mm de largo.

        Escribí una función recursiva que para una entrada N mayor que cero, devuelva el ancho y el largo de la hoja
        A(N) calculada recursivamente a partir de las medidas de la hoja A(N−1), usando la hoja A0 como caso base.

### Ejercicio 10.14 (precio_alquiler.py)

        1. Consideramos datos de precios (en miles de pesos) de alquiler mensual de departamentos en el barrio de
        Caballito, CABA, y sus superficies (en metros cuadrados). Queremos modelar el precio de alquiler a partir
        de la superficie para este barrio. A veces este modelo se nota con precio_alquiler ~ superficie.

        Usando la función que definimos antes, ajustá los datos con una recta.
        Graficá los datos junto con la recta del ajuste.
