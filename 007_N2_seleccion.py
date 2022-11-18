import time 
import numpy as np 

def selection_sort(seq):
	for i in range(len(seq) -1, 0, -1):
		max_j = i
		for j in range(max_j):
			if seq[j] > seq[max_j]:
				max_j = j
			seq[i], seq[max_j] = seq[max_j], seq[i]
	return seq


if __name__ == "__main__":
	
	inicio = time.perf_counter()		
	vector = np.random.randint(10, size=22)
	
	print( "Vector en desorden -->", vector )
	vector = selection_sort(vector)
	final = time.perf_counter()
	print( "Vector en orden    -->", vector )
	print(f"Elementos ordenados en  {final - inicio : 0.4f} seconds")
