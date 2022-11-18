#Implementar la estructura de datos: Cola.
import numpy as np 

class Colas: #Creamos un objeto llamado colas.
	def __init__(self): #El método constructor no recibe parametros.
		self.cola = []
		

	def cantidad(self): #Tiempo de ejecución O(1).
		return len(self.cola) #Método que nos indica la cantidad de elementos dentro de la cola.

	def estaVacio(self): #Tiempo de ejecución O(1).
		return len(self.cola) == 0 #Devuelve verdadero si el tamaño es igual a cero.

	def insertar(self, elemento): #Tiempo de ejecución O(1).
		self.cola.append(elemento) #El nuevo elemtno es almacenado al fina de la cola.

	def extraer(self): #Tiempo de ejecución O(1).
		if self.estaVacio(): 
			return  #Si la lista esta vacia nos saca de la ejecución del programna.
		return self.cola[0] #En caso contrario nos devuelve el ultimo elemento en la cola.
	
	def remover(self): #Tiempo de ejecución O(1).
		if self.estaVacio(): 
			return  #Si la lista esta vacia nos saca de la ejecución del programna.
		return self.cola.pop(0) #Devuelve el ultimo elemento en la cola y lo elimina de la misma.


if __name__ == "__main__":
	vector = np.random.randint(100,size=6)
	c = Colas()
	print("Cantidad de elementos al inicio: ", c.cantidad())
	print("Esta la cola vacia: ", c.estaVacio())
	
	#Insertar valores en la pila
	for i in vector:
		c.insertar(i)
		
	print("Elementos dentro de la cola\n", c.cola)
	print("Extraer el ultimo elemento ingresado\n", c.extraer())
	print("La cola no cambia solo muestra el elemento\n", c.cola)
	print("Remover el ultimo elemento ingresado\n", c.remover())
	print("La cola si cambia al remover el elemento\n",c.cola)