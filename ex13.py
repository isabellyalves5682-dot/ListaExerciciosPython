#Exercicio 13 - Recea a qualidade de alimento em quilos.
#Calcule e mostre quantos dias durara esse alimentos 
#sabendo que a pessoa consiome 50g ao dia

kgAlimento = (float(input ("Digite a quantidade de alimentos em kg")))

#1kg = 1000g

dias = (kgAlimento * 1000) / 50

print ("A quantidade" , (kgAlimento) , "kg, ira durar" , (dias) , "dias")