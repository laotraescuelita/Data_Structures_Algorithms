#Implementar la estructura de datos: Lista enlazada Doble.

class Nodo(): #Crear el objeto nod que almacena el elemento y los apuntadores siguiente y anterior.
	def __init__(self,elemento): #El método contructor recibe el elemento por parametro.
		self.elemento = elemento
		self.siguiente = None
		self.anterior = None

class ListaEnlazadaDoble(): #Crear el objeto que tiene los métodos insertar, eliminar etc...
	def __init__(self):
		self.cabeza = None
		self.cantidad = 0

	def cantidadElementos(self): #Tiempo de ejecución O(1)
		return self.cantidad       #Devuelve la cantidad de elementos en la lista.

		if self.head is None:
			self.head = Node(d)
		else:
			self._prePend(d, self.head)

	def insertarAlInicio(self, elemento): #Tiempo de ejecución O(1)
		if self.cabeza is None: #Si la lista esta vacia hay que iniciar la cabeza con el elemento.
			self.cabeza = Nodo(elemento)
		else:
			nodoNuevo = Nodo(elemento) #De otra manera hay que crear un nodo nuevo con el elemento.
			nodoNuevo.siguiente	= self.cabeza # El nuevo nodo apunta a la cabeza.
			self.cabeza.anterior = nodoNuevo #La cabeza apunta al nuevo nodo.
			self.cabeza =  nodoNuevo #y el nodo nuevo toma la posición de la cabeza.
		self.cantidad += 1 #Incrementamos el numero de elementos.

	def insertarAlFinal(self, elemento):#Tiempo de ejecución O(n)
		if self.cabeza is None: #Si la lista esta vacia hay que iniciar la cabeza con el elemento.
			self.cabeza = Nodo(elemento)
		else: #De otra manera hay que recorrer la lista para insertar el elemento al final.
			nodoActual = self.cabeza #El nodo actual va tomando la posicion conforme avanza comenzando con la cabeza. 
			nodoNuevo = Nodo(elemento) #Creamos un nodo nuevo para almacenar el nuevo elemento.
			while nodoActual.siguiente:	#Hay que recorrer la lista mientras el apuntador siguiente no este vacio.
				nodoActual = nodoActual.siguiente
			nodoActual.siguiente = nodoNuevo #El ultimo nodo apunta al nuevo nodo.
			nodoNuevo.anterior = nodoActual #El nuevo nodo apunta al nodo actual.
		self.cantidad += 1 #Incrementamos el numero de elementos.


	def imprimirLista(self): #Tiempo de ejecución O(n)
		if self.cabeza is None: #Si la lista esta vacia salimos de la ejecución del programa.
			return
		else: #De otra manera lo recorremos mientras imprimos los elementos.
			nodoActual = self.cabeza #Actualizamos el nodo comenzando con la cabeza.
			lista = ""
			while nodoActual: #Mientras el valor de nodo no este vacio se recorrer la lista.
				lista += " <-- " + nodoActual.elemento + " --> " # Esta variable va almacenando los elementos.
				nodoActual = nodoActual.siguiente
		print(lista)			

	def remover(self, elemento): #Tiempo de ejecución pero caso O(n) y mejor caso O(1).
		if self.cabeza is None: #Si la cabeza esta vacia termina la ejecución del programa.
			return
		if self.cabeza.elemento == elemento: #Si el elemento es igual a la cabeza.
			self.cabeza = self.cabeza.siguiente #La cabeza toma el valor del elemento al que apuntaba.
			self.cabeza.anterior = None #Y su apuntador anterior apunta a un elemento nulo.
		#elif nodoActual.siguiente == None:
		#	self.cabeza = None
		else: #Otro caso es que haya que recorrer la lsita para encontrar el elemento.
			nodoActual = self.cabeza #Vamos actualizando el nodo comenzado por la cabeza.
			while nodoActual and nodoActual.elemento != elemento: #Mientras el nodo actual no este nulo y el elemento no este en ese nodo.
				nodoActual = nodoActual.siguiente 						
			if nodoActual: #Si se encontro el elemento actualizamos los punteros.
				if nodoActual.siguiente is None:
					nodoActual.anterior.siguiente = None
				else:
					nodoActual.siguiente.anterior = nodoActual.anterior
					nodoActual.anterior.siguiente = nodoActual.siguiente				
		self.cantidad -= 1 #Decrementamos el numero de elementos.


if __name__ == "__main__":
	led = ListaEnlazadaDoble()
	led.insertarAlFinal("Bart")
	led.insertarAlFinal("Lisa")
	led.insertarAlInicio("Marge")
	led.insertarAlInicio("Homer")	
	print("Cantidad de elelementos en la lista: ", led.cantidadElementos())
	print("Elementos en la lista:")
	led.imprimirLista()
	led.remover("Lisa")  
	print("Elementos en la lista:")
	led.imprimirLista()
	print("Cantidad de elelementos en la lista: ", led.cantidadElementos())