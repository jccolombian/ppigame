from ayudas import *
from pygame.sprite import Sprite
from jugador import *

class enemigo:
    sprite = None
    archivo = 'japonecita'
    imagen = './imagenes/japonecita/idle/1.png'
    size = VECTOR((46,81))
    coord = VECTOR((64,800))
    indice = 0
    movimientos = []
    velocidad = VECTOR((64,0))
    distanciaAtaque = 80
    distanciaDetecta = 360
    ataque_cooldown = 0  # Tiempo de espera tras atacar
    atacando = False
    retirada = 0  # Tiempo de retirada en frames
    animacion_ataque_activa = False
    tiempo_animacion_ataque = 0
    duracion_animacion_ataque = 6 # 6 imagenes para atacar

def animarEnemigo(jugador, archivo):
    """Cargar animaciones del enemigo"""
    
    def cargar_animacion(ruta):
        try:
            archivos = sorted([f for f in os.listdir(ruta) if f.endswith('.png')])
            return [pygame.image.load(os.path.join(ruta, f)).convert_alpha() for f in archivos]
        except FileNotFoundError:
            print(f"Error: No se encontró {ruta}")
            return []
    
    ruta_base = f'./imagenes/{archivo}'
    
    # Cargar animaciones

    caminar_derecha = cargar_animacion(f'{ruta_base}/run') # 0
    caminar_izquierda = [pygame.transform.flip(img, True, False) for img in caminar_derecha] # 1
    atacando_derecha = cargar_animacion(f'{ruta_base}/atacar') # 2
    atacando_izquierda = [pygame.transform.flip(img, True, False) for img in atacando_derecha] # 3
    esperando = cargar_animacion(f'{ruta_base}/idle') # 4

    jugador.movimientos = [caminar_derecha, caminar_izquierda, atacando_derecha, atacando_izquierda, esperando]

def crearEnemigo(jugador):
    sprite = Sprite()
    imagen = pygame.image.load(jugador.imagen).convert_alpha()
    sprite.image = pygame.transform.scale(imagen,(jugador.size.x,jugador.size.y))
    sprite.rect = sprite.image.get_rect() 
    sprite.rect.x = jugador.coord.x
    sprite.rect.y = jugador.coord.y  

    jugador.sprite = sprite
    jugador.hitbox = jugador.sprite.rect.inflate(-2,-2)
    animarEnemigo(jugador,jugador.archivo)
  
def enemigoAtaca(enemigo, jugador):
    # Calcular distancia y dirección
    dx = jugador.sprite.rect.centerx - enemigo.sprite.rect.centerx
    dy = jugador.sprite.rect.centery - enemigo.sprite.rect.centery
    distancia = math.hypot(dx, dy)

    # Si está en retirada, mostrar idle y no hacer nada
    if enemigo.retirada > 0:
        enemigo.retirada -= 1
        cargarAnimaciones(enemigo, 4)  # Idle
        return

    # Determinar dirección (derecha o izquierda)
    direccion = 'derecha' if dx > 0 else 'izquierda'
    indice_caminar = 0 if direccion == 'derecha' else 1
    indice_atacar = 2 if direccion == 'derecha' else 3

    # Si está fuera de rango de detección, mostrar idle
    if distancia > enemigo.distanciaDetecta:
        cargarAnimaciones(enemigo, 4)  # Idle
        return

    # Normalizar vector de dirección
    if distancia > 0:
        dx /= distancia
        dy /= distancia

    # Si está en rango de ataque
    if distancia <= enemigo.distanciaAtaque:
        # Si no está en cooldown, atacar
        if enemigo.ataque_cooldown <= 0:
            # Iniciar animación de ataque
            enemigo.animacion_ataque_activa = True
            enemigo.tiempo_animacion_ataque = enemigo.duracion_animacion_ataque
            cargarAnimaciones(enemigo, indice_atacar)  # Animación de ataque
            
            # Aplicar daño solo al iniciar el ataque
            jugador.vida -= 10
            
            # Configurar cooldowns
            enemigo.ataque_cooldown = 60  # 60 frames = 1 segundo (a 60 FPS)
            enemigo.retirada = 60  # 1 segundo de retirada
            enemigo.atacando = True
        
        # Controlar la duración de la animación de ataque
        if enemigo.animacion_ataque_activa:
            enemigo.tiempo_animacion_ataque -= 1
            
            # Cuando termina la animación de ataque, volver a idle
            if enemigo.tiempo_animacion_ataque <= 0:
                enemigo.animacion_ataque_activa = False
                cargarAnimaciones(enemigo, 4)  # Volver a idle
        else:
            # En cooldown pero sin animación activa, mostrar idle
            cargarAnimaciones(enemigo, 4)
    else:
        # Fuera de rango de ataque, perseguir
        cargarAnimaciones(enemigo, indice_caminar)  # Animación de caminar
        enemigo.sprite.rect.x += dx * enemigo.velocidad.x
        enemigo.sprite.rect.y += dy * enemigo.velocidad.x  # ← CORREGIDO: era .x

    # Reducir cooldown
    if enemigo.ataque_cooldown > 0:
        enemigo.ataque_cooldown -= 1