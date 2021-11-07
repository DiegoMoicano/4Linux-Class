tabuada = int(input("Digite a tabuada desejada: "))
cont = 1

print(f"A tabuada do {tabuada} é: ")
while cont <= 10:
    tab = tabuada * cont
    print(f"{tabuada} x {cont} = {tab}")
    cont += 1
