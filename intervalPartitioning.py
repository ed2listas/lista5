import csv
from funcoes_auxiliares import *
import random

class Classroom:
    start = 0
    finish = 0
    name = ""

    def __init__ (self,name,start, finish):
        self.start = start
        self.finish = finish
        self.name = name

def search_for_time(obj, grade):
    for i in range(len(grade)):
        if(obj.start >= grade[i][-1].finish):
            return i
    return -1

def sum_string(row, col, grade):
    plus = 0
    for j in range(len(grade[row])):
        if(j < col):
            plus += len(grade[row][j].name)
    return plus


def print_the_grades(grade):
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

    for col in range(len(grade)):
        for row in range(len(grade[col])):
            if(row > 0):
                aux = (grade[col][row].start - 8)*11 #- sum_string(col,row)
                print("")
            else:
                aux = (grade[col][row].start - 8)*11

            print(" "*aux, end="")
            print("%s"%(grade[col][row].name), end="")
            end = (grade[col][row].finish - grade[col][row].start - 1) * 11 + (10-len(grade[col][row].name))
            print(" "*end, end="")    
            print("*", end="")
        print("")

        for i in range(13):
            print("-"*10, end="")
            print("|", end="")
        print("")
    
def intervalPartitioning():

    classrooms_file = []
    classrooms = []
    grade = []
    start_activity = 8
    finish_activity = 20
    number_class_open = 0


    with open ("companies.csv", "r") as f:
        data = csv.reader(f)
        next(data)

        for line in data:
            classrooms_file.append(Classroom(line[0], int(line[1]), int(line[2])))

        classrooms = random.sample(classrooms_file, 15)



    classrooms.sort(key=lambda x: x.start)


    for i in classrooms: 
        obj_compatibility = search_for_time(i,grade)

        if(number_class_open == 0 and len(classrooms) != 0 or obj_compatibility == -1):
            aux = []
            aux.append(i)
            grade. append(aux)
            number_class_open += 1 
        elif(obj_compatibility != -1):
            grade[obj_compatibility].append(i)

    print_the_grades(grade)

    print("")

    print("A quantidade minima de salas a ser alocada é de %d"%(len(grade) - 1))
    pausar()