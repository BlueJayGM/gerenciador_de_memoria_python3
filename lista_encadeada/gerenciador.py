from typing import Final

from processo import Processo

FIRST_FIT:Final = 0; BEST_FIT:Final = 1; WORST_FIT:Final = 2 #Constantes

class Gerenciador:

  def __init__(self, tamanho_memoria):
    self.processo_main = Processo(-1, 0, 0)
    self.tamanho_memoria = tamanho_memoria
    self.identificadores = {}

  def criar_novo_processo(self, processo: Processo):
    
    if processo.estrategia == FIRST_FIT: # caso seja first_fit
      if self.processo_main.processo == None: # checa se ha processos
        if processo.tamanho < self.tamanho_memoria: # checa o processo
          self.processo_main.processo = processo # adiciona o processo a cabeca
          processo.id = 0
          self.identificadores[0] = processo.tamanho # adiciona o tamanho e o id 
        else:
          return False
      else:
        currentProcess = self.processo_main # pega a cabeca como atual
        while currentProcess.processo != None: # pega o ultimo processo
          currentProcess = currentProcess.processo
        id = currentProcess.id + currentProcess.tamanho
        if processo.tamanho + id < self.tamanho_memoria:
          processo.id = id
          self.identificadores[id] = processo.tamanho
          currentProcess.processo = processo
        else:
          return False
        


  def deletar_processo(self, id):
    pass
  
  def imprimir_dump_memoria(self):
    pass



  
