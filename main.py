import os
import time

from character_classes import *

def clear():
    os.system('clear')
#END clear

def sleep():
    time.sleep(1)
#END sleep


line = raw_input("Podaj napis: ")
clear()


li = []
for item in line:
    li.append(buildCharacter(item))
#END FOR

li = li[::-1]

line_matrix = [""] * 6

for item in li:
    for j in range(2, -1, -1):
        for i in range(0, 6):
            print(item.get(i, j, 3) + line_matrix[i])
        #END FOR
        sleep()
        clear()
    #END FOR
    for i in range(0, 6):
        line_matrix[i] = " " + item.get(i, 0, 3) + line_matrix[i]
    #END FOR
#END FOR

li = reversed(li)

for item in li:
    for i in range(0, 6):
        line_matrix[i] = line_matrix[i][4:]
    #END FOR

    for j in range(0, 3, 1):
        for i in range(0, 6):
            print(item.get(i, j, 3) + line_matrix[i])
        #END FOR
        sleep()
        clear()
    #END FOR
#END FOR
