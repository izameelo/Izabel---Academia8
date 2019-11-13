class Mamiferos():
    olhos = 2
    patas = 4

    def __init__(self, pelo, especie, rabo, cor):
        self.pelo = pelo
        self.especie = especie
        self.rabo = rabo
        self.cor = cor

    def comer(self):
        print("comi")
    def fazer_som(self):
        print("sons")

mamifero = Mamiferos('longo','doguinho canino', True, 'cinza')
mamifero2 = Mamiferos('curto', 'agrarios monata', False, 'azul bebê')

mamifero.comer()
mamifero.fazer_som()
print(mamifero.especie)
print(mamifero2.especie)