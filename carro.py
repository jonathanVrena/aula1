#def cria funções (ou métodos dentro da classe)
class Carro:
    marca = ""
    modelo = ""
    ano = 0
    cor = ""

    def buzinar(self):
        print("Bi-Bi")s
    def ligar(self):
        print("PHAM PHAM BRRRRRRRRRRRR...")

c1 = Carro()
c1.marca = "Nissan"
c1.modelo = "Nissan GT3"
c1.ano = "Verde"
c1.cor = "Verde de Ben10"

print("Carro: ", c1.marca, "-", c1.modelo),
" Ano:", c1.ano, "Cor: ", c1.cor
c1.ligar()
c1.buzinar()