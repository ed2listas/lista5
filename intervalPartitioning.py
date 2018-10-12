import csv
from funcoes_auxiliares import *
import random

classrooms_file = []
classrooms = []
start_activity = 8
finish_activity = 20

class Classroom:
    start = 0
    finish = 0
    name = ""

    def __init__ (self,name,start, finish):
        self.start = start
        self.finish = finish
        self.name = name

    
with open ("companies.csv", "r") as f:
    data = csv.reader(f)
    next(data)

    for line in data:
        classrooms_file.append(Classroom(line[0], int(line[1]), int(line[2])))

    for i in classrooms_file:
        print(i.name)


classrooms = random.sample(classrooms_file, 15)

for i in classrooms:
        print(i.start)

print("\n")

classrooms.sort(key=lambda x: x.start)


for i in classrooms:
        print(i.start)






    
