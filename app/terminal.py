#!/usr/bin/env python3

import tkinter
import parser
import sys
from sys import argv
from PIL import Image, ImageTk

window = tkinter.Tk(className="main")

image_name = argv[1] if len(argv) >= 2 else "test.jpg"
image = Image.open(image_name)
if image.size[0] > image.size[1]:
    x_size = min(1920, image.size[0])
    y_size = x_size * image.size[1] // image.size[0]
else:
    y_size = min(1080, image.size[1])
    x_size = y_size * image.size[0] // image.size[1]

image = image.resize((x_size, y_size), Image.ANTIALIAS)
canvas = tkinter.Canvas(window, width=x_size, height=y_size)

canvas.pack()

image_tk = ImageTk.PhotoImage(image)

canvas.create_image(x_size//2, y_size//2, image=image_tk)

current_tuple = []
tuples = []

def callback(event):
    global current_tuple, tuples
    if len(current_tuple) > 0:
        full_tuple = (current_tuple[0], current_tuple[1], event.x, event.y)
        tuples.append(full_tuple)
        canvas.create_rectangle(full_tuple[0], full_tuple[1], full_tuple[2], full_tuple[3])
        current_tuple = []
    else:
        current_tuple.append(event.x)
        current_tuple.append(event.y)

def runner(event):
    # print("Tuples: ", tuples)
    print(parser.get_latex_code_object(image, tuples))
    sys.exit(0)


canvas.bind("<Button 1>", callback)
canvas.bind("<Button 3>", runner)

tkinter.mainloop()


