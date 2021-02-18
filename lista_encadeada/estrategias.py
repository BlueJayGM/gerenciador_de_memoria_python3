from processo import Processo

class Estrategia:

  def __init__(self, processo_main = None, tamanho_memoria = 0, identificadores = []):
    self.processo_main = processo_main
    self.tamanho_memoria = tamanho_memoria
    self.identificadores = identificadores

  def firstFit(self, processo):
    if self.processo_main.processo == None: # checa se ha processos
      if processo.tamanho < self.tamanho_memoria: # checa o processo
          self.processo_main.processo = processo # adiciona o processo a cabeca
          processo.id = 0
          self.identificadores[0] = processo.tamanho # adiciona o tamanho e o id 
          return True
    else:
      currentProcess = self.processo_main # pega a cabeca como atual
      while currentProcess.processo != None: # pega o ultimo processo
        atual = currentProcess.processo
        prox = atual.processo
        if prox != None:
          if atual.id + atual.tamanho == prox.id:
            currentProcess = currentProcess.processo
          else:
            if atual.id + atual.tamanho + processo.tamanho < prox.id:
              currentProcess = currentProcess.processo
              break
        else:
          currentProcess = currentProcess.processo
      id = currentProcess.id + currentProcess.tamanho # gera o id do novo processo
      if processo.tamanho + id - 1 <= self.tamanho_memoria: # guarda o processo
        processo.id = id
        self.identificadores[id] = processo.tamanho
        currentProcess.processo = processo
        return True
      return False
    
  def bestFit(self, processo):
    return True
  def worstFit(self, processo):
    return True