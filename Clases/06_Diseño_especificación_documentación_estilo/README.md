# 6. Diseño, especificación, documentación y estilo.

En este curso queremos que aprendas a escribir un script que te resuelva un problema computacional. Pero también queremos que puedas escribir adecuadamente programas más grandes, que los puedas compartir y volver a usar vos misme unos años más tarde.

Por eso insistimos con algunos temas de estilo, documentación, especificiación y diseño que ya hemos comentado anteriormente y sobre los que volveremos en esta clase. Uno de ellos es que es conveniente administrar los errores; seguiremos hablando sobre las formas adecuadas de hacerlo y porqué no conviene hacerlo de más. También se vuelve indispensable estructurar adecuadamente el código y aprender a definir una función main. Vamos a continuar con nuestras discusiones sobre el diseño de algoritmos y sus estructuras de datos asociadas. También queremos que aprendas algunos conceptos elementales sobre especificación de problemas. Son procesos de abstracción que nos ayudan a pensar con mayor claridad. Al especificar un problema con precondiciones y poscondiciones estamos definiendo qué es lo que debe pasar en una función, por ejemplo (aunque en ningún momento decimos cómo debe pasar esto). Una especificación es como un contrato y podemos definir varias funciones que cumplan el contrato, y cada una puede resolverlo a su manera.

Finalmente, daremos un poco más sistemáticamente algunos conceptos de la biblioteca matplotlib, incluyendo el manejo de figuras y subplots.


### Ejercicios 6.4/6.5 (fileparse.py/informe.py)

        1. La función parse_csv() que escribiste en el Ejercicio 5.6 admite seleccionar algunas columnas por el usuario,
         pero eso sólo funciona si el archivo de entrada tiene encabezados.Modifcá tu código para que lance una
         excepción en caso que ambos parámetros select y has_headers = False sean pasados juntos.

        2. Modificá la función parse_csv() de modo que atrape todas las excepciones de tipo ValueError generadas durante
         el armado de los registros a devolver e imprima un mensaje de advertencia para las filas que no pudieron ser
         convertidas. Estas filas no deben ser procesadas (ya que no se puede hacer adecuadamente), y deben ser omitidas
         en el output de la función.

        3. Modificá parse_csv() de modo que le usuarie pueda silenciar los informes de errores en el parseo de los
        datos que agregaste antes.

        4. Modificá la función parse_csv() de forma que (opcionalmente) pueda trabajar con este tipo de archivos, creando
        tuplas en lugar de diccionarios cuando no haya encabezados.

        5. Usando sys y __main__, agregá a tu programa informe.py una función main() que tome una lista de parámetros en la
        línea de comandos y produzca la misma salida que antes.

        6. Análogamente, modificá el archivo costo_camion.py para que incluya una función similar main().

        7. Actualmente la función solicita el nombre de un archivo, pero podés hacer el código más flexible. Modificá la función
        de modo que funcione con cualquier objeto ó iterable que se comporte como un archivo.

### Ejercicio 6.8 (documentacion.py)

        1. Para cada una de las funciones dadas:
          - Pensá cuál es el contrato de la función.
          - Agregale la documentación adecuada.
          - Comentá el código si te parece que aporta.
          - Detectá si hay invariantes de ciclo y comentalo al final de la función


### Ejercicio 5.9 (costo_camion.py)

        1.
