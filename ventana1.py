# zona de imports
from ayudas import *
from imagenes import *
from boton import *

# zona de variables
class fondo1:
    size = VECTOR(ANCHO,ALTO)
    coord = VECTOR(0,0)
    archivo = pygame.image.load(paisajeCiervos).convert_alpha()
    imagen = pygame.transform.scale(archivo,(size.x,size.y))
    posicion = 0

class safari:
    size = VECTOR(60,80)
    coord = VECTOR(120,200)
    archivo = pygame.image.load(safari).convert_alpha()
    imagen = pygame.transform.scale(archivo,(size.x,size.y))
    posicion = 0

class botonSalir:
    boton = None
    click = False
    texto = 'Salir'
    font = stencil
    fontSize = 30
    colorInactivo = blanco
    colorActivo = yellow1
    colorTexto = negro
    coord = VECTOR(200,200)
    size = VECTOR(120,70)
    borde = True
    tipo = 'system'
    

class irAVentana2:
    boton = None
    click = False
    texto = 'Siguiente'
    font = dumb3d
    fontSize = 30
    colorInactivo = blanco
    colorActivo = yellow1
    colorTexto = negro
    coord = VECTOR(400,200)
    size = VECTOR(150,70)
    borde = False
    tipo = 'ttf'


# zona de funciones


def ventana1():

    imagen(fondo1)

    imagen(safari)

    boton(botonSalir)

    if click(botonSalir):
        pygame.quit()
        sys.exit()
        botonSalir.click = False
        
    boton(irAVentana2)    

    if click(irAVentana2):

        Ayudas.actual = 'ventana2'
        irAVentana2.click = False