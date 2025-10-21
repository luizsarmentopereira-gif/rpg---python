class Arma:
    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano
    def __str__(self):
        return f'{self.nome}  (Dano : {self.dano})'

class Poção:
    def __init__(self, nome, cura):
        self.nome = nome
        self.cura = cura
    def __str__(self):
        return f'{self.nome} usada, cura de +{self.cura} restauradas'

    
class Arqueiro:
    def __init__(self, nome, vida, poder, precisão, arma):
        self.nome = nome
        self.vida = vida
        self.poder = poder
        self.precisão = precisão
        self.arma = None
    def __str__(self):
        return (
            f"======PERSONAGEM=======\n"
            f'Nome: {self.nome}\n'
            f'Vida: {self.vida}\n'
            f'Poder: {self.poder}\n'
            f'Precisão: {self.precisão}\n'
            f'Arma: {self.arma if self.arma else 'nenhuma'}\n'
            )
    def equipar(self, arma):
        self.arma = arma
        print(f'{self.nome} equipou: {arma.nome}!')
        
    def ataque(self):
        if self.arma:
            dano_total = self.poder + self.arma.dano
            print(f'{self.nome} ataca com {self.arma.nome} causando {dano_total} de dano!')
        else:
            print(f'{self.nome} tenta atacar mas está desarmado')

espada = Arma("Espada elfica", 88)
arcoflecha = Arma("Arco e Flecha", 45)
arqueiro = Arqueiro("Aragon", 85, 45, 80, arcoflecha)
exilir = Poção("Exilir de cura", 30)

from time import sleep

print(arqueiro)
arqueiro.equipar(arcoflecha)
print(arqueiro)
print(arcoflecha)
arqueiro.ataque()
print(exilir)