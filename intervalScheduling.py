from funcoes_auxiliares import *
from sortByFinish import *

class Job:
    name = ""
    start = None
    finish = None

    def __init__(self, name, start, finish):
        self.name = name
        self.start = start
        self.finish = finish

def compativel(job, selected):
    if len(selected) == 0:
        return True
    return job.start >= selected[-1].finish

def printTarefas(jobs):
    print("   Todas as tarefas:")
    for job in jobs:
        print("tarefa {}: inicio = {}, fim = {}".format(job.name, job.start, job.finish))
    print("")

def intervalScheduling():
    jobs = []
    jobs.append(Job("a",0,6))
    jobs.append(Job("b",1,4))
    jobs.append(Job("c",3,5))
    jobs.append(Job("d",3,8))
    jobs.append(Job("e",4,7))
    jobs.append(Job("f",5,9))
    jobs.append(Job("g",6,10))
    jobs.append(Job("h",8,11))

    limparTela()
    printColorido("\t\t** interval Scheduling **\n","GREEN","NORMAL","ITALIC")
    printTarefas(jobs)

    '''opcao = 1
    while opcao != 0:
        limparTela()
        printColorido("\t\t** interval Scheduling **\n","GREEN","NORMAL","ITALIC")
        printTarefas(jobs)
        opcao = menuComOpcao(["inserir", "retirar", "continuar"])
        if opcao == 1:
            print("Digite o nome: ",end="")
            nome = lerString()
            print("Digite o inicio: ",end="")
            inicio = lerInteger()
            print("Digite o fim: ",end="")
            fim = lerInteger()
            jobs.append(Job(nome,inicio,fim))
        elif opcao == 2:
            print("Digite o nome da tarefa a ser deletado:")
            nome = lerString()
            for job in jobs:
                if job.name == nome:
                    jobs.remove(job)
                break
        else:
            print("valor invalido")
            pausar()'''

    jobs = sortByFinish(jobs)
    selected = []

    for job in jobs:
        if compativel(job, selected):
            selected.append(job)

    print("   Maior numero possivel de tarefas sem conflito")
    for job in selected:
        print("tarefa {}".format(job.name))

    print("")
    pausar()

#
