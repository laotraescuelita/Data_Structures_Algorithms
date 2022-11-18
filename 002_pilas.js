//Implementar la estructura de datos: Pila.

class Pilas{ //Creamos un objeto llamado pila.
	constructor(){ //El método constructor no recibe parametros.
		this.pila = []
  }

	cantidad(){ //Tiempo de ejecución O(1).
		return len(this.pila) //Método que nos indica la cantidad de elementos dentro de la pila.
  }

	estaVacio(){ //Tiempo de ejecución O(1).
		return len(this.pila) == 0 //Devuelve verdadero si el tamaño es igual a cero.
  }

	apilar(elemento){ //Tiempo de ejecución O(1).
		this.pila.push(elemento) //El nuevo elemtno es almacenado al fina de la pila.
  }

	extraer(){ //Tiempo de ejecución O(1).
		if (this.estaVacio()){ 
			return  //Si la lista esta vacia nos saca de la ejecución del programna.
    }
		return this.pila[-1] //En caso contrario nos devuelve el ultimo elemento en la pila.
    
  }
	
	remover(){ //Tiempo de ejecución O(1).
		if (this.estaVacio()){ 
			return  //Si la lista esta vacia nos saca de la ejecución del programna.
    }
		return this.pila.pop() //Devuelve el ultimo elemento en la pila y lo elimina de la misma.
  }

  mostrarLista(){ //Tiempo de ejecución O(n)
		if (this.pila == null){ //Si la lista esta vacia se termina la ejecución del programa.
			return }
		else{ //De otra manera se recorre la lista y se imprimen cada uno de sus elementos.
			for (var i=0; i < this.pila.length; i++ ){        
				textAlign(CENTER)        
        text(this.pila[i], 100, i*30)
        ellipse(100, i*30, 30,30)  
      }
			
      }     
    } 
      


} // cierra la clase pilas

// Visualizar resultados en el navegador. 
var p 
function setup() {
  createCanvas(800, 400) // Definir las dimensiones de la pantalla.
  p = new Pilas()
  
  for (var i = 0; i < 10; i++) {
    p.apilar(floor(random(0, 100)))
  }
  console.log( p.pila ) 
}


function draw() {
  background(0) // El color de fondo es negro.
  stroke(255) // El grosor del trazo.
  noFill() // La figura no tiene relleno.
   p.mostrarLista()
}
	