# 5. Escriba un programa de Python que acepta una
# palabra del usuario y la invierte. 

palabra = input("\n Ingresa una palabra: ")
#print(palabra)
palabraInvert=""
indice=0

while indice<len(palabra):
#    print(palabra[indice])
    palabraInvert=(palabra[indice])+palabraInvert
    indice=indice+1
print(palabraInvert)
