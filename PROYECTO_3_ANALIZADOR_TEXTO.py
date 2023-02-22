#PROYECTO 3 - ANALIZADOR DE TEXTO

'''

cuantas palabras hay en todo el texto
'''

texto_or = input('Hola, por favor ingresa un texto para analizarlo: ').lower()
texto_lista = list(texto_or)
texto_palabras = texto_or.split()
largo_texto = len(texto_or.split())
texto_palabras.reverse()
texto_reverso = texto_palabras

letra1 = input('Ahora ingresa 1 letra a elección: ').lower()
letra2 = input('ingresa 1 letra mas: ').lower()
letra3 = input('ingresa una ultima letra: ').lower()
letras_lista = [letra1,letra2,letra3]

total_letra1 = str(texto_or.count(letra1))
total_letra2 = str(texto_or.count(letra2))
total_letra3 = str(texto_or.count(letra3))


primera_letra = texto_lista[0]
ultima_letra = texto_or[-1]
palabra_python = 'Python'.lower() in texto_or

print(f'La primera letra es {primera_letra} \n')
print(f'La ultima letra es {ultima_letra}\n')
print(f'El texto tiene una cantidad total de palabras: {largo_texto}\n')
print(f'La palabra Python está en el texto es: {palabra_python}\n')
print(f'El texto inverso se veria: {texto_reverso}\n')


#ANALIZADOR TEXTO PROFESOR---------------------------------------------------------------------------------------------------------------------------------------

textop = input("Ingresa un texto: ")
letrasp = []

textop = textop.lower()

letrasp.append(input("Ingresa la primera letra").lower())
letrasp.append(input("Ingresa la segunda letra").lower())
letrasp.append(input("Ingresa la tercera letra").lower())

print("CANTIDAD DE LETRAS")
print("\n")
cantidad_letras0 = textop.count(letrasp[0])
cantidad_letras1 = textop.count(letrasp[1])
cantidad_letras2 = textop.count(letrasp[2])

print(f"Hemos encontrado la letra '{letrasp[0]}' repetida {cantidad_letras0} veces")
print(f"Hemos encontrado la letra '{letrasp[1]}' repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra '{letrasp[2]}' repetida {cantidad_letras2} veces")

print("CANTIDAD DE PALABRAS")
print("\n")

palabrasp = textop.split()
print(f"Hemos encontrado {len(palabrasp)} palabras en tu texto")

print("LETRA INICIO Y LETRA FINAL")
print("\n")
letra_inicio = textop[0]
letra_final = textop[-1]

print(f"La letra inicial es '{letra_inicio}' y la letra final es {letra_final}")

print("TEXTO INVERTIDO")
print("\n")

palabrasp.reverse()
textop_invertido = ' '.join(palabrasp)
print(textop_invertido)

print("BUSCANDO LA PALABRA PYTHON")
print("\n")
buscar_python = 'python' in textop
dic = {True:"si", False:"no"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")

