from processo import Processo

from estrategias import Estrategia

FIRST_FIT = 0; BEST_FIT = 1; WORST_FIT = 2 #Constantes

class Gerenciador:

  def __init__(self, tamanho_memoria):
    self.processo_main = Processo(-1, 0, 0, 0, None)
    self.tamanho_memoria = tamanho_memoria
    self.estrategia = Estrategia(self.processo_main, self.tamanho_memoria)

  def criar_novo_processo(self, processo: Processo):
    
    if processo.estrategia == FIRST_FIT: # caso seja first_fit
      return self.estrategia.firstFit(processo)
    elif processo.estrategia == BEST_FIT:
      return self.estrategia.bestFit(processo)
    elif processo.estrategia == WORST_FIT:
      return self.estrategia.worstFit(processo)
        
  def deletar_processo(self, id):
    current = self.processo_main
    logId = None
    while current.processo != None:
      p = current.processo
      if p.id == id:
        p.id = -1
        p.status = 'L'
        logId = id
        break
      current = p
    self.joinAllOpenProcess()
    print("Processo de id: {} deletado com sucesso!".format(logId)) if logId != None else print("Id inválido!")
  
  def imprimir_dump_memoria(self):
    current = self.processo_main.processo;
    while current.processo != None:
      print("[{}, {}, {}] ->".format(current.status, current.posicao, current.tamanho), end=" ")
      current = current.processo
    print("[{}, {}, {}]".format(current.status, current.posicao, current.tamanho))

  def joinAllOpenProcess(self):
    current = self.processo_main
    while current.processo != None:
      top = current
      mid = top.processo
      if top.status == 'L' and mid.status == 'L':
        top.tamanho += mid.tamanho
        top.processo = mid.processo
      current = mid







  
