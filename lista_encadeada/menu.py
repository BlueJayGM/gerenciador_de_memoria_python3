from gerenciador import Gerenciador
from processo import Processo

class Menu:

  def __init__(self, tamanho_memoria):
    self.gerenciador = Gerenciador(tamanho_memoria)
  
  def criar(self):
    id = int(input("Digite o id do processo: "))
    tamanho = int(input("Digite o tamanho do processo: "))
    print("Defina o tipo de estrategia [ 0 - First-Fit; 1 - Best-Fit; 2 - Worst-Fit ]")
    estrategia = int(input("valor: "))
    processo = Processo(id, tamanho, estrategia, None)
    return self.gerenciador.criar_novo_processo(processo)

  def deletar(self):
    id = int(input("Digite o id do processo: "))
    self.gerenciador.deletar_processo(id)
  
  def imprimir(self):
    self.gerenciador.imprimir_dump_memoria()
    

if __name__ == "__main__":

  print("\n ------------------- Menu ------------------- ")
  tamanho_memoria = int(input("> Digite o tamanho da memoria em blocos: "))
  menu = Menu(tamanho_memoria)
  
  while True:
    print("\n ------------------- Menu ------------------- ")
    print("> 1 - Criar Processo\n> 2 - Deletar Processo\n> 3 - Imprimir Dump\n> Outro - Sair")
    op = int(input("Digite a opcao desejada: "))

    if op > 0 and op <= 3:
      if op == 1: print("Processo criado com sucesso!") if menu.criar() else print("Erro ao criar processo!")
      if op == 2: menu.deletar()
      if op == 3: menu.imprimir()
    else:
      print("\nPrograma Finalizado!")
      break
