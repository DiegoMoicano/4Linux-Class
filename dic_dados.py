dados = {}

cont = 0
while cont < 3:
    name = input("Digite seu nome: ")
    tel = int(input("Digite seu telefone: "))
    age = int(input("Digite sua idade: "))
    cepef = int(input("Digite seu CPF: "))
    course = input("Digite o seu curso: ")

    dados.update({"nome": name})
    dados.update({"telefone": tel})
    dados.update({"idade": age})
    dados.update({"cpf": cepef})
    dados.update({"curso": course})

    cont += 1

print(dados)
