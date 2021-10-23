valor = float(input(f"Digite o seu valor/hora: "))
horas = float(input(f"Digite as horas trabalhadas: "))

salario_bruto = valor * horas
imposto_renda = salario_bruto * 0.11
inss = (salario_bruto - imposto_renda) * 0.14
sindicato = (salario_bruto - (imposto_renda + inss)) * 0.05
salario_liquido = salario_bruto - (imposto_renda + inss + sindicato)

print(f"\nValor Salário Bruto é de R$ {round(salario_bruto, 2)}")
print(f"Pagou para o Imposto Renda o valor de R$ {round(imposto_renda, 2)}")
print(f"Pagou para o INSS o valor de R$ {round(inss, 2)}")
print(f"Pagou para o Sindicato o valor R$ {round(sindicato, 2)}")
print(f"Valor do Salário Liquido é de R$ {round(salario_liquido, 2)}")
