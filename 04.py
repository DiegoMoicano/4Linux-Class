n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3

if media > 6:
    print(f"Aprovado")
elif media >= 4:
    print(f"Recuperação")
elif media <= 4:
    print(f"Retido")
