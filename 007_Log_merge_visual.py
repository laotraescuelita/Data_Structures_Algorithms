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

def mergeSort(a):      
    current_size = 1      
    
    while current_size < len(a) - 1:            
        left = 0    
        while left < len(a)-1:          
            
            mid = min((left + current_size - 1),(len(a)-1)) 
            right = ((2 * current_size + left - 1,  
                    len(a) - 1)[2 * current_size  
                        + left - 1 > len(a)-1])  
                              
            merge(a, left, mid, right)  
            left = left + current_size*2
              
        
        current_size = 2 * current_size  
 

def merge(a, l, m, r):  
    n1 = m - l + 1
    n2 = r - m  
    L = [0] * n1  
    R = [0] * n2  
    for i in range(0, n1):  
        L[i] = a[l + i]
        state[i] = 0 
        for j in range(len(h_arr)):
            if state[j] == 0:
                color = RED
            elif state[j] == 2:
                color = GREEN
            else:
                color = WHITE
            pygame.draw.rect(win, color, pygame.Rect(j*n, HEIGHT - h_arr[j], n, h_arr[j])) 
        state[i] = 1
    for i in range(0, n2):  
        R[i] = a[m + i + 1]  
        state[i] = 0
        for j in range(len(h_arr)):
            if state[j] == 0:
                color = RED
            elif state[j] == 2:
                color = GREEN
            else:
                color = WHITE
            pygame.draw.rect(win, color, pygame.Rect(j*n, HEIGHT - h_arr[j], n, h_arr[j]))
        state[i] = 1
    i, j, k = 0, 0, l  
    while i < n1 and j < n2:  
        if L[i] > R[j]:  
            a[k] = R[j]  
            j += 1
        else:  
            a[k] = L[i]  
            i += 1
        k += 1 
    while i < n1:  
        a[k] = L[i]  
        i += 1
        k += 1
    while j < n2:  
        a[k] = R[j]  
        j += 1
        k += 1

flag = False
indiceActual = 0 

while True:
    pantalla.fill((10, 10, 10))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                flag = True

    if flag:
        if indiceActual < len(vectorAlturas) - 1:
            izquierda = 0
            while True:
                if izquierda < len(vectorAlturas)-1:  
                    valorMedio = min((izquierda + indiceActual - 1), (len(vectorAlturas)-1))
                    derecha = ((2 * indiceActual + izquierda - 1, len(vectorAlturas) - 1)[2 * indiceActual + izquierda - 1 > len(vectorAlturas)-1])  
                    n1 = mid - left + 1
                    n2 = right - mid  
                    L = [0] * n1  
                    R = [0] * n2  
                    for i in range(0, n1):  
                        L[i] = h_arr[left + i]
                    for i in range(0, n2):  
                        R[i] = h_arr[mid + i + 1]  
                    i, j, k = 0, 0, left  
                    
                    while i < n1 and j < n2:  
                        if L[i] > R[j]:  
                            h_arr[k] = R[j]
                            state[k] = 0
                            state[j] = 0
                            win.fill((10, 10, 10))
                            state[k] = 1
                            state[j] = 1
                            j += 1
                        else:  
                            h_arr[k] = L[i]
                            state[k] = 0
                            state[i] = 0
                            win.fill((10, 10, 10))
                            state[k] = 1 
                            state[i] = 1 
                            i += 1
                        k += 1 
                    while i < n1:  
                        h_arr[k] = L[i] 
                        state[k] = 0
                        state[i] = 0
                        win.fill((10, 10, 10))
                        state[k] = 1 
                        state[i] = 1
                        i += 1
                        k += 1
                    while j < n2:  
                        h_arr[k] = R[j] 
                        state[k] = 0
                        state[j] = 0
                        win.fill((10, 10, 10))
                        state[k] = 1 
                        state[i] = 1
                        j += 1
                        k += 1 
                    left = left + current_size*2
                else:
                    break

            current_size = 2 * current_size
    
    for i in range(len(h_arr)):
        h_ar = maps(h_arr[i], 0, 400, 20, 255)
        pygame.draw.rect(win, (h_ar//3, h_ar, h_ar//4), pygame.Rect(int(i*n), (HEIGHT - h_arr[i])//2, n, h_arr[i]))

    
    clock.tick(60)
    pygame.display.flip()