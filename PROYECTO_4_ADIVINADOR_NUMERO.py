# PROYECTO 4 - ADIVINADOR DE NUMERO

from random import *

participante = input('Hola, ingresa tu nombre para comenzar: \n')
print('Comencemos, adivina un numero del 1 al 100, tienes 8 intentos, suerte =)\n')
numero_azar = round(random() * 100)

intentos = 0

while intentos < 8:
    numero_participante = int(input('ingresa un numero entre 1 y 100: '))
    intentos += 1
    if numero_participante not in range(1,101):
        print('El numero que ingresaste es invalido')
    elif numero_participante > numero_azar:
        print('El numero que ingresaste es mayor')
    elif numero_participante < numero_azar:
        print('El numero que ingresaste es menor')
    else:
        print(f'\nFelicidades {participante}, adivinaste el numero en {intentos} intentos')
        break
if numero_participante != numero_azar:
    print(f'Lo siento has agotado los intentos, el numero secreto era {numero_azar}')
