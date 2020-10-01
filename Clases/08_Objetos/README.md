# 8. Clases y objetos

En esta clase vamos a meternos con la programación orientada a objetos. Vamos a ver los conceptos de clases y objetos. Hasta ahora los programas que escribimos usaron sólo tipos de datos nativos de Python, con la instrucción class vamos a definir nuevas clases. Vamos a ir más allá y a hablar del concepto de herencia, una herramienta comúnmente usada para escribir programas extensibles. Por último, vamos a referirnos a algunos métodos especiales de los objetos de Python.


### Ejercicios 8.8 (informe.py)

        1. Creá un archivo llamado lote.py y adentro definí una clase llamada Lote que represente un lote de cajones de una misma fruta.
        Definila de modo que cada instancia de la clase Lote (es decir, cada objeto lote) tenga los atributos nombre, cajones, y precio.
        Agregá los métodos costo() y vender() a tu objeto Lote. Modificá la función leer_camion() en el programa informe.py de modo que
        lea un archivo con el contenido de un camion y devuelva una lista de instancias de Lote

        2. Imaginá que necesitás que la función imprimir_informe() pueda exportar el informe en una variedad de formatos: texto plano,
        HTML, CSV ó XML. Podrías escribir una función enorme que resuelva todos los casos, pero resultaría en código repetido, y difícil
        de mantener. Esta es una oportunidad perfecta para usar herencia de objetos. Modificá tu programa informe.py de modo que la
        función informe_camion() acepte un parámetro opcional que especifique el formato de salida deseado.

### Ejercicio 8.9 (lote.py)

        1. Modificá el objeto Lote que definiste en lote.py (del Ejercicio 8.1) de modo que el método __repr__() genere una salida más agradable.

### Ejercicio 8.11 (canguros_buenos.py)

        1. Este ejercicio está relacionado con un error muy común en Python. Escribí una definición de una clase Canguro que tenga:
        Un método __init__ que inicializa un atributo llamado contenido_marsupio como una lista vacía.
        Un método llamado meter_en_marsupio que, dado un objeto cualquiera, lo agregue a la lista contenido_marsupio.
        Un método __str__ que devuelve una representación como cadena del objeto Canguro y de los contenidos de su marsupio.
        Probá tu código creando dos objetos, madre_canguro y cangurito y guardá en el marsupio de la madre algunos objetos y al cangurito.

### Ejercicio 8.12 (torre_control.py)

        1. Una cola es una estructura de datos. Se caracteriza por contener una secuencia de elementos y dos operaciones: encolar y desencolar.
        La primera, encolar, agrega un elemento al final de la secuencia que contiene la cola. Desencolar, por su parte, devuelve el primer
        elemento de la secuencia y lo elimina de la misma.

        Usando un par de objetos de la clase Cola, escribí una nueva clase llamada TorreDeControl que modele el trabajo de una torre
        de control de un aeropuerto con una pista de aterrizaje. Los aviones que están esperando para aterrizar tienen prioridad sobre
        los que están esperando para despegar.
