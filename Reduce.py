#Reduce - Recebe uma lista e devolve um unico valor atravês de alguma operação
#A função reduce precisa ser importada antes
from functools import reduce

#função usada para somar os valores
def soma(x, y):
	return x+y

lista = [1, 3, 4, 5, 7, 10, 20,]

#valor_reduce = reduce(operação, lista)
resultado = reduce(soma, lista)

print(resultado)