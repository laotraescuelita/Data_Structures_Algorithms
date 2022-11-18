//Implementar la estructura de datos: Lista enlazada Doble.

class Nodo{ //Crear el objeto nod que almacena el elemento y los apuntadores siguiente y anterior.
	constructor(elemento, x, y){ //El método contructor recibe el elemento por parametro.
		this.elemento = elemento
		this.siguiente = null
		this.anterior = null
		this.x = x
		this.y = y 
	}
	} // cierra la clase nodo

class ListaEnlazadaDoble{ //Crear el objeto que tiene los métodos insertar, eliminar etc...
	constructor(){
		this.cabeza = null
		this.cantidad = 0
	}

	cantidadElementos(){ //Tiempo de ejecución O(1)
		return this.cantidad //Devuelve la cantidad de elementos en la lista.	
	}

	insertarAlIncio(elemento){ //Tiempo de ejecución O(1)
		if (this.cabeza == null){ //Si la lista esta vacia hay que iniciar la cabeza con el elemento.
			this.cabeza = new Nodo(elemento, 40, height/2)
		}else{
			let nodoNuevo = new Nodo(elemento, this.cabeza.x + 40, this.cabeza.y) //De otra manera hay que crear un nodo nuevo con el elemento.
			nodoNuevo.siguiente	= this.cabeza // El nuevo nodo apunta a la cabeza.
			this.cabeza.anterior = nodoNuevo //La cabeza apunta al nuevo nodo.
			this.cabeza =  nodoNuevo //y el nodo nuevo toma la posición de la cabeza.
		}
		this.cantidad += 1 //Incrementamos el numero de elementos.
	}	

	imprimirLista(){ //Tiempo de ejecución O(n)
		if (this.cabeza == null){ //Si la lista esta vacia salimos de la ejecución del programa.
			return
		}else{ //De otra manera lo recorremos mientras imprimos los elementos.
			let nodoActual = this.cabeza //Actualizamos el nodo comenzando con la cabeza.
			let lista = ""
			while (nodoActual){ //Mientras el valor de nodo no este vacio se recorrer la lista.
				lista += " <-- " + nodoActual.elemento + " --> " // Esta variable va almacenando los elementos.
				nodoActual = nodoActual.siguiente
			}
		console.log(lista)
		}
	}

	mostrarLista(){ //Tiempo de ejecución O(n)
		if (this.cabeza == null){ //Si la lista esta vacia se termina la ejecución del programa.
			return 
		}else{ //De otra manera se recorre la lista y se imprimen cada uno de sus elementos.
			let nodoActual = this.cabeza //El primer nodo es la cabeza.	      
      
    	while (nodoActual){ //Mientras el valor de nodo no este vacio se recorrer la lista.
				textAlign(CENTER)
				text(nodoActual.elemento, nodoActual.x, nodoActual.y)
				ellipse(nodoActual.x, nodoActual.y, 30,30)  
				nodoActual = nodoActual.siguiente //El nodo actual adquier el valor del siguiente nodo.
      }     
    } 
    }  

} // cierra la clase lista doble

// Visualizar resultados en el navegador. 
let lld 
function setup() {
  createCanvas(800, 400) // Definir las dimensiones de la pantalla.
  lld = new ListaEnlazadaDoble()
  
  for (var i = 0; i < 10; i++) {
    lld.insertarAlIncio(floor(random(0, 100)))
  }

  lld.imprimirLista()
}

function draw() {
  background(0) // El color de fondo es negro.
  stroke(255) // El grosor del trazo.
  noFill() // La figura no tiene relleno.
  lld.mostrarLista()
}
	