class Processo:

  def __init__(self, id = 0, tamanho = 0, estrategia = None, posicao = 0, status = 'N',processo=None):
    self.id = id
    self.tamanho = tamanho
    self.estrategia = estrategia
    self.status = status
    self.posicao = posicao
    self.processo = processo
  