import sys
# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:
itens = []

# TODO: Crie um loop para solicita os itens ao usuário:
print("Digite os itens a serem adicionados: ")
while len(itens) < 3:
# TODO: Solicite o item e armazena na variável "item":
    item = sys.stdin.readline()
# TODO: Adicione o item à lista "itens":
    itens.append(item)


# Exibe a lista de itens
print("Lista de Equipamentos:")  
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")