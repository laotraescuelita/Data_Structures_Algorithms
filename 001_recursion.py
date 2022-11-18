#Importamos librerias de python.
import numpy as np 
import matplotlib.pyplot as plt
import time

#Recursión.
#Ejemplo con la serie de fibonacci la cual suma los dos valores anteriores comenzando con cero y uno. 
#n = 0,1,1,2,3,5,8,13,21,34....

print("Serie de fibonacci")
print(" ")

#Variables
n = 22

def fibonacci( n ):
	if n <= 0:
		return 1		
	return fibonacci(n-1) + fibonacci(n-2)


#Calcular el tiempo que tarda en devolver los valores.
inicio = time.perf_counter()		
for n in range(n):
	print(n, ":", fibonacci(n))
final = time.perf_counter()
print(f"Valores devueltos en: {final - inicio : 0.4f} seconds")
print(" ")

print("Serie de fibonacci con memorización" )
print(" ")
#Memorizaremos los valores que se repitan en este diccionario.
memorizacion = {}
def fibonacci_memorización( n ):	
	if n in memorizacion:  #Si el valor ya esta en el diccionario lo devolvemos para no entrar en la recursión.
		return memorizacion[n]
	valor = fibonacci(n-1) + fibonacci(n-2)  #Si no esta el valor entramos en la recursión.	
	memorizacion[n] = valor #Memorizamos el valor.
	return valor #Devolvemos 

#Calculamos el tiempo de ejecución con la técnica de memorización.
inicio = time.perf_counter()		
for n in range(n):
	print( n, " : ", fibonacci_memorización(n))
final = time.perf_counter()
print(f"Valores devueltos en: {final - inicio : 0.4f} seconds")
print(" ")

print("Serie de fibonacci forma tabular" )
print(" ")

fibonacci = [-1]*(n-1)  #Iniciamos un vector que contendra los valores de la serie.
def fibonacci_tabular( n ):	
	fibonacci[0] = 0 #Escribimos los indices uno y dos con el valor uno. 
	fibonacci[1] = 1
	
	for i in range(2,n): #Con este bucle llenamos el vector con la suma de los valores anteriores.
		fibonacci[i] = fibonacci[i-2] + fibonacci[i-1]
	return fibonacci

#Calculamos el tiempo de ejecución con la técnica tabular.
inicio = time.perf_counter()		
for n in range(n):
	print( n, " : ", fibonacci_tabular(n))
final = time.perf_counter()
print(f"Valores devueltos en: {final - inicio : 0.4f} seconds")
print(" ")


