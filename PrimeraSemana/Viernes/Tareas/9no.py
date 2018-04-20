# 9. Escriba un programa de Python que calcule el factorial de un número.
# Ejemplo: Factorial de 5 = 5 x 4 x 3 x 2 x 1 = 120
# NOTA: Factorial de 0 = 1.

def factorial(num):
    if num!=1:
        return factorial(num-1)*num
    return num

numero=5
print(factorial(numero))
