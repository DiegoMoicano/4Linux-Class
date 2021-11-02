num = int(input("Digite um número inteiro: "))
fat = 1

while num >= 1:
    fat *= num
    num = num - 1

print(fat)
