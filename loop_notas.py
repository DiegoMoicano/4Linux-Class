soma = "soma"
fim = "Sim"
notas = 0.0
cont = 0

while True:
    if soma == "soma":
        nota = float(input("Digite sua nota: "))
        notas += nota
        cont += 1
        fim = input("Deseja continuar? (Sim/Não): ")
        if fim.title() == "Sim":
            continue
        else:
            break

media = notas / cont
print(f"\nA sua média foi {media}")
