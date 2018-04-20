# 3. Escriba un programa Python para adivinar un número entre 1 y 9. 
# Nota: Se le pide al usuario que ingrese una conjetura. Si el usuario
# se equivoca, entonces el mensaje aparece de nuevo hasta que la suposición
# es correcta, con una conjetura exitosa, el usuario obtendrá un
# "bien adivinado". Mensaje, y el programa saldrá.

from random import randint

#print(random.randrange(9))
numRandom = randint(1,9)
#print("\n El NumRandom es: ",numRandom)
conjetura = 100

while not numRandom==conjetura:
    conjetura = int(input("Ingrese una conjetura: "))
    if numRandom==conjetura:
        print("\n Bien adivinado")
    else:
        print("\n Intentalo de nuevo :/")
print("Ya sali")
