operacoes = {
    "soma": lambda x, y: x + y,
    "subtracao": lambda x, y: x - y,
    "divisao": lambda x, y: x / y,
    "multiplicacao": lambda x, y: x * y
}


def menu():
    print("""
        0 soma
        1 subtracao
        2 divisao
        3 multiplicacao
        4 Outros números
        5 Sair
    """)


x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))

while True:
    menu()
    op = input("Digite a operação: ")

    if op == "0":
        print(operacoes["soma"](x, y))
    elif op == "1":
        print(operacoes["subtracao"](x, y))
    elif op == "2":
        print(operacoes["divisao"](x, y))
    elif op == "3":
        print(operacoes["multiplicacao"](x, y))
    elif op == "4":
        x = float(input("Digite o primeiro número: "))
        y = float(input("Digite o segundo número: "))
        menu()
    elif op == "5":
        break
