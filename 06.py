dado = input("Digite qualquer coisa: ")
for i in dado:
    if i.isupper():
        print(f"Caractere {i} é maiúsculo")
    elif i.islower():
        print(f"Caractere {i} é minúsculo")
    elif i.isnumeric():
        print(f"Caractere {i} é número")
    else:
        print(f"Não é coisa alguma!")
