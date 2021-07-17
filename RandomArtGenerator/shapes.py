"""
Semplice algoritmo, ma con figure geometriche casuali.
"""


from PIL import Image, ImageDraw


from random import randint, choice

from config import *

SQUARE_SIZE = 8
CHOICES = ["square", "circle"]

with Image.new('RGB', (IMAGE_WIDTH, IMAGE_HEIGHT), color=(255, 255, 255)) as image:
    draw = ImageDraw.Draw(image)
    
    for _ in range(1000):
        x, y = randint(0, IMAGE_WIDTH), randint(0, IMAGE_HEIGHT)
        chosen_choice = choice(CHOICES)
            
        if chosen_choice == "square":
            draw.rectangle([(x, y), (x + randint(0, 1000), y + randint(0, 1000))], fill=(randint(0, 255), randint(0, 255), randint(0, 255)))

        elif chosen_choice == "circle":
            draw.ellipse([(x, y), (x + randint(0, 1000), y + randint(0, 1000))], fill=(randint(0, 255), randint(0, 255), randint(0, 255)))

    image.show()