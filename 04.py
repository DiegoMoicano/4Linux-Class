n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3

if media > 6:
    print(f"Aprovado")
elif media >= 4:
    print(f"Recuperação")
else:
    print(f"Retido")

