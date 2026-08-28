#Exercicio 14 - Receba 2 angulos de um triangulo 
#Calcule e mostre o valor do 3º angulo.

angulo1 = float(input("Digite o valor do primeiro angulo\n"))
angulo2 = float(input("Digite o valor do segundo angulo\n"))
angulo3 = 180 - angulo1 - angulo2

print ("O terceiro angulo do triangulo é" , (angulo3) , "º")