from ayudas import *

class enemigo:
    sprite = None
    archivo = 'Jugador'
    imagen = './imagenes/.png'
    size = VECTOR((64,128))
    coord = VECTOR((32,64))
    indice = 0
    movimientos = []
    salud = 100
    exp = 100
    damage = 20
    ataque = 'ataque'
    sonido = 'ruta sonido'
    velocidad = VECTOR((3,0))
    resistencia = 3
    distanciaAtaque = 80
    distanciaDetecta = 360

    