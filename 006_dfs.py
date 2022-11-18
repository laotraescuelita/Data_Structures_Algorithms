#Implementar la estructura de datos: Depth first search.

class DFS: #Crerar el objeto dfs.
    def __init__( self, inicio, final, grafo): #Que reciba el vertice de inicio y el grafo.
        self.inicio = inicio        
        self.final = final
        self.visitado = {}
        self.grafo = grafo
        self.enCola = []
        
        self.enCola.append(self.inicio) #Almacenar los vertices a visitar.
        self.visitado = {self.inicio : None} #Llevar el registro de los vertices visitados y de donde han venido.

    
    def dfs(self):

        if self.enCola is None: #Condición base para terminar la recursión, que la cola no tenga vertices.
            return        
        
        nodoActual = self.enCola.pop() #Comenzar el recorrido sacando el ultimo elemento de la cola.

        if self.final == nodoActual:
            return
        
        for nodo in self.grafo[nodoActual]: #Visitar cada nodo conecatado al nodo actual.
            if nodo not in self.visitado: #Si no ha sido visitado el nodo.
                self.enCola.append(nodo) #Colocarlo en cola para su visita.
                self.visitado[nodo] = nodoActual #Registrar su visita y de donde se ha visitado.
                self.dfs() #De manera recursiva visitar todos los nodos.

        return self.visitado
    

if __name__ == "__main__":
    #Probemos que el algoritmo funciona como lo requerimos.
    grafo = {'A': ['B', 'C'],
             'B': ['A', 'D'],
             'C': ['A', 'E'],
             'D': ['B', 'E'],
             'E': ['C', 'D']}


    inicio = 'A'
    final = "E"
    dfs = DFS(inicio, final, grafo)
    recorrido = dfs.dfs()
    print("Este es el recorrido del grafo: \n", recorrido)       

    #Imprimir el recorrido que realizo el algoritmo.
    nodoActual = final #Para conocer el recorrido de inicio al final se inicia el vertice objetivo.
    print(f'\n Este es el recorrido de {inicio} hacia {final}: \n {final} ', end='') 
    while nodoActual != inicio: #Se recorre el diccionario hasta que el vertice coincida con el inicio.
        nodoActual = recorrido[nodoActual]  #Se va recorriendo de acuerdo al vertice del que llegamos al actual.
        print(f'---> {nodoActual} ', end='') #Se van imprimiendo los vertices.
