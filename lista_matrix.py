vetA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vetB = [7, 8, 9, 6, 5, 4, 3, 2, 1, 10]
pos = 0

for A in vetA:
    vetB.insert(pos, A)
    pos = pos + 2
print(vetB)