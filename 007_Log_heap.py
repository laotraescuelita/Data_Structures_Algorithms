#Implementar el algoritmo de ordenamiento : heaps.
import time 
import numpy as np 
import heapq

def heapOrdenamiento1( vector ): #Utilizando el módulo heapq
  h = []
  for elemento in vector:
    heapq.heappush(h, elemento)
  return [heapq.heappop(h) for i in range(len(h))]

"""
from heap import Heap 
def heapOrdenamiento2(vector):
  heap = Heap(vector)
  res = []
  for i in range(len(vector)):
    res.insert(0, heap.extract_max())
  return res


def heapOrdenamiento3(vector):
  for inicio in range( (len(vector)-2)//2, -1, -1):
    shiftdown(vector, inicio, len(vector)-1)
    for final in range(len(vector)-1, 0, -1):
      vector[fin], vector[0] = vector[0], vector[fin]
      shiftdown(vector, 0, final - 1)
  return vector

def shiftdown(vector, inicio, fin):
  raiz = inicio
  while True:
    hijo = raiz * 2 + 1
    if hijo > fin: break
    if hijo + 1 <= final and vector[hijo] < vector[hijo + 1]:
      hijo += 1
    if vector[raiz] < vector[hijo]:
      vector[raiz], vector[hijo] = vector[hijo], vector[raiz]
      raiz = hijo
    else:
      break
"""
if __name__ == '__main__':
	#Medir el tiempo de ejecucion
	import time
	inicio = time.perf_counter()
	vector = np.random.randint(10,size=22)
	print( "Vector en desorden -->", vector )
	heapOrdenamiento1( vector ) 
	print( "Vector en orden    -->", vector )
	final = time.perf_counter()
	print(f"Elementos ordenados en  {final - inicio : 0.4f} seconds")


