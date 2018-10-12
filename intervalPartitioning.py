import csv
from funcoes_auxiliares import *

classrooms = []
start_activity = 8
finish_activity = 20

class Classroom:
    start = 0
    finish = 0
    name = ""

    def __init__ (self, start, finish, name):
        self.start = start
        self.finish = finish
        self.name = name

    
with open ("companies.csv", "r") as f:
    data = csv.DictReader(f, delimiter=",")
    #next(dados) # Descarta o cabeçalho

    for line in data:
        classrooms.append(list(line.values()))

    for i in classrooms:
        print(i)



    
