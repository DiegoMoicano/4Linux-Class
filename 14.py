area = float(input(f"Quantos metros quadrados quer pintar?: "))
litro_tinta = area / 6
lata_grande = litro_tinta / 18
lata_pequena = litro_tinta / 3.6

print(f"Vai precisar de {round(litro_tinta)} litros!")
print(f"Litros lata grande: {round(lata_grande)} litros!")
print(f"Litros lata grande: {round(lata_pequena)} litros!")


# 18l == 108m
# xl == area
# (18 * area) / 108

# 3.6 = 21.6m
# xl == area
# (3.6 * area) / 21.6
