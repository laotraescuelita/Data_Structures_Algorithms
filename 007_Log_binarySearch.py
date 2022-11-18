import time 
import numpy as np
#Craer una función que nos ayude a encontrar un valor en un vector ordenado.
#El algoritmo a utiliar es una busqueda binaria de manera recursiva e iterativa.

def busquedaBinariaRecursiva(vector, elemento, inicio, fin):
	if inicio == fin:
		if vector[inicio] == elemento:
			return True
		else:
			return False
	else:
		valorMedio = (inicio+fin)//2
		if elemento == vector[valorMedio]:
			return True
		elif elemento < vector[valorMedio]:
			return busquedaBinariaRecursiva(vector,elemento,inicio,valorMedio-1)
		else: #elemento > vector[valorMedio]
			return busquedaBinariaRecursiva(vector,elemento,valorMedio+1,fin)


#Implementar el mismo algoritmo pero en forma recursiva.

def busquedaBinariaIterativa(vector,elemento):
	#Debemos establecer los indices inicio y fin del vactor.
	inicio = 0 
	fin = len(vector)-1
	while inicio < fin:
		#Variable que almacenará el indice del valor medio del vector.
		valorMedio = (inicio+fin)//2
		if elemento == vector[valorMedio]:
			return True
		elif elemento < vector[valorMedio]:
			fin = valorMedio - 1
		else: #elemento > vector[valorMedio]
			inicio = valorMedio + 1
	return False

if __name__ == '__main__':
	#Medir el tiempo de ejecucion	
	vector = [0,1,1,3,5,8,13,21,34,55]
	elemento = 3 
	low = 0
	high = len(vector)-1
	
	inicio = time.perf_counter()	
	print( "Vector en desorden -->", vector )
	encontrado = busquedaBinariaIterativa( vector, elemento ) 	
	final = time.perf_counter()
	print( "Vector encontrado   -->", encontrado )
	

	inicio = time.perf_counter()	
	print( "Vector en desorden -->", vector )
	encontrado = busquedaBinariaRecursiva( vector, elemento, low, high ) 	
	final = time.perf_counter()
	print( "Vector encontrado   -->", encontrado )