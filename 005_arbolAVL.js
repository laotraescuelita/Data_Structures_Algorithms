//Implementar la estructura de datos: Árbol AVL.

class Nodo{
    constuctor(elemento){ //método constructor recibe el elemento a insertar.
        this.elemento = elemento
        this.izquierdo = null
        this.derecho = null
        this.altura = 1
    }
}


class arbolAVL{ //Objeto AVL que contiene las propiedades y métodos.
    constructor(){
        this.raiz == null     
    }
    
    insertar(elemento){ //Insertar el elemento.
        this.raiz = this._insertar(elemento, this.raiz)
    }

    _insertar(elemento, nodoActual){

        if (nodoActual == null){ //Si el nodo esta vacio insertamos el nuevo elemento.            
            return  new Nodo(elemento)
        }

        else if (elemento  < nodoActual.elemento){ //Si el elemento es menor al elemento de la raiz ir a la izquierda del árbol.
            nodoActual.izquierdo = this._insertar(elemento, nodoActual.izquierdo)
        }else{ //De otra manera nos vamos al lado derecho de árbol.
            nodoActual.derecho = this._insertar(elemento, nodoActual.derecho)
        }
    
        //Actualizar la altura del nodo que se ha isertado.        
        nodoActual.altura = 1 + max(this.obtenerAltura(nodoActual.izquierdo), this.obtenerAltura(nodoActual.derecho))
        
        // Actualizar el balance del árbol y cumplir las propiedades del árbol.
        let factorDeBalance = this.obtenerBalance(nodoActual)
                
        if (factorDeBalance > 1){ //Si el balance es mayor a 1.
            if (elemento < nodoActual.izquierdo.elemento){ //Si el elemento es menor al elemento del nodo izquierdo.
                return this.rotarAlaDerecha(nodoActual) //Hay que rotar a la derecha.
            }else{ //La otra manera es que el elemento es mayor al nodo izquierdo.
                nodoActual.izquierdo = this.rotarAlaIzquierda(nodoActual.izquierdo) //Hay que rotar a la izquierda primero.
                return this.rotarAlaDerecha(nodoActual) //Hay que rotar a la derecha después.
                }
            }

        if (factorDeBalance < -1){
            if (elemento > nodoActual.derecho.elemento){
                return this.rotarAlaIzquierda(nodoActual)
            }else{
                nodoActual.derecho = this.rotarAlaDerecha(nodoActual.derecho)
                return this.rotarAlaIzquierda(nodoActual)
                }
            }

        return nodoActual
    }
    
    rotarAlaIzquierda(z){
        y = z.derecho
        T2 = y.izquierdo
        y.izquierdo = z
        z.derecho = T2
        z.altura = 1 + max(this.obtenerAltura(z.izquierdo), this.obtenerAltura(z.derecho))
        y.altura = 1 + max(this.obtenerAltura(y.izquierdo), this.obtenerAltura(y.derecho))
        return y
    }


    rotarAlaDerecha(z){
        y = z.izquierdo
        T3 = y.derecho
        y.derecho = z
        z.izquierdo = T3
        z.altura = 1 + max(this.obtenerAltura(z.izquierdo), this.obtenerAltura(z.derecho))
        y.altura = 1 + max(this.obtenerAltura(y.izquierdo), this.obtenerAltura(y.derecho))
        return y
    }

    //Devolver la altura de cada nodo.
    obtenerAltura(nodoActual){
        if (nodoActual == null){
            return 0
        }
        return nodoActual.altura
    }

    // Devolver el balance del árbol.
    obtenerBalance(nodoActual){
        if (nodoActual == null){
            return 0
        }
        return this.obtenerAltura(nodoActual.izquierdo) - this.obtenerAltura(nodoActual.derecho)
    }

    imprimirEnOrden(){
        if (this.raiz == null){
            return 
        }else{
            this._imprimirEnOrden(this.raiz)
        }
    }

    _imprimirEnOrden(nodoActual){
        if (nodoActual == null){
            return
        }
        console.log(nodoActual.elemento)
        this._imprimirEnOrden(nodoActual.izquierdo)             
        this._imprimirEnOrden(nodoActual.derecho)
    }

} // cierra la clase AVL 

// Visualizar resultados en el navegador. 
let avl 
function setup() {
  createCanvas(800, 400) // Definir las dimensiones de la pantalla.
  avl = new arbolAVL()
  
  for (var i = 0; i < 10; i++) {
    avl.insertar(floor(random(0, 100)))
  }

  avl.imprimirEnOrden()
}

function draw() {
  background(0) // El color de fondo es negro.
  stroke(255) // El grosor del trazo.
  noFill() // La figura no tiene relleno.
  //avl.mostrarArbol()
}
