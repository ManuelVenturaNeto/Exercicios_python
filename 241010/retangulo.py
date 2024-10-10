class Retangulo:
    lado_a = None
    lado_b = None
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b
        print('criado uma nova instancia retangulo')
        
    def calcula_area(self):
        return self.lado_a*self.lado_b
    
    def calcula_perimetro(self):
        return 2*self.lado_a + 2*self.lado_b

retangulo1 = Retangulo(10, 20)

class Circulo(Retangulo):
    def __init__(self, raio):
        self.raio = raio
        
    def calcula_area(self):
        return self.raio*2*3.14/2

ciruclo1 = Circulo(10).calcula_area()

# print(retangulo1.lado_a)
# print(retangulo1.lado_b)
# print(retangulo1.calcula_area())
# print(retangulo1.calcula_perimetro())


print(int(ciruclo1))