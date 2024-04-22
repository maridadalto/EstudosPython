import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = [] # lista para armazenar as contas do cliente
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def add_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self,nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self,numero,cliente):
        self._saldo = 0 # inicializando a conta com saldo 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self._saldo

        if valor > saldo:
            print("\nxxx Saldo insuficiente xxx")
        elif valor > 0:
            self._saldo -= valor
            print(f"\n| Saque no valor de R$ {valor:.2f} |")
            print(f"\n| Saldo atualizado R$ {self._saldo:.2f} |")
            return True
        else:
            print("\nxxx Saque não realizado, valor inválido xxx")
        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"\n| Depósito realizado, seu saldo é: R$ {self._saldo:.2f} |")
        else:
            print("\nxxx Valor para depósito inválido xxx")
            return False
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, qtde_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.qtde_saques = qtde_saques
    
    def __str__(self):
        return f"""\
        Agência:\t{self.agencia}
        C/C:\t\t{self.numero}
        Titular:\t{self.cliente.nome}
        """

    def sacar(self, valor):
        nro_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"]==Saque.__name__])

        if valor > self.limite:
            print("\nxxx Limite máximo para saque de 500,00 xxx")
        elif nro_saques >= self.qtde_saques:
            print("\nxxx Número máximo de saques excedido xxx")
        else:
            return super().sacar(valor) # chama o método sacar dentro da classe Conta
        return False # caso o retorno seja a execução do IF ou ELIF

class Historico:
    def __init__(self):
        self._transacoes = [] # crio a lista de transacoes para armazenar todas as realizadas
    
    @property
    def transacoes(self):
        return self._transacoes

    def add_transacao(self,transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
        })

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor

    def registrar(self,conta):
        transacao_ok = conta.sacar(self.valor)

        if transacao_ok:
            conta.historico.add_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        transacao_ok = conta.depositar(self.valor)

        if transacao_ok:
            conta.historico.add_transacao(self)


def menu():
    menu = '''\n
    ######## OPÇÕES ########

    [d]\tDEPOSITAR
    [s]\tSACAR
    [e]\tEXTRATO
    [nu]\tNOVO USUÁRIO
    [nc]\tNOVA CONTA
    [lc]\tLISTAR CONTAS
    [x]\tENCERRAR
    ########################
    '''
    return input(textwrap.dedent(menu))

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def novo_cliente(clientes):
    cpf = input("-> Informe o cpf do titular da conta: ")
    cliente = filtrar_cliente(cpf,clientes)

    if cliente:
        print("\nxxx CPF já cadastrado, não foi possível criar uma nova conta. xxx")
        return
    nome = input("-> Informe o nome completo: ")
    data_nascimento = input("-> Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("-> Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento,cpf=cpf,endereco=endereco)
    clientes.append(cliente)
    print("| Novo cliente cadastrado com sucesso!! |")

def nova_conta(numero_conta, clientes, contas):
    cpf = input("-> Informe o cpf do titular da conta: ")

    cliente = filtrar_cliente(cpf,clientes)

    if not cliente:
        print("\nxxx Cliente não encontrado, não foi permitido criar a nova conta. xxx")
        return

    conta = ContaCorrente(numero_conta,cliente)
    contas.append(conta)
    cliente.add_conta(conta)
    print("\n| Conta criada com sucesso |")      

def listar_contas(contas):
    print("=== Contas registradas para esse cliente. ===")
    for conta in contas:
        print(textwrap.dedent(str(conta)))

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\nxxx Cliente não possui conta! xxx")
        return
    
    return cliente.contas[0]


def depositar(clientes): 
    cpf = input("-> Informe o CPF do titular: ")
    cliente = filtrar_cliente(cpf,clientes)

    if not cliente:
        print("\nxxx Cliente não cadastrado. xxx")
        return
   
    valor = float(input("-> Informe o valor do depósito: "))
    transacao = Deposito(valor)
    conta = recuperar_conta_cliente(cliente)
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("-> Informe o CPF do titular: ")
    cliente = filtrar_cliente(cpf,clientes)
    if not cliente:
        print("\nxxx Cliente não cadastrado. xxx")
        return
    valor = float(input("-> Informe o valor do saque: "))
    transacao = Saque(valor)
    conta = recuperar_conta_cliente(cliente)
    cliente.realizar_transacao(conta, transacao)

def extrato(clientes):
    cpf = input("-> Informe o CPF do titular: ")
    cliente = filtrar_cliente(cpf,clientes)
    if not cliente:
        print("\nxxx Cliente não cadastrado. xxx")
        return
    print("=== Movimentações ===")
    conta = recuperar_conta_cliente(cliente)
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        print("\n=== Não foram realizadas movimentações ===")
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\tR$ {transacao['valor']:.2f}"
    print(extrato)
    print(f"\n| Saldo final R$ {conta.saldo:.2f} |")

def main():
    clientes = []
    contas = []
 
    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            extrato(clientes)
        elif opcao == "nu":
            novo_cliente(clientes)
        elif opcao == "nc":
            numero_conta =len(contas)+1
            nova_conta(numero_conta,clientes,contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "x":
            print("=== Obrigada por usar nosso sistema ===")
            break

main()