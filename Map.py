#Map - Pega um lista e aplica nela uma função a todos os elementos

#função para dobrar o valor
def dobro(x):
	return x*2

valor = [1, 2, 3, 4, 5]

#lista_map = map(função, lista)
valor_dobrado = map(dobro, valor)

#Temos que converter para uma lista, porque a função Map devolver no formato map
valor_dobrado = list(valor_dobrado)
print(valor_dobrado)