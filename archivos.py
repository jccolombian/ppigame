import pygame, sys

from pygame.locals import *


pygame.init()

pygame.font.init()

def existe(archivo,contenido):
    try:
        with open(archivo, 'r') as file:
            content = file.read()
            if contenido in content:
                return True
            else:
                return False
    except FileNotFoundError:
        print(f"File {archivo} not found.")
        return None

def insertar(archivo,contenido):
    try:
        with open(archivo, 'a') as file:
            file.write(contenido+'\n')
            return True   
    except FileNotFoundError:
        print(f"File {archivo} not found.")
        return None
    return False