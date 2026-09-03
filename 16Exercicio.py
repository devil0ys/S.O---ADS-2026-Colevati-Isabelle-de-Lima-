horas = float(input("Digite a quantidade de horas trabalhadas: "))
valor_hora = float(input("Digite o valor da hora: "))
desconto = float(input("Digite o percentual de desconto: "))
dependentes = int(input("Digite o número de dependentes: "))

salario_bruto = horas * valor_hora
valor_desconto = salario_bruto * desconto / 100
salario_liquido = salario_bruto - valor_desconto

salario_liquido = salario_liquido + (dependentes * 100)

print("Salário bruto:", salario_bruto)
print("Desconto:", valor_desconto)
print("Salário a receber:", salario_liquido)