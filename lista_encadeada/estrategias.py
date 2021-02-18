from processo import Processo

class Estrategia:

  def __init__(self, processo_main = None, tamanho_memoria = 0, identificadores = []):
    self.processo_main = processo_main
    self.tamanho_memoria = tamanho_memoria
    self.identificadores = identificadores

  def firstFit(self, processo):
    if self.processo_main.processo == None: # checa se ha processos
      if processo.tamanho < self.tamanho_memoria: # valida o processo
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
          if atual.id + atual.tamanho != prox.id:
            print("newLen: ", atual.id + atual.tamanho)
            if atual.id + atual.tamanho + processo.tamanho - 1 < prox.id:
              processo.id = atual.id + atual.tamanho
              self.identificadores[processo.id] = processo.tamanho
              processo.processo = prox
              atual.processo = processo
              return True
            atual = prox
        currentProcess = atual

      id = currentProcess.id + currentProcess.tamanho # gera o id do novo processo

      if processo.tamanho + id <= self.tamanho_memoria: # guarda o processo
        processo.id = id
        self.identificadores[id] = processo.tamanho
        currentProcess.processo = processo
        return True
      return False
    
  def bestFit(self, processo):
    menorTamanhoProcesso = self.tamanho_memoria

    if self.processo_main.processo == None: # checa se ha processos
      if processo.tamanho < self.tamanho_memoria: # checa o processo
          self.processo_main.processo = processo # adiciona o processo a cabeca
          processo.id = 0
          self.identificadores[0] = processo.tamanho # adiciona o tamanho e o id
          return True
    else:
      currentProcess = self.processo_main # pega a cabeca como atual
      print("Tamanho do Processo que deseja Adicionar: ", processo.tamanho)  # Tamanho do Processo adicionado
      print("-----------------------------------------------")
      while currentProcess.processo != None: # pega o ultimo processo
        atual = currentProcess.processo
        prox = atual.processo
        print("Tamanho: ", atual.tamanho) # Referente ao tamanho oculpado/disponivel atual na memoria.
        print("Tamanho currentProcess: ", currentProcess.tamanho) # Referente ao tamanho processo anterior
        if prox != None:
          if atual.id + atual.tamanho != prox.id:
            print("newLen: ", atual.id + atual.tamanho)
            tamanhoNewLen = int(prox.id) - (int(atual.id) + int(atual.tamanho))
            print("tamanhoNewLen: ", tamanhoNewLen)
            if atual.id + atual.tamanho + processo.tamanho - 1 < prox.id and processo.tamanho == tamanhoNewLen:
              processo.id = atual.id + atual.tamanho
              self.identificadores[processo.id] = processo.tamanho
              processo.processo = prox
              atual.processo = processo
              return True
            elif atual.id + atual.tamanho + processo.tamanho - 1 < prox.id and processo.tamanho <= tamanhoNewLen:
              saveAtualId = atual.id
              saveAtualTamanho = atual.tamanho
              saveProcessoTamanho = processo.tamanho
              saveProxId = prox.id
              saveTamanhoNewLen = tamanhoNewLen
            atual = prox
        currentProcess = atual

      id = currentProcess.id + currentProcess.tamanho # gera o id do novo processo

      if processo.tamanho + id - 1 <= self.tamanho_memoria: # guarda o processo
        processo.id = id
        self.identificadores[id] = processo.tamanho
        currentProcess.processo = processo
        return True
      return False

  def bestFitProcessoEmTamanhoMaior(self, saveAtualId, saveAtualTamanho, saveProcessoTamanho, saveProxId, saveTamanhoNewLen):

  def worstFit(self, processo):
    return True