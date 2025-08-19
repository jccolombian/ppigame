import pygame

from pygame.sprite import Sprite

from ayudas import *

import math

'''
class Objeto:
    sprite = None
    imagen = './imagenes/objetos/.png'
    size = VECTOR((64,128))
    coord = VECTOR((32,64))
    velocidad = VECTOR((0,0))
    angulo = 0 
'''

def objeto(objeto):

    sprite = Sprite()

    imagen = pygame.image.load(objeto.imagen).convert_alpha()
    sprite.image = pygame.transform.scale(imagen,(objeto.size.x,objeto.size.y))
    sprite.rect = sprite.image.get_rect() 
    sprite.rect.x = objeto.coord.x
    sprite.rect.y = objeto.coord.y   
    sprite.angulo = objeto.angulo
    objeto.sprite = sprite

    

def rotar(objeto):
    objeto.sprite.angulo += objeto.angulo
    ROTAN.add(objeto.sprite)

def girar(objeto):
    objeto.sprite.angulo += objeto.angulo
    GIRAN.add(objeto.sprite)

def moverDerechaIzquierda(objeto):
    objeto.sprite.rect.x-=objeto.velocidad.x
    if objeto.sprite.rect.x < 0:
        objeto.sprite.rect.x = ANCHO_MUNDO
    ventana.blit(objeto.sprite.image,objeto.sprite.image.get_rect(center=(objeto.sprite.rect.x,objeto.sprite.rect.y)))    

def moverYgirar(objeto):    
    objeto.sprite.rect.x-=objeto.velocidad.x
    if objeto.sprite.rect.x < 0:
        objeto.sprite.rect.x = ANCHO_MUNDO
    girar(objeto)    

# Limite inferior es mas arriba
# Limite superior es mas abajo
# posy debe ser mayor a limite INferior y menor que limite superior
def rebotar(objeto,limiteInferior,limiteSuperior,posy): 
  
    if objeto.sprite.rect.left < 0:
        objeto.sprite.rect.x = ANCHO_MUNDO
        objeto.sprite.rect.y = posy
    
    if objeto.sprite.rect.y < limiteInferior:    
        objeto.velocidad.y*=-1

    if objeto.sprite.rect.y > limiteSuperior:    
        objeto.velocidad.y*=-1
    
    objeto.sprite.rect.x += -objeto.velocidad.x
    objeto.sprite.rect.y += objeto.velocidad.y

    ventana.blit(objeto.sprite.image,
                 objeto.sprite.image.get_rect(center=(objeto.sprite.rect.x,objeto.sprite.rect.y)))  


def colisiona(sprite):
    return pygame.sprite.spritecollide(sprite.sprite, COLISIONES, False)


