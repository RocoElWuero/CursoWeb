# 8. Escriba un programa de Python que imprima todos los números de 0 a 6 excepto 3 y 6.
# Nota: Utilice la instrucción 'continue'.
# Resultado esperado: 0 1 2 4 5

numeros=0
while numeros<=6:
    if numeros==3 or numeros==6:
        numeros=numeros+1
        continue

    print(numeros)
    numeros=numeros+1
