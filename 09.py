operacoes = {
    "soma": lambda x, y: x + y,
    "subtracao": lambda x, y: x - y,
    "divisao": lambda x, y: x / y,
    "multiplicacao": lambda x, y: x * y
}

x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))

while True:
    print("""
        0 soma
        1 subtracao
        2 divisao
        3 multiplicacao
    """)

    op = input("Digite a operação: ")

    if op == "0":
        print(operacoes["soma"](x, y))
        break
    elif op == "1":
        print(operacoes["subtracao"](x, y))
        break
    elif op == "2":
        print(operacoes["divisao"](x, y))
        break
    elif op == "3":
        print(operacoes["multiplicacao"](x, y))
        break
