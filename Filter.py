#Filter - Pega uma lista submete a uma condição e apartir disso faz uma nova lista condicionada

#Função Condicional, no caso essa pega os numeros pares
def pares(i):
	if i % 2 == 0:
		return i

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#lista_condicional = filter(função_condição, lista_base)
lista_pares = filter(pares, lista)

#ela retorna uma função filter, então é preciso converter lista_pares usando o list()
print(list(lista_pares))