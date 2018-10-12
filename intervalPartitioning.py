import csv
from funcoes_auxiliares import *
import random

classrooms_file = []
classrooms = []
grade = []
start_activity = 8
finish_activity = 20
number_class_open = 0

class Classroom:
    start = 0
    finish = 0
    name = ""

    def __init__ (self,name,start, finish):
        self.start = start
        self.finish = finish
        self.name = name

def search_for_time(obj):
    for i in range(len(grade)):
        if(obj.start >= grade[i][-1].finish):
            return i
    return -1

    
with open ("companies.csv", "r") as f:
    data = csv.reader(f)
    next(data)

    for line in data:
        classrooms_file.append(Classroom(line[0], int(line[1]), int(line[2])))

    for i in classrooms_file:
        print(i.name)


classrooms = random.sample(classrooms_file, 15)



print("\n")

classrooms.sort(key=lambda x: x.start)


for i in classrooms: 
    obj_compatibility = search_for_time(i)
    print(obj_compatibility)

    if(number_class_open == 0 and len(classrooms) != 0 or obj_compatibility == -1):
        aux = []
        aux.append(i)
        grade. append(aux)
        number_class_open += 1 
    elif(obj_compatibility != -1):
        grade[obj_compatibility].append(i)

for i in range(len(grade)):
    for j in range(len(grade[i])):
        print("start: %d  finish: %d" %(grade[i][j].start, grade[i][j].finish))
    print("amanda")






    
