from processo import Processo

from estrategias import Estrategia

FIRST_FIT = 0; BEST_FIT = 1; WORST_FIT = 2 #Constantes

class Gerenciador:

  def __init__(self, tamanho_memoria):
    self.processo_main = Processo(-1, 0, 0, 0)
    self.tamanho_memoria = tamanho_memoria
    self.identificadores = {}
    self.estrategia = Estrategia(self.processo_main, self.tamanho_memoria, self.identificadores)

  def criar_novo_processo(self, processo: Processo):
    
    if processo.estrategia == FIRST_FIT: # caso seja first_fit
      return self.estrategia.firstFit(processo)
    elif processo.estrategia == BEST_FIT:
      return self.estrategia.bestFit(processo)
    elif processo.estrategia == WORST_FIT:
      return self.estrategia.worstFit(processo)
        
  def deletar_processo(self, id):
    
    currentProcess = self.processo_main # pega o primeiro existente
    
    while currentProcess != None:
      #print("id_processo: {}".format(currentProcess.id))
      if currentProcess.processo.id == id:
        currentProcess.processo = currentProcess.processo.processo
        #print(currentProcess.id if currentProcess != None else "is None")
        break
      else:
        currentProcess = currentProcess.processo

  
  def imprimir_dump_memoria(self):
    elements = [] # guarda os logs
    lastProcesso = None
    if self.processo_main.processo == None: # checa se há processos
      print("[D, {}, {}]".format(0, self.tamanho_memoria))
      return False
    currentProcess:Processo = self.processo_main.processo # pega o primeiro processo
    posicao = 0
    print("Legendas:\nD = Disponível\nO = Oculpado\n[Condição, ID, Tamanho Processo Atual]")
    while currentProcess != None: # checa se existe
      if currentProcess.posicao == posicao: # checa se o id esta entre os ocupados
        elements.append("[O, {}, {}]".format(posicao, currentProcess.tamanho))
      else: # entra na condicao do espaco Disponivel e guarda ambos
        elements.append("[D, {}, {}]".format(posicao, currentProcess.posicao - posicao))
        elements.append("[O, {}, {}]".format(currentProcess.posicao, currentProcess.tamanho))
      
      posicao = currentProcess.posicao + currentProcess.tamanho # gera o novo posicao
      lastProcesso = currentProcess
      currentProcess = currentProcess.processo

    if lastProcesso != None:
      lastPosition = lastProcesso.posicao + lastProcesso.tamanho
      resto = self.tamanho_memoria - lastPosition
      if  resto > 0:
        elements.append("[D, {}, {}]".format(lastPosition, resto))

    # imprime os elementos
    lastElement = elements.pop()
    for e in elements:
      print(e, end=" -> ")
    print(lastElement)






  
