# -*- coding: utf-8 -*-
depositos = []
saques = []
saldo = 0
numero_saques = 0

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
            if valor_dep <= 0:
                print("Não permitido depósito de valor negativo")
            else:
                depositos.append(valor_dep)
                saldo += valor_dep
                print(f"Depósito realizado, seu saldo é: R$ {saldo:.2f}")
        elif opcao == "s":
            print("Operação - Saque")
            valor_saque = float(input("Informe o valor a ser sacado: "))

            if valor_saque > 500:
                print("Valor máximo permitido é R$ 500,00")
            elif saldo <= 0 or valor_saque > saldo:
                print("Saldo insuficiente")
            else:
                if numero_saques >=3:
                    print("Número máximo de saques excedido")
                saldo -= valor_saque
                saques.append(valor_saque)
                numero_saques += 1
                print(f"Saque realizado, seu saldo é: R$ {saldo:.2f}")
        elif opcao == "e":
            print("Operação - Extrato")
            i = 0
            for i in range(len(depositos)):
                print(f"Depósito no valor de + {depositos[i]}")
                i += 1
            for i in range(len(saques)):
                print(f"Saque no valor de - {saques[i]}")
                i += 1
            print(f"\nSaldo final R$ {saldo:.2f}")
        elif opcao == "x":
            print("Obrigada por usar nosso sistema")
            break
