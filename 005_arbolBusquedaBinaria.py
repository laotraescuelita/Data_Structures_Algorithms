import numpy as np

#Implementar la estructura de datos: Árbol de busqueda binaria.
class Nodo(): #Crear el objeto nodo que almacena los elementos.
	def __init__(self, elemento): #Método contructor almacena el elemento. Y tiene las propiedades nodo izquierdo y derecho.
		self.elemento = elemento
		self.izquierdo = None 
		self.derecho = None


class ArbolBusquedaBinaria(): #Objeto que inserta, elimina, imprime y cumple las propiedades del árbol binario.
	def __init__(self):
		self.raiz = None #El árbol tiene un nodo inicio llamado raiz. 

	def insertar(self, elemento): #Mejor caso O(log(n)), peor caso O(n).
		if self.raiz is None: #Si no hay raiz comenzar el árbol con el elemento.
			self.raiz = Nodo(elemento)
		else: #De otra manera insertar el elemento cumpliendo las propiedades del árbol binario.
			self._insertar(elemento,self.raiz) 

	def _insertar(self,elemento,nodo):
		if elemento < nodo.elemento: #Si el elemento es menor que el elemento del nodo raiz ir a la izquierda.
			if nodo.izquierdo: #Si el nodo de la izquierda tiene un elemento recorrer el árbol recursivamente.
				self._insertar(elemento,nodo.izquierdo)
			else: #Si el nodo no tiene elementos hay que almacenar el elemento ahí.
				nodo.izquierdo = Nodo(elemento)
		elif elemento > nodo.elemento: #Si el elemento es menor que el elemento del nodo raiz ir a la derecha.
			if nodo.derecho: #Si el nodo derecho tiene un elemento hay que recorrer el árbol recursivamente.
				self._insertar(elemento,nodo.derecho) 
			else: #De otra manera hay que insertar el elemento ahí.
				nodo.derecho = Nodo(elemento)

	
	def remover(self, elemento): #Mejor caso O(log(n)), peor caso O(n).
		if self.raiz is None: #Si no hay raiz salimos del programa.
			return 
		else: #De otra manera se busca el elemento y se elimina.
			self._remover(elemento, self.raiz)

	def _remover(self, elemento, nodoActual): 
		if nodoActual is None:
			return nodoActual  #Si el nodo esta vacío hay que devolver ese nodo.

		#Hay que buscar el elemento en el árbol.
		if elemento < nodoActual.elemento: #Si el elemento es menor al elemento de la raiz hay que buscar en la izquerda del árbol.
			if nodoActual.izquierdo: #Si hay elementos en el lado izquierdo de manera recursiva buscar el elemento.
				nodoActual.izquierdo = self._remover(elemento, nodoActual.izquierdo) 
				return nodoActual #Devolver el nodo que tiene el elemento que vamos a eliminar.
		
		elif elemento > nodoActual.elemento: #Si el elemento es menor al elemento de la raiz hay que buscar en la derecha del árbol.
			if nodoActual.derecho: #Si hay elementos en el lado derecho de manera recursiva buscar el elemento.
				nodoActual.derecho = self._remover(elemento, nodoActual.derecho)
				return nodoActual #Devolver el nodo que tiene el elemento que vamos a eliminar.
		else: #Una vez que se encontro el elemento hay tres casos para eliminarlo.
			if nodoActual.izquierdo is None and nodoActual.derecho is None: #Primero que el nodo no tenga hijos.
				print("Removiendo un nodo sin hijos.")
				del nodoActual #Remueve espacio de la memoria ya que el nodo tiene apuntado un nod izquierdo y derecho sin informacion.
				return None #sale del bucle y devuelve None ya que el nodo ya no existe.
			
			elif nodoActual.izquierdo is None: #Segundo el nodo tiene un hijo derecho.
				print("Removiendo un nodo con un hijo derecho.")
				nodoTemporal = nodoActual.derecho
				del nodoActual  #Remueve el nodo con el elemento.
				return nodoTemporal # Devuelve el nodo con el elemento del hijo derecho.
			
			elif nodoActual.derecho is None: #Tercero el nodo tiene un hijo izquierdo.
				print("Removiendo un nodo con un hijo izquierdo.")
				nodoTemporal = nodoActual.izquierdo
				del nodoActual  #Remueve el nodo con el elemento.
				return nodoTemporal # Devuelve el nodo con el elemento del hijo derecho.
			
			elif nodoActual.derecho and nodoActual.izquierdo: #Cuarto el nodo tiene ambos hijos.
				print("Removiendo un nodo con ambos hijos.")
				nodoTemporal = self.obtenerPredecesor(nodoActual.derecho) #Buscamos el elemento que ocupara el lugar del nodo que remvemos.
				nodoActual.elemento = nodoTemporal.elemento #Asignamos el elemento que ocupa el lugar del nuevo elemento.
				nodoActual.derecho = self._remover(nodoTemporal.elemento, nodoActual.derecho) #Hay que remover el nodo derecho.

			return nodoActual
				

	def obtenerPredecesor(self,nodoActual): #Al escojer el nodo derecho hay que buscar el valor minimo en el lado izquierdo del arbol.
		if nodoActual.izquierdo:			
			return self.obtenerPredecesor(nodoActual.izquierdo)
		return nodoActual


	def imprimirEnOrden(self):
		if self.raiz is None:
			return 
		else:
			self._imprimirEnOrden(self.raiz)

	def _imprimirEnOrden(self, nodoActual):
		if nodoActual is None:
			return 		
		print("Imprimiendo en orden", end="")
		print(nodoActual.elemento)
		self._imprimirEnOrden(nodoActual.izquierdo)				
		self._imprimirEnOrden(nodoActual.derecho)

	def imprimirEnPostOrden(self):
		if self.raiz is None:
			return 
		else:
			self._imprimirEnPostOrden(self.raiz)

	def _imprimirEnPostOrden(self, nodoActual):
		if nodoActual is None:
			return 				
		self._imprimirEnPostOrden(nodoActual.izquierdo)				
		self._imprimirEnPostOrden(nodoActual.derecho)
		print("Imprimiendo en post orden", end="")
		print(nodoActual.elemento)

	def imprimirEnPreOrden(self):
		if self.raiz is None:
			return 
		else:
			self._imprimirEnPreOrden(self.raiz)

	def _imprimirEnPreOrden(self, nodoActual):
		if nodoActual is None:
			return 				
		self._imprimirEnPreOrden(nodoActual.izquierdo)				
		print("Imprimiendo en pre orden", end="")
		print(nodoActual.elemento)	
		self._imprimirEnPreOrden(nodoActual.derecho)

	def valorMinimo(self):
		if self.raiz is None:
			return
		else:
			self._valorMinimo(self.raiz)

	def _valorMinimo(self, nodoActual):
		if nodoActual.izquierdo:
			return self._valorMinimo(nodoActual.izquierdo)
		print(nodoActual.elemento)
		

	def valorMaximo(self):
		if self.raiz is None:
			return
		else:
			self._valorMaximo(self.raiz)

	def _valorMaximo(self, nodoActual):
		if nodoActual.derecho:
			return self._valorMaximo(nodoActual.derecho)
		print(nodoActual.elemento)
	
vector = np.random.randint(100,size=6)
bst = ArbolBusquedaBinaria()
for i in vector:
	bst.insertar(i)

bst.imprimirEnOrden()
print(" ")
#bst.remover(20)
#bst.imprimirEnOrden()
#print(" ")
bst.imprimirEnPostOrden()
print(" ")
bst.imprimirEnPreOrden()
print(" ")
bst.valorMinimo()
bst.valorMaximo()
