class Ingresso:
    def __init__(self, reais):
        self.reais = reais

    def imprimevalor(self):
        print(f"O valor do ingresso é {self.reais}")


class IngressoVIP:
    def __init__(self, reais):
        super().__init__(reais)

    def imprimevalor(self):
        print(f"O valor do ingresso  é {self.reais * 1, 5}")


