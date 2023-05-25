class Animal:
    def __init__(self, nome, cor, ):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"{self.nome} comendo ...")


class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def emitirSom(self):
        print(f"O {self.nome} foi miando...")

    def comer(self,comida):
        print(f"{self.nome} comendo {comida}")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def emitirSom(self):
        print(f" {self.nome} foi latindo ...")

    def comer(self,comida):
        print(f"{self.nome} comendo {comida}")


class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def emitirSom(self):
        print(f" {self.nome} foi mugindo ...")


class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def emitirSom(self):
        print(f" {self.nome} foi pulando ...")


aaa = Gato("A", "B")
print(aaa.__dict__)
print(f"{aaa.nome}")
aaa.comer("Manga")
