//Implementar el algoritmo "Breath first search"

class BFS{ //crear el objeto bfs
    constructor(inicio, final, grafo){ //El método contructor recibe el nodo inicio el final y el grafo.
        this.inicio = inicio
        this.final = final
        this.grafo = grafo
        this.enCola = []
        this.visitado = {}
        this.recorrido = {}

        this.enCola.push(this.inicio) //La cola inicia con el vertice  inicio del grafo.
        this.visitado = { inicio : null} //Diccionario almacena los vertices ya visitados.

    }

    bfs(){
        
        while (this.enCola){ //Mientras haya vertices en la cola.
            let nodoActual = this.enCola.pop() //Se extrae el valor que haya en cola.
            if (nodoActual == this.final){ //El inicio y el final es el mismo, se sale de la ejecución.
                break 
            }
            //En otro caso hay que recorrer los vertices que esten conenctados al nodo actual.
            let nodosSiguientes = grafo[nodoActual] //En una lista se pasan los vertices conectados al vertice actual.
            for (let nodoSiguiente in nodosSiguientes){ //Se recorre cada vertice.
                if (!(nodoSiguiente in this.visitado)){ //Si el vertice no ha sido visitado.
                    this.enCola.push(nodoSiguiente) //El vertice se pone en cola.
                    this.visitado[nodoSiguiente] = nodoActual //El vertice se coloca como vistado y de que vertice se visito.
                }
            }
        return this.visitado
        }
    }

    recorrido(){        
    nodoActual = this.final //Para conocer el recorrido de inicio al final se inicia el vertice objetivo.
    while (nodoActual != this.inicio){ //Se recorre el diccionario hasta que el vertice coincida con el inicio.
        nodoActual = this.visitado[nodoActual]  //Se va recorriendo de acuerdo al vertice del que llegamos al actual.
        console.log('---> {nodoActual} ') //Se van imprimiendo los vertices.
    }

    }
}// Cierra la clase bfs

function setup() {
    createCanvas(800, 400) // Definir las dimensiones de la pantalla.
    //Grafo se almacena en un diccionario
    grafo = {'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'E'],
        'D': ['B', 'E'],
        'E': ['C', 'D']}

    inicio = 'A'
    final = 'E'
    let bfs = new BFS(inicio, final, grafo)
    recorrido = bfs.bfs()
    console.log("Este es el recorrido del grafo: \n", recorrido)

  }
  
  function draw() {
    background(0) // El color de fondo es negro.
  }
  

