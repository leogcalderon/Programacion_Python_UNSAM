class TorreDeControl():
  def __init__(self):
    self.arribos = Cola()
    self.partidas = Cola()

  def nueva_partida(self, vuelo):
    self.partidas.encolar(vuelo)

  def nuevo_arribo(self, vuelo):
    self.arribos.encolar(vuelo)

  def ver_estado(self):
    print('Vuelos esperando para aterrizar:\n' + ', '.join(self.arribos.items) + '\n\nVuelos esperando para despegar:\n' + ', '.join(self.partidas.items))

  def asignar_pista(self):
    if len(self.arribos.items) > 0:
      vuelo_pista_asignada = self.arribos.desencolar()
      return f'El vuelo {vuelo_pista_asignada} aterizó con éxito'

    elif len(self.partidas.items) > 0:
      vuelo_pista_asignada = self.partidas.desencolar()
      return f'El vuelo {vuelo_pista_asignada} despegó con éxito'

    else:
      return 'No existen arribos ni partidas para asignar.'
