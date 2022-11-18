import time
import numpy as np
#Implementar el algoritmo de ordenamiento: Insercion.

class Insercion:
	def __init__(self, vector):
		self.vector = vector

	def insertarIterativamente(self):
		
		#Este algoritmo es O(n^2)
		for i in range(1, len(self.vector)):  #Ya que recorre todo el vector.
			j = i
		
			while j > 0 and self.vector[j-1] > self.vector[j]: #Si el indice no es cero y el elemento anteriro es mayor al actual.
				self.vector[j-1], self.vector[j] = self.vector[j], self.vector[j-1]  #Se cambia el orden.
				j -= 1 #El indice se decrementa.
			
		return self.vector

	def insertarRecursivamente(self, vector, i = None):
		if i == None: 
			i = len(self.vector) - 1
		
		if i == 0: 
			return i
		
		self.insertarRecursivamente(self.vector, i-1)
		j = i
		
		while j > 0 and self.vector[j-i] > self.vector[j]:
			self.vector[j-1], self.vector[j] = self.vector[j], self.vector[j-1]
			j -= 1
		return self.vector


if __name__ == "__main__":
	
	inicio = time.perf_counter()		
	vector = np.random.randint(10, size=22)
	ins = Insercion(vector)
	print( "Vector en desorden -->", vector )
	vector = ins.insertarIterativamente()
	final = time.perf_counter()
	print( "Vector en orden    -->", vector )
	print(f"Elementos ordenados en  {final - inicio : 0.4f} seconds")

