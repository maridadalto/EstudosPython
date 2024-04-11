saldo = 2000.00
saque = float(input("Informe o valor do saque: "))
# O Python precisa estar identado para saber onde termina um bloco pois nao tem identificador de final
if saldo >= saque: #ponto para dizer onde começa o bloco if
    print("Saque realizado")
else: 
    print("Saldo insuficiente")