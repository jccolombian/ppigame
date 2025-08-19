import pygame, sys, os

from pygame.locals import *

from pytmx.util_pygame import load_pygame

import math

pygame.init()

pygame.font.init()

FPS = 40

RELOJ = pygame.time.Clock()

TILESIZE = 32

ANCHO_MUNDO = TILESIZE*72

ALTO_MUNDO = TILESIZE*32

info = pygame.display.Info()

ventana = pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN | pygame.SCALED)

ANCHO, ALTO = size = ventana.get_size()

MEDIO_ANCHO = ANCHO//2

MEDIO_ALTO = ALTO//2

pygame.display.set_caption('Aqui va el titulo de la ventana')

class Ayudas:
    pygame.init()
    EVENTOS = pygame.event.get()
    actual = 'inicio'
    usuario = ''
    ACCION = 'ninguna'

# PALETA DE COLORES:
verdeGris = (224,238,224)
limon = '#EEE9BF'
slateblue4 = '#473C8B'
mediumseagreen = '#3CB371'
yellow1 = '#FFFF00'
darkgoldenrod4 = '#8B6508'
negro = (0,0,0)
blanco = (255,255,255)
springgreen = '#00FF7F'
springgreen3 = '#008B45'
cobaltgreen = '#3D9140'
darkorange2 = '#EE7600'
tan1 = '#FFA54F'
red = '#FF0000'
hotpink3 = '#CD6090'
hotpink	= '#FF69B4'
gold1 = '#FFD700'
honeydew3 = '#C1CDC1'
dodgerblue2 = '#1C86EE'
azul = (0, 0, 255)


# TIPOS DE FUENTES:

letra1 = 'bahnschrift'

letra2 = 'papyrus'

letra3 = 'jokerman'

letra4 = 'frenchscript'

letra5 = 'stencil'

letra6 = './fonts/Anagram.ttf'

letra7 = './fonts/VT323-Regular.ttf'

arialblack = 'arialblack'

AirstreamTTF = './fonts/Airstream.ttf'

# LISTA DE IMAGENES
grama = './imagenes/grama.png'
grama2 = './imagenes/grama2.png'
montaña = './imagenes/montaña.png'
nubes = './imagenes/nubes.png'
safari = './imagenes/safari.png'
summer = './imagenes/Summer5.png'

back = './imagenes/botones/back.png'
menu = './imagenes/botones/menu.png'
mfx = './imagenes/botones/mfx.png'
mfxs = './imagenes/botones/mfxs.png'
moregames = './imagenes/botones/moregames.png'

logo = './imagenes/logos/logo.png'
paisaje = './imagenes/fondos/landscape.png'

sfx = './imagenes/botones/sfx.png'
sfxs = './imagenes/botones/sfxs.png'

forest2 = './imagenes/fondos/forest2.jpg'

# ARCHIVOS PLANOS:
usuarios = './archivos/usuarios.txt'

# SONIDOS:
amusement = pygame.mixer.Sound('./sonidos/amusement_park_stage_bpm150.mp3')
cave  = pygame.mixer.Sound('./sonidos/cave.mp3')
daydream  = pygame.mixer.Sound('./sonidos/daydream.mp3')
salto = pygame.mixer.Sound('./sonidos/jump_10.wav')
saltoJuancho = pygame.mixer.Sound('./sonidos/saltoJuancho.mp3')

VECTOR = pygame.math.Vector2 


def mostrarLetraSistema():
    letras = pygame.font.get_fonts()
    for l in letras:
        print(l)

# variable texto normal:
'''
class texto:
    texto = 'Politécnico Colomibiano Jaime Isaza Cadavid'
    size = 50
    color = mediumseagreen
    font = letra4
    coord = VECTOR(50,50)
'''

# variable texto tipo parrafo:
'''
class texto:
    texto = ["Uno de los mayores anhelos después de cursar un programa académico en una institución",
             "universitaria, es culminar este ciclo con un acto de reconocimiento por parte de la institución al",
             "esfuerzo del estudiante, en el que le hace entrega formal del diploma que lo acredita como",
             "magíster, especialista, profesional, tecnólogo o técnico ñ."]
    size = 20
    color = darkgoldenrod4
    font = letra2
    coord = VECTOR(10,120)
'''

# variable texto normal efecto maquina de escribir:
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

# variable texto tipo parrafo efecto maquina de escribir:
'''
class texto:
    texto = ["Uno de los mayores anhelos después de cursar un programa académico en una institución",
             "universitaria, es culminar este ciclo con un acto de reconocimiento por parte de la institución al",
             "esfuerzo del estudiante, en el que le hace entrega formal del diploma que lo acredita como",
             "magíster, especialista, profesional, tecnólogo o técnico ñ."]
    size = 20
    color = darkgoldenrod4
    font = letra2
    coord = VECTOR(10,120)
    contador = 0
    velocidad = 1
    actual = 0
    linea = texto[actual]
    listo = False
'''

def mostrarTextoSistema(texto):
    letra = pygame.font.SysFont(texto.font,texto.size)
    ventana.blit(letra.render(str(texto.texto),
                                  True,texto.color),
                                  (texto.coord.x,texto.coord.y))    

def mostrarTextoTTF(texto):
    letra = pygame.font.Font(texto.font,texto.size)
    ventana.blit(letra.render(str(texto.texto),
                                  True,texto.color),
                                  (texto.coord.x,texto.coord.y))  
    

def mostrarTextoLargoSistema(texto):
    letra = pygame.font.SysFont(texto.font,texto.size)
    y = texto.coord.y
    for linea in texto.texto:
        ventana.blit(letra.render(str(linea),
                                    True,texto.color),
                                    (texto.coord.x,y))
        y += 30        


def mostrarTextoSistemaMaquinaDeEscribir(texto):
    letra = pygame.font.SysFont(texto.font,texto.size)
    if texto.contador < texto.velocidad * len(texto.texto):
        texto.contador += 1
  
    ventana.blit(letra.render(str(texto.texto[0:texto.contador//texto.velocidad]),
                                  True,texto.color),
                                  (texto.coord.x,texto.coord.y))

def mostrarTextoTTFMaquinaDeEscribir(texto):
    letra = pygame.font.Font(texto.font,texto.size)
    if texto.contador < texto.velocidad * len(texto.texto):
        texto.contador += 1
  
    ventana.blit(letra.render(str(texto.texto[0:texto.contador//texto.velocidad]),
                                  True,texto.color),
                                  (texto.coord.x,texto.coord.y)) 


def mostrarTextoLargoSistemaMaquinaDeEscribir(texto):
    letra = pygame.font.SysFont(texto.font,texto.size)

    if texto.contador < texto.velocidad * len(texto.linea):
        texto.contador += 1
    elif texto.contador >= texto.velocidad * len(texto.linea):
        texto.listo = True

    for evento in Ayudas.EVENTOS:
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_RETURN and texto.listo and texto.actual < len(texto.texto)-1:
                texto.actual += 1
                texto.listo = False
                texto.linea = texto.texto[texto.actual]
                texto.contador = 0

    ventana.blit(letra.render(str(texto.linea[0:texto.contador//texto.velocidad]),
                                  True,texto.color),
                                  (texto.coord.x,texto.coord.y))
    
# variable texto que parpadea:
'''
class texto:
    texto = 'Politécnico Colomibiano Jaime Isaza Cadavid'
    size = 50
    color = mediumseagreen
    font = letra4
    coord = VECTOR(50,50)
    parpadeando = True
    parpadear = pygame.USEREVENT + 1
    pygame.time.set_timer(parpadear,800)
'''

def intermitenteTextoSistema(texto):
    for evento in Ayudas.EVENTOS:
        if evento.type == texto.parpadear:
            texto.parpadeando = not texto.parpadeando
    if texto.parpadeando:
        mostrarTextoSistema(texto)

def intermitenteTextoTTF(texto):
    for evento in Ayudas.EVENTOS:
        if evento.type == texto.parpadear:
            texto.parpadeando = not texto.parpadeando
    if texto.parpadeando:
        mostrarTextoTTF(texto)        

# variable texto que temporal:
'''
class texto:
    texto = 'Politécnico Colomibiano Jaime Isaza Cadavid'
    size = 50
    color = mediumseagreen
    font = letra4
    coord = VECTOR(50,50)
    inicio = pygame.time.get_ticks()
    tiempo = 1000 #10segundos
'''

def temporalTextoSystema(texto):
    segundos = (pygame.time.get_ticks() - texto.inicio)/texto.tiempo
    if segundos < texto.tiempo:
        mostrarTextoSistema(texto)

def temporalTextoTTF(texto):
    segundos = (pygame.time.get_ticks() - texto.inicio)/texto.tiempo
    if segundos < texto.tiempo:
        mostrarTextoTTF(texto)        


def error(mensaje):

    ancho = 300
    alto = 300
    
    tablero = pygame.Surface((ancho,alto))  
    tablero.fill(blanco)
    
    font = pygame.font.SysFont('Arial', 24)
    paso = 10

    for texto in mensaje:
        text_surface = font.render(texto,True,negro)
        tablero.blit(text_surface, (10, paso))
        paso += 30

    ventana.blit(tablero,
                 (ANCHO//2-tablero.get_width()//2, 
                  ALTO//2-tablero.get_height()//2))

    
class textoError:
    texto = []
    inicio = pygame.time.get_ticks()
    tiempo = 100 #10segundos

def mostrarTextoError(mensaje):
    segundos = (pygame.time.get_ticks() - mensaje.inicio)/mensaje.tiempo
    if segundos < mensaje.tiempo:
        error(mensaje.texto)

class textoInfo:
    texto = ['',
             '',
             '']

def info(mensaje):

    ancho = 300
    alto = 300
    
    tablero = pygame.Surface((ancho,alto))  
    tablero.set_alpha(64)
    tablero.fill((220,20,60))
    
    font = pygame.font.SysFont('Arial', 24)
    paso = 10

    for texto in mensaje:
        text_surface = font.render(texto,True,negro)
        tablero.blit(text_surface, (10, paso))
        paso += 30

    ventana.blit(tablero,
                 (ANCHO//2-tablero.get_width()//2, 
                  ALTO//2-tablero.get_height()//2))


# LISTAS DE SPRITES:
SPRITES = pygame.sprite.Group()

PLATAFORMAS = pygame.sprite.Group()

CAMARA = pygame.sprite.Group()

COLISIONES = pygame.sprite.Group()   

PORTAL = pygame.sprite.Group()

OBJETOS = pygame.sprite.Group()

BASURAS = pygame.sprite.Group()

CHERRIES = pygame.sprite.Group()

ROTAN = pygame.sprite.Group()

GIRAN = pygame.sprite.Group()

INCLINADAS1 = pygame.sprite.Group()

INCLINADAS2 = pygame.sprite.Group()

offset = VECTOR((0,0))

def emptySprites():
    SPRITES.empty()
    PLATAFORMAS.empty()
    CAMARA.empty()
    COLISIONES.empty()
    PORTAL.empty()
    INCLINADAS1.empty()
    INCLINADAS2.empty()

def camara(jugador):
    offset.x = jugador.sprite.rect.centerx-MEDIO_ANCHO
    offset.y = jugador.sprite.rect.centery-MEDIO_ALTO
    for sprite in CAMARA:
        offset_pos = sprite.rect.topleft-offset
        if sprite in ROTAN:
            sprite_x = offset_pos.x + 25 * math.cos(math.radians(sprite.angulo))
            sprite_y = offset_pos.y + 25 * math.sin(math.radians(sprite.angulo))
            ventana.blit(sprite.image,(sprite_x, sprite_y))
        elif sprite in GIRAN:
            imagen_rotada = pygame.transform.rotate(sprite.image,sprite.angulo)
            ventana.blit(imagen_rotada,imagen_rotada.get_rect(center=(offset_pos.x,offset_pos.y)))      
        else:
            ventana.blit(sprite.image,offset_pos) 

def mapa(mapa):
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
                if capa.name == 'portal':
                    PORTAL.add(sprite)
                else:                   
                    PLATAFORMAS.add(sprite) 
                CAMARA.add(sprite)    
    if 'objetos' in [layer.name for layer in datos_mapa.layers]:            
        for objeto in datos_mapa.get_layer_by_name('objetos'):
            sprite = pygame.sprite.Sprite()
            sprite.image = objeto.image
            resized_image = pygame.transform.scale(sprite.image,(128,128))
            sprite.image = resized_image
            sprite.rect = sprite.image.get_rect() 
            sprite.rect.x = objeto.x*2
            sprite.rect.y = objeto.y*2
            CAMARA.add(sprite)            

# LISTA DE MAPAS:
mapa1 = './mapas/mapa1/mapa1.tmx'      
mapa2 = './mapas/mapa2/mapa2.tmx'        