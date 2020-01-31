#Usando List Comprehension para montar uma nova lista apartir dos numeros de x

x = [1, 2, 3, 4, 5]

# lista = [valor_a_adicionar  laço  condição]

#lista com os termos de x ao quadrado
y = [i**2 for i in x]

#lista com os termos de x impares
z = [i for i in x if i%2==1]

print(x)
print(y)
print(z)