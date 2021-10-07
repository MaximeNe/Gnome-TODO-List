#!/usr/bin/env python3

"""
args recived :
* element to add to the TodoList
* path to the empty background
* path to the script.sh file
"""

import sys


i = 1
file = open(sys.argv[3][:-9] + "todo.txt", 'r')
for ligne in file:
    i += 1
file.close()

file = open(sys.argv[3][:-9] + "todo.txt", 'a')
file.write(str(i) + ' - ' + sys.argv[1] + '\n')
file.close()
