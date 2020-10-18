def hojas_ISO(N, ancho = 841, largo = 1189):

    if N == 0:
        return ancho, largo

    elif N == 1:
        return largo/2, ancho

    else:
        return hojas_ISO(N - 1, largo/2, ancho)
