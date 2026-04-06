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
    vida = 100
    # son necesarios si esta en 2d
    saltando = False
    enTierra = True
    sonido_saltando = #poner variable de audio
    # son necesarios si va a hablar
    dialogo = None
    dialogo_timer = 0
    # son necesarios si solo se mueve en una dirección y se devuelve
    direccion = 1
    VELOCIDAD_ANIMACIONES = pygame.USEREVENT + 1
    pygame.time.set_timer(VELOCIDAD_ANIMACIONES, 800)
'''  

def mover(jugador):

    variacion = VECTOR((0,0))

    teclas = pygame.key.get_pressed()

    if Ayudas.ACCION == 'dead':
        return

    if teclas[K_RIGHT]:
        Ayudas.ACCION = 'derecha'
        variacion.x += 4 
        cargarAnimaciones(jugador,0)

    elif teclas[K_LEFT]:
        Ayudas.ACCION = 'izquierda'
        variacion.x -= 4
        cargarAnimaciones(jugador,1)

    elif Ayudas.ACCION == 'pausado_derecha':
        cargarAnimaciones(jugador,2)    
        
    elif Ayudas.ACCION == 'pausado_izquierda':
        cargarAnimaciones(jugador,3)   
        
    # --- SALTO ---
    if (teclas[pygame.K_RSHIFT] or teclas[pygame.K_LSHIFT]) and not jugador.saltando and jugador.enTierra:
        jugador.sonido_saltando.play()
        jugador.velocidad.y = -30
        cargarAnimaciones(jugador, 4)
        jugador.saltando = True
        jugador.enTierra = False

    # --- GRAVEDAD ---
    if not jugador.enTierra:
        jugador.velocidad.y += 2
        if jugador.velocidad.y > 30:
            jugador.velocidad.y = 25   

    variacion.y += jugador.velocidad.y    

    # --- COLISIONES ---
    rect_jugador = pygame.Rect(
        jugador.sprite.rect.x + variacion.x,
        jugador.sprite.rect.y + variacion.y,
        jugador.size.x,
        jugador.size.y
    )

    # Colisiones con plataformas normales
    _colisionar_plataformas(jugador, variacion, PLATAFORMAS, False)
    
    # Colisiones con plataformas inclinadas
    _colisionar_plataformas(jugador, variacion, INCLINADAS1, True)
    _colisionar_plataformas(jugador, variacion, INCLINADAS2, True)

    # --- APLICAR MOVIMIENTO ---
    jugador.sprite.rect.x += variacion.x
    jugador.sprite.rect.y += variacion.y

def _colisionar_plataformas(jugador, variacion, plataformas, inclinada=False):
    """Maneja colisiones con un grupo de plataformas"""
    
    rect_jugador = pygame.Rect(
        jugador.sprite.rect.x + variacion.x,
        jugador.sprite.rect.y + variacion.y,
        jugador.size.x,
        jugador.size.y
    )

    for plataforma in plataformas:
        if not rect_jugador.colliderect(plataforma.rect):
            continue

        if inclinada:
            _colisionar_inclinada(jugador, variacion, plataforma)
        else:
            _colisionar_normal(jugador, variacion, plataforma)

def _colisionar_normal(jugador, variacion, plataforma):
    """Colisión con plataforma horizontal"""
    
    # Colisión en X
    rect_x = pygame.Rect(
        jugador.sprite.rect.x + variacion.x,
        jugador.sprite.rect.y,
        jugador.size.x,
        jugador.size.y
    )
    if rect_x.colliderect(plataforma.rect):
        variacion.x = 0

    # Colisión en Y
    if jugador.velocidad.y < 0:  # Saltando (golpeando techo)
        variacion.y = plataforma.rect.bottom - jugador.sprite.rect.top
    elif jugador.velocidad.y >= 0:  # Cayendo (pisando suelo)
        variacion.y = plataforma.rect.top - jugador.sprite.rect.bottom
        jugador.saltando = False
        jugador.enTierra = True

    jugador.velocidad.y = 0

def _colisionar_inclinada(jugador, variacion, plataforma):
    """Colisión con plataforma inclinada"""
    
    if Ayudas.ACCION == 'derecha':
        variacion.x += 2
        variacion.y -= 4
    elif Ayudas.ACCION == 'izquierda':
        variacion.x -= 2
        variacion.y += 1
    elif jugador.velocidad.y >= 0:
        variacion.y = plataforma.rect.top - jugador.sprite.rect.bottom + 11
        jugador.saltando = False
        jugador.enTierra = True

    jugador.velocidad.y = 0         

def cargarAnimaciones(jugador, animacion):
    """Carga y actualiza la animación del jugador"""
    
    # Validaciones
    if not jugador.movimientos or animacion >= len(jugador.movimientos):
        return
    
    animaciones = jugador.movimientos[animacion]
    
    if not animaciones:
        return
    
    # Mover a la siguiente imagen
    jugador.indice = moverAnimaciones(animaciones, jugador.indice)
    jugador.sprite.image = animaciones[jugador.indice]  

def moverAnimaciones(animaciones, actual):
    """Avanza al siguiente frame de la animación"""
    
    if actual < len(animaciones) - 1:
        return actual + 1
    else:
        return 0     

def moverIzquierdaDerecha(jugador, limiteIzquierdo, limiteDerecho):

    # Mover jugador
    jugador.coord.x -= 2 * jugador.direccion
    
    # Actualizar animación
    animaciones = jugador.movimientos[1 if jugador.direccion > 0 else 0]
    for event in Ayudas.EVENTOS:
        if event.type == jugador.VELOCIDAD_ANIMACIONES:
            jugador.indice = (jugador.indice + 1) % len(animaciones)
            break
    
    jugador.sprite.image = animaciones[jugador.indice]
    
    # Verificar condiciones de cambio de dirección
    if jugador.coord.x <= limiteIzquierdo:
        jugador.direccion *= -1
    
    if jugador.coord.x >= limiteDerecho:
        jugador.direccion *= -1
    
    jugador.sprite.rect.topleft = jugador.coord

def moverArribaAbajo(jugador,limiteArriba,limiteAbajo):
    # Mover jugador
    jugador.coord.y -= 2 * jugador.direccion
    
    # Actualizar animación
    animaciones = jugador.movimientos[3 if jugador.direccion > 0 else 2]
    for event in Ayudas.EVENTOS:
        if event.type == jugador.VELOCIDAD_ANIMACIONES:
            jugador.indice = (jugador.indice + 1) % len(animaciones)
            break
    
    jugador.sprite.image = animaciones[jugador.indice]
    
    # Verificar condiciones de cambio de dirección
    if jugador.coord.y <= limiteArriba:
        jugador.direccion *= -1
    
    if jugador.coord.y >= limiteAbajo:
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
        
def animaciones2(jugador, archivo):
    """Cargar animaciones del jugador"""
    
    def cargar_animacion(ruta):
        try:
            archivos = sorted([f for f in os.listdir(ruta) if f.endswith('.png')])
            return [pygame.image.load(os.path.join(ruta, f)).convert_alpha() for f in archivos]
        except FileNotFoundError:
            print(f"Error: No se encontró {ruta}")
            return []
    
    ruta_base = f'./imagenes/{archivo}'
    
    # Cargar animaciones
    derecha = cargar_animacion(f'{ruta_base}/derecha')
    izquierda = [pygame.transform.flip(img, True, False) for img in derecha]
    bajar = cargar_animacion(f'{ruta_base}/bajar')
    subir = cargar_animacion(f'{ruta_base}/subir')
    esperando = cargar_animacion(f'{ruta_base}/esperando')
    esperando2 = cargar_animacion(f'{ruta_base}/esperando2')
    
    jugador.movimientos = [derecha, izquierda, bajar, subir, esperando, esperando2]
  
def jugador2(jugador):

    sprite = Sprite()
    imagen = pygame.image.load(jugador.imagen).convert_alpha()
    sprite.image = pygame.transform.scale(imagen,(jugador.size.x,jugador.size.y))
    sprite.rect = sprite.image.get_rect() 
    sprite.rect.x = jugador.coord.x
    sprite.rect.y = jugador.coord.y  

    jugador.sprite = sprite
    jugador.hitbox = jugador.sprite.rect.inflate(-2, -2)

    animaciones2(jugador,jugador.archivo)

def jugador(jugador):

    sprite = Sprite()
    imagen = pygame.image.load(jugador.imagen).convert_alpha()
    sprite.image = pygame.transform.scale(imagen,(jugador.size.x,jugador.size.y))
    sprite.rect = sprite.image.get_rect() 
    sprite.rect.x = jugador.coord.x
    sprite.rect.y = jugador.coord.y  

    jugador.sprite = sprite

    animaciones(jugador,jugador.archivo)

def mover2(jugador):

    jugador.direccion = pygame.math.Vector2()

    tecla = pygame.key.get_pressed()

    if tecla[pygame.K_UP]:
        Ayudas.ACCION = 'subiendo'
        jugador.direccion.y = -jugador.velocidad
        cargarAnimaciones(jugador,3)
    elif tecla[pygame.K_DOWN]:
        Ayudas.ACCION = 'bajando'
        jugador.direccion.y = jugador.velocidad
        #jugador.sonido_saltando.play()
        cargarAnimaciones(jugador,2)
    else:
        jugador.direccion.y = 0

    if tecla[pygame.K_RIGHT]:
        Ayudas.ACCION = 'derecha'
        jugador.direccion.x = jugador.velocidad
        cargarAnimaciones(jugador,0)
    elif tecla[pygame.K_LEFT]:
        Ayudas.ACCION = 'izquierda'
        jugador.direccion.x = -jugador.velocidad
        cargarAnimaciones(jugador,1)
    else:
        jugador.direccion.x = 0

    if Ayudas.ACCION == 'pausado_derecha':
        cargarAnimaciones(jugador,4)

    if Ayudas.ACCION == 'pausado_izquierda':
        cargarAnimaciones(jugador,4)    

    if Ayudas.ACCION == 'pausado_bajando':
        cargarAnimaciones(jugador,4)      

    if Ayudas.ACCION == 'pausado_subiendo':
        cargarAnimaciones(jugador,5)     

    if jugador.direccion.magnitude() != 0:
        jugador.direccion = jugador.direccion.normalize()

    if Ayudas.ACCION == 'saltando_derecha':
        jugador.direccion.y = -2
        jugador.direccion.x = 3
        cargarAnimaciones(jugador,0)

    if Ayudas.ACCION == 'pausado_saltando_derecha':
        jugador.direccion.y = 2
        jugador.direccion.x = 0
        cargarAnimaciones(jugador,0)   
        Ayudas.ACCION = 'pausado_derecha'  

    if Ayudas.ACCION == 'saltando_izquierda':
        jugador.direccion.y = -2
        jugador.direccion.x = -3
        cargarAnimaciones(jugador,1)

    if Ayudas.ACCION == 'pausado_saltando_izquierda':
        jugador.direccion.y = 2
        jugador.direccion.x = 0
        cargarAnimaciones(jugador,1)   
        Ayudas.ACCION = 'pausado_izquierda'    

    jugador.hitbox.center += jugador.direccion*jugador.velocidad

    jugador.sprite.rect.center = jugador.hitbox.center    
     
    
    for plataforma in COLISIONES:   
            if plataforma.rect.colliderect(jugador.hitbox):
                if Ayudas.ACCION == 'derecha':
                    jugador.hitbox.right = plataforma.rect.left      
                if Ayudas.ACCION == 'izquierda':
                    jugador.hitbox.left = plataforma.rect.right    
                if Ayudas.ACCION == 'subiendo':
                    jugador.hitbox.top = plataforma.rect.bottom
                if Ayudas.ACCION == 'bajando':
                    jugador.hitbox.bottom = plataforma.rect.top        

def hablar(jugador, texto, duracion=3000):
        """Hacer que el sprite diga algo durante un tiempo (en milisegundos)"""
        jugador.dialogo = texto
        jugador.dialogo_timer = duracion       

def actualizarDialogo(jugador, dt):
        """Actualizar el temporizador de diálogo"""
        if jugador.dialogo_timer > 0:
            jugador.dialogo_timer -= dt
            if jugador.dialogo_timer <= 0:
                jugador.dialogo = None                  