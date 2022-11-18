
class Item:
	def __init__(self, valor, peso):
		self.valor = valor
		self.peso = peso


def fractionalKnapsack(peso, vector):	
	vector.sort(key=lambda x: (x.valor/x.peso), reverse=True)	
	valorFinal = 0.0	
	
	for elemento in vector:
		if elemento.peso <= peso:
			peso -= elemento.peso
			valorFinal += elemento.valor

		else:
			valorFinal += elemento.valor * peso / elemento.peso
			break
	
	return valorFinal



if __name__ == "__main__":

	peso = 50
	vector = [Item(10, 2), Item(5, 3), Item(15, 5), Item(7, 7), Item(6, 1), Item(18, 4), Item(3, 1)]

	maximo_valor = fractionalKnapsack(peso, vector)
	print(maximo_valor)
