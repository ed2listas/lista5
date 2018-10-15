from funcoes_auxiliares import *
from sortByDeadline import *

class Job:
    name = ""
    start = 0
    finish = 0 # nao usado (start + time)

    deadline = 0
    time = 0
    lateness = 0

    def __init__(self, name, time, deadline):
        self.name = name
        self.time = time
        self.finish = time
        self.deadline = deadline

    def setStart(self, start):
        self.start = start
        self.finish = start + self.time
        self.lateness = max(0, self.finish-self.deadline)

def minimizeLateness():
    jobs = []
    jobs.append(Job("3",1,9))
    jobs.append(Job("2",2,8))
    jobs.append(Job("6",2,15))
    jobs.append(Job("1",3,6))
    jobs.append(Job("5",3,14))
    jobs.append(Job("4",4,9))

    limparTela()
    printColorido("\t\t** minimize Lateness **\n","GREEN","NORMAL","ITALIC")
    print("Todas as tarefas:")
    for job in jobs:
        print("tarefa {}:  tempo = {}, deadline = {}".format(job.name, job.time, job.deadline))
    print("")

    jobs = sortByDeadline(jobs)

    time = 0
    maxLateness = 0
    for job in jobs:
        job.setStart(time)
        time = job.finish
        if (job.lateness > maxLateness):
            maxLateness = job.lateness

    print("Tarefas por ordem de deadline")
    for job in jobs:
        print("tarefa %s, " % job.name, end="")
        printColorido("inicio",'GREEN')
        print(" = %2d, " % job.start, end="")
        printColorido("fim",'RED')
        print(" = %2d, " % job.finish, end="")
        printColorido("atraso",'YELLOW')
        print(" = %2d" % job.lateness)

    print("\nAtraso máximo:",maxLateness,"\n")
    pausar()

#
