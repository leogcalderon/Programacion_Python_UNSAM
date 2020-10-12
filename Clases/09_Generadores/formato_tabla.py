class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        pass

    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        pass

class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()

class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))

class FormatoTablaHTML(FormatoTabla):
    '''
    Generar una tabla en formato HTML
    '''
    def encabezado(self, headers):
        result = '<tr>'
        for h in headers:
            result += f'<th>{h}</th>'
        result += '</tr>'
        print(result)

    def fila(self, data_fila):
        result = '<tr>'
        for d in data_fila:
            result += f'<td>{d}</td>'
        result += '</tr>'
        print(result)

def crear_formateador(nombre):
    if nombre.lower() == 'txt':
        return FormatoTablaTXT()
    elif nombre.lower() == 'csv':
        return FormatoTablaCSV()
    elif nombre.lower() == 'html':
        return FormatoTablaHTML()
    else:
        raise ValueError("Nombre debe ser 'txt', 'csv' o 'html'")
