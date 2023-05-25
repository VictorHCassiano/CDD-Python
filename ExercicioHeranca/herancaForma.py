class Forma:
    def __init__(self):
        self.perimetro = 0
        self.area = 0


class Retangulo(Forma):
    def __init__(self):
        super().__init__()

    def calculaArea(self,base,altura):
        self.area = base * altura

    def calculaPerimetro(self,base,altura):
        self.perimetro = 2 * (base + altura)


class Triangulo(Forma):
    def __init__(self):
        super().__init__()

    def calculaArea(self,base,altura):
        self.area = (base * altura) / 2

    def calculaPerimetro(self, lado1, lado2, lado3):
        self.perimetro = lado1 + lado2 + lado3


triangulo = Triangulo()
retangulo = Retangulo()
retangulo.calculaArea(10, 10)
retangulo.calculaPerimetro(10, 10)
triangulo.calculaArea(10,10)
triangulo.calculaPerimetro(5, 5, 5)

print(triangulo.__dict__)
print(retangulo.__dict__)
