#Mi clase
class Canguro:
    def __init__(self, nombre):
        self.nombre = nombre
        self.contenido_marsupio = []

    def meter_en_marsupio(self, elemento):
        self.contenido_marsupio.append(elemento)

    def __str__(self):
        if len(self.contenido_marsupio) > 0:
            strings = 'El canguro tiene:\n'
            for objeto in self.contenido_marsupio:
                strings += '- ' + objeto.__repr__() + '\n'
            return strings
        else:
            return 'El canguro no tiene nada en su marsupio'

#Clase sin bug
'''
class Canguro:
    """Un Canguro es un marsupial."""

    def __init__(self, nombre):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        self.contenido_marsupio = []   #Aca estaba el error, se necesita inicializar el atributo como una lista vacia.

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + " tiene en su marsupio:" ]
        for obj in self.contenido_marsupio:
            s = "   " + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)
'''
