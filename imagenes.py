import pygame

from ayudas import *

pygame.font.init()

'''
class imagen:
    size = VECTOR(100,100)
    coord = VECTOR(10,10)
    archivo = pygame.image.load('variableImagen').convert_alpha()
    imagen = pygame.transform.scale(archivo,(size.x,size.y))
    posicion = 0
'''

def imagen(imagen):
    ventana.blit(imagen.imagen,imagen.imagen.get_rect(topleft = (imagen.coord.x,imagen.coord.y)))

def desplazarFondo(fondo):

    ventana.blit(fondo.imagen,(fondo.posicion,0))

    ventana.blit(fondo.imagen,(fondo.size.x + fondo.posicion,0))       

    fondo.posicion -= 3

    if abs(fondo.posicion) > fondo.size.x:
        fondo.posicion = 0
        
background_layers = [
    {'image': pygame.transform.scale(pygame.image.load('./imagenes/parallax/1.png'),(ANCHO,ALTO)), 'speed': 7, 'pos': 0}, 
    {'image': pygame.transform.scale(pygame.image.load('./imagenes/parallax/2.png'),(ANCHO,ALTO)), 'speed': 5, 'pos': 0},  
    {'image': pygame.transform.scale(pygame.image.load('./imagenes/parallax/3.png'),(ANCHO,ALTO)), 'speed': 3, 'pos': 0},  
    {'image': pygame.transform.scale(pygame.image.load('./imagenes/parallax/4.png'),(ANCHO,ALTO)), 'speed': 6, 'pos': 0},  
    {'image': pygame.transform.scale(pygame.image.load('./imagenes/parallax/5.png'),(ANCHO,ALTO)), 'speed': 4, 'pos': 0},  
     {'image': pygame.transform.scale(pygame.image.load('./imagenes/parallax/6.png'),(ANCHO,ALTO)), 'speed': 9, 'pos': 0} 
]        

class parallaxFondo:
    layers = background_layers


def parallax(parallax):
    for layer in parallax.layers:

        ventana.blit(layer['image'],(layer['pos'],0))

        ventana.blit(layer['image'],(ANCHO + layer['pos'],0))       

        layer['pos'] -= layer['speed']

        if abs(layer['pos']) > ANCHO:
            layer['pos'] = 0                       