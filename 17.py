salario = float(input("Digite seu salário: "))

if salario <= 280:
    print(f"Seu salario atual é R$ {salario}.")
    print(f"Seu aumento será de 20%.")
    salario = salario + (salario * 0.2)
    print(f"Seu novo salário é de R$ {salario}.")
elif salario > 280 and salario < 700:
    print(f"Seu salario atual é R$ {salario}.")
    print(f"Seu aumento será de 15%.")
    salario = salario + (salario * 0.15)
    print(f"Seu novo salário é de R$ {salario}.")
elif salario >= 700 and salario <= 1500:
    print(f"Seu salario atual é R$ {salario}.")
    print(f"Seu aumento será de 10%.")
    salario = salario + (salario * 0.1)
    print(f"Seu novo salário é de R$ {salario}.")
elif salario > 1500:
    print(f"Seu salario atual é R$ {salario}.")
    print(f"Seu aumento será de 5%.")
    salario = salario + (salario * 0.05)
    print(f"Seu novo salário é de R$ {salario}.")
