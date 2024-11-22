class Heroi:

    lista_de_herois = []

    def __init__(self, nome_heroi, nome_real, raca, poderes, poder_principal, fraquezas, nível_de_força):
        self.nome_heroi = nome_heroi
        self.nome_real = nome_real
        self.raca = raca
        self.poderes = poderes
        self.poder_principal = poder_principal
        self.fraquezas = fraquezas
        self.nível_de_força = nível_de_força
        Heroi.lista_de_herois.append(self)

    @classmethod
    def listar_herois(cls):

        print(f'{'Nome Herói'.ljust(10)} | {'Nome verdadeiro'.ljust(15)} | {'Raça'.ljust(15)} | {'Poderes'.ljust(25)} | {'Poder Principal'.ljust(15)} | {'Fraquezas'.ljust(20)} | {'Nível de força'.ljust(15)}')
        
        for heroi in Heroi.lista_de_herois:
            print(f'{str(heroi.nome_heroi).ljust(10)} | {str(heroi.nome_real).ljust(15)} | {str(heroi.raca).ljust(15)} | {str(heroi.poderes).ljust(25)} | {str(heroi.poder_principal).ljust(15)} | {str(heroi.fraquezas).ljust(20)} | {str(heroi.nível_de_força).ljust(15)}')

    def __str__(self):
        return f'{'Nome Herói'.ljust(10)} | {'Nome verdadeiro'.ljust(15)} | {'Raça'.ljust(15)} | {'Poderes'.ljust(35)} | {'Poder Principal'.ljust(15)} | {'Fraquezas'.ljust(25)} | {'Nível de força'.ljust(15)} \n{str(self.nome_heroi).ljust(10)} | {str(self.nome_real).ljust(15)} | {str(self.raca).ljust(15)} | {str(self.poderes).ljust(35)} | {str(self.poder_principal).ljust(15)} | {str(self.fraquezas).ljust(25)} | {str(self.nível_de_força).ljust(15)}'

thor = Heroi('Thor', 'Thor', 'Deus Nórdico', 'Telecinese, voar, super força...', 'Controlar raios', 'jóias do infinito', 'Alta')

print(thor)
