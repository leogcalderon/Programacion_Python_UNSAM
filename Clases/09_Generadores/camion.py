from collections import Counter

class Camion:

    def __init__(self, lotes):
        self._lotes = lotes

    def __iter__(self):
        return self._lotes.__iter__()

    def precio_total(self):
        return sum([l.costo() for l in self._lotes])

    def contar_cajones(self):
        cantidad_total = Counter()

        for l in self._lotes:
            cantidad_total[l.nombre] += l.cajones

        return cantidad_total

    def __len__(self):
        return len(self._lotes)

    def __getitem__(self, index):
        return self._lotes[index]

    def __contains__(self, nombre):
        return any([lote.nombre == nombre for lote in self._lotes])

    def __str__(self):
        return f'Camion con {len(self._lotes)} lotes.'
