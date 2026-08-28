#Exercicio 17 - Calcule a quantidade de litros
#gastos em uma viagem, sabendo que o automovel 
#faz 12 km por l. Receber o tempo de percurso 
#e a velocidade media

tempo = float(input ("Digite o tempo da viagem\n"))
velocidadeMedia = float(input ("Digite a velocidade media\n"))

distancia = tempo * velocidadeMedia
litro = distancia /12

print ("A quantidade de litros gastos foi de" , (litro))

