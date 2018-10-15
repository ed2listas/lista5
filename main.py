from funcoes_auxiliares import *
from intervalPartitioning import *
from intervalScheduling import *
from minimizeLateness import *


# função principal
opcao = 1
while opcao != 0:
    limparTela()
    opcao = menuComOpcao([
        "interval Scheduling",
        "interval Partitioning",
        "minimize Lateness", "Sair"])

    if opcao == 1:
        intervalScheduling()
    elif opcao == 2:
        intervalPartitioning()
    elif opcao == 3:
        minimizeLateness()
    elif opcao == 0:
        print("Saindo...")
    else:
        print("valor invalido")
        pausar()
