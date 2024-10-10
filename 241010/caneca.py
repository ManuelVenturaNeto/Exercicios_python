class Caneca:
    formato = 'cilindrico com alça'
    
    def __init__(self, nome, logo, cor):
        self.nome = nome
        self.logo = logo
        self.cor = cor
        self.preco_fabricacao = 15
        
    def beber(self):
        self.status = "Vazia"
        return f'É da {self.nome} que estou bebendo'
    
    def encher(self):
        self.status = 'Cheia'
        return f'Enchando a= {self.nome}'

class CanecaCefet(Caneca):
    def __init__(self):
        super().__init__('Caneca do cefet', 'C grande', 'Cinza')
        self.preco_fabricacao += 20
        
    def lanche(self):
        print('Como bonus voce recebe o lanche do Rango do Rei')
        
    def beber(self):
        self.status = 'Cheia'
        return 'Toma rapido porque tem prova agora!'
    
class CanecaPuc(Caneca):
    def __init__(self):
        super().__init__('Caneca da puc', 'simbolo da pontifica', 'branca')
        self.bebida = 'café'
        self.preco_fabricacao += 50
        
    def bag():
        print('voce ganhou uma mochila para levar a caneca')
    
    def beber(self):
        return super().beber() + f' {self.bebida} '
    
presente_do_cefet = CanecaCefet()
presente_da_una = Caneca('Caneca da una', 'escrito una', 'vermelha')
presente_da_puc = CanecaPuc()

print(presente_do_cefet.beber())
print(presente_da_puc.beber())
print(presente_da_una.beber())

print(f'{presente_do_cefet.nome} e {presente_do_cefet.preco_fabricacao}')
print(f'{presente_da_puc.nome} e {presente_da_puc.preco_fabricacao}')
print(f'{presente_da_una.nome} e {presente_da_una.preco_fabricacao}')


print(f'\nVoce legou a {presente_do_cefet.nome} que custou para instituição um preço de R${presente_do_cefet.preco_fabricacao}.'
      f'\nAlém disso voce também levou {presente_da_una.nome} e {presente_da_puc.nome} que custaram para as instituições, respectivamente'
      f'R${presente_da_una.preco_fabricacao} e R${presente_da_puc.preco_fabricacao}.')