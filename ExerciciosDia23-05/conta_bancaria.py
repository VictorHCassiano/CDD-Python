class Conta:
    def __init__(self, numero_conta, nome_cliente, tipo_da_conta):
        self.nome_cliente = nome_cliente
        self.numero_conta = numero_conta
        self.saldo = 0
        self.tipo_conta = tipo_da_conta
        self.status = False
        self.limitecredito = 0
        self.auxlimitecredito = 0
    def depositar(self, deposito):
        
        if self.status == False:
            print("Conta desativada!!! , procure a agencia mais proxima para ativar")
        else:
                aux = deposito
                deposito -= abs(self.auxlimitecredito)
                self.auxlimitecredito += aux
                if self.auxlimitecredito>self.limitecredito:
                    self.auxlimitecredito = self.limitecredito
                if deposito < 0:
                     deposito = 0

                self.saldo += deposito
                print(f"Depositado com sucesso! O saldo agora é {self.saldo} e o limite é {self.auxlimitecredito}")


    def sacar(self, saque):
        if self.status == True:
            if self.saldo >= saque:
                self.saldo = self.saldo - saque
                print(f"Saldo:{self.saldo} Limite:{self.auxlimitecredito}")
            elif self.saldo+self.limitecredito >= saque:
                self.auxlimitecredito = self.saldo - saque
                self.saldo = 0
                print(f"Saldo:{self.saldo} Limite:{self.auxlimitecredito}")
            else:
                print("Não foi possivel sacar,saldo insuficiente")


        else:
            print("Conta desativada!!! , procure a agencia mais proxima para ativar")

    def verificarsaldo(self):
        print(f"Saldo:{self.saldo} Limite:{self.auxlimitecredito}")
    def ativarconta(self):
        if self.status == True:
            print("Conta ja está ativa")
        else:
            self.status = True
            print("Conta ativada com sucesso")

    def desativarconta(self):
        if self.saldo > 0:
            print("Ainda há saldo na conta por favor retire antes de desativar")
        elif self.status == False:
            print("Conta ja está desativada")
        else:
            self.status = False
            print("Conta desativada com sucesso")

    def ativarlimitecredito(self, limite):
        self.limitecredito = limite
        self.auxlimitecredito = self.limitecredito

    def desativarlimitecredito(self):
        self.limitecredito = 0
        self.auxlimitecredito = 0
        print("Credito Desativado")


cont = Conta(10,"AAA", "Corrente")
cont.ativarconta()
print(cont.__dict__)
cont.ativarlimitecredito(200)
print(cont.__dict__)
cont.sacar(200)
cont.depositar(200)
cont.depositar(1000)
cont.sacar(100)
cont.sacar(1000)
cont.depositar(10)
