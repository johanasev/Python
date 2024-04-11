#Ejercicio de cadenas

#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, 
# y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

from tabulate import tabulate

frase = input("Ingrese una frase: ")
vocal = input("Ingrese una vocal: ")

data = []

if vocal in frase:
   vocalU = vocal.upper()
   newfrase = frase.replace(vocal, vocalU)

data.append([frase.lower(), newfrase])

headers = ('Frase original', 'Frase nueva')

tabla = tabulate(data, headers=headers, tablefmt="grid")

print(tabla)