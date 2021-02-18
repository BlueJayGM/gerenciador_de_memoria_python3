from processo import Processo

class Estrategia:

  def __init__(self, processo_main = None, tamanho_memoria = 0, identificadores = []):
    self.processo_main = processo_main
    self.tamanho_memoria = tamanho_memoria
    self.identificadores = identificadores

  def firstFit(self, processo):
    #checa se tem processo, caso n tenha adiciona
    if self.processo_main.processo == None: # checa se ha processos
      if processo.tamanho < self.tamanho_memoria: # valida o processo
          self.processo_main.processo = processo # adiciona o processo a cabeca
          processo.posicao = 0
          self.identificadores[0] = processo.tamanho # adiciona o tamanho e o id 
          return True
    else:
      '''
        - percorre os processos em busca de espaco para alocar
        - verifica se tem espaco entre processos, caso n tenha, verifica o proximo
        - se tiver espaco apos todos os processos, adiciona, caso nao, nao adiciona
      '''
      currentProcess = self.processo_main # pega a cabeca como atual
      while currentProcess.processo != None: # pega o ultimo processo
        atual = currentProcess
        prox = atual.processo
        if prox != None:
          if atual.posicao + atual.tamanho != prox.posicao:
            #print("newLen: ", atual.posicao + atual.tamanho)
            if atual.posicao + atual.tamanho + processo.tamanho - 1 < prox.posicao:
              processo.posicao = atual.posicao + atual.tamanho
              self.identificadores[processo.posicao] = processo.tamanho
              processo.processo = prox
              atual.processo = processo
              return True
            atual = prox
        currentProcess = prox

      posicao = currentProcess.posicao + currentProcess.tamanho # gera o posicao do novo processo

      if processo.tamanho + posicao <= self.tamanho_memoria: # guarda o processo
        processo.posicao = posicao
        self.identificadores[posicao] = processo.tamanho
        currentProcess.processo = processo
        return True
      return False
    
  def bestFit(self, processo):
    menorTamanhoProcesso = self.tamanho_memoria
    saveAtual = None
    if self.processo_main.processo == None: # checa se ha processos
      if processo.tamanho < self.tamanho_memoria: # checa o processo
          self.processo_main.processo = processo # adiciona o processo a cabeca
          processo.posicao = 0
          self.identificadores[0] = processo.tamanho # adiciona o tamanho e o id
          return True
    else:
      currentProcess = self.processo_main # pega a cabeca como atual
      while currentProcess.processo != None: # pega o ultimo processo
        atual = currentProcess
        prox = atual.processo
        # print("Tamanho: ", atual.tamanho) # Referente ao tamanho oculpado/disponivel atual na memoria.
        # print("Tamanho currentProcess: ", currentProcess.tamanho) # Referente ao tamanho processo anterior
        if prox != None:
          if atual.posicao + atual.tamanho != prox.posicao:
            tamanhoNewLen = int(prox.posicao) - (int(atual.posicao) + int(atual.tamanho))
            if atual.posicao + atual.tamanho + processo.tamanho - 1 < prox.posicao and processo.tamanho == tamanhoNewLen:
              processo.posicao = atual.posicao + atual.tamanho
              self.identificadores[processo.posicao] = processo.tamanho
              processo.processo = prox
              atual.processo = processo
              return True
            elif atual.posicao + atual.tamanho + processo.tamanho - 1 < prox.posicao and processo.tamanho < tamanhoNewLen:
              if tamanhoNewLen < menorTamanhoProcesso:
                menorTamanhoProcesso = tamanhoNewLen
                saveAtual = currentProcess.processo
                saveProx = atual.processo
            atual = prox
        if prox == None and saveAtual != None:
          processo.posicao = saveAtual.posicao + saveAtual.tamanho
          self.identificadores[processo.posicao] = processo.tamanho
          processo.processo = saveProx
          saveAtual.processo = processo
          return True
        currentProcess = atual

      posicao = currentProcess.posicao + currentProcess.tamanho # gera o id do novo processo

      if processo.tamanho + posicao - 1 <= self.tamanho_memoria: # guarda o processo
        processo.posicao = posicao
        self.identificadores[posicao] = processo.tamanho
        currentProcess.processo = processo
        return True
      return False

  def worstFit(self, processo):
    if self.processo_main.processo == None:  # checa se ha processos
      if processo.tamanho < self.tamanho_memoria:  # valida o processo
        self.processo_main.processo = processo  # adiciona o processo a cabeca
        processo.posicao = 0
        self.identificadores[0] = processo.tamanho  # adiciona o tamanho e o id
        return True
    else:
      '''
      -Percorre a memória em busca de espaços alocáveis,
      -ao encontrar um espaço ele salva como a maiorPosicao
      -continua percorrendo para checar se existem espaços maiores,
      -caso haja espaços maiores ele salva o maior, caso não salva o processo
      -no maiorPosicao
      '''
      currentProcess = self.processo_main
      maiorPosicao = None
      while currentProcess.processo != None:
        tamanhoProcesso = processo.tamanho
        atual = currentProcess
        prox = atual.processo
        currentPosicao = atual.posicao + atual.tamanho
        if currentPosicao + tamanhoProcesso - 1 < prox.posicao:
          if maiorPosicao != None:
            if maiorPosicao < currentPosicao:
              maiorPosicao = currentPosicao
          else:
            maiorPosicao = currentPosicao
          atual = prox
        currentProcess = prox

      currentPosicao = currentProcess.posicao + currentProcess.tamanho
      if maiorPosicao != None and maiorPosicao < currentPosicao:
        maiorPosicao = currentPosicao
      elif maiorPosicao == None:
        maiorPosicao = currentPosicao

      currentProcess = self.processo_main
      while currentProcess != None: # pega o ultimo processo e transforma em cabeca
        atual = currentProcess
        prox = atual.processo
        if atual.posicao + atual.tamanho == maiorPosicao:
          processo.posicao = maiorPosicao
          self.identificadores[maiorPosicao] = processo.tamanho
          processo.processo = prox
          atual.processo = processo
          return True
        atual = prox
        currentProcess = prox

    return False