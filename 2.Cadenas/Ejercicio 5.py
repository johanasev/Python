#Ejercicio de cadenas

#Escribir un programa que pida al usuario que introduzca una frase 
# en la consola y muestre por pantalla la frase invertida.

from tabulate import tabulate

frase = input("Ingresa frase: ")


data =[]
reverso = frase[::-1]

data.append([frase, reverso])

headers = ['Original','Reverso']

tabla = tabulate(data, headers=headers, tablefmt="grid")

print(tabla)


