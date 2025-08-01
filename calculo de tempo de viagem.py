distancia = float(input("Digite a distância em km: "))
velocidade = float(input("Digite a velocidade média em km/h:"))

tempo = distancia / velocidade

pint(f"Tempo estimado de viagem: {tempo:.1f} horas")
