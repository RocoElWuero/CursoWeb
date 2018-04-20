# 6. Escriba un programa Python para contar el
# número de números pares e impares de una serie de números. 
# Números de muestra : números = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Producto esperado :
#	Número de números pares: 5
#	Número de números impares: 4

serie=1
cantidPar=0
cantidImpar=0

while serie<=9:
    if 0==(serie%2):
        cantidPar=cantidPar+1
    else:
        cantidImpar=cantidImpar+1
    serie=serie+1
print("Numero de numeros pares: ",cantidPar)
print("Numero de numeros impares: ",cantidImpar)
