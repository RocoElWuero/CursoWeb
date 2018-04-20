# 1. Escriba un programa Python para encontrar los números
# que son divisibles por 7 Y múltiplos de 5, entre 1500 Y
# 2700 (ambos incluidos). 
numeroComparado=1500
comprobadorSiete=0
comprobadorCinco=0

while numeroComparado<=2700:
	comprobadorSiete=numeroComparado%7
	comprobadorCinco=numeroComparado%5
	if comprobadorSiete==0 and comprobadorCinco==0:
	    print("\n\n ",numeroComparado," divisible entre 7 y multiplo de 5")
	numeroComparado=numeroComparado+1
print('\n\tYa sali')
