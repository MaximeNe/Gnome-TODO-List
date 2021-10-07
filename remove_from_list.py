#!/usr/bin/env python3

"""
args recived :
* path to the script.sh file
"""

import sys

index = int(sys.argv[1])
liste_ligne = []
file = open(sys.argv[2][:-9] + "todo.txt", 'r')
for ligne in file:
    liste_ligne.append(ligne)
file.close()

new_list = []
k = 1
for i, ligne in enumerate(liste_ligne):
    if i+1 != int(index):
        m = ''
        for mot in ligne.split(' ')[2:]:
            m += (mot + ' ')
        m = m[:-1]
        new_list.append(str(k) + ' - ' + m)
        k += 1

file = open(sys.argv[2][:-9] + "todo.txt", 'w')
for e in new_list:
    file.write(e)
file.close()
