# Entrada
massa = float(input("Digite a massa (em kg): "))
volume = float(input("Digite o volume (em m³): "))

# Processamento
densidade = massa / volume

# Saída
if densidade > 5:
    print("Material muito denso")
elif 2 <= densidade <= 5:
    print("Material com densidade média")
else:
    print("Material com pouca densidade")