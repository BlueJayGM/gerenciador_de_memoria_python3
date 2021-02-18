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
        
  def deletar_processo(self, id):
    
    currentProcess = self.processo_main # pega o primeiro existente
    
    while currentProcess != None:
      print("id_processo: {}".format(currentProcess.id))
      if currentProcess.processo.id == id:
        currentProcess.processo = currentProcess.processo.processo
        print(currentProcess.id if currentProcess != None else "is None")
        break
      else:
        currentProcess = currentProcess.processo

  
  def imprimir_dump_memoria(self):
    elements = [] # guarda os logs
    if self.processo_main.processo == None: # checa se há processos
      print("Nenhum processo existente!")
      return False
    currentProcess:Processo = self.processo_main.processo # pega o primeiro processo
    id = 0
    while currentProcess != None: # checa se existe
      if currentProcess.id == id: # checa se o id esta entre os ocupados
        elements.append("[O, {}, {}]".format(id, currentProcess.tamanho))
      else: # entra na condicao do espaco Disponivel e guarda ambos
        elements.append("[D, {}, {}]".format(id, currentProcess.id - id - 1))
        elements.append("[O, {}, {}]".format(currentProcess.id, currentProcess.tamanho))
      
      id = currentProcess.id + currentProcess.tamanho # gera o novo id

      currentProcess = currentProcess.processo

    # imprime os elementos
    lastElement = elements.pop()
    for e in elements:
      print(e, end=" -> ")
    print(lastElement)






  
