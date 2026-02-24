from ayudas import *
from ventana1 import *
from ventana2 import *
from ventana3 import *
from ventana4 import *



# zona de variables

   

# zona de funciones
    


if __name__ == '__main__':

    #mostrarLetraSistema()

    

    while True:

        Ayudas.EVENTOS = pygame.event.get()

        for evento in Ayudas.EVENTOS:

            if evento.type == QUIT or (evento.type == KEYDOWN and evento.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_RIGHT:
                    Ayudas.ACCION = 'pausado_derecha'    
                if evento.key == pygame.K_LEFT:
                    Ayudas.ACCION = 'pausado_izquierda'    
                if evento.key == pygame.K_DOWN:
                    Ayudas.ACCION = 'pausado_bajando'     
                if evento.key == pygame.K_UP:
                    Ayudas.ACCION = 'pausado_subiendo'    
                if evento.key == pygame.K_RSHIFT:
                    Ayudas.ACCION = 'pausado_saltando_derecha'
                if evento.key == pygame.K_LSHIFT:
                    Ayudas.ACCION = 'pausado_saltando_izquierda'     

            if evento.type == pygame.KEYDOWN:    
                if evento.key == pygame.K_RSHIFT:
                    Ayudas.ACCION = 'saltando_derecha'
                if evento.key == pygame.K_LSHIFT:
                    Ayudas.ACCION = 'saltando_izquierda'    

        ventana.fill(verdeGris)

        eval(Ayudas.actual+'()')

        pygame.display.update()
        Ayudas.DT = RELOJ.tick(FPS)