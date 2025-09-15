# Definindo a classe Pessoa
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def status_idade(self):
        if self.idade < 18:
            return "menor de idade"
        else:
            return "maior de idade"

    def __str__(self):
        return f"{self.nome} tem {self.idade} anos e é {self.status_idade()}."

# Criando 10 objetos Pessoa
pessoas = [
    Pessoa("Ana", 25),
    Pessoa("Bruno", 17),
    Pessoa("Carlos", 22),
    Pessoa("Daniela", 15),
    Pessoa("Eduardo", 35),
    Pessoa("Fernanda", 16),
    Pessoa("Gustavo", 40),
    Pessoa("Helena", 13),
    Pessoa("Igor", 33),
    Pessoa("Juliana", 14)
]

# Exibindo os dados das pessoas
for pessoa in pessoas:
    print(pessoa)