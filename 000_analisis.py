
#Importamos librerias de python.
import numpy as np 
import matplotlib.pyplot as plt

#****************************************BUCLES************************************************************
#Analisis de tiempo de las siguientes funciones.
#Variables
n = 11
m = 11
#n y m representan una unidad de tiempo por cada sentencia dentro de la función.


print("Analisis de una función lineal.")
print(" ")
print("Funcion Lineal.")
def funcionLineal( n ):
	for i in range( n ):                    # n + 1		
		print("Incremento i-->", i)			# n	
# Se suma el numero de unidades de tiempo en este caso es 2n + 1.
#Nos interesa el grado de la ecuación resultante.
#Así la complejidad de este algoritmo es de O( n ) y es lineal.
funcionLineal(n)
print(" ")




print("Analisis de una función cuadratica.")
print(" ")
print("Funcion Cuadratica.")
def funcionCuadratica( m , n  ):
	for i in range( m ):						# n + 1			= n + 1 
		print("Incremento i-->", i)				# n * n 		= n^2
		for j in range( n ):					# n * ( n + 1)	= n^2 + n
			print("		Incremento j-->", j)	# n * n 		= n^2
#La ecuación es 3n^2 + 2n+ 1, pero solo nos interesa el grado mayor.
#Complejidad es de O( n^2 ) y es cuadratica.
funcionCuadratica(m,n)
print(" ")




print("Analisis de una función cuadratica.")
print(" ")
print("Funcion Cuadratica.")
def funcionCuadratica( n ):
	for i in range( n ):						# n + 1			= n + 1 
		print("Incremento i-->", i)				# n * n 		= n^2
		for j in range( i ):					# n * ( n + 1)	= n^2 + n
			print("		Incremento i-->", j)	# n * n 		= n^2
#La ecuación es n(n+1)/2 --> n**2 + 2
#Complejidad es de O( n^2 ) y es cuadratica.
funcionCuadratica(n)
print(" ")


print("Analisis de una función radical.")
print(" ")
print("Funcion Radical.")
def funcionRadical( n ):
	p = 0
	for i in range( n ):						      # n + 1  
		if p < n:                                     # n + 1
			p += i								      # n + 1 
			print("Incremento i-->", i, "Incremento p-->", p)		  		  # n			
#La ecuación es P = k(k+1) / 2 si sabemos que p < k asi que k**2 > n  --> k > raiz(n).
#Complejidad es de O( raiz(n) ) y es radical.
funcionRadical(n)
print(" ")



print("Analisis de una función logaritmica.")
print(" ")
print("Funcion logaritmica.")
def unidadDeTiempo( n ):
	for i in range( n ):						  	# n + 1			
		i *= 2										# n	
		if i >= n:									# n			
			return 									# n
		print("Incremento i-->", i)    				# n
#Se asume que i = 2**k -> 2**k>n -> 2**k=n -> k=log(n)
#Complejidad es de O( log(n) ) y es logaritmica.
unidadDeTiempo(n)
print(" ")



print("Analisis de una funcion lineal.")
print(" ")
print("Funcion Lineal.")
def funcionLineal(n):
	for i in range(n):						  			# n + 1	
		print("Incremnento i-->", i)	    			# n
	for j in range(n):									# n + 1
		print("		Incremnento j-->", j)	    		# n
#Se asume cada unidad de tiempo por separado y asi el resultado es 4n + 1 = 2n
#Complejidad es de O( n ), es lineal y no exponencial.
funcionLineal(n)
print(" ")



#Recursión.
#Variebles
n = 3

print("Analisis de una función recursiva lineal.")
print(" ")
print("Funcion recursiva Lineal.")
def funcionRecursivaLineal( n ):
	if n > 0:								# 1
		print("Incremento n-->", n)			# n
		funcionRecursivaLineal(n-1)			# T(n-1)
#Sumamos las unidades de tiempo y el resultado es T(n-1)+n+1 = 2n.
#El analisis de tiempo es o( n ), lineal.
funcionRecursivaLineal(n)
print(" ")


#****************************************RECURSION************************************************************
print("Analisis de una función recursiva exponencial.")
print(" ")
print("Funcion recursiva Exponencial.")
def funcionRecursivaExponencial( n ):	
	if n > 0:								# 1
		for i in range( n ):				# n + 1
			print("Incremento n-->", n)		# n
		funcionRecursivaExponencial(n-1)	# T(n-1)
#Sumamos las unidades de tiempo y el resultado es T(n-1)+2n+2 = T(n-1)+n = n^2.
#El analisis de tiempo es o( n^2 ), expoencial.
funcionRecursivaExponencial(n)
print(" ")



print("Analisis de una función recursiva logaritmica.")
print(" ")
print("Funcion recursiva Logaritmica.")
def funcionRecursivaLogaritmica( n ):	
	if n > 0:								# 1
		for i in range( n ):				# n + 1
			i*=2							# log(n) 
			print("Incremento n-->", n, "Incremento i-->", i)		# n
		funcionRecursivaLogaritmica(n-1)	# T(n-1)
#Sumamos las unidades de tiempo y el resultado es T(n-1)+log(n).
#El analisis de tiempo es o( nlog(n) ), expoencial.
funcionRecursivaLogaritmica(n)
print(" ")

#Formas de las funciones en un gráfico.
x = np.linspace(0.5,2,num=1000)
plt.scatter(x,x//x, label=("Constante"))
plt.scatter(x,np.log(x), label=("Logaritmica"))
plt.scatter(x,np.sqrt(x), label=("Radical"))
plt.scatter(x,x, label=("Lineal"))
plt.scatter(x,x**2, label=("Cuadratica"))
plt.scatter(x,2**x, label=("Exponencial"))
plt.xlabel("Eje de las x´s")
plt.ylabel("Eje de las y´s")
plt.legend()
plt.show()
