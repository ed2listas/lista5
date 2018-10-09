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

    print("Todas as tarefas:")
    for job in jobs:
        print("tarefa {}: inicio = {}, fim = {}".format(job.name, job.start, job.finish))
    print("")

    jobs = sortByFinish(jobs)
    selected = []

    for job in jobs:
        if compativel(job, selected):
            selected.append(job)

    print("Maior numero possivel de tarefas sem conflito")
    for job in selected:
        print("tarefa {}".format(job.name))

    print("")
    pausar()

#
