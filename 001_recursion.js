//Importamos librerias de python.

//Recursión.
//Ejemplo con la serie de fibonacci la cual suma los dos valores anteriores comenzando con cero y uno. 
//n = 0,1,1,2,3,5,8,13,21,34....

console.log("Serie de fibonacci")

//Variables
n = 11

function fibonacci( n ){
	if ( n <= 0 ){
    	return 1
  }
  return fibonacci(n-1) + fibonacci(n-2)  
  
}
//Calcular el tiempo que tarda en devolver los valores.
var inicio = Date.now()
for (i=0; i<=n; i++){
	console.log(i, ":", fibonacci(i))
}
var final = Date.now()
console.log("Elementos devueltos en ", final-inicio)


console.log("Serie de fibonacci con memorización" )
//Memorizaremos los valores que se repitan en este diccionario.
var memorizacion = {}
function fibonacciMemorizacion( n ){	
	if (n in memorizacion){  //Si el valor ya esta en el diccionario lo devolvemos para no entrar en la recursión.
		return memorizacion[n]
  }
	var valor = fibonacciMemorizacion(n-1) + fibonacciMemorizacion(n-2)  //Si no esta el valor entramos en la recursión.	
	memorizacion[n] = valor //Memorizamos el valor.
	return valor 
}

//Calculamos el tiempo de ejecución con la técnica de memorización.
//Calcular el tiempo que tarda en devolver los valores.
var inicio = Date.now()
//for (i=0; i<=n; i++){
//	console.log(i, ":", fibonacciMemorizacion(i))
//}
var final = Date.now()
console.log("Elementos devueltos en ", final-inicio)



console.log("Serie de fibonacci forma tabular" )

var vectorFibonacci = [-1]*(n-1)  //Iniciamos un vector que contendra los valores de la serie.
function fibonacciTabular( n ){	
	vectorFibonacci[0] = 0 //Escribimos los indices uno y dos con el valor uno. 
	vectorFibonacci[1] = 1
	
	for (i=2; i<=n; i++){ //Con este bucle llenamos el vector con la suma de los valores anteriores.
		vectorFibonacci[i] = vectorFibonacci[i-2] + vectorFibonacci[i-1]
	return vectorFibonacci
  }
}
//Calculamos el tiempo de ejecución con la técnica tabular.
//Calcular el tiempo que tarda en devolver los valores.
var inicio = Date.now()
for (i=0; i<=n; i++){
	console.log(i, ":", fibonacciTabular(i))
}
var final = Date.now()
console.log("Elementos devueltos en ", final-inicio)
