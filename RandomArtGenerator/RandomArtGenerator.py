#!/usr/bin/env python3

import sys
import importlib


def menu():
    print("1. Pixel art")
    print("2. Shaped art")
    print("3. Complex shape art")
    # print("4. Pixelate existing image")
    print("0. Exit")
    return input("scelta: ")

if __name__ == '__main__':
    print("Random Art Generator")
    print("--------------------")
    while True:
        scelta = menu()
        if scelta == '1':
            if 'pixels' not in sys.modules:
                import pixels

            else:
                importlib.reload(pixels)

        elif scelta == '2':
            if 'shapes' not in sys.modules:
                import shapes

            else:
                importlib.reload(shapes)

        elif scelta == '3':
            if 'shapesv2' not in sys.modules:
                import shapesv2

            else:
                importlib.reload(testing)

        # elif scelta == '4':
        #     if 'pixelify' not in sys.modules:
        #         import pixelify

        #     else:
        #         importlib.reload(pixelify)

        elif scelta == '0':
            sys.exit(0)