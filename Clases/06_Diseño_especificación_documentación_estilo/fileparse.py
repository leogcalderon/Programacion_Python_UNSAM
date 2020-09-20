import csv

def parse_csv(lines, select = None, types = None, has_headers = True, silence_errors = True):
    '''
    Parsea un archivo CSV en una lista de registros
    --------------------------------
    select = lista de columnas a seleccionar
    types = lista con tipos de datos de cada columna
    has_header = boolean
    silence_errors = boolean
    '''


    if not silence_errors:
        '''Manejo de excepcion 1'''
        if not has_headers and select:
            raise RuntimeError("Para seleccionar, necesito encabezados.")

    '''Duck taping'''
    rows = []
    for row in lines:
        if row.endswith('\n'):
            rows.append(row[:-1])
        else:
            rows.append(row)

    if has_headers:
        # Lee los encabezados
        headers = rows[0].split(',')
        records = []

        #Indices seleccionados
        if select:
            idx = [headers.index(col) for col in select]
            headers = select
        else:
            idx = []

        for i,row in enumerate(rows[1:]):

            '''Manejo de excepcion 2'''
            try:
                if not row:    # Saltea filas sin datos
                    continue

                row = row.split(',')

                if idx:        # Si hay indices seleccionados
                    row = [row[i] for i in idx]

                if types:      # Si hay tipos especificados
                    row = [func(val) for func,val in zip(types,row)]

                record = dict(zip(headers,row))
                records.append(record)

            except ValueError as e:
                if not silence_errors:
                    print(f'Row {i+1}: No pude convertir',row)
                    print(f'Row {i+1}: Motivo:',e)
                else:
                    pass

    else:
        records = []
        for row in rows:
            if not row:
                continue
            if types:
                row = [func(val) for func,val in zip(types,row)]

            row = tuple(i for i in row)
            records.append(row)

    return records
