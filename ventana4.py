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

                if capa.name == 'casas' or capa.name == 'borde':
                    COLISIONES.add(sprite)

                if capa.name == 'cesped' or capa.name == 'camino':
                    FONDO.add(sprite)    

                CAMARA.add(sprite)   
                       
    
class canibalito2:
    sprite = None
    archivo = 'canibalito2'
    imagen = './imagenes/canibalito2/bajar/1.png'
    size = VECTOR((24,56))
    coord = VECTOR((1100,1000))
    velocidad = 32
    indice = 0
    movimientos = []
    saltando = False
    enTierra = True
    sonido_saltando = saltoJuancho
    dialogo = None
    dialogo_timer = 0

jugador2(canibalito2)

class junko:
    sprite = None
    archivo = 'junko'
    imagen = './imagenes/junko/bajar/1.png'
    size = VECTOR((17,38))
    coord = VECTOR((1000,700))
    velocidad = 32
    indice = 0
    movimientos = []
    # son necesarios si esta en 2d
    saltando = False
    enTierra = True
    sonido_saltando = saltoJuancho
    # son necesario si va a hablar
    dialogo = None
    dialogo_timer = 0
    # son necesarios si solo se mueve en una dirección y se devuelve
    direccion = 1
    VELOCIDAD_ANIMACIONES = pygame.USEREVENT + 1
    pygame.time.set_timer(VELOCIDAD_ANIMACIONES, FPS)

jugador2(junko)

def dibujarGloboDialogo(texto,jugador):

    letra = pygame.freetype.SysFont(arial, 20)
    relleno = 10
    color = blanco
    colortext = negro

    # Ajustar el texto si es demasiado largo
    palabras = texto.split(' ')
    lineas = []
    lineaactual = []
    ancho = 200

    for palabra in palabras:
            linea_cargada = ' '.join(lineaactual + [palabra])
            text_rect = letra.get_rect(linea_cargada)
            if text_rect.width <= ancho:
                lineaactual.append(palabra)
            else:
                if lineaactual:
                    lineas.append(' '.join(lineaactual))
                lineaactual = [palabra]    

    if lineaactual:
            lineas.append(' '.join(lineaactual))      

    # Calcular el tamaño del globo
    altura_linea = letra.get_sized_height()
    ancho_globo = max([letra.get_rect(linea).width for linea in lineas]) + relleno * 2
    altura_globo = len(lineas) * altura_linea + relleno * 2              

    # Colocar el globo sobre el sprite
    globo_x = jugador.sprite.rect.centerx - ancho_globo // 2 - (jugador.coord.x-MEDIO_ANCHO)
    globo_y = jugador.sprite.rect.top - altura_globo - 25 - (jugador.coord.y-MEDIO_ALTO) 


    # Dibujar el rectangulo del globo
    globo_rect = pygame.Rect(globo_x, globo_y, ancho_globo, altura_globo)
    pygame.draw.rect(ventana, color, globo_rect, border_radius=10)
    pygame.draw.rect(ventana, colortext, globo_rect, 2, border_radius=10)

    # Dibujar la punta (triángulo apuntando al sprite)
    cola_points = [
            (jugador.sprite.rect.centerx - (jugador.coord.x-MEDIO_ANCHO), globo_y + altura_globo + 15),
            (jugador.sprite.rect.centerx - (jugador.coord.x-MEDIO_ANCHO) - 5, globo_y + altura_globo),
            (jugador.sprite.rect.centerx - (jugador.coord.x-MEDIO_ANCHO) + 5, globo_y + altura_globo)
        ]
    
    pygame.draw.polygon(ventana, color, cola_points)
    pygame.draw.polygon(ventana, colortext, cola_points, 2)

    # Escribir el texto
    y_offset = globo_y + relleno
    for line in lineas:
        letra.render_to(ventana, (globo_x + relleno, y_offset), line, colortext)
        y_offset += altura_linea

# Secuencia de conversación
class conversacion:
    conversacion = [
        (canibalito2, "Hello! How are you today?", 2000),
        (canibalito2, "I'm doing great! Thanks for asking.", 2000),
        (canibalito2, "That's wonderful to hear!", 2000),
    ]
    conversacion_index = 0
    conversacion_timer = 0

# Handle conversation
def manejarConversación(conv,sprites):
    if conv.conversacion_index < len(conv.conversacion):
        if conv.conversacion_timer <= 0:
            sprite, text, duration = conv.conversacion[conv.conversacion_index]
            hablar(sprite,text, duration)
            conv.conversacion_timer = duration
            conv.conversacion_index += 1
        else:
            conv.conversacion_timer -= Ayudas.DT
    
    # Actualizar sprites y Dibujar globos de diálogo
    for sprit in sprites:
        actualizarDialogo(sprit, Ayudas.DT)
        if sprit.dialogo:
            dibujarGloboDialogo(sprit.dialogo,sprit)







def ventana4():

    emptySprites()

    cargarmapa(mapa3)

    CAMARA.add(canibalito2.sprite)

    CAMARA.add(junko.sprite)

    camara(canibalito2)

    mover2(canibalito2)

    manejarConversación(conversacion,[canibalito2])

    moverIzquierdaDerecha(junko,900,1100)

    #moverArribaAbajo(junko,600,800)