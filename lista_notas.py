notas = [5, 6, 8, 2]
soma = 0

print("As notas são: ")
for nota in notas:
    soma += nota
    print(nota, end=", ")
media = soma / 4
print(f"\nA media das notas é {media}")
