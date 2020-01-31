#Função enumerate
#Ela tem como objetivo pegar uma lista e retornar o indice do item e o item nessa respectiva posição 

lista = ["ana" , "gabriel", "maria", "caio"]


#for índice_da_lista , item_da_lista in enumerate(lista)
for i, nome in enumerate(lista):
	print(i, nome)