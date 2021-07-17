"""
Rileva il colore di ogni area e sovrascrivila...
"""


from PIL import Image, ImageDraw
from matplotlib import image as img

from tkinter import Tk
from tkinter.filedialog import askopenfilename


from random import randint

from config import *

SQUARE_SIZE = 8

Tk().withdraw()
filename = askopenfilename() 
print("Opening file: %s" % filename)
print("Type: %s" % type(filename))

if len(filename) > 1:
    original_image = img.imread(filename)
    with Image.open(filename) as image:
        draw = ImageDraw.Draw(image)

        for y in range(0, image.height, SQUARE_SIZE):
            for x in range(0, image.width, SQUARE_SIZE):
                # Get the dominant color.
                AVG_RED, AVG_GRN, AVG_BLU = 0, 0, 0
                for offset_y in range(SQUARE_SIZE):
                    for offset_x in range(SQUARE_SIZE):
                        selected_pixel = image.getpixel((x + offset_x, y + offset_y))
                        AVG_RED += selected_pixel[0]
                        AVG_GRN += selected_pixel[1]
                        AVG_BLU += selected_pixel[2]

                AVG_RED //= SQUARE_SIZE ** 2
                AVG_GRN //= SQUARE_SIZE ** 2
                AVG_BLU //= SQUARE_SIZE ** 2
                draw.rectangle([(x, y), (SQUARE_SIZE, SQUARE_SIZE)], fill=(AVG_RED, AVG_GRN, AVG_BLU))

        image.show()

else:
    print("Nessun file")