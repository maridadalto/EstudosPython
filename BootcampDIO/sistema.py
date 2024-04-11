# -*- coding: utf-8 -*-
depositos = []
saques = []
saldo = 0
numero_saques = 0

def depositar():
    global saldo
    print("Operação - Depósito")
    valor_dep = float(input("Informe o valor a ser depositado: "))
    if valor_dep < 0:
        print("Não permitido depósito de valor negativo")
    else:
        depositos.append(valor_dep)
        saldo += valor_dep
        print(f"Depósito realizado, seu saldo é: R$ {saldo:.2f}")

def sacar():
    global saldo, numero_saques
    print("Operação - Saque")
    valor_saque = float(input("Informe o valor a ser sacado: "))
    if saldo <= 0:
        print("Saldo insuficiente")
    elif valor_saque > 500:
        print("Valor máximo permitido é R$ 500,00")
    else:
        saldo -= valor_saque
        saques.append(valor_saque)
        numero_saques += 1
        print(f"Saque realizado, seu saldo é: R$ {saldo:.2f}")
        if numero_saques >= 3:
            print("Número máximo de saques excedido")

def extrato():
    print("Operação - Extrato")
    for i, dep in enumerate(depositos):
        print(f"Depósito {i} no valor de + {dep}")
    for i, saq in enumerate(saques):
        print(f"Saque {i} no valor de - {saq}")
    print(f"Saldo final R$ {saldo:.2f}")

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

    opcao = input(menu)

    if opcao == "d":
        depositar()
    elif opcao == "s":
        sacar()
    elif opcao == "e":
        extrato()
    elif opcao == "x":
        print("Obrigada por usar nosso sistema")
        break
