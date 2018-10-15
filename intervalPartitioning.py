import csv
from funcoes_auxiliares import *
import random

class Var:
    lassrooms_file = []
    classrooms = []
    grade = []
    start_activity = 8
    finish_activity = 20
    number_class_open = 0
    def reset(self):
        self.lassrooms_file = []
        self.classrooms = []
        self.grade = []
        self.start_activity = 8
        self.finish_activity = 20
        self.number_class_open = 0

var = Var()

class Classroom:
    start = 0
    finish = 0
    name = ""

    def __init__ (self,name,start, finish):
        self.start = start
        self.finish = finish
        self.name = name

def search_for_time(obj):
    for i in range(len(var.grade)):
        if(obj.start >= var.grade[i][-1].finish):
            return i
    return -1

def sum_string(row, col):
    plus = 0
    for j in range(len(var.grade[row])):
        if(j < col):
            plus += len(var.grade[row][j].name)
    return plus


def print_the_grades():
    for i in range(13):
        print("-"*10, end="")
        print("|", end="")
    print("")

    print(" "*5, end="")

    for i in range(8,21,1):
        print(i, end="")
        print(" "*9, end="")
    print("")

    for i in range(13):
        print("-"*10, end="")
        print("|", end="")
    print("")

    for col in range(len(var.grade)):
        for row in range(len(var.grade[col])):
            if(row > 0):
                aux = (var.grade[col][row].start - 8)*11 #- sum_string(col,row)
                print("")
            else:
                aux = (var.grade[col][row].start - 8)*11

            print(" "*aux, end="")
            print("%s"%(var.grade[col][row].name), end="")
            end = (var.grade[col][row].finish - var.grade[col][row].start - 1) * 11 + (10-len(var.grade[col][row].name))
            print(" "*end, end="")
            print("*", end="")
        print("")

        for i in range(13):
            print("-"*10, end="")
            print("|", end="")
        print("")

def intervalPartitioning():

    var.reset()

    limparTela()
    with open ("companies.csv", "r") as f:
        data = csv.reader(f)
        next(data)

        for line in data:
            var.lassrooms_file.append(Classroom(line[0], int(line[1]), int(line[2])))

    var.classrooms = random.sample(var.lassrooms_file, 15)

    var.classrooms.sort(key=lambda x: x.start)

    for i in var.classrooms:
        obj_compatibility = search_for_time(i)
        if((var.number_class_open == 0) and (len(var.classrooms) != 0) or (obj_compatibility == -1)):
            aux = []
            aux.append(i)
            var.grade.append(aux)
            var.number_class_open += 1
        elif(obj_compatibility != -1):
            var.grade[obj_compatibility].append(i)

    print_the_grades()

    print("\nA quantidade minima de salas a ser alocada é de %d"%(len(var.grade) - 1))
    pausar()
