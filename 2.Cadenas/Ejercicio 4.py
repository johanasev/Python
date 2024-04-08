#Ejercicios de cadenas

#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension 
# donde el prefijo es el código del país +34, y la extensión tiene dos dígitos 
# (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número 
# de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

import random
from tabulate import tabulate

cant_datos = int(input("Ingresa cantidad de datos a generar: "))

data = []
for n in range(1, cant_datos +1):

    prefijo = str(random.randint(00, 99)).zfill(2)
    numero_central = str(random.randint(100000000, 999999999))
    numero_extension = str(random.randint(10, 99)).zfill(2)

    numero_completo = f"+{prefijo}-{numero_central}-{numero_extension}"

    prefj = numero_completo[:3]
    central = numero_completo[4:13]
    exten = numero_completo[14:]
        
    data.append([n, numero_completo, prefj, central, exten])
    
headers = ['Cant', 'Teléfono','Prefijo', 'Nro-central','Extensión' ]

tabla = tabulate(data, headers=headers, tablefmt="grid")

print(tabla)
