class Atleta():
    def __init__(self,peso):
        self.peso = peso
        self.aposentado = False
    def aposentar(self):
        self.aposentado = True
        print("Atleta foi aposentado")
    def aquecer(self):
        print("Atleta aquecendo...")
class Corredor(Atleta):
    def __init__(self, peso):
        super().__init__(peso)
    def correr(self):
        print("Atleta correndo...")

class Nadador(Atleta):
    def __init__(self, peso):
        super().__init__(peso)
    def nadar(self):
        print("Atleta nadando...")

class Ciclista(Atleta):
    def __init__(self, peso):
        super().__init__(peso)
    def pedalar(self):
        print("Atleta pedalando ...")
    
class TriAtleta(Nadador,Ciclista,Corredor):
    def __init__(self, peso):
        super().__init__(peso)


n = TriAtleta(100)
n.nadar()
n.pedalar()
n.correr()
n.aquecer()