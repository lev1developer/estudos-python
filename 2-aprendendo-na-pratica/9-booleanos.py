# Booleanos

# Booleanos são um tipo de dado que pode ter apenas dois valores: True (verdadeiro) ou False (falso). Eles são frequentemente usados para representar condições, estados ou resultados de comparações.

# condicionais
if False:
    print("Isso é verdadeiro! (bloco if executado)")
else:
    print("Isso é falso! (bloco else executado)")

# operador logicos: and e or

# and 
# precisamos de todas as condições verdadeiras para que o bloco if seja executado
if True and True:
    print("Isso é verdadeiro! (bloco if executado)")
else:
    print("Isso é falso! (bloco else executado)")

# or
# precisamos de apenas uma condição verdadeira para que o bloco if seja executado
if True or False or False:
    print("Isso é verdadeiro! (bloco if executado)")
else:
    print("Isso é falso! (bloco else executado)")