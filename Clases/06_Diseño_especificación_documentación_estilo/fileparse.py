import gzip
import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    '''if not has_headers and select:
        raise RuntimeError('Para seleccionar, necesito encabezados')'''

    if nombre_archivo.endswith('.csv'):
        lines = open(nombre_archivo)

    elif nombre_archivo.endswith('tar.gz'):
        lines = gzip.open(nombre_archivo, 'rt')

    else:
        lines = lines

        if has_headers:
            # Lee los encabezados
            headers = next(lines)
            records = []

            #Indices seleccionados
            if select:
                idx = [headers.index(col) for col in select]
                headers = select
            else:
                idx = []

            row_n = 1

            for row in lines:
                try:
                    if not row:    # Saltea filas sin datos
                        continue
                    if idx:        # Si hay indices seleccionados
                        row = [row[i] for i in idx]

                    if types:      # Si hay tipos especificados
                        row = [func(val) for func,val in zip(types,row)]

                    record = dict(zip(headers,row))
                    records.append(record)

                except:
                    pass

                row_n += 1
        else:
            records = []
            for row in lines:
                if not row:
                    continue
                if types:      # Si hay tipos especificados
                    row = [func(val) for func,val in zip(types,row)]

                row = tuple(i for i in row)
                records.append(row)

    return records
