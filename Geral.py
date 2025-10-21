class Arma:
    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano
    def __str__(self):
        return f'{self.nome} - Dano de: {self.dano}'
    
class Pocao:
    def __init__(self, nome, cura):
        self.nome = nome
        self.cura = cura
    def __str__(self):
        return f'**{self.nome} tomada! cura de + {self.cura}**'

class Personagem:
    def __init__(self, nome, vida, poder, arma, magia=0, precisão=0):
        self.nome = nome
        self.vida = vida
        self.poder = poder
        self.magia = magia
        self.precisão = precisão
        self.arma = None
        
    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, novo_valor):
        if novo_valor < 0:
            self._vida = 0
        elif novo_valor > 100:
            self._vida = 100
        else:
            self._vida = novo_valor

    def __str__(self):
        return(
            f'========= PERSONAGEM =========\n'
            f'Nome:{self.nome}\n'
            f'Vida: {self.vida}\n'
            f'Poder: {self.poder}\n'
            f'Magia: {self.magia}\n'
            f'Precisão: {self.precisão}\n'
            f'Arma: {self.arma if self.arma else "nenhuma"}\n'
            f'==============================\n'
        )
    def equipar (self, arma):
        self.arma = arma
        print(f'\n'
            f"--> {self.nome} equipou {arma.nome} <--\n"
            f'__________________________________\n'
            )

    def atacar (self, alvo):
        if self.arma:
            dano_total = self.poder + self.arma.dano
            print(f'\n'
                f'{self.nome} ataca {alvo.nome} com {self.arma.nome} causando dano de {dano_total}!\n'
                f'_______________________________________\n'
                )
            alvo.receber_dano(dano_total)
        else:
            print(f"{self.nome} tenta atacar mas está desarmado!")

    def receber_dano(self, dano):
        print(f'{self.nome} recebeu {dano} de dano')
        self.vida -= dano
        print(f'Vida atual de {self.nome} : {self.vida}')

class Guerreiro(Personagem):
    def __init__(self, nome, vida, poder, arma):
        super().__init__(nome, vida, poder, arma, magia=0, precisão=0)

class Arqueiro(Personagem):
    def __init__(self, nome, vida, poder, arma, precisão):
        super().__init__(nome, vida, poder, arma, magia=0, precisão=precisão)

class Mago(Personagem):
    def __init__(self, nome, vida, poder, arma, magia):
        super().__init__(nome, vida, poder, arma, magia=magia, precisão=0)

class Monstro(Personagem):
    def __init__(self, nome, vida, poder, arma):
        super().__init__(nome, vida, poder, arma, magia=0, precisão=0)



espada = Arma("espada", 33)
arcoflecha = Arma("Arco e Flecha", 20)
cajado = Arma ("Cajado", 40)
machado = Arma("machado", 50)

guerreiro = Guerreiro("Edyye", 100, 45, espada)
arqueiro = Arqueiro("Legolas", 100, 55, arcoflecha, precisão=80)
mago = Mago ("Dumbledore", 100, 50, cajado, magia=85)
goblin = Monstro ("Golum", 85, 35, machado)

exilir = Pocao("Exilir", 45)

guerreiro.equipar(espada)
arqueiro.equipar(arcoflecha)
mago.equipar(cajado)
goblin.equipar(machado)

print(guerreiro)
print(arqueiro)
print(mago)
print(goblin)

guerreiro.atacar(goblin)
goblin.atacar(guerreiro)

print(exilir)
