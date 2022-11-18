function setup() {
  createCanvas(800, 400) // Definir las dimensiones de la pantalla.
}

function draw() {
  background(0) // El color de fondo es negro.
  stroke(255) // El grosor del trazo.
  noFill() // La figura no tiene relleno.
  elipseRecursiva(300,200,300) // Función que dibuja de manera recursiva una elipse.
  
}

function elipseRecursiva(x,y,d){
  ellipse(x,y,d) // Dibuja una elipse.
  if (d > 2){
    //let nd = d * random(0.2,0.85)
    elipseRecursiva(x+d*0.5,y,d*0.5) // Dibuja otra elipse de manera recursiva a la derecha.
    elipseRecursiva(x-d*0.5,y,d*0.5) // Dibuja otra elipse de manera recursiva a la izquierda.
    //elipseRecursiva(x,y+d*0.5,d*0.5) // Dibuja otra elipse de manera recursiva hacia abajo.
    //elipseRecursiva(x,y-d*0.5,d*0.5) // Dibuja otra elipse de manera recursiva hacia arriba.
  }
  
}
