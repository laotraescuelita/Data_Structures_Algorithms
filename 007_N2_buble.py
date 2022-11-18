#Implementar el algoritmo de ordenamiento : Bubble.
import numpy as np
import time 

def bubbleSort(vector):
	for numero in range( len(vector)-1, 0, -1):#Recorrer el vector de fin a inicio.
		for i in range( numero ):
			if vector[i] > vector[i+1]: #Si el elemento actual es mayor al elemento que le sigue.
				vector[i], vector[i+1] = vector[i+1],vector[i]
	return vector


if __name__ == '__main__':
	#Medir el tiempo de ejecucion
	import time
	inicio = time.perf_counter()
	vector = np.random.randint(10,size=22)
	print( "Vector en desorden -->", vector )
	bubbleSort( vector ) 
	print( "Vector en orden    -->", vector )
	final = time.perf_counter()
	print(f"Elementos ordenados en  {final - inicio : 0.4f} seconds")

