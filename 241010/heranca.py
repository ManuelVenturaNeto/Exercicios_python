class Exemplo:
    def __init__(self, a=2, b=3):
        self.a = a
        self.b = b
    def calc(self, x):
        return self.a*x + self.b

obj1 = Exemplo().calc(5)
print(obj1)

obj2 = Exemplo(a=3, b=2).calc(5)
print(obj2)