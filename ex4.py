#Exercicio 4 -Receba a temperatura em graus 
# e mostre a sua temperatura convertisa em fahrenheit 
# F = (9 * C + 160) / 5

tempCelsius = (float (input ("Digite a temperatura em celsius\n")))

tempFahrenheit = ( 9 * tempCelsius + 160 ) / 5

print ("A temperatura" , tempCelsius , "º. Convertida em temperatura " \
"Fahrenheit é" , tempFahrenheit , "º")