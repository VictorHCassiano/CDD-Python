class Forma():
    def __init__(self,base,altura):
       self.base = base
       self.altura = altura
class Retangulo(Forma):
    def __init__(self, base, altura):
        super().__init__(base, altura)
    def calculaArea(self):
            print(self.base*self.altura)
    def calculaPerimetro(self):
         print(2*(self.base+self.altura))
class Triangulo(Forma):
     def __init__(self, base, altura):
          super().__init__(base, altura)
     def calculaArea(self):
          print((self.base*self.altura)/2)
     def calculaPerimetro(self,lado1,lado2,lado3):
          print(lado1+lado2+lado3)

triangulo = Triangulo(10,10)
retangulo = Retangulo(10,10)
retangulo.calculaArea()
triangulo.calculaArea()
