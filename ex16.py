#Exercicio 16 - Receba a quantidade de horas 
# trabalhadas, o valor por hora, o percentual
#de desconto e o numero de dependentes. Calcule
#o salario que sera as horas trabalhadas *o valor 
#por hora. Calcule o salario liquido = salario bruto 
# - desconto. A cada dependente sera acrescido rs100 
# no salario liquido. Exiba o salario a receber.

horasTrabalhadas = float(input("Digite as horas trabalhadas\n"))
valorHora = float(input("Digite o valor da hora trabalhadas\n"))
percentual = float(input("Digite o desconto em %\n"))
dependentes = (int(input ("Digite o numero de dependentes\n")))

salarioBruto = horasTrabalhadas * valorHora
desconto = salarioBruto * (percentual/100)
salarioLiquido = salarioBruto- desconto
salarioLiquido = salarioLiquido + (dependentes * 100)

print ("O salario liquido é" , (salarioLiquido))
