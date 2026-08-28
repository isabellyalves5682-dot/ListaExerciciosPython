#Exeercicio 5 - Receba os coeficientes A, B, C, de uma
#equação do 2º grau (AX^2+BX+C=0). Calcule e mostre 
# as raizes reais (considerar que a equação possui
# duas raizes) 

a = int (input ("Digite o valor de A\n"))
b = int (input ("Digite o valor de B\n"))
c = int (input ("Digite o valor de C\n"))

delta = (b**2 - 4*a*c)
x1 = (- b +  (delta ** 0.5)) / 2 * a
x2 = (- b - (delta ** 0.5)) / 2 * a

print ("A primeira raiz é" , (x1) , "\nA segunda raiz é" , (x2))