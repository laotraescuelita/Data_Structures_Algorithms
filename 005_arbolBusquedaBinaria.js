//Implementar la estructura de datos: Árbol de busqueda binaria.

class Nodo{
  constructor(elemento, x, y){
    this.elemento = elemento
    this.left = null
    this.right = null
    this.x = x 
    this.y = y
    this.distancia = 2
  }
}

class ArbolBusquedaBinaria{ //Objeto que inserta, elimina, imprime y cumple las propiedades del árbol binario.
  constructor(){
    this.raiz = null //El árbol tiene un nodo inicio llamado raiz.
    this.indice = 0 // Llevar el tamaño del vector
  }

  insertar(elemento){ //Mejor caso O(log(n)), peor caso O(n).
    if (this.raiz === null){ //Si no hay raiz comenzar el árbol con el elemento.
      this.raiz = new Nodo(elemento, width/2, 16)
      
    } else { //De otra manera insertar el elemento cumpliendo las propiedades del árbol binario.
      this._insertar(elemento,this.raiz)
    }
  }
  
  _insertar(elemento, nodo){
    if (elemento < nodo.elemento){ //Si el elemento es menor que el elemento del nodo raiz ir a la izquierda.
      if (nodo.izquierdo){ //Si el nodo de la izquierda tiene un elemento recorrer el árbol recursivamente.        
        this._insertar(elemento,nodo.izquierdo)
      } else{ //Si el nodo no tiene elementos hay que almacenar el elemento ahí.
        nodo.izquierdo = new Nodo(elemento, nodo.x - 50, nodo.y + 50)//nodo.x - (width / pow(2, this.distancia)), nodo.y + (height / 12) )
      }
    }
    else if (elemento > nodo.elemento){ //Si el elemento es menor que el elemento del nodo raiz ir a la derecha.
      if (nodo.derecho){ //Si el nodo derecho tiene un elemento hay que recorrer el árbol recursivamente.
        this._insertar(elemento,nodo.derecho) 
      } else{ //De otra manera hay que insertar el elemento ahí.
        nodo.derecho = new Nodo(elemento, nodo.x + 50, nodo.y + 50 )//nodo.x + (width / pow(2, this.distancia)), nodo.y + (height / 12) )  
      }
    }
  }
  
  imprimirEnOrden(){
    if (this.raiz == null){
      return
    }
    else{
      this._imprimirEnOrden(this.raiz)
    }
  }

  _imprimirEnOrden(nodoActual){
    if (nodoActual == null){
      return    
    }    
    
    console.log("Imprimiendo en orden", nodoActual.elemento)    
    this._imprimirEnOrden(nodoActual.izquierdo)     
    this._imprimirEnOrden(nodoActual.derecho)
  }

  mostrarArbol(){
    if (this.raiz == null){
      return
    }
    else{
      this._mostrarArbol(this.raiz)
    }
  }

  _mostrarArbol(nodoActual){
    if (nodoActual == null){
      return    
    }  
    
    textAlign(CENTER)    
    text(nodoActual.elemento, nodoActual.x, nodoActual.y)        
    ellipse(nodoActual.x, nodoActual.y, 30,30)  
    this._mostrarArbol(nodoActual.izquierdo)     
    this._mostrarArbol(nodoActual.derecho)
  }

} // Llave que cierra la clase arbol  


// Visualizar resultados en el navegador. 
var bst 
function setup() {
  createCanvas(800, 400) // Definir las dimensiones de la pantalla.
  bst = new ArbolBusquedaBinaria()
  
  for (var i = 0; i < 15; i++) {
    bst.insertar(floor(random(0, 100)))
  }

  bst.imprimirEnOrden()
}

function draw() {
  background(0) // El color de fondo es negro.
  stroke(255) // El grosor del trazo.
  noFill() // La figura no tiene relleno.
  bst.mostrarArbol()
}
