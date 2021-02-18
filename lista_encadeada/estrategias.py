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
          processo.posicao = 0
          self.identificadores[0] = processo.tamanho # adiciona o tamanho e o id 
          return True
    else:
      currentProcess = self.processo_main # pega a cabeca como atual
      while currentProcess.processo != None: # pega o ultimo processo
        atual = currentProcess.processo
        prox = atual.processo
        if prox != None:
          if atual.posicao + atual.tamanho != prox.posicao:
            print("newLen: ", atual.posicao + atual.tamanho)
            if atual.posicao + atual.tamanho + processo.tamanho - 1 < prox.posicao:
              processo.posicao = atual.posicao + atual.tamanho
              self.identificadores[processo.posicao] = processo.tamanho
              processo.processo = prox
              atual.processo = processo
              return True
            atual = prox
        currentProcess = atual

      posicao = currentProcess.posicao + currentProcess.tamanho # gera o posicao do novo processo

      if processo.tamanho + posicao <= self.tamanho_memoria: # guarda o processo
        processo.posicao = posicao
        self.identificadores[posicao] = processo.tamanho
        currentProcess.processo = processo
        return True
      return False
    
  def bestFit(self, processo):
    menorTamanhoProcesso = self.tamanho_memoria

    if self.processo_main.processo == None: # checa se ha processos
      if processo.tamanho < self.tamanho_memoria: # checa o processo
          self.processo_main.processo = processo # adiciona o processo a cabeca
          processo.posicao = 0
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
          if atual.posicao + atual.tamanho != prox.posicao:
            print("newLen: ", atual.posicao + atual.tamanho)
            tamanhoNewLen = int(prox.posicao) - (int(atual.posicao) + int(atual.tamanho))
            print("tamanhoNewLen: ", tamanhoNewLen)
            if atual.posicao + atual.tamanho + processo.tamanho - 1 < prox.posicao and processo.tamanho == tamanhoNewLen:
              processo.posicao = atual.posicao + atual.tamanho
              self.identificadores[processo.posicao] = processo.tamanho
              processo.processo = prox
              atual.processo = processo
              return True
            elif atual.posicao + atual.tamanho + processo.tamanho - 1 < prox.posicao and processo.tamanho <= tamanhoNewLen:
              saveAtualId = atual.posicao
              saveAtualTamanho = atual.tamanho
              saveProcessoTamanho = processo.tamanho
              saveProxId = prox.posicao
              saveTamanhoNewLen = tamanhoNewLen
            atual = prox
        currentProcess = atual

      posicao = currentProcess.posicao + currentProcess.tamanho # gera o id do novo processo

      if processo.tamanho + posicao - 1 <= self.tamanho_memoria: # guarda o processo
        processo.posicao = posicao
        self.identificadores[posicao] = processo.tamanho
        currentProcess.processo = processo
        return True
      return False

  def bestFitProcessoEmTamanhoMaior(self, saveAtualId, saveAtualTamanho, saveProcessoTamanho, saveProxId, saveTamanhoNewLen):
    pass

  def worstFit(self, processo):
    return True