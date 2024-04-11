# -*- coding: utf-8 -*-
depositos = []
saques = []
saldo = 0
numero_saques = 3

opcao = ""
while opcao != "x":
    menu = '''
    ##### OPÇÕES #####

    [d] DEPOSITAR
    [s] SACAR
    [e] EXTRATO
    [x] ENCERRAR

    ##################
    '''

    while True:
        opcao = input(menu)

        if opcao == "d":
            print("Operação - Depósito")
            valor_dep = float(input("Informe o valor a ser depositado: "))
            if valor_dep < 0:
                print("Não permitido depósito de valor negativo")
            else:
                depositos.append(valor_dep)
                saldo += valor_dep
                print(f"Depósito realizado, seu saldo é: R$ {saldo:.2f}")
        elif opcao == "s":
            print("Operação - Saque")
            print(f"Limite de saques disponíveis: {numero_saques}")
            valor_saque = float(input("Informe o valor a ser sacado: "))

            if numero_saques == 0:
                print("Número máximo de saques excedido")
            elif valor_saque > 500:
                print("Valor máximo permitido é R$ 500,00")
            elif saldo <= 0:
                print("Saldo insuficiente")
            elif valor_saque >0:
                saldo -= valor_saque
                saques.append(valor_saque)
                numero_saques -= 1
                print(f"Saque realizado, seu saldo é: R$ {saldo:.2f}")
                print(f"Limite de saques disponíveis: {numero_saques}")  
            else:
                print("Valor inválido para saque")  
        elif opcao == "e":
            print("Operação - Extrato")
            i = 0
            for i in range(len(depositos)):
                print(f"Depósito {i} no valor de + {depositos[i]}")
                i += 1
            for i in range(len(saques)):
                print(f"Saque {i} no valor de - {saques[i]}")
                i += 1
            print(f"Saldo final R$ {saldo:.2f}")
        elif opcao == "x":
            print("Obrigada por usar nosso sistema")
            break
