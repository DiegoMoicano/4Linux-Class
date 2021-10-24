print("Digite 5 (cinco) números inteiros e veja qual é o maior deles!")


while True:
    sair = input("Digite 'Sair' para finalizar ou 'Enter' para continuar...: ")
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))
    num3 = int(input("Digite o terceiro número inteiro: "))
    num4 = int(input("Digite o quarto número inteiro: "))
    num5 = int(input("Digite o quinto número inteiro: "))
    if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
        print(f"Número {num1} é o maior de todos!")
    elif num2 > num1 and num2 > num3 and num1 > num4 and num1 > num5:
        print(f"Número {num2} é o maior de todos!")
    elif num3 > num1 and num3 > num2 and num1 > num4 and num1 > num5:
        print(f"Número {num3} é o maior de todos!")
    elif num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:
        print(f"Número {num4} é o maior de todos!")
    elif num5 > num1 and num5 > num2 and num5 > num3 and num5 > num4:
        print(f"Número {num5} é o maior de todos!")
    elif sair.title() == "Sair":
        break
