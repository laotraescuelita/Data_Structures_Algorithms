//Implementar la estructura de datos: Pila.

class Colas{ //Creamos un objeto llamado pila.
	constructor(){ //El método constructor no recibe parametros.
		this.cola = []
  }

	cantidad(){ //Tiempo de ejecución O(1).
		return len(this.cola) //Método que nos indica la cantidad de elementos dentro de la pila.
  }

	estaVacio(){ //Tiempo de ejecución O(1).
		return len(this.cola) == 0 //Devuelve verdadero si el tamaño es igual a cero.
  }

	insertar(elemento){ //Tiempo de ejecución O(1).
		this.cola.push(elemento) //El nuevo elemtno es almacenado al fina de la pila.
  }

	extraer(){ //Tiempo de ejecución O(1).
		if (this.estaVacio()){ 
			return  //Si la lista esta vacia nos saca de la ejecución del programna.
    }
		return this.cola[-1] //En caso contrario nos devuelve el ultimo elemento en la pila.
    
  }
	
	remover(){ //Tiempo de ejecución O(1).
		if (this.estaVacio()){ 
			return  //Si la lista esta vacia nos saca de la ejecución del programna.
    }
		return this.cola.pop() //Devuelve el ultimo elemento en la pila y lo elimina de la misma.
  }

  mostrarLista(){ //Tiempo de ejecución O(n)
		if (this.cola == null){ //Si la lista esta vacia se termina la ejecución del programa.
			return }
		else{ //De otra manera se recorre la lista y se imprimen cada uno de sus elementos.
			for (var i=0; i < this.cola.length; i++ ){        
				textAlign(CENTER)        
        text(this.cola[i], 100, i*30)
        ellipse(100, i*30, 30,30)  
      }
			
      }     
    } 
      


} // cierra la clase pilas

// Visualizar resultados en el navegador. 
var c 
function setup() {
  createCanvas(800, 400) // Definir las dimensiones de la pantalla.
  c = new Colas()
  
  for (var i = 0; i < 10; i++) {
    c.insertar(floor(random(0, 100)))
  }
  console.log( c.cola ) 
}


function draw() {
  background(0) // El color de fondo es negro.
  stroke(255) // El grosor del trazo.
  noFill() // La figura no tiene relleno.
  c.mostrarLista()
}
	