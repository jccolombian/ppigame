from ayudas import *
from jugador import *

mapa3 = './mapas/mapa3/mapa3.tmx'

def cargarmapa(mapa):
    datos_mapa = load_pygame(mapa)
    for capa in datos_mapa.visible_layers:
        if hasattr(capa,'data'):
            for x,y,surf in capa.tiles():
                sprite = pygame.sprite.Sprite()
                sprite.image = surf
                resized_image = pygame.transform.scale(sprite.image,(TILESIZE,TILESIZE))

                if capa.name == 'casas' or capa.name == 'arboles':
                    resized_image = pygame.transform.scale(sprite.image,(256,256))

                
                sprite.image = resized_image
                sprite.rect = sprite.image.get_rect() 
                sprite.rect.x = x*TILESIZE
                sprite.rect.y = y*TILESIZE 

                if capa.name == 'casas' or capa.name == 'arboles' or capa.name == 'borde' or capa.name == 'arbustos':
                    COLISIONES.add(sprite)
                
                CAMARA.add(sprite)    
    
class canibalito2:
    sprite = None
    archivo = 'canibalito2'
    imagen = './imagenes/canibalito2/bajar/1.png'
    size = VECTOR((24,56))
    coord = VECTOR((MEDIO_ANCHO,MEDIO_ALTO))
    velocidad = 32
    indice = 0
    movimientos = []
    saltando = False
    enTierra = True
    sonido_saltando = saltoJuancho

jugador2(canibalito2)


def ventana4():

    emptySprites()

    cargarmapa(mapa3)

    CAMARA.add(canibalito2.sprite)

    camara(canibalito2)

    mover2(canibalito2)