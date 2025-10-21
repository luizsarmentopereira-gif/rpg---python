class Arma:
    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano
    def __str__(self):
        return f' {self.nome} - (Dano {self.dano})'
    
class Poção:
    def __init__(self, nome, cura):
        self.nome = nome
        self.cura = cura
    def __str__(self):
        return f'{self.nome} usado! cura de +{self.cura} restauradas'
    
class Guerreiro:
    def __init__(self, nome, vida, poder, arma):
        self.nome = nome
        self.vida = vida
        self.poder = poder
        self.arma = None
    def __str__(self):
        return(
            f'=====PERSONAGEM=======\n'
            f'Nome: {self.nome}\n'
            f'Vida: {self.vida} \n' 
            f'Poder: {self.poder}\n'
            f'Arma: {self.arma if self.arma else 'nenhuma'}\n'
            )
    def equipar(self, arma):
        self.arma = arma
        print(f'{self.nome} equipou {arma.nome}')
    def ataque(self):
        if self.arma:
            dano_total = self.poder + self.arma.dano
            print(f'Guerreiro {self.nome} ATACA com {self.arma.nome} causando {dano_total} de dano!')
        else:
            print(f'{self.nome} tenta atacar mas está desarmado')

arma = Arma("Espada Mágica", 40)
guerreiro = Guerreiro("Arthur", 65, 25, "Espada")
exilir = Poção("Exilir de cura", 30)

print(guerreiro)
guerreiro.equipar(arma)
print(guerreiro)
print(arma)
guerreiro.ataque()
print(exilir)