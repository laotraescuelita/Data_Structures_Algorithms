#Implementar el algoritmo de ordenamiento : gnome.
import numpy as np
import time 

def gnomeSort( vector ):
  i = 0
  while i < len(vector):
    if i == 0 or vector[i-1] <= vector[i]:
      i += 1
    else:
      vector[i], vector[i-1] = vector[i-1], vector[i]
      i -= 1
  return vector


if __name__ == '__main__':
	#Medir el tiempo de ejecucion
	import time
	inicio = time.perf_counter()
	vector = np.random.randint(10,size=22)
	print( "Vector en desorden -->", vector )
	gnomeSort( vector ) 
	print( "Vector en orden    -->", vector )
	final = time.perf_counter()
	print(f"Elementos ordenados en  {final - inicio : 0.4f} seconds")

