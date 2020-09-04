import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)

        if has_headers:
            # Lee los encabezados
            headers = next(rows)
            records = []

            #Indices seleccionados
            if select:
                idx = [headers.index(col) for col in select]
                headers = select
            else:
                idx = []

            for row in rows:
                if not row:    # Saltea filas sin datos
                    continue
                if idx:        # Si hay indices seleccionados
                    row = [row[i] for i in idx]

                if types:      # Si hay tipos especificados
                    row = [func(val) for func,val in zip(types,row)]

                record = dict(zip(headers,row))
                records.append(record)

        else:
            records = []
            for row in rows:
                if not row:
                    continue
                if types:      # Si hay tipos especificados
                    row = [func(val) for func,val in zip(types,row)]

                row = tuple(i for i in row)
                records.append(row)

    return records
