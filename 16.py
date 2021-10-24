print("Informe os preços dos produtos!")
prod1 = float(input("Produto 1: "))
prod2 = float(input("Produto 2: "))
prod3 = float(input("Produto 3: "))

if prod1 <= prod2 and prod1 <= prod3:
    print(f"O preço menor é {prod1} > produto1")
elif prod2 <= prod1 and prod2 <= prod3:
    print(f"O preço menor é {prod2} > produto2")
elif prod3 <= prod2 and prod3 <= prod1:
    print(f"O preço menor é {prod3} > produto3")
