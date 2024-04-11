texto = input("Informe um texto: ")
vogais = "AEIOU"

for letra in texto:
    if letra.upper() in vogais: #upper converte para maiuscula
        print(letra, end="")
print()#quebra de linha

#posso usar também dessa forma
#for letra in texto:
#    if letra.upper() in vogais: #upper converte para maiuscula
#        print(letra, end="")
#else:
#    print()#quebra de linha