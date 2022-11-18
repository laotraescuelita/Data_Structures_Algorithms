import pygame, sys, random, math
from collections import deque
from tkinter import messagebox, Tk

tamañoPantalla = (ancho, alto) = 640, 480
pygame.init()

pantalla = pygame.display.set_mode(tamañoPantalla) #Inicia el tamaño de la ventana
pygame.display.set_caption('Dijkstra') #El titulo en la ventana.
reloj = pygame.time.Clock() #Objeto que nos ayuda a establcer los frames.
columnas, filas = 64, 48 # Columnas y filas de la matriz que contendra a los objetos casillas.
w = ancho//columnas #El numero de casillas a lo largo.
h = alto//filas #El numero de casillas a lo alto.

parrilla, recorrido = [], []
queue, visited = deque(), []

class Casilla:
    def __init__(self, i, j):
        self.x, self.y = i, j
        self.f, self.g, self.h = 0, 0, 0
        self.vecinos = []
        self.anterior = None
        self.obstaculo = False
        self.visitado = False
        if random.randint(0, 100) < 20:
            self.obstaculo = True
        
    def mostrar(self, pantalla, color):
        if self.obstaculo == True:
            color = (0, 0, 0)
        pygame.draw.rect(pantalla, color, (self.x*w, self.y*h, w-1, h-1))
    
    def agregarVecinos(self, parrilla):
        if self.x < columnas - 1:
            self.vecinos.append(parrilla[self.x+1][self.y])
        if self.x > 0:
            self.vecinos.append(parrilla[self.x-1][self.y])
        if self.y < filas - 1:
            self.vecinos.append(parrilla[self.x][self.y+1])
        if self.y > 0:
            self.vecinos.append(parrilla[self.x][self.y-1])
        #Add Diagonals
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
inicio.obstaculo = False
fin.obstaculo = False

queue.append(inicio)
inicio.visitado = True

def main():
    flag = False
    noflag = True
    startflag = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    startflag = True

        if startflag:
            if len(queue) > 0:
                current = queue.popleft()
                if current == fin:
                    temp = current
                    while temp.anterior:
                        recorrido.append(temp.anterior)
                        temp = temp.anterior
                    if not flag:
                        flag = True
                        print("Done")
                    elif flag:
                        continue
                if flag == False:
                    for i in current.vecinos:
                        if not i.visitado and not i.obstaculo:
                            i.visitado = True
                            i.anterior = current
                            queue.append(i)
            else:
                if noflag and not flag:
                    Tk().wm_withdraw()
                    messagebox.showinfo("No Solution", "There was no solution" )
                    noflag = False
                else:
                    continue


        pantalla.fill((0, 20, 20))
        for i in range(columnas):
            for j in range(filas):
                casilla = parrilla[i][j]
                casilla.mostrar(pantalla, (44, 62, 80))
                if casilla in recorrido:
                    casilla.mostrar(pantalla, (46, 204, 113))
                    casilla.mostrar(pantalla, (192, 57, 43), 0)
                elif casilla.visitado:
                    casilla.mostrar(pantalla, (39, 174, 96))
                if casilla in queue and not flag:
                    casilla.mostrar(pantalla, (44, 62, 80))
                    casilla.mostrar(pantalla, (39, 174, 96))
                if casilla == inicio:
                    casilla.mostrar(pantalla, (0, 255, 200))
                if casilla == fin:
                    casilla.mostrar(pantalla, (0, 120, 255))
                
                
        pygame.display.flip()


main()