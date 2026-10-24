
nome_completo = "Felipe Levi"   

nome_completo_quebra_de_linhas = """Felipe Levi


Sou um estudante de Python""" 

nome_com_linha_quebrada = "Felipe \n " \
"Levi " 

nome = "Felipe"

sobrenome = "Levi"

#formatacao

print("nome completo (1a forma):", nome_completo) #uniao das strings com a variavel, com um espaco entre elas
print("nome completo (2a forma):" + nome_completo) #uniao das strings sem espaco entre elas
print("nome completo (3a forma):" + "Felipe" + "Levi") # outra forma uniao das strings sem espaco entre elas
print("nome completo (4a forma):" + "Felipe", "Levi") # outra forma uniao das strings com um espaco entre elas
print("nome completo (5a forma):", nome_completo_quebra_de_linhas) #a funcao da quebra de linha com 3 aspas duplas
print("nome completo (6a forma):", nome_com_linha_quebrada) #a funcao da quebra de linha com \n
print("nome completo (7a forma): %s" % nome_completo) #uma substituicao de string com o operador %S
print("nome completo (8a forma): %s %s" % (nome, sobrenome)) #uma substituicao de string com o operador %S
print(f"nome completo (9a forma): {nome} {sobrenome}") #uma substituicao de string com f-string (format strings)
print("nome completo (10a forma): {} {}".format (nome, sobrenome)) #uma substituicao de string com o metodo .format()