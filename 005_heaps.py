import numpy as np

class Heap:
	def __init__(self, tamaño):
		self.tamaño = tamaño
		self.heap = []
		self.indice = -1

	def insertar(self, dato):
		self.heap.append(dato) #Se inserta el dato al final del vector.
		self.indice +=1 #Este contador nos indica la posicion del dato dentro del vector, de ahi que al inicio sea -1 + 1 = 0 
		self.filtrarHaciaArriba(self.indice) #Hay que colocar el dato de acuerdo con las propiedades del heap.

	def filtrarHaciaArriba(self, indice):
		while indice //2 > 0: #Aquí se detendra cuando el vector llegue al primer elemento.
			if self.heap[indice] > self.heap[indice//2]: #Si el dato es mayor que el dato de su padre hay que cambiarlos.
				self.heap[indice], self.heap[indice//2] = self.heap[indice//2], self.heap[indice]
			indice = indice//2 #El indice debe ser ahora el del padre para continuar en el cumplimeinto de las propiedades.

	def ordenar(self):
		n = len(self.heap) - 1
		for i in range(n): #Debe de recorrer todo el vector para cumplir con las propiedaes del heap.
			self.heapify(i,n)
		return self.heap

	def heapify(self,i,j):
		valorMayor = i #Se asume que el primer indice contiene el elemento con el valor mas grande. En el caso de heap max.
		izq = 2*i+1
		der = 2*i+2

		if izq < j and self.heap[i] < self.heap[izq]:
			valorMayor = izq #En este caso el valor mas grande esta en el nodo izquierdo.
		if der < j and self.heap[valorMayor] < self.heap[der]:
			valorMayor = der # En esta condicion el nodo derecho es mayor que el nodo izquierdo.
		if valorMayor != i: #Si el indice del valor maoyr es difernete del indice ingresado hayq ue intercambniarlos.
			self.heap[i], self.heap[valorMayor] = self.heap[valorMayor],self.heap[i]
			self.heapify(valorMayor,j)
		


if __name__ == "__main__":
	hp = Heap(7)
	vector = np.random.randint(100,size=6)

	for i in vector:
		hp.insertar( i )

	print("Vector al azar: ", vector )
	print("Vector como minimo heap: ", hp.heap )
	print("Vector ordenado:",  hp.ordenar() )
	

	