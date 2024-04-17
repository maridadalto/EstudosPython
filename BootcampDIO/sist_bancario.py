# -*- coding: utf-8 -*-

def menu():
    menu = '''
    ##### OPÇÕES #####

    [d] DEPOSITAR
    [s] SACAR
    [e] EXTRATO
    [nu] NOVO USUÁRIO
    [nc] NOVA CONTA
    [lc] LISTAR CONTAS
    [x] ENCERRAR

    ##################
    '''
    return input(menu)

def depositar(saldo,valor,operacoes,/): #apenas por posicao
    if valor <= 0:
        print("Não permitido depósito de valor negativo")
    else:
        operacoes.append(f"Depósito no valor de R$ {valor:.2f}")
        saldo += valor
        print(f"Depósito realizado, seu saldo é: R$ {saldo:.2f}")
    return saldo, operacoes

def sacar(*, saldo,valor,numero_saques,operacoes):# apenas por palavras chaves
    if valor< 0:
        print("Não é permitido saque de valor negativo")
    else:
        if valor > 500:
            print("Valor máximo permitido é R$ 500,00")
        elif saldo <= 0 or valor > saldo:
            print("Saldo insuficiente")
        else:
            if numero_saques >=3:
                print("Número máximo de saques excedido")
            else:
                operacoes.append(f"Saque no valor de R$ {valor:.2f}")
                saldo -= valor
                numero_saques += 1
                print(f"Saque realizado, seu saldo é: R$ {saldo:.2f}")
    return saldo, operacoes, numero_saques

def extrato(saldo,/,*,operacoes):#por posicao e palavras chaves
    i = 0
    for i in range(len(operacoes)):
        print(operacoes[i])
        i += 1
    print(f"\nSaldo final R$ {saldo:.2f}")

def novo_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf,usuarios)

    #Verifico se já existe o CPF
    if usuario:
        print("CPF já cadastrado")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})
    print("Novo usuário cadastrado com sucesso!!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def nova_conta(agencia,numero_conta, usuarios):
    cpf = input("Informe o cpf do titular ca conta: ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("Conta criada com sucesso")
        return {"agencia": agencia,"numero_conta": numero_conta, "usuario": usuario}
    else:
        print("Usuário não encontrado, não foi permitido criar a nova conta")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print(linha)


def main():
    AGENCIA = "0001"
    operacoes = []
    saldo = 0
    numero_saques = 0
    usuarios = []
    contas = []
 
    while True:
        opcao = menu()

        if opcao == "d":
            print("Depósito")
            valor_dep = float(input("Informe o valor a ser depositado: "))
            saldo, operacoes = depositar(saldo,valor_dep,operacoes)
        elif opcao == "s":
            print("Saque")
            valor_saque = float(input("Informe o valor a ser sacado: "))
            saldo, operacoes, numero_saques = sacar(
                saldo = saldo,
                valor = valor_saque,
                numero_saques = numero_saques,
                operacoes = operacoes)
        elif opcao == "e":
            print("Extrato")
            extrato(saldo,operacoes=operacoes)
        elif opcao == "nu":
            novo_usuario(usuarios)
        elif opcao == "nc":
            numero_conta =len(contas)+1
            conta = nova_conta(AGENCIA, numero_conta,usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "x":
            print("Obrigada por usar nosso sistema")
            break

main()