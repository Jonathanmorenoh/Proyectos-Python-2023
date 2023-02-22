#PROYECTO 5 - JUEGO EL AHORCADO


from random import *

# VARIABLES LISTA DE PALABRAS SELECCIONABLES:

lista_palabras = ['Manzana','Python','Carroza','Juego','Nieve']

# VARIABLES LETRAS ADIVINADAS

letras_correctas = []
letras_incorrectas = []
intentos = 10
aciertos = 0
juego_terminado = False

#FUNCION SELECCION DE PALABRA

def seleccion_palabra(lista_palabras): 
    palabra = choice(lista_palabras).lower()
    letras_unicas = len(set(palabra))
    
    return palabra, letras_unicas


#FUNCION PEDIR LETRA

def pedir_letra ():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnopqrstuvwxyz'

    while not es_valida:
        letra_elegida = input('Elige una letra: ').lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print('No has elegido una letra correcta')
    return letra_elegida


#FUNCION MOSTRAR NUEVO TABLERO

def mostrar_nuevo_tablero (palabra_elegida):

    lista_oculta = []

    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('-')
    print(' '.join(lista_oculta))


# FUNCION PARA CHEQUEAR SI LA LETRA SE ENCUENTRA O NO

def chequear_letra (letra_elegida, palabra_oculta, vidas, coincidencias):
    fin = False
    if letra_elegida in palabra_oculta:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1
    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)
    return vidas, fin, coincidencias

# FUNCION PERDER

def perder():
    print('Te has quedado sin vidas')
    print('La palabra oculta era ' + palabra)
    return True

# FUNCION GANAR

def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print('Felicitaciones, has enconetrado la palabra: ' + palabra)   
    return True


palabra, letras_unicas = seleccion_palabra(lista_palabras)

while not juego_terminado:
   
    print('\n' + '*'*20 + '\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print('Letras incorrectas: ' + '-'.join(letras_incorrectas))
    print(f'vidas: {intentos}')
    print('\n' + '*'*20 + '\n')
    letra = pedir_letra()

    intentos, terminado,  aciertos = chequear_letra(letra, palabra,intentos,aciertos)

    juego_terminado = terminado
