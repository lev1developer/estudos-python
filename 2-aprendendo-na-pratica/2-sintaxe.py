#comentario de uma linha, é marcado com uma "hashtag", fora dessa linha, ele nn sera marcado como comentario.

"""comentario de varias linhas, 
é marcado com tres aspas duplas, 
e pode ser usado para documentar grandes blocos de codigo."""

nome = "Felipe" + "Levi"
print(nome)

idade = 18

if idade < 18: #isso é um bloco de condicional, tudo o que estiver dentro desse bloco, será executado caso a condicional seja verdadeira.
    print("Menor de idade") #isso é uma condicional, que será executada dentro do bloco "if idade < 18"
else: 
    print("Maior de idade") #isso é uma condicional, que será executada dentro do bloco "else"


"""resumindo, caso os dois prints estejam fora do bloco de condicional, 
eles não serão executado"""