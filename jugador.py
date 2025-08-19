import pygame

from pygame.sprite import Sprite

from ayudas import *

'''
class Jugador:
    sprite = None
    archivo = 'Jugador'
    imagen = './imagenes/.png'
    size = VECTOR((64,128))
    coord = VECTOR((32,64))
    velocidad = VECTOR((0,0))
    indice = 0
    movimientos = []
    saltando = False
    enTierra = True
    sonido_saltando = #poner variable de audio
'''  

def mover(jugador):

    variacion = VECTOR((0,0))

    teclas = pygame.key.get_pressed()

    if not Ayudas.ACCION == 'dead':

        if teclas[K_RIGHT]:
            Ayudas.ACCION = 'derecha'
            variacion.x += 4 
            cargarAnimaciones(jugador,0)
            jugador.enTierra = False

        elif teclas[K_LEFT]:
            Ayudas.ACCION = 'izquierda'
            variacion.x -= 4
            cargarAnimaciones(jugador,1)
            jugador.enTierra = False

        elif Ayudas.ACCION == 'pausado_derecha':
            cargarAnimaciones(jugador,2)    
            jugador.enTierra = True

        elif Ayudas.ACCION == 'pausado_izquierda':
            cargarAnimaciones(jugador,3)   
            jugador.enTierra = True
            
        elif teclas[pygame.K_RSHIFT] and not jugador.saltando:
            jugador.sonido_saltando.play()
            jugador.velocidad.y = -30
            cargarAnimaciones(jugador,4)  
            jugador.enTierra = False
            jugador.saltando = True

        elif teclas[pygame.K_LSHIFT] and not jugador.saltando:
            jugador.sonido_saltando.play()
            jugador.velocidad.y = -30
            cargarAnimaciones(jugador,5)    
            jugador.enTierra = False 
            jugador.saltando = True

        if not jugador.enTierra:
            jugador.velocidad.y += 2

        if jugador.velocidad.y > 30:
            jugador.velocidad.y = 25    

        variacion.y += jugador.velocidad.y    

        for plataforma in PLATAFORMAS:    
            # colision en x:
            if plataforma.rect.colliderect(jugador.sprite.rect.x + variacion.x,
                                        jugador.sprite.rect.y, 
                                        jugador.size.x,jugador.size.y):
                
                variacion.x = 0     

            # colision en y:          
            if plataforma.rect.colliderect(jugador.sprite.rect.x,
                                        jugador.sprite.rect.y+variacion.y, 
                                        jugador.size.x,jugador.size.y):
                
                # saltando y por debajo del suelo:
                if jugador.velocidad.y < 0:
                    variacion.y = plataforma.rect.bottom-jugador.sprite.rect.top
                    jugador.velocidad.y = 0
                # callendo y por encima del suelo:    
                elif jugador.velocidad.y >= 0:
                    variacion.y = plataforma.rect.top-jugador.sprite.rect.bottom    
                    jugador.velocidad.y = 0
                    jugador.saltando = False # Para volver a saltar de nuevo

        for plataforma in INCLINADAS1:
            
            # colision en y:          
            if jugador.sprite.rect.colliderect(plataforma.rect):

                

                if Ayudas.ACCION == 'derecha': # subiendo superficie inclinada
                    variacion.x += 2
                    variacion.y -= 4
                    jugador.velocidad.y = 0

                elif Ayudas.ACCION == 'izquierda':  # bajando superficie inclinada
                    variacion.x -= 2
                    variacion.y += 1
                    jugador.velocidad.y = 0  

                elif jugador.velocidad.y >= 0:
                    variacion.y = plataforma.rect.top-jugador.sprite.rect.bottom  + 11 
                    jugador.velocidad.y = 0
                    jugador.saltando = False # Para volver a saltar de nuevo    

        for plataforma in INCLINADAS2:
            
            # colision en y:          
            if jugador.sprite.rect.colliderect(plataforma.rect):
                
                
                
                if Ayudas.ACCION == 'derecha':  # bajando superficie inclinada
                    variacion.x += 2
                    variacion.y += 1
                    jugador.velocidad.y = 0

                elif Ayudas.ACCION == 'izquierda':  # subiendo superficie inclinada
                    variacion.x -= 2
                    variacion.y -= 3.5
                    jugador.velocidad.y = 0

                elif jugador.velocidad.y >= 0:
                    variacion.y = plataforma.rect.top-jugador.sprite.rect.bottom + 11
                    jugador.velocidad.y = 0
                    jugador.saltando = False # Para volver a saltar de nuevo    

        jugador.sprite.rect.x += variacion.x
        jugador.sprite.rect.y += variacion.y 
             

      

def cargarAnimaciones(jugador,animacion):
    animaciones = jugador.movimientos[animacion]
    jugador.indice = moverAnimaciones(animaciones,jugador.indice)
    jugador.sprite.image = animaciones[jugador.indice]     


def moverAnimaciones(animaciones,actual):

    if actual < len(animaciones)-1:
        actual += 1    
    else:
        actual = 0    

    return actual     

   
def moverIzquierdaDerecha(jugador,limiteIzquierdo,limiteDerecho):

    jugador.coord.x -= 1 * jugador.direccion

    if jugador.direccion > 0: 
        
        animaciones = jugador.movimientos[1]

        for event in Ayudas.EVENTOS:
            if event.type == jugador.VELOCIDAD_ANIMACIONES:
                if jugador.indice < len(animaciones)-1:
                    jugador.indice += 1    
                else:
                    jugador.indice = 0    

        jugador.sprite.image = animaciones[jugador.indice] 
    else:      
        animaciones = jugador.movimientos[0]
        
        for event in Ayudas.EVENTOS:
            if event.type == jugador.VELOCIDAD_ANIMACIONES:
                if jugador.indice < len(animaciones)-1:
                    jugador.indice += 1    
                else:
                    jugador.indice = 0   

        jugador.sprite.image = animaciones[jugador.indice] 

    if jugador.coord.x <= limiteIzquierdo:
        jugador.direccion *= -1

    if jugador.coord.x >= limiteDerecho:
        jugador.direccion *= -1
        
    jugador.sprite.rect.topleft = jugador.coord
           

def estanCerca(jugador1, jugador2,umbral):
    rect1 = jugador1.sprite.rect
    rect2 = jugador2.sprite.rect
    distancia = math.sqrt((rect1.centerx - rect2.centerx) ** 2 + (rect1.centery - rect2.centery) ** 2)
    
    if distancia < umbral and not rect1.colliderect(rect2):
        return True  
    return False           

def animaciones(jugador,archivo):

    # caminar_derecha:
    caminar_derecha = []

    for i in range(1,len(os.listdir(f'./imagenes/{archivo}/run'))+1):
        img = pygame.image.load(f'./imagenes/{archivo}/run/{i}.png').convert_alpha()
        caminar_derecha.append(
            pygame.transform.scale(img,(img.get_width(),img.get_height()))
        )
    jugador.movimientos.append(caminar_derecha) # indice 0

    # caminar_izquierda
    caminar_izquierda = []
    for sprite in caminar_derecha:
        caminar_izquierda.append(pygame.transform.flip(sprite,True,False))#imagen,horizontal,vertical
    jugador.movimientos.append(caminar_izquierda) # 1

    # Inactivo derecha:
    inactivo_derecha = []
    for i in range(1,len(os.listdir(f'./imagenes/{archivo}/idle'))+1):
        img = pygame.image.load(f'./imagenes/{archivo}/idle/{i}.png').convert_alpha()
        inactivo_derecha.append(
            pygame.transform.scale(img,(img.get_width(),img.get_height()))
        )
    jugador.movimientos.append(inactivo_derecha) # 2

    # Inactivo izquierda:
    inactivo_izquierda = []
    for sprite in inactivo_derecha:
        inactivo_izquierda.append(pygame.transform.flip(sprite,True,False))#imagen,horizontal,vertical
    jugador.movimientos.append(inactivo_izquierda) # 3

    # saltar_derecha:
    saltar_derecha = []
    for i in range(1,len(os.listdir(f'./imagenes/{archivo}/jump'))+1):
        img = pygame.image.load(f'./imagenes/{archivo}/jump/{i}.png').convert_alpha()
        saltar_derecha.append(
            pygame.transform.scale(img,(img.get_width(),img.get_height()))
        )
    jugador.movimientos.append(saltar_derecha) # 4

    # saltar izquierda:
    saltar_izquierda = []
    for sprite in saltar_derecha:
        saltar_izquierda.append(pygame.transform.flip(sprite,True,False))#imagen,horizontal,vertical
    jugador.movimientos.append(saltar_izquierda) # 5
    
    '''
    # herir:
    herir = []
    for i in range(1,len(os.listdir(f'./imagenes/{archivo}/hurt'))+1):
        img = pygame.image.load(f'./imagenes/{archivo}/hurt/{i}.png').convert_alpha()
        herir.append(
            pygame.transform.scale(img,(img.get_width()*2,img.get_height()*2))
        )
    jugador.movimientos.append(herir) # 6   
    '''     

def jugador(jugador):

    sprite = Sprite()
    imagen = pygame.image.load(jugador.imagen).convert_alpha()
    sprite.image = pygame.transform.scale(imagen,(jugador.size.x,jugador.size.y))
    sprite.rect = sprite.image.get_rect() 
    sprite.rect.x = jugador.coord.x
    sprite.rect.y = jugador.coord.y  

    jugador.sprite = sprite

    animaciones(jugador,jugador.archivo)
     
