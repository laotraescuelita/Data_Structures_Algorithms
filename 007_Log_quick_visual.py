import pygame, sys, random, math, time
import numpy as np 

tamañoPantalla = (ancho, alto) = 640, 480
pygame.init()

pantalla = pygame.display.set_mode(tamañoPantalla) #Inicia el tamaño de la ventana
pygame.display.set_caption('Merge Sort') #El titulo en la ventana.
reloj = pygame.time.Clock() #Objeto que nos ayuda a establcer los frames.
columnas, filas = 64, 48 # Columnas y filas de la matriz que contendra a los objetos casillas.
#Ancho de las barras
n = 4
w = int(ancho/n) #El numero de casillas a lo largo.
h = alto//filas #El numero de casillas a lo alto.
vectorAlturas, vectorEstado = [], [] #Vectores que almacenan las alturas y los estados de cada barra.

c_blanco = (255, 255, 255)
c_rojo = (255, 0, 0)
c_verde = (0, 255, 0)

vectorAlturas = np.random.randint(low=0,high=ancho,size=w)
vectorEstado = [1]*w

def maps(num, in_min, in_max, out_min, out_max):
  return (num - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def partition(arr, start, end):
    for i in range(start, end):
        state[i] = 0
    i = start
    pivot = arr[end]
    state[start] = 0

    for j in range(start, end):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            state[i] += 1
            i+= 1
            state[i] = 0

    arr[i], arr[end] = arr[end], arr[i]
    return i

end = len(h_arr) - 1
start = 0
size = end - start + 1
stack = [0] * (size)

top = 0
stack[top] = 0
top += 1
stack[top] = end

j = 0

flag = False

while True:
    win.fill((10, 10, 10))

    if flag:
        if top >= 0:
            end = stack[top]
            top -= 1
            start = stack[top]
            top -= 1

            p = partition(h_arr, start, end)

            state[p] = 1
            if p-1 > start:
                top += 1
                stack[top] = start
                top += 1
                stack[top] = p - 1

            if p+1 < end:
                top += 1
                stack[top] = p+1
                top += 1
                stack[top] = end

        else:
            if j < len(h_arr):
                state[j] = 2
                j+=1

    for i in range(len(h_arr)):
        h_ar = maps(h_arr[i], 0, 400, 20, 255)
        pygame.draw.rect(win, (h_ar//3, h_ar, h_ar//4), pygame.Rect(int(i*n), (HEIGHT - h_arr[i])//2, n, h_arr[i]))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                flag = True 

    clock.tick(60)
    pygame.display.flip()    

