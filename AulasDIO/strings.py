nome = "Marina"
idade = 40
formacao = "ADS"
valor = 23.456

#metodo format, mantendo as variaveis na ordem
print("Meu nome é {}, tenho {} anos e sou formada em {}".format(nome,idade,formacao))

#metodo format, sem ordem nas variaveis
print("Meu nome é {1}, tenho {2} anos e sou formada em {0}".format(formacao,nome,idade))

#metodo f-string
print(f"Meu nome é {nome}, tenho {idade} anos e sou formada em {formacao}")
print(f"O valor é {valor:.1f}")
print(f"O valor é {valor:15.1f}")#com espaço
