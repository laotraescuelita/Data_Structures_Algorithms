import time
import numpy as np
#Implementar el algoritmo de ordenamiento: Merge.

def merge(vector, izquierda, derecha):
	#Dimensión de los vectores enque se ha dividio el original.
	largo_izquierda = len(izquierda)
	largo_derecha = len(derecha)
	#Iniciar los indices 
	i=j=k=0

	#Si el indice i y j son menores que las dimensiones de los vectores hay que 
	#crear un nuevo vector respetando las propiedades delalgoritmo.
	while i < largo_izquierda and j < largo_derecha: 
		if izquierda[i] <= derecha[j]:
			vector[k] = izquierda[i]
			i += 1
		else:
			vector[k] = derecha[j]
			j += 1
		k += 1

	#En los casos en que los nuevosvectores aun contengan elementos hay 
	#que recorrerlos hasta cumplir las propiedades delalgoritmo.
	while i < largo_izquierda:
		vector[k] = izquierda[i]
		i += 1
		k += 1

	while j < largo_derecha:
		vector[k] = derecha[j]
		j += 1
		k += 1

	return vector

#De manera recurisiva partir el vector para cumplir las propiedades del algoritmo.
def mergeSort(vector):
	if len(vector) <= 1:
		return
	pivote = len(vector)//2
	izquierda = vector[:pivote]
	derecha = vector[pivote:]

	mergeSort(izquierda)
	mergeSort(derecha)		
	return merge(vector,izquierda,derecha)


if __name__ == '__main__':
	#Medir el tiempo de ejecucion
	import time
	inicio = time.perf_counter()
	vector = np.random.randint(10,size=22)
	print( "Vector en desorden -->", vector )
	mergeSort( vector ) 
	print( "Vector en orden    -->", vector )
	final = time.perf_counter()
	print(f"Elementos ordenados en  {final - inicio : 0.4f} seconds")
