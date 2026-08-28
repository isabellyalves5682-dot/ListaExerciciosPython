#Exercicio 15 - Receba os valores de 2 catetos
#  de um triangulo retangulo. Mostre a hipotenusa

cateto1 = float(input("Digite o valor do primeiro cateto\n"))
cateto2 = float(input("Digite o valor do segundo cateto\n"))

hipotenusa = (cateto1**2 + cateto2**2)**0.5

print ("A hipotenusa é" , (hipotenusa))