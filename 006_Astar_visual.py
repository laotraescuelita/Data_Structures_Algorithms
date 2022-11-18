import pygame, sys, random, math
from tkinter import messagebox, Tk

tamañoPantalla = (ancho, alto) = 600, 600

pygame.init()
pantalla = pygame.display.set_mode(tamañoPantalla)
pygame.display.set_caption('A star') #El titulo en la ventana.
reloj = pygame.time.Clock()
columnas, filas = 50, 50
recorrido, parrilla, conjuntoAbierto, conjuntoCerrado = [], [], [], []

w = ancho//columnas
h = alto//filas

class Casilla:
    def __init__(self, i, j):
        self.x, self.y = i, j
        self.f, self.g, self.h = 0, 0, 0
        self.vecinos = []
        self.anterior = None
        self.obstaculo = False
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
          
def heuristica(a, b):
    return math.sqrt((a.x - b.x)**2 + abs(a.y - b.y)**2)

for i in range(columnas):
    vector = []
    for j in range(filas):
        vector.append(Casilla(i, j))
    parrilla.append(vector)

for i in range(columnas):
    for j in range(filas):
        parrilla[i][j].agregarVecinos(parrilla)

inicio = parrilla[0][0]
fin = parrilla[filas//2][columnas//2]

conjuntoAbierto.append(inicio)
 
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
            if len(conjuntoAbierto) > 0:
                winner = 0
                for i in range(len(conjuntoAbierto)):
                    if conjuntoAbierto[i].f < conjuntoAbierto[winner].f:
                        winner = i

                current = conjuntoAbierto[winner]
                
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
                    conjuntoAbierto.remove(current)
                    conjuntoCerrado.append(current)

                    for vecino in current.vecinos:
                        if vecino in conjuntoCerrado or vecino.obstaculo:
                            continue
                        tempG = current.g + 1

                        nuevoRecorrido = False
                        if vecino in conjuntoAbierto:
                            if tempG < vecino.g:
                                vecino.g = tempG
                                
                                nuevoRecorrido = True
                        else:
                            vecino.g = tempG
                            nuevoRecorrido = True
                            conjuntoAbierto.append(vecino)
                        
                        if nuevoRecorrido:
                            vecino.h = heuristica(vecino, fin)
                            vecino.f = vecino.g + vecino.h
                            vecino.anterior  = current

            else:
                if noflag:
                    Tk().wm_withdraw()
                    messagebox.showinfo("No Solution", "There was no solution" )
                    noflag = False

        pantalla.fill((0, 20, 20))
        for i in range(columnas):
            for j in range(filas):
                casilla = parrilla[j][i]
                casilla.mostrar(pantalla, (255, 255, 255))
                if flag and casilla in recorrido:
                    casilla.mostrar(pantalla, (25, 120, 250))
                elif casilla in conjuntoCerrado:
                    casilla.mostrar(pantalla, (255, 0, 0))
                elif casilla in conjuntoAbierto:
                    casilla.mostrar(pantalla, (0, 255, 0))
                try:
                    if casilla == fin:
                        casilla.mostrar(pantalla, (0, 120, 255))
                except Exception:
                    pass
                
        pygame.display.flip()



main()