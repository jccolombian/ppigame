from ayudas import *
from boton import *


class irAVentana1:
    boton = None
    click = False
    texto = 'Ventana 1'
    font = dumb3d
    fontSize = 20
    colorInactivo = blanco
    colorActivo = yellow1
    colorTexto = negro
    coord = VECTOR(10,10)
    size = VECTOR(150,70)
    borde = False
    tipo = 'ttf'


def mapa3(mapa):
    datos_mapa = load_pygame(mapa)
    for capa in datos_mapa.visible_layers:
        if hasattr(capa,'data'):
            for x,y,surf in capa.tiles():
                sprite = pygame.sprite.Sprite()
                sprite.image = surf
                resized_image = pygame.transform.scale(sprite.image,(TILESIZE,TILESIZE))
                sprite.image = resized_image
                sprite.rect = sprite.image.get_rect() 
                sprite.rect.x = x*TILESIZE
                sprite.rect.y = y*TILESIZE 
                if capa.name == 'casas' or capa.name == 'arboles' or capa.name == 'borde':
                    COLISIONES.add(sprite)
                
                CAMARA.add(sprite)    
    



def ventana3():

    boton(irAVentana1)

    if click(irAVentana1) :

        Ayudas.actual = 'ventana1'

        irAVentana1.click = False