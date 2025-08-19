import pygame
from ayudas import *

class progreso1:
    size = VECTOR(600,30)
    coord = VECTOR(10,10)
    color = azul
    progress = 0
    progress_increment = 1
    completed = False

def progreso(barra):

    pygame.draw.rect(ventana,
                    barra.color,
                    (barra.coord.x,barra.coord.y, 
                    int(barra.size.x*(barra.progress/100)), 
                    barra.size.y))
    
    pygame.draw.rect(ventana,(128, 128, 128), (barra.coord.x,barra.coord.y, barra.size.x, barra.size.y), 1)

    barra.progress = min(barra.progress + barra.progress_increment, 100)
    
    if barra.progress >= 100:
        barra.progress = 0
        barra.completed = True
        

if progreso1.completed:
    
    # TO-DO HERE
    progreso.completed = False
    progreso.progress = 0        