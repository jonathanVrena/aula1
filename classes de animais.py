class Animal:
    def __init__(self, nome, barulho):
        self.nome = nome
        self.barulho = barulho

    def fazer_barulho(self):
        print(f"O {self.nome} faz: {self.barulho}")

    def mostrar_nome(self):
        print(f"Este é um {self.nome}")

# Criando 5 animais
cachorro = Animal("Cachorro", "Au au")
gato = Animal("Gato", "Miau")
vaca = Animal("Vaca", "Muu")
pato = Animal("Pato", "Quack")
leao = Animal("Leão", "Rooaar")

# Lista de animais
animais = [cachorro, gato, vaca, pato, leao]

# Executando ações dos animais
for animal in animais:
    animal.mostrar_nome()
    animal.fazer_barulho()
    print("-" * 20)
