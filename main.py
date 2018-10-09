from funcoes_auxiliares import *
from intervalPartitioning import *
from intervalScheduling import *
from minimizeLateness import *

def menu():
    opcao = 0
    print("==========================================");
    print("|         >>>>>>>>> Menu <<<<<<<<<       |");
    print("| 1 - interval Scheduling                |");
    print("| 2 - bbbbbbbbbbbbb                      |");
    print("| 3 - cccccccccccccccccccccccccc         |");
    # outros
    print("| 0 - Sair                               |");
    print("==========================================");
    print("Sua opcao: ");
    opcao = lerInteger()
    return opcao;

# função principal
opcao = 1
while opcao != 0:
    limparTela()
    opcao = menu()

    if opcao == 1:
        intervalScheduling()
    elif opcao == 2:
        #intervalPartitioning()
        a = 1
    elif opcao == 3:
        #minimizeLateness() #Scheduling to Minimize Lateness
        a = 1
    elif opcao == 0:
        print("Saindo...")
    else:
        print("valor invalido")
        pausar()
