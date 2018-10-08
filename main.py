from funcoes_auxiliares import *

def menu():
    opcao = 0
    print("==========================================");
    print("|         >>>>>>>>> Menu <<<<<<<<<       |");
    print("| 1 - aaaaaaaaaaaaa                      |");
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
        #intervalScheduling()
    elif opcao == 2:
        #intervalPartitioning()
    elif opcao == 3:
        #minimizeLateness() #Scheduling to Minimize Lateness
    elif opcao == 0:
        print("Saindo...")
    else:
        print("valor invalido")
        pausar()
