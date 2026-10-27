# listas 

# listas sao uma sequencia de elementos ordenaveis e imutaveis, que podem ser de qualquer tipo de dado, como numeros, strings, booleanos, etc.

# declarando uma lista
lista = [1, 2, 3, 4, 5, True, False, "Hello", "World"] #os indicies começam do 0, ou seja, o primeiro elemento da lista tem indice 0, o segundo elemento tem indice 1, e assim por diante.

#exibindo a lista completa
print(lista)

#exibindo os elementos da lista
print(lista[0]) #acessando o primeiro elemento da lista, no caso o 1
print(lista[1]) #acessando o segundo elemento da lista, no caso o 2
print(lista[2]) #acessando o terceiro elemento da lista, no caso o 3


print(lista[:6]) #acessando os elementos da lista do indice 0 ao indice 5, ou seja, do primeiro elemento ao sexto elemento
print(lista[6:9]) #acessando os elementos da lista do indice 6 ao indice 8, ou seja, do sétimo elemento ao nono elemento
print(lista[2:5]) #acessando os elementos da lista do indice 2 ao indice 4, ou seja, do terceiro elemento ao quinto elemento