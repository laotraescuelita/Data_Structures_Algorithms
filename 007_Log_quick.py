import time
import numpy as np
#Implementar el algoritmo de ordenamiento: Quick.
 
# Funcióin para partir el vector otriginal
def particion(vector, inicio, fin):
 
    # Se escoje el pivote,eneste caso es el elemento mas a laderecha.
    pivote = vector[fin]
 
    # apuntar a un elemento mayor.
    i = inicio - 1
 
    # Recorrer todos los elementos.
    # Comapara cadad elemento del vector con el elemento.
    for j in range(inicio, fin):
        if vector[j] <= pivote: 
            # SI hay un elemeto menor que el pivote hay que intercambiarlos.
            i = i + 1 
            vector[i], vector[j] = vector[j], vector[i]
 
    # Intercambiar el pivote con el elmento mayor especificado por i 
    vector[i + 1], vector[fin] = vector[fin], vector[i + 1]
 
    # Devolver la posicion donde se hizo la particion.
    return i + 1
 
# funcion para realiazar el ordenamiento quick. 
def quickSort(vector, inicio, fin):
    if inicio <fin:
 
        #Encontrar el elemento pivote quedivide el vector en izquierdo y dereho.
        pivote = particion(vector, inicio, fin)
 
        quickSort(vector, inicio, pivote - 1)
        quickSort(vector, pivote + 1, fin)
 
 
if __name__ == '__main__':
	#Medir el tiempo de ejecucion
	import time
	inicio = time.perf_counter()
	vector = np.random.randint(10,size=22)
	print( "Vector en desorden -->", vector )
	quickSort( vector, 0, len(vector)-1) 
	print( "Vector en orden    -->", vector )
	final = time.perf_counter()
	print(f"Elementos ordenados en  {final - inicio : 0.4f} seconds")
