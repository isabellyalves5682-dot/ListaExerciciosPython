#Exercicio 12

#Receba o ano de nascimento e o ano atual.
#Calcule e mostre a idade e quantos
#anos tera daqui a 17anos

anoNasc = int(input ("Digite o ano do seu nascimento\n"))
anoAtual: int = 2026

idade = anoAtual - anoNasc
idadeFuturo = (anoAtual + 17) - anoNasc

print ("A sua idade é" , (idade) , "\nDaqui a 17 anos você terá" , (idadeFuturo))