#Zip - Vai concatenar duas ou mais listas

lista1 = [1, 2, 3, 4, 5]
lista2 = ["ana", "bernardo", "caio", "daniel", "eduardo"]
lista3 = ["azul", "branco", "cinza", "rosa", "esmeralda"]

#for x, y, z in zip(lista1, lista2, lista3)
for numero, nome, cor in zip(lista1, lista2, lista3):
	print(numero, nome, cor)