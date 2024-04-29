def ParImpar(numero):

    if numero % 2 == 0:
        return print("Numero e par")
    else:
        return print("Numero e impar")
    
def main():
    numero = input("Digite o numero para verificar se e par ou impar:")
    ParImpar(int(numero))

main()