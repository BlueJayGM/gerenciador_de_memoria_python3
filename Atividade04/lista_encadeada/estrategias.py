from processo import Processo

class Estrategia:

  def __init__(self, processo_main = None, tamanho_memoria = 0):
    self.processo_main = processo_main
    self.tamanho_memoria = tamanho_memoria
    self.processo_main.processo = Processo(None, self.tamanho_memoria, None, 0, 'L')

  def checkIdExists(self, id):
    current = self.processo_main
    while current != None:
      if current.id == id:
        return True
      current = current.processo
    return False

  def addProcessInTop(self, top, process):
    mid = top.processo

    print("Process: ", mid)
    if mid.tamanho - process.tamanho > 0:
      mid.tamanho -= process.tamanho
      process.posicao = mid.posicao
      mid.posicao += process.tamanho
      process.processo = mid
    elif mid.tamanho - process.tamanho == 0:
      process.posicao = mid.posicao
      process.processo = mid.processo
    process.status = 'O'
    top.processo = process
    return True

  def firstFit(self, processo):
    top = self.processo_main
    
    while top.processo != None:
      mid = top.processo

      if mid.status == 'L':
        if processo.tamanho <= mid.tamanho:
          return self.addProcessInTop(top, processo)

      top = top.processo
      
    return False;

    
  def bestFit(self, processo):
    topBestLen = None
    lastLen = None
    top = self.processo_main

    while top.processo != None:
      mid = top.processo

      if mid.status == 'L':
        if processo.tamanho <= mid.tamanho:
          if lastLen == None:
            topBestLen = top
            lastLen = mid.tamanho
          elif lastLen > mid.tamanho:
            topBestLen = top
            lastLen = mid.tamanho
      top = top.processo

    if topBestLen != None:
      return self.addProcessInTop(topBestLen, processo)

    return False;

  def worstFit(self, processo):
    topWorstLen = None
    lastLen = None
    top = self.processo_main

    while top.processo != None:
      mid = top.processo

      if mid.status == 'L':
        if processo.tamanho <= mid.tamanho:
          if lastLen == None:
            topBestLen = top
            lastLen = mid.tamanho
          elif lastLen < mid.tamanho:
            topBestLen = top
            lastLen = mid.tamanho
      top = top.processo

    if topBestLen != None:
      return self.addProcessInTop(topBestLen, processo)
    return False;