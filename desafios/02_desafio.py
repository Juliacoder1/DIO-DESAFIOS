from abc import ABC, abstractmethod
from datetime import datetime
import pytz

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._agencia = "001"
        self._numero = numero
        self._cliente = cliente
        self._historico = []

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        if valor > self.saldo:
            print("\n== Valor excedido, não foi possível sacar ==")
            return False
        else:
            self._saldo -= valor
            print("\n== Valor sacado com sucesso ==")
            self.adicionar_transacao(Saque(valor))
            return True

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso")
            self.adicionar_transacao(Deposito(valor))
            return True
        else:
            print("Valor inválido, tente novamente")
            return False

    def adicionar_transacao(self, transacao):
        self._historico.append(transacao)


class Cliente:
    def __init__(self, nome, endereco, email):
        self.nome = nome
        self.endereco = endereco
        self.email = email
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite=1000, limites_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limites_saques = limites_saques
        self.numero_saques = 0

    def sacar(self, valor):
        if self.numero_saques >= self.limites_saques:
            print("Número de saques excedido, não foi possível sacar.")
            return False

        if valor > self.limite:
            print("Valor excede o limite, não foi possível sacar.")
            return False
        
        if super().sacar(valor):
            self.numero_saques += 1
            return True
        
        return False


class Transacao:
    def __init__(self, valor):
        self._valor = valor
        self.data = datetime.now(pytz.timezone("America/Fortaleza"))

    @property
    def valor(self):
        return self._valor


class Saque(Transacao):
    pass


class Deposito(Transacao):
    pass


class Banco:
    def __init__(self):
        self.clientes = []

    def criar_cliente(self):
        nome = input("Digite o nome do cliente: ")
        endereco = input("Digite o endereço do cliente: ")
        email = input("Digite o e-mail do cliente: ")
        cliente = Cliente(nome, endereco, email)
        self.clientes.append(cliente)
        print(f"Cliente {nome} criado com sucesso!")
        return cliente

    def criar_conta(self, cliente):
        numero_conta = input("Digite o número da conta: ")
        conta = ContaCorrente(cliente, numero_conta)
        cliente.adicionar_conta(conta)
        print(f"Conta {numero_conta} criada com sucesso para {cliente.nome}!")

    def listar_contas(self, cliente):
        if cliente.contas:
            print(f"Contas de {cliente.nome}:")
            for conta in cliente.contas:
                print(f"Agência: {conta.agencia}, Número da Conta: {conta.numero}, Saldo: {conta.saldo}")
        else:
            print(f"{cliente.nome} não possui contas.")

    def realizar_deposito(self, conta):
        valor = float(input("Digite o valor do depósito: "))
        conta.depositar(valor)
        print(f"Saldo atual: {conta.saldo}")

    def realizar_saque(self, conta):
        valor = float(input("Digite o valor do saque: "))
        conta.sacar(valor)
        print(f"Saldo após saque: {conta.saldo}")

    def exibir_extrato(self, conta):
        print("Extrato:")
        for transacao in conta.historico:
            print(f"Transação: {transacao.valor} na data {transacao.data}")

    def menu(self):
        while True:
            print("\n=== Menu do Banco ===")
            print("1. Criar Cliente")
            print("2. Criar Conta")
            print("3. Listar Contas")
            print("4. Depositar")
            print("5. Sacar")
            print("6. Extrato")
            print("7. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.criar_cliente()
            elif opcao == "2":
                if not self.clientes:
                    print("Você precisa criar um cliente primeiro!")
                else:
                    cliente = self.clientes[-1]  
                    self.criar_conta(cliente)
            elif opcao == "3":
                if not self.clientes:
                    print("Você precisa criar um cliente primeiro!")
                else:
                    cliente = self.clientes[-1] 
                    self.listar_contas(cliente)
            elif opcao == "4":
                if not self.clientes or not self.clientes[-1].contas:
                    print("Você precisa ter uma conta para depositar!")
                else:
                    conta = self.clientes[-1].contas[-1]  
                    self.realizar_deposito(conta)
            elif opcao == "5":
                if not self.clientes or not self.clientes[-1].contas:
                    print("Você precisa ter uma conta para sacar!")
                else:
                    conta = self.clientes[-1].contas[-1]  
                    self.realizar_saque(conta)
            elif opcao == "6":
                if not self.clientes or not self.clientes[-1].contas:
                    print("Você precisa ter uma conta para ver o extrato!")
                else:
                    conta = self.clientes[-1].contas[-1]  
                    self.exibir_extrato(conta)
            elif opcao == "7":
                print("Saindo...")
                break
            else:
                print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    banco = Banco()
    banco.menu()
