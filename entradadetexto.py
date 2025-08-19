import pygame

from ayudas import *

pygame.font.init()

class entradadetexto:
    entrada = None
    click = False
    texto = ''
    cursor = True
    font = letra4
    fontSize = 20
    colorInactivo = negro
    colorActivo = springgreen3
    eventoCursor = pygame.USEREVENT + 1
    pygame.time.set_timer(eventoCursor,500)
    coord = VECTOR(200,100)
    size = VECTOR(200,50)
    password = False

def activa(entrada):
    pos = pygame.mouse.get_pos()
    if pos[0] > entrada.entrada.left and pos[0] < entrada.entrada.left + entrada.size.x:
        if pos[1] > entrada.entrada.top and pos[1] < entrada.entrada.top + entrada.size.y:
            return True
    return False     

def activar(entrada):

    if len(entrada.texto) > 0 and entrada.texto[-1] == '|':
        entrada.texto = entrada.texto[:-1] 
    entrada.cursor = False

    color = entrada.colorInactivo

    if activa(entrada):
        entrada.cursor = True 
        color = entrada.colorActivo    

    for evento in Ayudas.EVENTOS:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if entrada.entrada.collidepoint(evento.pos):
                entrada.click = True    
            else:
                entrada.click = False      

        if evento.type == pygame.KEYDOWN:  
            if entrada.click:
                if evento.key == pygame.K_BACKSPACE or evento.key == pygame.K_DELETE:
                    entrada.size.x -=20
                    entrada.texto = entrada.texto[:-1]
                else:
                    entrada.texto += evento.unicode

    letra = pygame.font.SysFont(entrada.font,entrada.fontSize)
    contenido = letra.render(entrada.texto,True,entrada.colorActivo)    

    if entrada.password:
        contenido = letra.render('*'*len(entrada.texto),True,entrada.colorActivo)

    for evento in Ayudas.EVENTOS:
        if evento.type == entrada.eventoCursor:
            if entrada.cursor:
                contenido = letra.render(entrada.texto+'|',True,entrada.colorActivo)   
                entrada.cursor = False
            else:
                entrada.cursor = False

    entrada.size.x = max(entrada.size.x,contenido.get_width() + 15)

    pygame.draw.rect(ventana,color,entrada.entrada,2)    

    ventana.blit(
        contenido,
        (entrada.coord.x + 5, 
         entrada.coord.y + (entrada.size.y/2 - contenido.get_height()/2))
    )                                       

def entrada(entrada):
    caja = pygame.Rect(entrada.coord.x,entrada.coord.y,entrada.size.x,entrada.size.y)
    entrada.entrada = pygame.draw.rect(ventana,entrada.colorInactivo,caja,2)
    activar(entrada)

def resetear(entrada):
    letra = pygame.font.SysFont(entrada.font,entrada.fontSize)
    contenido = letra.render('',True,entrada.colorInactivo) 

    ventana.blit(
        contenido,
        (entrada.coord.x+5,entrada.coord.y + (entrada.size.y/2 - contenido.get_height()/2) )
    )       

    entrada.click = False
    entrada.texto = ''
    entrada.size.x = 200