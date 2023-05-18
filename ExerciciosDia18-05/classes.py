class Pessoa:
    def __init__(self, nome, peso, idade, comendo=False,falando=False,andando=False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        self.andando = andando
    def comer(self,comida):
        self.comida = comida
        if self.comendo == True:
             print(f"{self.nome} ja está comendo")
        elif self.falando == True:
            print(f"{self.nome} não pode comer falando")
        else:
            self.comendo = True
            print(f"{self.nome} está comendo {self.comida}")
    def pararcomer(self):
        if self.comendo == True:
            self.comendo = False
            print(f"{self.nome} parou de comer")
        else:
            print(f"{self.nome} não está comendo")
    def falar(self):
        if self.comendo == True:
            print(f"{self.nome} não pode falar comendo")
        elif self.falando == True:
            print(f"{self.nome} já está falando")
        else:
            self.falando = True
            print(f"{self.nome} está falando")

    def pararfalar(self):
        if self.falando == True:
            print(f"{self.nome} parou de falar")
            self.falando = False
        else:
            print(f"{self.nome} não está falando")

    def andar(self):
        if self.andando == False:
            self.andando = True
            print(f"{self.nome} está andando")
        else:
            print(f"{self.nome} ja está andando")
    def pararAndar(self):
        if self.andando == True:
            self.andando = False
            print(f"{self.nome} parou de andar")
        else:
            print(f"{self.nome} não está andando")

p1 = Pessoa("Joao",80,19)
p2 = Pessoa("Maria",56,22,comendo=True)
#print(p2.__dict__)
#print(vars(p1))
print(p1.__dict__)

p1.pararcomer()
p1.comer("manga")
p1.falar()
p1.comer("pipoca")
p1.pararcomer()
p1.falar()
p1.comer("Castanha")
p1.pararfalar()
p1.andar()
p1.andar()
p1.pararAndar()
p1.pararAndar()
