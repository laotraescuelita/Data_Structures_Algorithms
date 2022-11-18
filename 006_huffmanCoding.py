import heapq

class Nodo:
	def __init__(self, frecuencia, simbolo, izquierdo=None, derecho=None):		
		self.frecuencia = frecuencia
		self.simbolo = simbolo
		self.izquierdo = izquierdo
		self.derecho = derecho
		# tree direction (0/1)
		self.huff = ''
		
	def __lt__(self, siguiente):
		return self.frecuencia < siguiente.frecuencia
		
def imprimirNodos(nodo, valor=''):		
	valorNuevo = valor + str(nodo.huff)

	if(nodo.izquierdo):
		imprimirNodos(nodo.izquierdo, valorNuevo)
	if(nodo.derecho):
		imprimirNodos(nodo.derecho, valorNuevo)		
	if(not nodo.izquierdo and not nodo.derecho):
		print(f"{nodo.simbolo} -> {valorNuevo}")

caracteres = ['a', 'b', 'c', 'd', 'e']
frecuencia = [ 3, 5, 6, 4, 2]
nodos = []

for x in range(len(caracteres)):
	heapq.heappush(nodos, Nodo(frecuencia[x], caracteres[x]))

while len(nodos) > 1:	
	izquierda = heapq.heappop(nodos)
	derecha = heapq.heappop(nodos)
	
	izquierda.huff = 0
	derecha.huff = 1

	nodoNuevo = Nodo(izquierda.frecuencia + derecha.frecuencia, izquierda.simbolo + derecha.simbolo, izquierda, derecha)

	heapq.heappush(nodos, nodoNuevo)


imprimirNodos(nodos[0])
