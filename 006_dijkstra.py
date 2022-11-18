from heapq import *

class Dijkstra:
    def __init__(self, inicio, fin, grafo):
        self.inicio = inicio
        self.fin = fin 
        self.grafo = grafo
        self.enCola = []
        self.visitados = {}
        self.costoVisitados = {}

        #Asi comienzan los parametros.        
        heappush(self.enCola, (self.inicio, 0 )) 
        self.visitados = {inicio: None}
        self.costoVisitados = {inicio: 0}  

    def dijkstra(self):
              
        while self.enCola:
            nodoActual, nodoActualCosto = heappop(self.enCola) 
            if nodoActual == fin:
                break            
            
            for nodoSiguiente in grafo[nodoActual]:
                nodoVecino, nodoVecinoCosto = nodoSiguiente                
                nuevoCosto = self.costoVisitados[nodoActual] + nodoVecinoCosto

                if nodoVecino not in self.costoVisitados or nuevoCosto < self.costoVisitados[nodoVecino]:
                    heappush(self.enCola, (self.inicio, 0 ))
                    self.costoVisitados[nodoVecino] = nuevoCosto
                    self.visitados[nodoVecino] = nodoActual
                    
        return self.visitados , self.costoVisitados

if __name__ == "__main__":
    grafo = {'A': [('M',2), ('P',3)],
             'M': [('A',2), ('N',2)],
             'N': [('M',2), ('B',2)],
             'P': [('A',3), ('B',2)],
             'B': [('P',4), ('N',2)]}

    inicio = 'A'
    fin = 'B'
    dij = Dijkstra(inicio, fin , grafo)
    recorrido, costos = dij.dijkstra()
    print( recorrido )
    print( costos )

    
    """
    nodoActual = fin
    print(f'\npath from {fin} to {inicio}: \n {fin} ', end='')
    while nodoActual != inicio:
        nodoActual = recorrido[nodoActual]
        print(f'---> {nodoActual} ', end='')
    """