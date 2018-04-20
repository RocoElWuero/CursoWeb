#10. Escriba un programa de Python que solicite una cadena
# al usuario e imprima la misma cadena omitiendo todas sus vocales.
# EJEMPLO: Entrada: "¡Hola, mundo!" - Salida: "¡Hl, mnd!"

cadena = input("\n Ingresa una cadena: ")
cadena2=""
indice=0

while indice<len(cadena):
    if cadena[indice]!='a' and cadena[indice]!='e' and cadena[indice]!='u' and cadena[indice]!='i' and cadena[indice]!='o':
        cadena2=cadena2+(cadena[indice])
    indice=indice+1
print(cadena2)
