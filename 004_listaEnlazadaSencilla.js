//Implementar la estructura de datos: Lista enlazda sencilla.

class Nodo{ //Crear objeto nodo que almacena elementos y apunta al siguiente nodo.
	constructor(elemento, x , y){ //El método contructor recibe el elemento.
		this.elemento = elemento
		this.siguiente = null
    	this.x = x 
    	this.y = y
  }
}//Cierra la clase nodo.

class ListaEnlazadaSencilla{ //Crear el objeto lista enlazda que realiza las oeraciones de insercion, eliminacion, etc..
	constructor(){
		this.cabeza = null
		this.tamaño = 0 
  }

	cantidadElementos(){
		return this.tamaño
  }

	insertarAlIncio(elemento){ //Tiempo de ejecución O(1)
		if (this.cabeza == null){ //Si la lista esta vacia se inicia el nodo cabeza con el primer valor.
			this.cabeza = new Nodo(elemento, 40, height/2)
    }else{
			let nodoNuevo = new Nodo(elemento, this.cabeza.x + 40, this.cabeza.y) //De otra manera el nuevo elemento se almacena en un nodo.
			nodoNuevo.siguiente = this.cabeza //El nuevo nodo apunta a la cabeza.
			this.cabeza = nodoNuevo //El nuevo nodo ahora es la cabeza.
		  self.tamaño += 1 //Se incrementa la propiedad tamaño.
    }
  } 
	
	imprimirLista(){ //Tiempo de ejecución O(n)
		if (this.cabeza == null){ //Si la lista esta vacia se termina la ejecución del programa.
			return }
		else{ //De otra manera se recorre la lista y se imprimen cada uno de sus elementos.
			let nodoActual = this.cabeza //El primer nodo es la cabeza.
			let lista = ""
			while (nodoActual){ //Mientras el valor de nodo no este vacio se recorrer la lista.
				lista += nodoActual.elemento + " --> " //Esta variable almacena los elementos de la lista.
				nodoActual = nodoActual.siguiente //El nodo actual adquier el valor del siguiente nodo.
      }
		console.log(lista) //se imprimen los elementos de la lista.
    }
  }

  	mostrarLista(){ //Tiempo de ejecución O(n)
		if (this.cabeza == null){ //Si la lista esta vacia se termina la ejecución del programa.
			return }
		else{ //De otra manera se recorre la lista y se imprimen cada uno de sus elementos.
			let nodoActual = this.cabeza //El primer nodo es la cabeza.	      
      
    		while (nodoActual){ //Mientras el valor de nodo no este vacio se recorrer la lista.
			textAlign(CENTER)
        	text(nodoActual.elemento, nodoActual.x, nodoActual.y)
        	ellipse(nodoActual.x, nodoActual.y, 30,30)  
				nodoActual = nodoActual.siguiente //El nodo actual adquier el valor del siguiente nodo.
      }     
    } 
    }  

  } // cierra la clase lista


// Visualizar resultados en el navegador. 
var lls 
function setup() {
  createCanvas(800, 400) // Definir las dimensiones de la pantalla.
  lls = new ListaEnlazadaSencilla()
  
  for (var i = 0; i < 10; i++) {
    lls.insertarAlIncio(floor(random(0, 100)))
  }

  lls.imprimirLista()
}

function draw() {
  background(0) // El color de fondo es negro.
  stroke(255) // El grosor del trazo.
  noFill() // La figura no tiene relleno.
  lls.mostrarLista()
}
	