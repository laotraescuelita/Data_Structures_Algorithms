#Implementar la estructura de datos: Árbol AVL.
import sys
import numpy as np

class Nodo:
    def __init__(self, elemento): #Método constructor recibe el elemento a insertar.
        self.elemento = elemento
        self.izquierdo = None
        self.derecho = None
        self.altura = 1


class arbolAVL: #Objeto AVL que contiene las propiedades y métodos.
    def __init__(self):
        self.raiz = None 
    
    
    def insertar(self, elemento): #Insertar el elemento.
        self.raiz = self._insertar(elemento, self.raiz)

    def _insertar(self, elemento, nodoActual):

        if nodoActual is None: #Si el nodo esta vacio insertamos el nuevo elemento.            
            return Nodo(elemento)

        elif elemento  < nodoActual.elemento: #Si el elemento es menor al elemento de la raiz ir a la izquierda del árbol.
            nodoActual.izquierdo = self._insertar(elemento, nodoActual.izquierdo)            
        else: #De otra manera nos vamos al lado derecho de árbol.
            nodoActual.derecho = self._insertar(elemento, nodoActual.derecho)                    
    
        #Actualizar la altura del nodo que se ha isertado.        
        nodoActual.altura = 1 + max(self.obtenerAltura(nodoActual.izquierdo), self.obtenerAltura(nodoActual.derecho))
        
        # Actualizar el balance del árbol y cumplir las propiedades del árbol.
        factorDeBalance = self.obtenerBalance(nodoActual)
                
        if factorDeBalance > 1: #Si el balance es mayor a 1.
            if elemento < nodoActual.izquierdo.elemento: #Si el elemento es menor al elemento del nodo izquierdo.
                return self.rotarAlaDerecha(nodoActual) #Hay que rotar a la derecha.
            else: #La otra manera es que el elemento es mayor al nodo izquierdo.
                nodoActual.izquierdo = self.rotarAlaIzquierda(nodoActual.izquierdo) #Hay que rotar a la izquierda primero.
                return self.rotarAlaDerecha(nodoActual) #Hay que rotar a la derecha después.

        if factorDeBalance < -1:
            if elemento > nodoActual.derecho.elemento:
                return self.rotarAlaIzquierda(nodoActual)
            else:
                nodoActual.derecho = self.rotarAlaDerecha(nodoActual.derecho)
                return self.rotarAlaIzquierda(nodoActual)

        return nodoActual

    """
    def remover(self, elemento):
        if self.raiz == None: 
            return #Si la raiz esta vacia salir del programa.
        else: #De otra manera hay que recorrer el árbol para cumplir con las propiedades del árbol AVL.
            self._remover(elemento, self.raiz)

    def _remover(self, elemento, nodoActual):        
        
        if not nodoActual:
            return nodoActual  #Si el nodo esta vacío hay que devolver ese nodo.

        if elemento < nodoActual.elemento:
            nodoActual.izquierdo = self._remover(nodoActual.izquierdo, elemento)
            return nodoActual #Devolver el nodo que tiene el elemento que vamos a eliminar.
        elif elemento > nodoActual.elemento:
            nodoActual.derecho = self._remover(nodoActual.derecho, elemento)
            return nodoActual #Devolver el nodo que tiene el elemento que vamos a eliminar.
        else:
            
            if nodoActual.izquierdo is None:
                nodoTemporal = nodoActual.derecho
                nodoActual = None
                return nodoTemporal
            elif nodoActual.derecho is None:
                nodoTemporal = nodoActual.izquierdo
                nodoActual = None
                return nodoTemporal
            
            nodoTemporal = self.obtenerPredecesor(nodoActual.derecho)
            nodoActual.elemento = nodoTemporal.elemento
            nodoActual.derecho = self._remover(nodoActual.derecho, nodoTemporal.elemento)
        
        if nodoActual is None:
            return nodoActual

        #Actualizar la altura del nodo que se ha isertado.
        nodoActual.altura = 1 + max(self.obtenerAltura(nodoActual.izquierdo), self.obtenerAltura(nodoActual.derecho))

        # Actualizar el balance del árbol y cumplir las propiedades del árbol.
        factorDeBalance = self.obtenerBalance(nodoActual)
        
        if factorDeBalance > 1: #Si el balance es mayor a 1.
            if elemento < nodoActual.izquierdo.elemento: #Si el elemento es menor al elemento del nodo izquierdo.
                return self.rotarAlaDerecha(nodoActual) #Hay que rotar a la derecha.
            else: #La otra manera es que el elemento es mayor al nodo izquierdo.
                nodoActual.izquierdo = self.rotarAlaIzquierda(nodoActual.izquierdo) #Hay que rotar a la izquierda primero.
                return self.rotarAlaDerecha(nodoActual) #Hay que rotar a la derecha después.

        if factorDeBalance < -1:
            if elemento > nodoActual.derecho.elemento:
                return self.leftRotate(nodoActual)
            else:
                nodoActual.derecho = self.rightRotate(nodoActual.derecho)
                return self.leftRotate(nodoActual)        
        
        return nodoActual
   
    """
    def rotarAlaIzquierda(self, z):
        y = z.derecho
        T2 = y.izquierdo
        y.izquierdo = z
        z.derecho = T2
        z.altura = 1 + max(self.obtenerAltura(z.izquierdo), self.obtenerAltura(z.derecho))
        y.altura = 1 + max(self.obtenerAltura(y.izquierdo), self.obtenerAltura(y.derecho))
        return y


    def rotarAlaDerecha(self, z):
        y = z.izquierdo
        T3 = y.derecho
        y.derecho = z
        z.izquierdo = T3
        z.altura = 1 + max(self.obtenerAltura(z.izquierdo), self.obtenerAltura(z.derecho))
        y.altura = 1 + max(self.obtenerAltura(y.izquierdo), self.obtenerAltura(y.derecho))
        return y

    # Devolver la altura de cada nodo.
    def obtenerAltura(self, nodoActual):
        if not nodoActual:
            return 0
        return nodoActual.altura

    # Devolver el balance del árbol.
    def obtenerBalance(self, nodoActual):
        if not nodoActual:
            return 0
        return self.obtenerAltura(nodoActual.izquierdo) - self.obtenerAltura(nodoActual.derecho)

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
        print("Imprimiendo en orden: ", end="")
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
        print("Imprimiendo en post orden: ", end="")
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
        print("Imprimiendo en pre orden: ", end="")
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
   

if __name__ == "__main__":
    #vector = np.random.randint(100,size=6)
    vector = [10,20,30,40]
    avl = arbolAVL()
    for i in  vector:
        avl.insertar(i)
    
    avl.imprimirEnOrden()
    print(" ")
    avl.imprimirEnPreOrden()
    print(" ")
    avl.imprimirEnPostOrden()
    print(" ")
    print("El valor máximo es:", avl.valorMaximo() )
    print("El valor mínimo es:", avl.valorMinimo() )
    #avl.remover(40)


