class Arma:
    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano
    def __str__(self):
        return f"{self.nome} (Dano de {self.dano})"
    
class Poção:
    def __init__(self, nome, cura):
        self.nome = nome
        self.cura = cura
    def __str__(self):
        return f'{self.nome} Usada! cura de +{self.cura} restauradas'
    
class Monstro:
    def __init__(self, nome, vida, poder, arma):
        self.nome = nome
        self.vida = vida
        self.poder = poder
        self.arma = None
    def __str__(self):
        return (
            f'==============PERSONAGEM==============\n'
            f'\n'
            f'============ Nome: {self.nome} ============\n'
            f'============= Vida: {self.vida} ===============\n'
            f'============= Poder: {self.poder} ==============\n'
            f'  Arma: {self.arma if self.arma else 'nenhuma'}\n'
            f'\n'
            f'==============================\n'
        )
    def equipar(self, arma):
        self.arma = arma
        print(f'****{self.nome} equipou {arma.nome}!!****')

    def ataque(self):
        if self.arma:
            dano_total = self.poder + self.arma.dano
            print(f"O {self.nome} atacou com {self.arma.nome} causando {dano_total} de dano!")
        else:
            print(f'o {self.nome} tenta atacar mas está desarmado')

monstro = Monstro("Goblin", 70, 45, "Pedaço de madeira")
arma = Arma("Pedaço de madeira", 10)
exilir = Poção("Exilir de cura", 30)

print(monstro)
monstro.equipar(arma)
print(monstro)
monstro.ataque()
print(arma)
print(exilir)