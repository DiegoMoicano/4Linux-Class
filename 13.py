valor = float(input(f"Digite o seu valor/hora: "))
horas = float(input(f"Digite as horas trabalhadas: "))

salario_bruto = valor * horas
inss = salario_bruto * 0.14
imposto_renda = (salario_bruto - inss) * 0.1375
salario_liquido = salario_bruto - (imposto_renda + inss)

print(f"\nValor Salário Bruto é de R$ {round(salario_bruto, 2)}")
print(f"Pagou para o INSS o valor de R$ {round(inss, 2)}")
print(f"Pagou para o Imposto de Renda o valor de R$ {round(imposto_renda, 2)}")
print(f"Valor do Salário Liquido é de R$ {round(salario_liquido, 2)}")
