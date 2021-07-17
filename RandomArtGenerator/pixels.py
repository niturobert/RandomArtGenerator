"""
Semplice algoritmo di scrittura.
"""


from PIL import Image, ImageDraw


from random import randint

from config import *

SQUARE_SIZE = 8

with Image.new('RGB', (IMAGE_WIDTH, IMAGE_HEIGHT)) as image:
    draw = ImageDraw.Draw(image)

    for y in range(0, IMAGE_HEIGHT, SQUARE_SIZE):
        for x in range(0, IMAGE_WIDTH, SQUARE_SIZE):
            draw.rectangle([(x, y), (x + SQUARE_SIZE, y + SQUARE_SIZE)], fill=(randint(0, 255), randint(0, 255), randint(0, 255)))

    image.show()