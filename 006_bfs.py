from collections import deque 

class BFS: #crear el objeto bfs
    def __init__(self, inicio, final, grafo): #El método contructor recibe el nodo inicio el final y el grafo.
        self.inicio = inicio
        self.final = final
        self.grafo = grafo

    def bfs(self):
        enCola = deque([self.inicio]) #La cola inicia con el vertice  inicio del grafo.
        visitado = {self.inicio : None} #Diccionario almacena los vertices ya visitados.

        while enCola: #Mientras haya vertices en la cola.
            nodoActual = enCola.popleft() #Se extrae el valor que haya en cola.
            if nodoActual == self.final: #El inicio y el final es el mismo, se sale de la ejecución.
                break 
            #En otro caso hay que recorrer los vertices que esten conenctados al nodo actual.
            nodosSiguientes = grafo[nodoActual] #En una lista se pasan los vertices conectados al vertice actual.
            for nodoSiguiente in nodosSiguientes: #Se recorre cada vertice.
                if nodoSiguiente not in visitado: #Si el vertice no ha sido visitado.
                    enCola.append(nodoSiguiente) #El vertice se pone en cola.
                    visitado[nodoSiguiente] = nodoActual #El vertice se coloca como vistado y de que vertice se visito.
        return visitado

if __name__ == "__main__":
    #Grafo se almacena en un diccionario
    grafo = {'A': ['B', 'C'],
             'B': ['A', 'D'],
             'C': ['A', 'E'],
             'D': ['B', 'E'],
             'E': ['C', 'D']}

    inicio = 'A'
    final = 'E'
    bfs = BFS(inicio, final, grafo)
    recorrido = bfs.bfs()
    print("Este es el recorrido del grafo: \n", recorrido)

    nodoActual = final #Para conocer el recorrido de inicio al final se inicia el vertice objetivo.
    print(f'\n Este es el recorrido de {inicio} hacia {final}: \n {final} ', end='') 
    while nodoActual != inicio: #Se recorre el diccionario hasta que el vertice coincida con el inicio.
        nodoActual = recorrido[nodoActual]  #Se va recorriendo de acuerdo al vertice del que llegamos al actual.
        print(f'---> {nodoActual} ', end='') #Se van imprimiendo los vertices.

