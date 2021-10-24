file_duplo = 1
alcatra = 2
picanha = 3

print("-" * 50)
print("                 Até 5Kg         Acima de 5Kg")
print("1 - Filé Duplo   R$ 4,90/kg      R$ 5,80/kg  ")
print("2 - Alcatra      R$ 5,90/kg      R$ 6,80/kg  ")
print("3 - Picanha      R$ 6,90/kg      R$ 7,80/kg  ")
print("-" * 50)
print("")

carne_tipo = input("Escolha a carne que quer comprar: ")
quantidade_carne = float(input("Quantos kilos quer: "))

if carne_tipo == "1":
    if quantidade_carne <= 5:
        total = 4.9 * quantidade_carne
        print(f"Total {total}")
    elif quantidade_carne > 5:
        total = 5.8 * quantidade_carne
        print(f"Total {total}")
elif carne_tipo == "2":
    if quantidade_carne <= 5:
        total = 5.9 * quantidade_carne
        print(f"Total {total}")
    elif quantidade_carne > 5:
        total = 6.8 * quantidade_carne
        print(f"Total {total}")
elif carne_tipo == "3":
    if quantidade_carne <= 5:
        total = 6.9 * quantidade_carne
        print(f"Total {total}")
    elif quantidade_carne > 5:
        total = 7.8 * quantidade_carne
        print(f"Total {total}")

cartao = input("\nVai pagar com cartão? (S/N): ")
if cartao.upper() == "S":
    print("Ganhou 5% de desconto")
else:
    print("Nada de desconto")
