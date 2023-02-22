#PROYECTO 2 - CALCULADOR DE COMISIONES

vendedor = input('Hola, ingresa tu nombre: ')
ventas = float(input('Ahora ingresa el monto total de ventas realizadas durante el mes: '))
comisiones = round(ventas * 13 / 100,2)

print(f'{vendedor} tus comisiones para esté mes son de: ${comisiones}')