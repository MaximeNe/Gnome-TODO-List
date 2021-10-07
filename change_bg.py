#!/usr/bin/env python3

"""
args recived :
* path to the empty background
* path to the script.sh file
"""

# We are gonna use PIL to edit our current background
import sys
from PIL import Image, ImageFont, ImageDraw


message_list = []
file = open(sys.argv[2][:-9] + "todo.txt", 'r')
for line in file:
    message_list.append(line.strip())
file.close()

my_image = Image.open(sys.argv[1][8:-7] + "bg_save.png")
title_font = ImageFont.truetype(sys.argv[2][:-9] + 'Goldman-Regular.ttf', 25)
image_editable = ImageDraw.Draw(my_image)

h = 20
for message in message_list:
    i = 0
    while i < len(message):
        image_editable.text((1300,h), message[i:i+40], (237, 230, 211), font=title_font)
        i += 40
        h += 25
    h += 10

my_image.save(sys.argv[2][:-9] + "bg.png")
