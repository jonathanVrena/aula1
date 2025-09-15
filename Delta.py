a = float(input("Digite o valor de a:"))
b = float(input("Digite o valor de b:"))
c = float(input("Digite o valor de c:"))

delta = b**2 - 4*a*c

print("Valor de Delta:", delta)

if delta > 0:
    print("A equação tem duas raízes reaís")
elif delta == 0:
    print("A equação tem  uma raíz real")
else:
    print("A equação não possui raízes reais")