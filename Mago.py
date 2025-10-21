class Arma:
    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano
    def __str__(self):
        return f"{self.nome} - Dano de {self.dano}"
    
class Poção:
    def __init__(self, nome, cura):
        self.nome = nome
        self.cura = cura
    def __str__(self):
        return f'{self.nome} usada! Cura de +{self.cura} restauradas!'
    
class Mago:
    def __init__(self, nome, vida, poder, magia, arma):
        self.nome = nome
        self.vida = vida
        self.poder = poder
        self.magia = magia
        self.arma = None
    def __str__(self):
        return (
            f'======PERSONAGEM========\n'
            f'Nome: {self.nome}\n'
            f'Vida: {self.vida}\n'
            f'Poder: {self.poder}\n'
            f'Magia: {self.magia}\n'
            f'Arma: {self.arma if self.arma else 'nenhuma'}\n'
        )
    def equipar(self, arma):
        self.arma = arma
        print(f'{self.nome} equipou sua arma {arma.nome}') 

    def ataque (self):
        if self.arma:
            dano_total = self.poder + self.arma.dano
            print(f'{self.nome} ataca com {self.arma.nome} causando {dano_total} de dano!')
        else:
            print(f'{self.nome} tenta atacar mas está desarmado')

varinha = Arma("Varinha Mágica", 45)
mago = Mago("Ford", 85, 40, 75, "Varinha")
exilir = Poção("Exilir de Cura", 30)

print(mago)
mago.equipar(varinha)
print(mago)
mago.ataque()
print(exilir)