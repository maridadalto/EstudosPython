conta_normal = False
conta_universitaria = True
saldo = 2000
cheque_especial = 450
saque = 2300

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com o uso do cheque especial")
    else:
        print("Saldo insuficiente")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente")
else:
    print("Sistema nao reconhece o tipo de conta")