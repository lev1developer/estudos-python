# operacoes aritmedicas

# no python, podemos fazer calculos matematicos utilizando os operadores aritmeticos, que sao:

# soma +
soma = 1 + 1
print("1+1 =", soma)

# subtracao -s
subtracao = 2 - 1
print("2-1 =", subtracao)

# multiplicacao *
multiplicacao = 2 * 2
print("2*2 =", multiplicacao)

# divisao /
divisao = 4 / 2
print("4/2 =", divisao) #na divisao, o resultado sempre sera um float, mesmo que a divisao seja exata

# funcao int()
print("4/2 valor em inteiro =", int(divisao)) #para transformar o resultado em inteiro, podemos utilizar a funcao int()
print("4/2 valor em inteiro com tipo=", int(divisao), type(divisao)) #transformando o resultado em inteiro e verificando o tipo de dado

# funcao float()
print("1+1 =", float(soma)) #para transformar o resultado em float, podemos utilizar a funcao float()

# modulo %

modulo = 5 % 2
print("modulo 5%2 =", modulo) #o resultado sera 1, pois 5 dividido por 2 tem o resto 1 (modulo)

# divisao inteira //
divisao_inteira = 5 // 2
print("divisao inteira 5//2 =", divisao_inteira) #o operador // retorna o quociente da divisao, ou seja, a parte inteira que é 2, pois 5 dividido por 2 é 2.5, e a parte inteira é 2