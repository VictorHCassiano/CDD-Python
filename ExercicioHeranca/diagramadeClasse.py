class Atleta:
    def __init__(self, peso):
        self.peso = peso
        self.aposentado = False
        self.aquecido = False

    def aposentar(self):
        self.aposentado = True
        print("Atleta foi aposentado")

    def aquecer(self):
        if self.aquecido == False:
            self.aquecido = True
            print("Atleta aquecendo...")
        else:
            print("Atleta ja aquecido...")

class Corredor(Atleta):
    def __init__(self, peso):
        self.correndo = False
        super().__init__(peso)

    def correr(self):
        if self.aposentado == True:
            print("Atleta aposentado não pode competir")
        elif self.aquecido == False:
            print("Atleta não aquecido, aqueca antes de competir...")
        elif self.correndo == False:
            self.correndo = True
            print("Atleta correndo...")
        else:
            print("Atleta ja correndo...")
    def pararcorrer(self):
        if self.correndo == True:
            self.correndo = False
            print("Atleta parou de correr")
        else:
            print("Atleta não está correndo")

class Nadador(Atleta):
    def __init__(self, peso):
        self.nadando = False
        super().__init__(peso)

    def nadar(self):
        if self.aposentado == True:
            print("Atleta aposentado não pode competir")
        elif self.aquecido == False:
            print("Atleta não aquecido, aqueca antes de competir...")
        elif self.nadando == False:
            self.nadando = True
            print("Atleta nadando...")
        else:
            print("Atleta ja nadando...")
    def pararnadar(self):
        if self.nadando == True:
            self.nadando = False
            print("Atleta parou de nadar")
        else:
            print("Atleta não está nadando")
class Ciclista(Atleta):
    def __init__(self, peso):
        self.pedalando = False
        super().__init__(peso)

    def pedalar(self):

        if self.aposentado == True:
            print("Atleta aposentado não pode competir")
        elif self.aquecido == False:
            print("Atleta não aquecido, aqueca antes de competir...")
        elif self.pedalando == False:
            self.pedalando = True
            print("Atleta pedalando ...")
        else:
            print("Atleta ja pedalando...")
    def pararpedalar(self):
        if self.pedalando == True:
            self.pedalando = False
            print("Atleta parou de pedalar")
        else:
            print("Atleta não está pedalando")


class TriAtleta(Nadador, Ciclista, Corredor):
    def __init__(self, peso):
        super().__init__(peso)

    def pedalar(self):

        if self.aposentado == True:
            print("Atleta aposentado não pode competir")
        elif self.aquecido == False:
            print("Atleta não aquecido, aqueca antes de competir...")
        elif self.pedalando == True:
            print("Atleta já pedalando...")
        elif self.correndo == True:
            print("Atleta ja está correndo, nao pode pedalar")
        elif self.nadando == True:
            print("Atleta nadando, ele nao pode pedalar")
        else:
            self.pedalando = True
            print("Atleta pedalando...")


    def nadar(self):
        if self.aposentado == True:
            print("Atleta aposentado não pode competir")
        elif self.aquecido == False:
            print("Atleta não aquecido, aqueca antes de competir...")
        elif self.nadando == True:
            print("Atleta ja nadando...")
        elif self.pedalando == True:
            print("Atleta pedalando, não pode nadar")
        elif self.correndo == True:
            print("Atleta correndo, não pode nadar")
        else:
            self.nadando = True
            print("Atleta nadando...")


    def correr(self):

        if self.aposentado == True:
            print("Atleta aposentado não pode competir")
        elif self.aquecido == False:
            print("Atleta não aquecido, aqueca antes de competir...")
        elif self.pedalando == True:
            print("Atleta pedalando, ele não pode correr.")
        elif self.correndo == True:
            print("Atleta ja está correndo")
        elif self.nadando == True:
            print("Atleta está nadando, não pode correr")
        else:
            self.correndo = True
            print("Atleta correndo...")



n = TriAtleta(100)
n.nadar()
n.aposentar()
n.nadar()
n.pedalar()
n.pararnadar()
n.pedalar()
n.correr()
