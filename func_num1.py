n = int(input("Digite um número inteiro: "))


def exercicio1(n):
    for i in range(1, n + 1):
        # print(f"valor de i = {i}")
        for j in range(i):
            # print(f"valor de j = {j}")
            print(i, end=" ")  # print j times the number i in the same line
        print()   # print a new line


exercicio1(n)