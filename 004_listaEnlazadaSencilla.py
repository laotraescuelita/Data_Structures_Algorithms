#Implementar la estructura de datos: Lista enlazda sencilla.

class Nodo(): #Crear objeto nodo que almacena elementos y apunta al siguiente nodo.
	def __init__(self,elemento): #El método contructor recibe el elemento.
		self.elemento = elemento
		self.siguiente = None

class ListaEnlazadaSencilla(): #Crear el objeto lista enlazda que realiza las oeraciones de insercion, eliminacion, etc..
	def __init__(self):
		self.cabeza = None 
		self.tamaño = 0 

	def cantidadElementos(self):
		return self.tamaño

	def insertarAlIncio(self,elemento): #Tiempo de ejecución O(1)
		if self.cabeza is None: #Si la lista esta vacia se inicia el nodo cabeza con el primer valor.
			self.cabeza = Nodo(elemento)
		else:
			nodoNuevo = Nodo(elemento) #De otra manera el nuevo elemento se almacena en un nodo.
			nodoNuevo.siguiente = self.cabeza #El nuevo nodo apunta a la cabeza.
			self.cabeza = nodoNuevo #El nuevo nodo ahora es la cabeza.
		self.tamaño += 1 #Se incrementa la propiedad tamaño.


	def insertarAlFinal(self, elemento): #Tiempo de ejecución O(n)
		if self.cabeza is None: #Si la lista esta vacia se inicia el nodo cabeza con el primer valor.
			self.cabeza = Nodo(elemento)
		else: #De otra manera se inserta el nuevo elemento al final de la lista.
			nodoActual = self.cabeza #El primero nodo del recorrido es la cabeza.
			nodoNuevo = Nodo(elemento) #El nuevo elemento se inserta en un nodo.
			while nodoActual.siguiente: #Hay que recorrer la lista hasta llegar al final.		
				nodoActual = nodoActual.siguiente #El nodo actual adquier el valor del siguiente nodo.
			nodoActual.siguiente = nodoNuevo #Al llegar al final el ultimo nodo apunta la nuevo nodo.
		self.tamaño += 1 #Se incrementa la propiedad tamaño.


	def imprimirLista(self): #Tiempo de ejecución O(n)
		if self.cabeza is None: #Si la lista esta vacia se termina la ejecución del programa.
			return
		else: #De otra manera se recorre la lista y se imprimen cada uno de sus elementos.
			nodoActual = self.cabeza #El primer nodo es la cabeza.
			lista = ""
			while nodoActual: #Mientras el valor de nodo no este vacio se recorrer la lista.
				lista += nodoActual.elemento + " --> " #Esta variable almacena los elementos de la lista.
				nodoActual = nodoActual.siguiente #El nodo actual adquier el valor del siguiente nodo.
		print(lista) #Se imprimen los elementos de la lista.
	

	def remover(self,elemento): #Tiempo de ejecución mejro caso O(1), peor caso O(n).
		if self.cabeza is None: #Si la lista esta vacia se termina la ejecución del programa.
			return
		if self.cabeza.elemento == elemento: #Si el elemento es igual al elemento de la cabeza,
			self.cabeza = self.cabeza.siguiente #la cabeza será el elemento siguiente.
		else: #De otra manera hay que recorrer la lista para buscar el elemento.
			nodoPrevio = None #Variable que nos ayudará a no perder el nodo anterior.
			nodoActual = self.cabeza #El primer nodo en el recorrido es la cabeza.

			while nodoActual and nodoActual.elemento != elemento: #Mientras el nodo tenga un elemento y sea distinto al elemento buscado.
				nodoPrevio = nodoActual #Se tiene registro del nodo anterior.
				nodoActual = nodoActual.siguiente #El nodo va avanzando tomando el elemento siguiente.
			
			if nodoActual: #Si encontramos el elemento realizamos la eliminación.
				nodoPrevio.siguiente = nodoActual.siguiente #El nodo anterior apunta al elemento siguiente del nodo actual.
				nodoActual = None
		self.tamaño -= 1 #Se decrementa la propiedad tamaño.


if __name__ == "__main__":

	les = ListaEnlazadaSencilla()
	les.insertarAlIncio("Marge")
	les.insertarAlFinal("Bart")
	les.insertarAlIncio("Homer")
	les.insertarAlFinal("Lisa")
	les.insertarAlFinal("Maggie")
	print("Elementos en la lista: ")
	les.imprimirLista()	
	print("Cantidad de elementos en la lista: ", les.cantidadElementos())
	les.remover("Marge")
	print("Elementos en la lista: ")
	les.imprimirLista()
	print("Cantidad de elementos en la lista: ", les.cantidadElementos())





