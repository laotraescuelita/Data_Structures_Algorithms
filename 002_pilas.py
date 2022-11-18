#Implementar la estructura de datos: Pila.
import numpy as np

class Pilas: #Creamos un objeto llamado pila.
	def __init__(self): #El método constructor no recibe parametros.
		self.pila = []
		

	def cantidad(self): #Tiempo de ejecución O(1).
		return len(self.pila) #Método que nos indica la cantidad de elementos dentro de la pila.

	def estaVacio(self): #Tiempo de ejecución O(1).
		return len(self.pila) == 0 #Devuelve verdadero si el tamaño es igual a cero.

	def apilar(self, elemento): #Tiempo de ejecución O(1).
		self.pila.append(elemento) #El nuevo elemtno es almacenado al fina de la pila.

	def extraer(self): #Tiempo de ejecución O(1).
		if self.estaVacio(): 
			return  #Si la lista esta vacia nos saca de la ejecución del programna.
		return self.pila[-1] #En caso contrario nos devuelve el ultimo elemento en la pila.
	
	def remover(self): #Tiempo de ejecución O(1).
		if self.estaVacio(): 
			return  #Si la lista esta vacia nos saca de la ejecución del programna.
		return self.pila.pop() #Devuelve el ultimo elemento en la pila y lo elimina de la misma.


if __name__ == "__main__":
	vector = np.random.randint(100,size=6)
	p = Pilas()
	print("Cantidad de elementos al inicio: ", p.cantidad())
	print("Esta la pila vacia: ", p.estaVacio())
	
	#Insertar valores en la pila
	for i in vector:
		p.apilar(i)
		
	print("Elementos dentro de la pila\n", p.pila)
	print("Extraer el ultimo elemento ingresado\n", p.extraer())
	print("La pila no cambia solo muestra el elemento\n", p.pila)
	print("Remover el ultimo elemento ingresado\n", p.remover())
	print("La pila si cambia al remover el elemento\n",p.pila)