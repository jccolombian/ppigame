from ayudas import *
from imagenes import *
from boton import *


class fondoVentana2:
    size = VECTOR(ANCHO,ALTO)
    coord = VECTOR(0,0)
    archivo = pygame.image.load(forest2).convert_alpha()
    imagen = pygame.transform.scale(archivo,(size.x,size.y))
    posicion = 0

class letrerito1:
    texto = 'Texto de prueba en la ventana 2'
    size = 45
    color = gold1
    font = dumb3d
    coord = VECTOR(50,50)

'''
class texto:
    texto = 'Como animar texto con estilo de animación de maquina de escribir'
    size = 20
    color = slateblue4
    font = letra1
    coord = VECTOR(50,50)
    contador = 0
    velocidad = 3    
'''
    
class irAVentana1:
    boton = None
    click = False
    texto = 'Volver'
    font = dumb3d
    fontSize = 30
    colorInactivo = blanco
    colorActivo = yellow1
    colorTexto = negro
    coord = VECTOR(400,200)
    size = VECTOR(150,70)
    borde = False
    tipo = 'ttf'    


class irAVentana3:
    boton = None
    click = False
    texto = 'Ventana 3'
    font = dumb3d
    fontSize = 20
    colorInactivo = blanco
    colorActivo = yellow1
    colorTexto = negro
    coord = VECTOR(580,200)
    size = VECTOR(150,70)
    borde = False
    tipo = 'ttf'


def ventana2():

    imagen(fondoVentana2)

    mostrarTextoTTF(letrerito1)

    boton(irAVentana1)

    if click(irAVentana1):
        Ayudas.actual = 'ventana1'
        irAVentana1.click = False
        

    boton(irAVentana3)

    if click(irAVentana3):
        Ayudas.actual = 'ventana3'
        irAVentana3.click = False    