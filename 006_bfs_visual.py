import pygame, sys, random, math
from collections import deque
from tkinter import messagebox, Tk

tamañoPantalla = (ancho, alto) = 640, 480
pygame.init()

ventana = pygame.display.set_mode(tamañoPantalla) #Inicia el tamaño de la ventana
pygame.display.set_caption('Breadth First Search') #El titulo en la ventana.
reloj = pygame.time.Clock() #Objeto que nos ayuda a establcer los frames.

columnas, filas = 64, 48 # Columnas y filas de la matriz que contendra a los objetos casillas.

w = ancho//columnas #El numero de casillas a lo largo.
h = alto//filas #El numero de casillas a lo alto.

enCola, visitado, recorrido, parrilla = [], [], [], []

class Casilla:
    def __init__(self, i, j):
        self.x, self.y = i, j
        self.f, self.g, self.h = 0, 0, 0
        self.vecinos = []
        self.anterior = None
        self.obstaculo = False
        self.visitado = False
        if random.randint(0, 100) < 20: #Casillas con obstaculo al azar.
            self.obstaculo = True
        
    def mostrar(self, ventana, color):
        if self.obstaculo == True:
            color = (0, 0, 0)
        pygame.draw.rect(ventana, color, (self.x*w, self.y*h, w-1, h-1))
    
    def agregarVecinos(self, parrilla):
        if self.x < columnas - 1:
            self.vecinos.append(parrilla[self.x+1][self.y])
        if self.x > 0:
            self.vecinos.append(parrilla[self.x-1][self.y])
        if self.y < filas - 1:
            self.vecinos.append(parrilla[self.x][self.y+1])
        if self.y > 0:
            self.vecinos.append(parrilla[self.x][self.y-1])
        #Agrgar Diagonales
        if self.x < columnas - 1 and self.y < filas - 1:
            self.vecinos.append(parrilla[self.x+1][self.y+1])
        if self.x < columnas - 1 and self.y > 0:
            self.vecinos.append(parrilla[self.x+1][self.y-1])
        if self.x > 0 and self.y < filas - 1:
            self.vecinos.append(parrilla[self.x-1][self.y+1])
        if self.x > 0 and self.y > 0:
            self.vecinos.append(parrilla[self.x-1][self.y-1])


#Aquí se coloca cada objeto casilla dentro de la matriz parrilla.
for i in range(columnas):
    vector = []
    for j in range(filas):
        vector.append(Casilla(i, j))
    parrilla.append(vector)

# Se agregan los vecinos en la matriz parrilla.
for i in range(columnas):
    for j in range(filas):
        parrilla[i][j].agregarVecinos(parrilla)
 
#Se establece el nodo inicio y final y además se deja claro que no pueden ser obstaculos.
inicio = parrilla[columnas//8][filas//8]
fin = parrilla[filas//2][columnas//2]
inicio.wall = False
fin.wall = False

#La cola almacena el nodo inicio como vistado y su propiedad cambia a visitado
enCola.append(inicio)
inicio.visited = True 

#Todo el procedimiento esta dentro de la funciónmain
def main():
    flag = False
    noflag = True
    startflag = False

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #El programa incia al presionar enter.
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    startflag = True

        #Aquí inicia el algoritmo que recorre la parrilla.
        if startflag:
            if len(enCola) > 0:
                casillaActual = enCola.pop()
                
                if casillaActual == fin:
                    temporal = casillaActual
                    while temporal.anterior:
                        recorrido.append(temporal.anterior)
                        temporal = temporal.anterior
                    if not flag:
                        flag = True
                        print("Terminado")                        
                    elif flag:
                        continue
                
                if flag == False:
                    for i in casillaActual.vecinos:
                        if not i.visitado and not i.obstaculo:
                            i.visitado = True
                            i.anterior = casillaActual
                            enCola.append(i)
            else:
                if noflag and not flag:
                    Tk().wm_withdraw()
                    messagebox.showinfo("No hay solución.", "No hubo solución." )
                    noflag = False
                else:
                    continue


        ventana.fill((0, 20, 20))
        
        for i in range(columnas):
            for j in range(filas):
                casilla = parrilla[i][j]
                casilla.mostrar(ventana, (255, 255, 255))
                if casilla in recorrido:
                    casilla.mostrar(ventana, (25, 120, 250))
                elif casilla.visitado:
                    casilla.mostrar(ventana, (255, 0, 0))
                if casilla in enCola:
                    casilla.mostrar(ventana, (0, 255, 0))
                if casilla == fin:
                    casilla.mostrar(ventana, (0, 120, 255))
                
                
        pygame.display.flip()


main()

